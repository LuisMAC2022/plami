#!/usr/bin/env python3
import csv
import json
import re
from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path
from typing import List
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[2]
URLS_FILE = ROOT / "urls.txt"
ETAPA_DIR = ROOT / "docs" / "etapa-0"
AUDITS_DIR = ROOT / "docs" / "audits"
HANDOFFS_DIR = ROOT / "docs" / "handoffs"


@dataclass
class UrlRow:
    url: str
    status: int
    final_url: str
    language_guess: str
    page_type: str
    title: str
    meta_description: str
    canonical: str
    hreflang_count: int
    html_lang: str
    h1_count: int
    has_main: bool
    images_missing_alt: int


def normalize_seeds(lines: List[str]) -> List[str]:
    cleaned, seen = [], set()
    for line in lines:
        url = line.strip()
        if not url or url in seen:
            continue
        cleaned.append(url)
        seen.add(url)
    return cleaned


def guess_language(url: str) -> str:
    return "EN" if "/en/" in urlparse(url).path else "ES"


def guess_page_type(url: str) -> str:
    path = urlparse(url).path.lower()
    if any(x in path for x in ["aviso", "privacy", "notice"]):
        return "legal"
    if any(x in path for x in ["tienda", "carrito", "finalizar-compra", "mi-cuenta"]):
        return "e-commerce"
    if any(x in path for x in ["producto", "products", "empaque", "packaging", "food", "pharmaceutical"]):
        return "producto/categoría"
    if any(x in path for x in ["expo", "blog", "landing"]):
        return "blog/landing"
    return "corporativa"


def capture(pattern: str, text: str) -> str:
    match = re.search(pattern, text, flags=re.I | re.S)
    if not match:
        return ""
    return re.sub(r"\s+", " ", match.group(1)).strip()


def crawl(url: str) -> UrlRow:
    try:
        req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(req, timeout=20) as response:
            status = response.getcode() or 0
            final_url = response.geturl()
            html_text = response.read().decode("utf-8", errors="ignore")

        title = capture(r"<title[^>]*>(.*?)</title>", html_text)
        meta_description = capture(r"<meta[^>]+name=['\"]description['\"][^>]+content=['\"](.*?)['\"]", html_text)
        canonical = capture(r"<link[^>]+rel=['\"]canonical['\"][^>]+href=['\"](.*?)['\"]", html_text)
        hreflang_count = len(re.findall(r"<link[^>]+hreflang=['\"].*?['\"]", html_text, flags=re.I))
        html_lang = capture(r"<html[^>]+lang=['\"](.*?)['\"]", html_text)
        h1_count = len(re.findall(r"<h1\b", html_text, flags=re.I))
        has_main = bool(re.search(r"<main\b", html_text, flags=re.I))
        imgs = re.findall(r"<img\b[^>]*>", html_text, flags=re.I)
        images_missing_alt = sum(1 for img in imgs if not re.search(r"\balt=", img, flags=re.I))
    except (HTTPError, URLError, TimeoutError, ValueError):
        status, final_url, title = 0, "", ""
        meta_description, canonical, hreflang_count = "", "", 0
        html_lang, h1_count, has_main, images_missing_alt = "", 0, False, 0

    return UrlRow(url, status, final_url, guess_language(url), guess_page_type(url), title, meta_description, canonical, hreflang_count, html_lang, h1_count, has_main, images_missing_alt)


def main() -> None:
    ETAPA_DIR.mkdir(parents=True, exist_ok=True)
    AUDITS_DIR.mkdir(parents=True, exist_ok=True)
    HANDOFFS_DIR.mkdir(parents=True, exist_ok=True)

    seeds = normalize_seeds(URLS_FILE.read_text(encoding="utf-8").splitlines())
    rows = [crawl(url) for url in seeds]

    csv_path = ETAPA_DIR / "url-inventory.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(asdict(rows[0]).keys()))
        writer.writeheader()
        writer.writerows(asdict(row) for row in rows)

    (ETAPA_DIR / "url-inventory.json").write_text(json.dumps([asdict(r) for r in rows], ensure_ascii=False, indent=2), encoding="utf-8")

    lines = ["# Issues Etapa 0 (Inicial)", "", "| Severidad | URL | Hallazgo | Evidencia |", "|---|---|---|---|"]
    for row in rows:
        if row.status >= 400 or row.status == 0:
            lines.append(f"| P0 | {row.url} | URL no accesible | status={row.status} |")
        if row.h1_count != 1:
            lines.append(f"| P1 | {row.url} | h1_count fuera de norma | h1_count={row.h1_count} |")
        if not row.has_main:
            lines.append(f"| P1 | {row.url} | Falta landmark main | has_main={row.has_main} |")
    (ETAPA_DIR / "issues-etapa-0.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    total = len(rows)
    inaccessible = sum(1 for r in rows if r.status == 0 or r.status >= 400)
    multi_h1 = sum(1 for r in rows if r.h1_count != 1)
    without_main = sum(1 for r in rows if not r.has_main)

    (AUDITS_DIR / "baseline.md").write_text(
        f"# Baseline técnico — Etapa 0\n\nFecha: {date.today().isoformat()}\n\n## Cobertura\n- URLs semilla procesadas: {total}\n- URLs inaccesibles (status 0 o >=400): {inaccessible}\n\n## Señales iniciales de calidad\n- Páginas con h1_count != 1: {multi_h1}\n- Páginas sin `<main>`: {without_main}\n\n## Entregables generados\n- `docs/etapa-0/url-inventory.csv`\n- `docs/etapa-0/url-inventory.json`\n- `docs/etapa-0/issues-etapa-0.md`\n\n## Siguientes pasos\n1. Ejecutar pasada incremental para descubrir enlaces internos no listados en seed.\n2. Priorizar issues P0/P1 por impacto en navegación, indexación y WCAG 2.1 AA.\n3. Preparar backlog de Etapa 1 con dueños por agente.\n",
        encoding="utf-8",
    )

    (HANDOFFS_DIR / f"{date.today().isoformat()}_etapa-0_qa-release.md").write_text(
        f"# Handoff QA/Release — Etapa 0\n\nFecha: {date.today().isoformat()}\n\n## Resumen\nSe inicializó la Etapa 0 con inventario de URLs seed, baseline técnico e issues preliminares.\n\n## Riesgos iniciales\n- URLs inaccesibles: {inaccessible}\n- Estructura semántica potencialmente inconsistente (h1/main): revisar `issues-etapa-0.md`.\n\n## Pendientes para Etapa 1\n1. Validación manual de URLs críticas (home, contacto, tienda, checkout).\n2. Verificación de canónicos y hreflang por pares ES/EN.\n3. Priorización final P0/P1/P2 con evidencia reproducible.\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
