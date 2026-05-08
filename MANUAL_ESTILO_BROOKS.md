# Manual de Estilo de Brooks

> Base de coordinación para agentes del proyecto plami.com.mx.

## 1) Propósito

Este manual define **cómo se coordinan los agentes** durante cada etapa del proyecto para asegurar:

- Semántica HTML5 correcta y mantenible.
- Accesibilidad WCAG 2.1 AA o superior.
- Rendimiento web de alto nivel.
- Uso mínimo y justificado de JavaScript.
- Consistencia entre idiomas (es-MX / en).

## 2) Principios de Brooks aplicados al proyecto

### 2.1 Conceptual Integrity (Integridad conceptual)

Todo el sitio debe sentirse como un solo sistema:

- Un único lenguaje de diseño y contenido.
- Una sola convención de arquitectura.
- Una única fuente de verdad para especificaciones técnicas.
- Criterios uniformes de accesibilidad y SEO.

**Regla:** si una decisión rompe consistencia global, se rechaza o se rediseña.

### 2.2 Equipo pequeño con roles claros

Brooks enfatiza estructuras de comunicación eficientes. Se adopta un equipo de agentes con responsabilidades explícitas:

1. **Agente Arquitectura**: estructura del repositorio, rutas, canónicos, i18n.
2. **Agente Semántica/HTML**: layouts, componentes semánticos, reducción de divitis.
3. **Agente A11y**: WCAG, teclado, foco, formularios, validaciones.
4. **Agente Performance**: budget de recursos, imágenes, CSS/JS crítico.
5. **Agente Contenido e i18n**: copy, glosario técnico, EN actualizado (no literal).
6. **Agente QA/Release**: auditorías, regresiones, definición de DoD.

### 2.3 Comunicación mínima, documentación máxima

- Los acuerdos técnicos viven en documentos versionados.
- Cualquier cambio que afecte arquitectura, a11y o performance requiere registro en ADR.
- Las decisiones no documentadas no existen.

### 2.4 Planificar para reducir retrabajo

- Cambios estructurales primero (arquitectura + semántica).
- Mejoras visuales después.
- Features nuevas (comparador) al final de la estabilización base.

## 3) Reglas maestras del proyecto

## 3.1 HTML5 semántico obligatorio

- Usar: `header`, `nav`, `main`, `section`, `article`, `aside`, `footer`, `figure`, `figcaption`, `time`.
- Evitar `div`/`span` genéricos cuando exista equivalente semántico.
- Un único `main` visible por página.
- Un único `h1` por documento, jerarquía de `h2..h6` sin saltos arbitrarios.

## 3.2 Accesibilidad por defecto (shift-left)

- Navegación total por teclado.
- Skip link obligatorio.
- Foco visible en todos los elementos interactivos.
- Formularios con `label` asociado y mensajes de error claros.
- `alt` descriptivo en imágenes informativas; `alt=""` en decorativas.
- ARIA solo cuando HTML nativo no alcance.

## 3.3 Rendimiento como restricción de diseño

- Eliminar librerías/frameworks sin justificación de negocio.
- JS mínimo: preferir HTML/CSS para interacción básica.
- Imágenes en formatos modernos (`webp`/`avif`) cuando aplique.
- `width`/`height` en imágenes para evitar CLS.
- `loading="lazy"` en contenido no crítico.
- Evitar scripts bloqueantes en `head`.

## 3.4 SEO técnico y canonicalidad

- Cada contenido tiene una URL canónica única.
- Implementar `rel="canonical"` y `hreflang` es/en.
- Prohibir indexación de duplicados de navegación/filtros si no aportan valor.
- Mantener sitemap por idioma.

## 3.5 i18n y calidad lingüística

- EN no es traducción literal de ES: debe ser adaptación técnica natural.
- Glosario técnico bilingüe obligatorio.
- Si cambia ES, se marca EN como “desactualizado” hasta revisión.

## 4) Protocolo operativo por etapa

## Etapa 0: Ingesta y baseline

**Objetivo:** capturar estado actual y riesgos.

- Inventario de URLs, plantillas y metadatos.
- Auditoría Lighthouse + axe + revisión manual de teclado.
- Registro de duplicidad, errores tipográficos y deuda i18n.

**Salida:** informe baseline en `/docs/audits/baseline.md`.

## Etapa 1: Arquitectura y contenido

- Reorganizar rutas por idioma (`/es`, `/en`).
- Definir modelo de contenido canónico en archivos estructurados.
- Eliminar dependencia de contenido disperso y duplicado.

**Salida:** mapa de información + esquema de contenidos.

## Etapa 2: Refactor semántico + a11y

- Sustitución progresiva de plantillas con HTML5 semántico.
- Implementar checklist WCAG 2.1 AA por plantilla.
- Validar foco, headings, landmarks y formularios.

**Salida:** plantillas certificadas con checklist.

## Etapa 3: Performance

- Remover dependencias no esenciales.
- Ajustar estrategia de CSS/JS crítico.
- Optimizar medios e interacciones costosas.

**Salida:** reporte de mejora de CWV.

## Etapa 4: Comparador de especificaciones

- Definir esquema normalizado de propiedades/unidades.
- Construir interfaz accesible de comparación (tabla semántica).
- Exportación básica (CSV/PDF) y URL compartible.

**Salida:** MVP de comparador en producción.

## 5) Contrato entre agentes (hand-off)

Cada entrega entre agentes debe incluir:

1. **Contexto**: qué cambió y por qué.
2. **Impacto**: a11y, performance, SEO, i18n.
3. **Riesgos**: regresiones potenciales.
4. **Pruebas ejecutadas**: comandos + resultados.
5. **Pendientes**: lista priorizada.

Formato sugerido: archivo `docs/handoffs/YYYY-MM-DD_<etapa>_<agente>.md`.

## 6) Definition of Ready (DoR)

Una tarea entra a desarrollo solo si:

- Tiene alcance claro y criterios de aceptación.
- Indica impacto en semántica/a11y/performance.
- Define comportamiento en ES y EN.
- Incluye restricciones técnicas conocidas.

## 7) Definition of Done (DoD)

Una tarea se considera terminada solo si:

- Cumple semántica HTML5 requerida.
- Pasa checklist de accesibilidad aplicable.
- No supera budget de rendimiento acordado.
- No introduce duplicidad canónica.
- Incluye pruebas y evidencia.
- Está documentada (ADR/handoff/changelog según aplique).

## 8) Checklist obligatorio de revisión (por PR)

1. ¿Se redujo o evitó divitis?
2. ¿Hay `main` único y `h1` único?
3. ¿Navegable con teclado de extremo a extremo?
4. ¿Foco visible y sin trampas de foco?
5. ¿Imágenes con `alt` correcto?
6. ¿Formularios con `label` y errores accesibles?
7. ¿ARIA solo donde aporta valor real?
8. ¿Se eliminó JS/librería innecesaria?
9. ¿Se preservó canonical/hreflang?
10. ¿ES y EN están alineados y revisados?

## 9) Métricas de control

- Lighthouse Accesibilidad >= 95.
- Lighthouse SEO >= 95.
- Lighthouse Performance móvil >= 85 (mínimo inicial).
- 0 errores críticos de axe en plantillas core.
- 100% de páginas con canonical válido.
- 100% de páginas públicas con versión EN vigente cuando aplique.

## 10) Gobernanza de decisiones (ADR)

Toda decisión estructural se registra en `docs/adr/`:

- Contexto.
- Alternativas evaluadas.
- Decisión elegida.
- Consecuencias.
- Fecha y responsables.

Plantilla sugerida: `docs/adr/0001-nombre-corto.md`.

## 11) Cadencia de coordinación

- **Daily async (15 min):** bloqueo, progreso, siguiente paso.
- **Sync técnico 2 veces/semana:** decisiones transversales.
- **Review de calidad semanal:** a11y + performance + i18n.
- **Retro por etapa:** qué mantener, qué ajustar.

## 12) Anexos rápidos

### 12.1 Convenciones de idioma

- Español: `es-MX`.
- Inglés: `en` o `en-US` según alcance comercial final.
- No mezclar idiomas en labels críticos de UI.

### 12.2 Convenciones de naming

- IDs estables para productos/materiales (`product_id`, `material_id`).
- Slugs SEO legibles y consistentes por idioma.
- Evitar nombres ambiguos en componentes y contenido.

---

**Resumen ejecutivo:** Este manual adopta la disciplina de Brooks para mantener integridad conceptual, minimizar fricción entre agentes y asegurar que cada etapa del proyecto mejore semántica, accesibilidad, rendimiento y calidad editorial de forma medible.
