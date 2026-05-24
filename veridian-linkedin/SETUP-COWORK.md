# Setup: Automatización de LinkedIn con Claude Cowork

Guía paso a paso para conectar esta carpeta con Claude Cowork y automatizar la publicación.

## Requisitos

- Claude Desktop (Windows o macOS) con plan Pro o superior
- Cowork habilitado (Settings → Capabilities → Cowork)
- Skills habilitado (Settings → Capabilities → Skills)
- Esta carpeta (`veridian-linkedin/`) descargada en tu máquina

## Paso 1 — Ubicar la carpeta

Mové `veridian-linkedin/` a una ubicación permanente. Sugerencias:

```
Windows:  C:\Users\TuUsuario\Documents\veridian-linkedin\
macOS:    ~/Documents/veridian-linkedin/
```

## Paso 2 — Abrir en Cowork

1. Abrí Claude Desktop
2. Cambiá a modo **Cowork** (ícono de carpeta en la barra lateral)
3. Hacé click en "Open folder" → seleccioná `veridian-linkedin/`
4. Claude va a detectar automáticamente el `SKILL.md` y el `brand-voice.md`

## Paso 3 — Primer test

Escribí en el chat de Cowork:

```
Mostrá el pipeline de posts. ¿Cuál es el siguiente para publicar?
```

Claude debería:
- Leer todos los `post.md`
- Mostrarte una tabla con estado de cada post
- Sugerir cuál publicar primero

## Paso 4 — Workflow diario

### Para preparar un post:
```
Prepará el post 03 para publicar mañana. Mostrá preview del copy y la imagen.
```

### Para crear uno nuevo:
```
Creá un nuevo post sobre [tema]. Audiencia: [quién]. Tono: [ángulo].
```

### Para regenerar una imagen:
```
Cambiá el título de la imagen del post 02. En lugar de "200 módulos" quiero "50 módulos".
```

## Paso 5 (opcional) — Conectar scheduler para publicación automática

### Opción A: Postiz (open source, gratuito)

1. Instalá Postiz: https://postiz.com — podés correrlo local o en su cloud
2. Conectá tu cuenta de LinkedIn en Postiz
3. Generá una API key en Settings → API
4. En la terminal (o en Cowork) setear:
   ```
   export POSTIZ_API_KEY=tu_api_key_de_postiz
   ```
5. Ahora podés decirle a Cowork:
   ```
   Publicá el post 01 mañana a las 10 AM ART vía Postiz.
   ```

### Opción B: Blotato (pago, MCP nativo)

1. Registrate en https://blotato.com
2. Conectá LinkedIn
3. En Claude Desktop → Settings → Connectors → buscá "Blotato"
4. Autenticá con OAuth
5. Ahora podés decir:
   ```
   Programá el post 01 para mañana 10 AM usando Blotato.
   ```

### Opción C: Sin scheduler (manual)

Simplemente usá Cowork para preparar el contenido y después:
1. Copiá el copy desde el chat de Cowork
2. Subí la imagen a LinkedIn manualmente
3. Publicá
4. Decile a Cowork: "Marcá el post 01 como publicado"

## Paso 6 (opcional) — Scheduled tasks

Si querés que Cowork te recuerde automáticamente:

```
Todos los martes y jueves a las 9 AM, revisá el pipeline
de posts y mostrá cuál es el siguiente para publicar.
```

Cowork va a ejecutar eso como tarea programada y te muestra el resultado cuando abrís la app.

## Paso 7 — Tracking de resultados

Después de publicar, podés agregar métricas al frontmatter de cada post:

```yaml
metricas:
  likes: 45
  comentarios: 12
  compartidos: 3
  impresiones: 2400
```

Y después preguntarle a Cowork:

```
Analizá las métricas de todos los posts publicados.
¿Cuál funcionó mejor? ¿Qué patrón ves?
```

## Tips

- **Empezá con Nivel 1** (preparación manual) antes de conectar schedulers
- **No publiques 2 posts el mismo día** — se pisan el alcance
- **Respondé comentarios en las primeras 2 horas** — el algoritmo lo premia
- **Usá Dispatch** (feature de Cowork) para revisar el pipeline desde el celular
- **Backup**: si subís la carpeta a GitHub (`veridian-ware/linkedin-content`), tenés versionado de todo el contenido

## Troubleshooting

| Problema | Solución |
|----------|----------|
| Cowork no detecta el SKILL.md | Verificá que el archivo se llama exactamente `SKILL.md` (mayúsculas) |
| Las imágenes no se regeneran | Verificá que Python 3 y Pillow estén instalados: `pip install Pillow` |
| Postiz no conecta | Verificá la API key y que el servidor de Postiz esté corriendo |
| El copy es muy largo | LinkedIn tiene límite de ~3000 caracteres. Pedile a Cowork que lo recorte |
