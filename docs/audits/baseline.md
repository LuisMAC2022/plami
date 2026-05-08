# Baseline técnico — Etapa 0

Fecha: 2026-05-08

## Cobertura
- URLs semilla procesadas: 49
- URLs inaccesibles (status 0 o >=400): 49

## Señales iniciales de calidad
- Páginas con h1_count != 1: 49
- Páginas sin `<main>`: 49

## Entregables generados
- `docs/etapa-0/url-inventory.csv`
- `docs/etapa-0/url-inventory.json`
- `docs/etapa-0/issues-etapa-0.md`

## Siguientes pasos
1. Ejecutar pasada incremental para descubrir enlaces internos no listados en seed.
2. Priorizar issues P0/P1 por impacto en navegación, indexación y WCAG 2.1 AA.
3. Preparar backlog de Etapa 1 con dueños por agente.
