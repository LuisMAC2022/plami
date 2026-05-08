# Especificaciones operativas por agente (Etapa 0)

## 1) Agente Arquitectura
**Misión:** asegurar estructura de información y trazabilidad técnica del crawl.

### Responsabilidades
- Definir formato único del inventario (`csv` + `json`).
- Definir reglas de canonicalidad esperada (ES/EN).
- Establecer naming y organización en `docs/`.

### Criterios de aceptación
- Cada URL tiene `url`, `status`, `final_url`, `language_guess`, `page_type`.
- Existe estrategia clara para detectar páginas huérfanas/duplicadas.

## 2) Agente Semántica/HTML
**Misión:** auditar estructura semántica mínima por plantilla.

### Responsabilidades
- Verificar landmarks (`header/nav/main/footer`).
- Revisar jerarquía de encabezados y unicidad de `h1`.
- Detectar plantillas con divitis severa.

### Criterios de aceptación
- Registro de páginas con múltiples `h1` o sin `main`.
- Lista de plantillas prioritarias para refactor (Etapa 2).

## 3) Agente A11y
**Misión:** identificar brechas WCAG 2.1 AA tempranas.

### Responsabilidades
- Validar navegación por teclado en páginas core.
- Revisar presencia de skip link y foco visible.
- Detectar imágenes sin texto alternativo adecuado.

### Criterios de aceptación
- Matriz de hallazgos críticos con severidad y evidencia por URL.
- Recomendaciones accionables sin depender de rediseño completo.

## 4) Agente Performance
**Misión:** medir deuda técnica de carga inicial y ejecución.

### Responsabilidades
- Levantar señales de peso excesivo de recursos.
- Identificar JS/CSS potencialmente bloqueantes.
- Priorizar oportunidades de reducción de peticiones.

### Criterios de aceptación
- Lista de páginas con mayor riesgo de CWV.
- Top quick wins para Etapa 3.

## 5) Agente Contenido e i18n
**Misión:** detectar inconsistencias ES/EN y deuda de contenido.

### Responsabilidades
- Mapear pares ES/EN existentes y faltantes.
- Detectar traducciones incompletas o no naturales.
- Señalar contenido duplicado de bajo valor SEO.

### Criterios de aceptación
- Mapa de cobertura bilingüe con gaps.
- Prioridad de actualización de contenido para Etapa 1.

## 6) Agente QA/Release
**Misión:** consolidar evidencia y cerrar etapa con trazabilidad.

### Responsabilidades
- Ejecutar checklist global de etapa.
- Consolidar baseline y priorización final de issues.
- Emitir hand-off a la siguiente etapa.

### Criterios de aceptación
- `baseline.md` publicado y revisado.
- Handoff final con riesgos, pruebas y pendientes.

## Checklist de salida conjunta
- [ ] Inventario de URLs completo y normalizado.
- [ ] Metadatos SEO/a11y mínimos capturados.
- [ ] Riesgos priorizados P0/P1/P2.
- [ ] Evidencia reproducible (scripts + archivos).
- [ ] Handoff final disponible.
