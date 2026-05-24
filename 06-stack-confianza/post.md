---
title: "El stack que corre en planta"
serie: "Construyendo Veridian"
post_num: 06
estado: programado
fecha_sugerida: 2026-06-11
buffer_id: 6a12f746f78e0c3452303e7e
tags:
  - linkedin
  - veridian
  - tecnologia
  - confianza
imagen: imagen.png
audiencia: "Compradores técnicos: CTOs, líderes IT, devs que evalúan soluciones"
objetivo: "Cierre técnico de la serie. Mostrar madurez del stack. Construir confianza"
formato_linkedin: imagen cuadrada (1200x1200)
---

# 06 — Stack que corre en planta

## Imagen
![[imagen.png]]

## Copy (listo para pegar en LinkedIn)

Cuando alguien me pregunta "¿con qué está hecho Veridian?", respondo sin marketing:

▸ Frontend: React 18
▸ Runtime: Node.js
▸ API: Express
▸ Base de datos: PostgreSQL
▸ ORM: Sequelize
▸ Cache: Redis
▸ Containers: Docker
▸ Deploy: Railway

Nada exótico. Nada cool por ser cool.

Cada pieza está acá por una razón concreta:

▸ Postgres porque los datos industriales son relacionales y se quedan 10 años
▸ Redis porque las dashboards se consultan cien veces por minuto y la DB no tiene que pagar ese precio
▸ Docker porque despliego en infraestructura del cliente sin pedir favores al sysadmin
▸ Sequelize porque las migraciones de schema en producción no pueden ser drama

Lo importante no es la lista. Lo importante es que es el mismo stack que ya está corriendo, hoy, gestionando órdenes de trabajo reales en empresas argentinas.

No es un MVP en mi laptop. Es producción.

Y si sos dev, te lo digo claro: la mitad de los módulos los estoy empaquetando como productos independientes. AuthKit ya está afuera. WorkKit viene en camino. La idea es que cualquier desarrollador pueda apoyarse en piezas probadas en lugar de reescribir lo mismo en cada proyecto.

—

Si tu empresa está evaluando software de gestión y querés ver una demo del ERP completo, escribime por mensaje directo. Sin formularios, sin call de "discovery".

#Veridian #Stack #NodeJS #PostgreSQL #Docker #ERP #DesarrolloDeSoftware

## Notas internas

- **Este post cierra la serie inicial** — buen momento para CTA directa por DM
- **Tono técnico pero accesible**: justifico cada pieza, no la nombro y ya
- **El "argentinas" es un anchor de cercanía**: te diferencia de SaaS gringos
- **CTA suave**: "DM sin formulario" baja la barrera. Quien escribe está caliente
- **Métrica clave**: DMs recibidos en las 48h post-publicación
- **Sugerencia**: pinear este post al perfil por 1-2 semanas después de publicarlo
- **Posible follow-up**: post sobre arquitectura concreta (cómo se conectan las piezas) — para devs específicamente
