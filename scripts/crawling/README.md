# Scripts de crawling — Etapa 0

Este directorio centraliza utilerías para construir el baseline técnico.

## Flujo recomendado
1. Partir de `urls.txt`.
2. Generar inventario inicial (`url-inventory.csv/json`).
3. Ejecutar crawler técnico (status, canonical, hreflang, headings).
4. Consolidar reporte en `docs/audits/baseline.md`.

## Convención de salida
- `docs/etapa-0/url-inventory.csv`
- `docs/etapa-0/url-inventory.json`
- `docs/etapa-0/issues-etapa-0.md`

## Nota
Si se agregan scripts ejecutables, documentar comando exacto y versión de runtime requerida.
