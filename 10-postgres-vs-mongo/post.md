---
title: "Por qué uso PostgreSQL y no MongoDB para datos industriales"
serie: "Construyendo Veridian"
post_num: 10
estado: programado
fecha_sugerida: 2026-06-01
tags:
  - linkedin
  - tip
  - postgresql
  - arquitectura
imagen: imagen.png
audiencia: "Devs, CTOs, compradores técnicos que evalúan stack"
objetivo: "Justificar decisiones técnicas de Veridian. Construir autoridad técnica."
formato_linkedin: imagen cuadrada (1200x1200)
tipo: tip-tecnico
---

# 10 — PostgreSQL tip

## Copy (listo para pegar en LinkedIn)

Cada vez que digo que uso PostgreSQL en lugar de MongoDB, alguien me pregunta por qué.

Acá va la versión corta:

Los datos industriales son profundamente relacionales.

Una orden de trabajo tiene → un equipo → que pertenece a un sector → que tiene técnicos asignados → que tienen historial de intervenciones → que usan repuestos → que vienen de proveedores.

Eso no es un documento. Es un grafo de relaciones que vive en producción durante 10 años.

Con MongoDB terminás haciendo JOINs a mano en JavaScript. Con Postgres los JOINs son nativos, indexados y llevan 30 años optimizados.

Las otras razones concretas:

▸ Transacciones ACID: si falla una OT a mitad de guardar, no queda en estado inconsistente
▸ Migraciones de schema controladas: Sequelize + ALTER TABLE con historial versionado
▸ Consultas complejas con window functions para reportes de mantenimiento preventivo
▸ Full-text search nativo para buscar historial de fallas sin Elastic

MongoDB tiene su lugar. Logs de eventos, catálogos de productos, datos semi-estructurados. Para gestión industrial, Postgres gana sin discusión.

—

¿Usás Postgres o MongoDB en tus proyectos? ¿Qué factores pesaron en la decisión?

#PostgreSQL #MongoDB #Veridian #Backend #ArquitecturaDeSoftware #NodeJS

## Notas internas

- Post que genera debate (MongoDB vs Postgres) → comentarios y alcance
- No es un ataque a MongoDB — reconocé sus casos de uso para no parecer dogmático
- Lunes = buen día para contenido técnico (devs arrancando semana, modo "aprendizaje")
