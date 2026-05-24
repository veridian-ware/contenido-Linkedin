---
title: "Migraciones de base de datos en producción sin drama"
serie: "Construyendo Veridian"
post_num: 13
estado: programado
fecha_sugerida: 2026-06-08
tags:
  - linkedin
  - tip
  - sequelize
  - postgresql
  - produccion
imagen: imagen.png
audiencia: "Devs backend que trabajan con bases de datos en producción"
objetivo: "Dar valor técnico. Mostrar madurez de stack. Atraer devs que evalúan Veridian."
formato_linkedin: imagen cuadrada (1200x1200)
tipo: tip-tecnico
---

# 13 — Migrations tip

## Copy (listo para pegar en LinkedIn)

El momento más tenso en cualquier deploy no es el código nuevo. Es el `ALTER TABLE`.

Una migración mal ejecutada en producción puede dejar la base en estado inconsistente, bloquear tablas con millones de filas, o peor: aplicarse a medias.

Lo que aprendí después de varios sustos con Sequelize en Veridian:

**1. Nunca edittes una migración ya ejecutada**
Si está en producción, está sellada. Creá una nueva migración que revierta o modifique. El historial de cambios es sagrado.

**2. Siempre escribí el `down`**
```javascript
async down(queryInterface) {
  await queryInterface.removeColumn('work_orders', 'priority');
}
```
Parece redundante hasta que necesitás hacer rollback un domingo a las 11 PM.

**3. Usá transacciones en migraciones destructivas**
```javascript
async up(queryInterface, Sequelize) {
  await queryInterface.sequelize.transaction(async (t) => {
    await queryInterface.addColumn('equipments', 'serial_number',
      { type: Sequelize.STRING }, { transaction: t }
    );
  });
}
```
Si algo falla, revierte todo. Sin estado inconsistente.

**4. Probá en staging antes que en producción**
Obvio. Pero cuántas veces se saltea.

**5. Backups antes de migraciones grandes**
`pg_dump` tarda 2 minutos. Un ALTER TABLE mal pensado puede costar horas.

—

¿Usás Sequelize o algún otro ORM para manejar migraciones? ¿Qué workflow te funcionó mejor?

#Sequelize #PostgreSQL #NodeJS #Backend #Veridian #DesarrolloDeSoftware

## Notas internas

- Formato "lista de tips con código" funciona bien en LinkedIn para devs
- El tono del "domingo a las 11 PM" genera identificación inmediata
- Lunes técnico: devs en modo aprendizaje al arrancar la semana
