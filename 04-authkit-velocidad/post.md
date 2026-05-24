---
title: "El auth que construí para el ERP (y por qué tardé 3 semanas en hacerlo bien)"
serie: "Construyendo Veridian"
post_num: 04
estado: programado
fecha_sugerida: 2026-06-04
buffer_id: 6a12f722611cd1e6391735aa
tags:
  - linkedin
  - auth
  - erp
  - desarrolladores
imagen: imagen.png
audiencia: "Devs / CTOs / compradores técnicos que evalúan el ERP"
objetivo: "Mostrar profundidad técnica del ERP. CTA a demo."
formato_linkedin: imagen cuadrada (1200x1200)
---

# 04 — Auth del ERP

## Copy (listo para pegar en LinkedIn)

Cuando arranco un proyecto B2B, lo primero que subestimo siempre es el auth.

En el ERP de Veridian lo aprendí a las malas:

▸ Primera versión: JWT simple, sin refresh tokens → se rompió en producción
▸ Segunda versión: refresh tokens, pero la revocación era manual → agujero de seguridad
▸ Tercera versión: RBAC encima del auth → 5 días solo de permisos y middlewares
▸ Cuarta versión: rate limiting, bloqueo por IP, logs de sesión → otra semana

Tres semanas para hacer algo que el usuario final ni ve.

Pero que define si el sistema es seguro de verdad o solo parece seguro.

El módulo de auth del ERP de Veridian hoy incluye:

▸ JWT con refresh y rotación automática
▸ RBAC granular: roles por módulo, permisos por acción
▸ Recuperación de contraseña y verificación de email
▸ Rate limiting y bloqueo de IP por intentos fallidos
▸ Logs de sesión auditables

Todo esto no es una feature que el cliente pide. Es la base que hace que las otras features sean confiables.

En un ERP que maneja órdenes de trabajo, inventario y datos de producción — que el técnico de turno vea solo lo que le corresponde no es opcional. Es el punto de partida.

—

Si estás evaluando software de gestión para tu planta y querés ver cómo está construido el sistema de roles por dentro, escribime por DM. Hacemos una demo sin formularios ni calls de 45 minutos.

#Veridian #ERP #Seguridad #NodeJS #PyMEs #SoftwareIndustrial

## Notas internas

- Misma historia técnica que antes pero el CTA ahora apunta al ERP, no a un producto standalone
- El "el técnico ve solo lo que le corresponde" es el caso de uso real que resuena en planta
- CTA: DM para demo del ERP completo
