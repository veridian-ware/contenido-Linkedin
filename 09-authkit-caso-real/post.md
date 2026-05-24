---
title: "Un prospecto me preguntó cuántos usuarios puede manejar el ERP"
serie: "Construyendo Veridian"
post_num: 09
estado: programado
fecha_sugerida: 2026-05-29
buffer_id: 6a1317e5cc9ff193f819a0ff
tags:
  - linkedin
  - erp
  - producto
  - pymEs
imagen: imagen.png
audiencia: "Dueños y gerentes de PyMEs industriales que evalúan software"
objetivo: "Resolver objeción de escalabilidad. Mostrar que el ERP es producción real. CTA a demo."
formato_linkedin: imagen cuadrada (1200x1200)
---

# 09 — ERP: escalabilidad y producción real

## Copy (listo para pegar en LinkedIn)

Esta semana alguien me preguntó: "¿cuántos usuarios simultáneos puede manejar el ERP?"

La pregunta real detrás es: "¿esto es un MVP de un dev suelto o algo que aguanta producción?"

Respuesta directa:

El ERP de Veridian corre en Docker sobre Railway o en infraestructura propia del cliente. PostgreSQL como base de datos. Redis para caché de dashboards. Node.js en el backend.

No hay un límite arbitrario de usuarios. El límite lo pone el servidor donde lo desplegás — que podés escalar cuando lo necesitás.

Lo que sí puedo decir con certeza:

▸ Está corriendo en producción en empresas reales hoy
▸ Gestiona órdenes de trabajo, inventario, personal y dashboards en simultáneo
▸ El sistema de roles permite que cada usuario vea exactamente lo que le corresponde, sin más

No es un demo en mi laptop. Es el mismo código que uso con clientes.

Y porque soy el único que lo construye y lo soporta, cada implementación es una conversación directa. Sin ticket de soporte. Sin esperar que "el área técnica" responda.

Si tu empresa tiene entre 10 y 200 personas y gestiona operaciones, mantenimiento o inventario en planillas — vale la pena que hablemos.

—

¿Qué herramienta usás hoy para gestionar eso? Me ayuda entender dónde está el dolor real.

#Veridian #ERP #PyMEs #SoftwareIndustrial #Producción #ConstruyendoVeridian

## Notas internas

- Responde la objeción de "¿es serio esto?" sin ponerse defensivo
- "No hay límite arbitrario de usuarios" diferencia de SaaS con tiers por usuario
- El "conversación directa" es una ventaja competitiva real vs SAP/Oracle
- CTA indirecta: la pregunta final invita a revelar el dolor actual
