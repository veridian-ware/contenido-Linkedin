---
title: "De cero a Node + PostgreSQL en 3 minutos con Docker"
serie: "Construyendo Veridian"
post_num: 07
estado: programado
fecha_sugerida: 2026-05-25
tags:
  - linkedin
  - tip
  - docker
  - nodejs
imagen: imagen.png
audiencia: "Devs que arrancan proyectos y pierden tiempo configurando entornos"
objetivo: "Dar valor técnico concreto. Posicionar a Walter como dev que sabe lo que hace."
formato_linkedin: imagen cuadrada (1200x1200)
tipo: tip-tecnico
---

# 07 — Docker tip

## Copy (listo para pegar en LinkedIn)

La primera vez que vi un `docker-compose up` levantar Node + PostgreSQL + Redis en una laptop sin instalar nada más, supe que no iba a volver atrás.

Este es el `docker-compose.yml` base que uso en todos mis proyectos, incluido Veridian:

```yaml
services:
  app:
    build: .
    ports:
      - "3000:3000"
    environment:
      - DATABASE_URL=postgres://user:pass@db:5432/mydb
    depends_on:
      - db

  db:
    image: postgres:15
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: mydb
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

Tres cosas que me salvaron horas:

▸ `depends_on` evita que la app arranque antes que la DB
▸ El volumen `pgdata` persiste los datos entre reinicios
▸ `DATABASE_URL` como variable de entorno → mismo código en dev y producción

En producción reemplazo el servicio `db` por una instancia gestionada (Railway, Supabase, o servidor propio del cliente). El código no cambia.

—

¿Usás Docker en tu flujo de desarrollo? ¿O todavía instalás todo en la máquina? Contame cómo lo manejás.

#Docker #NodeJS #PostgreSQL #Veridian #DesarrolloDeSoftware #Backend

## Notas internas

- Post corto, técnico, con código. Funciona bien para devs que siguen el perfil
- El código tiene que renderizarse bien en LinkedIn (usar bloque de código)
- CTA: pregunta abierta que invita tanto a "sí uso Docker" como a "no, y quiero saber más"
