# Etapa 0 — Crawling del sitio y especificaciones de agentes

## Objetivo
Establecer un baseline verificable del sitio `plami.com.mx` (ES/EN), identificar riesgos críticos (a11y, performance, SEO técnico, i18n) y dejar una base operativa para etapas posteriores.

## Alcance de la etapa
1. Crawling completo de URLs conocidas y descubrimiento incremental.
2. Captura de metadatos técnicos por URL.
3. Detección de duplicados, errores de idioma y canónicos inconsistentes.
4. Preparación de auditoría automatizada y revisión manual guiada.
5. Entregables listos para hand-off entre agentes.

## Entregables obligatorios
- `docs/audits/baseline.md`
- `docs/etapa-0/url-inventory.csv`
- `docs/etapa-0/url-inventory.json`
- `docs/etapa-0/issues-etapa-0.md`
- `docs/handoffs/YYYY-MM-DD_etapa-0_qa-release.md`

## Flujo de trabajo (pipeline)

### Fase 1 — Seed e inventario inicial
**Entrada:** `urls.txt`.

1. Normalizar URLs semilla (sin duplicados exactos, sin espacios).
2. Marcar idioma presumido por ruta (`/en/` -> EN, resto ES).
3. Etiquetar tipo preliminar:
   - corporativa
   - producto/categoría
   - legal
   - e-commerce
   - blog/landing

**Salida:** `url-inventory.csv` inicial.

### Fase 2 — Crawling técnico
Por cada URL:
1. Resolver status code final (incluyendo redirecciones).
2. Capturar:
   - `title`
   - `meta description`
   - `rel=canonical`
   - `hreflang`
   - `lang` del documento
   - cantidad de `h1`
   - presencia de `main`
   - imágenes sin `alt`
3. Guardar enlaces internos descubiertos para siguiente pasada.

**Criterio de corte:**
- máximo 3 pasadas de descubrimiento o
- 0 URLs nuevas en una pasada.

### Fase 3 — Auditoría de calidad
Ejecutar checklist por URL:
- **SEO técnico:** canónico válido, indexabilidad, títulos vacíos/duplicados.
- **Accesibilidad estructural:** `h1` único, `main` único, `lang` correcto.
- **Rendimiento base:** peso de recursos y dependencias JS/CSS visibles.
- **i18n:** existencia de par ES/EN cuando aplique.

### Fase 4 — Consolidación y priorización
Clasificación de issues por severidad:
- **P0:** rompe navegación, indexación o cumplimiento a11y crítico.
- **P1:** impacto alto en UX/SEO/performance.
- **P2:** mejoras recomendadas sin bloqueo.

### Fase 5 — Hand-off
El agente QA/Release publica resumen con:
- top 10 riesgos
- páginas críticas afectadas
- backlog sugerido para Etapa 1 y 2

## Matriz RACI de agentes en Etapa 0
| Actividad | Arquitectura | Semántica/HTML | A11y | Performance | Contenido/i18n | QA/Release |
|---|---|---|---|---|---|---|
| Definir estrategia de crawl | R | C | C | C | C | A |
| Inventario y metadatos | C | C | C | C | C | R/A |
| Revisión semántica base | C | R | C | I | I | A |
| Revisión accesibilidad base | I | C | R | I | I | A |
| Revisión performance base | I | I | C | R | I | A |
| Revisión i18n y duplicados | C | I | I | I | R | A |
| Informe baseline final | C | C | C | C | C | R/A |

> R = Responsible, A = Accountable, C = Consulted, I = Informed.

## Definition of Done de Etapa 0
- Inventario actualizado con status y metadatos para 100% de URLs seed.
- Baseline documentado en `docs/audits/baseline.md`.
- Issues priorizados (P0/P1/P2) con URL y evidencia.
- Hand-off emitido con siguientes acciones para Etapa 1.
