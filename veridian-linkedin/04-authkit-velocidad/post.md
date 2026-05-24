---
title: "JWT + RBAC en 5 minutos, no en 5 semanas"
serie: "Construyendo Veridian"
post_num: 04
estado: programado
fecha_sugerida: 2026-06-04
buffer_id: 6a12f722611cd1e6391735aa
tags:
  - linkedin
  - authkit
  - producto
  - desarrolladores
imagen: imagen.png
audiencia: "Devs / CTOs / techleads que arrancan proyectos B2B y odian reinventar auth"
objetivo: "Vender AuthKit Express ($79). Post más comercial de la serie"
formato_linkedin: imagen cuadrada (1200x1200)
producto_link: "https://larira.gumroad.com/l/ojfbww"
---

# 04 — AuthKit velocidad

## Imagen
![[imagen.png]]

## Copy (listo para pegar en LinkedIn)

Cada vez que arranco un proyecto B2B nuevo, hago el mismo cálculo:

▸ Configurar JWT bien (refresh tokens, revocación, expiración): 4-6 horas si tengo suerte
▸ Roles, permisos y middlewares: 2-3 días
▸ Recuperación de contraseña, verificación de email: 1-2 días
▸ Tests, seguridad, edge cases: una semana más

Total: 2-3 semanas que el cliente paga, pero no ve.

Hace seis meses decidí dejar de pagar ese impuesto. Empaqueté la base de autenticación que ya estaba usando en el ERP de Veridian y la convertí en un boilerplate para Express.js.

Eso es AuthKit Express.

▸ JWT con refresh y rotación
▸ RBAC (roles + permisos granulares)
▸ Recuperación de contraseña por email
▸ Rate limiting y bloqueo de IP
▸ Sequelize + PostgreSQL listos
▸ Docker compose para arrancar en una línea
▸ README bilingüe, demo seed, deploy en Railway documentado

Lo usás como base, le agregás tu lógica de negocio, y te ahorrás las 2-3 semanas.

Demo en vivo: https://authkit-express-production.up.railway.app
Gumroad: https://larira.gumroad.com/l/ojfbww — 79 USD, una compra, código tuyo.

—

¿Vos cuánto tardás en configurar auth en un proyecto nuevo? Me interesa el dato real.

#AuthKitExpress #Veridian #ExpressJS #NodeJS #Backend #Boilerplate

## Notas internas

- **Este es el post más "vendedor"** de la serie. Encajarlo después de 2-3 posts de valor para que no parezca spam
- **El link a Gumroad sale al final, no al principio** — el lector primero entiende el valor
- **Estrategia de comentarios**: si alguien comenta cuánto tarda, responder con "te ahorrás X horas" y mencionar el producto
- **No hablar del precio en el primer comentario fijado** — que el lector lo descubra al hacer click
- **Métrica clave**: clicks al link de Gumroad. LinkedIn no los muestra pero Gumroad sí. Comparar visitas antes/después del post
- **Versión alternativa**: si después de 2 semanas hay <5 ventas, probar versión con un caso de uso real ("Cliente de e-commerce me llamó un viernes...")
