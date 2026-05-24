---
name: linkedin-publisher
description: >
  Gestión y publicación de la serie "Construyendo Veridian" para LinkedIn.
  Lee posts en formato markdown con frontmatter YAML, regenera imágenes,
  prepara copy para publicar, y opcionalmente programa vía Postiz API.
  Se activa cuando el usuario menciona LinkedIn, posts, publicar, o contenido.
---

# LinkedIn Publisher — Veridian

## Contexto de marca

- **Marca**: Veridian — software empresarial para PyMEs industriales
- **Tono**: directo, primera persona, técnico pero accesible, argentino (voseo)
- **Serie**: "Construyendo Veridian" — posts secuenciales con identidad visual coherente
- **Productos**: AuthKit Express ($79, en Gumroad), WorkKit Express (próximo), Veridian ERP (waitlist)
- **Autor**: Walter — 15 años mantenimiento industrial + fullstack dev

## Estructura de la carpeta

```
veridian-linkedin/
├── SKILL.md                ← este archivo
├── README.md               ← guía operativa
├── NN-slug/
│   ├── post.md             ← copy + frontmatter YAML
│   └── imagen.png          ← imagen lista para LinkedIn (1200x1200)
└── _assets/
    └── generate_images.py  ← generador de imágenes (Pillow)
```

Cada `post.md` tiene frontmatter con:
- `estado`: draft | listo | publicado
- `fecha_sugerida`: fecha planificada (YYYY-MM-DD)
- `serie`, `post_num`, `tags`, `audiencia`, `objetivo`

## Workflows disponibles

### 1. Revisar pipeline

Cuando el usuario pida ver el estado de los posts:

1. Leer todos los `post.md` en cada subcarpeta
2. Extraer `titulo`, `estado`, `fecha_sugerida`, `post_num`
3. Mostrar tabla ordenada por `post_num`:

| # | Título | Estado | Fecha |
|---|--------|--------|-------|

### 2. Preparar próximo post

Cuando el usuario diga "preparar el siguiente" o "qué publico hoy":

1. Buscar el primer post con `estado: draft` ordenado por `post_num`
2. Mostrar el copy completo
3. Mostrar la imagen (verificar que existe)
4. Preguntar si quiere ajustes antes de cambiar estado a `listo`
5. Si aprueba: cambiar `estado: draft` → `estado: listo` y agregar `fecha_real: [hoy]`

### 3. Crear nuevo post

Cuando el usuario pida un post nuevo:

1. Identificar el próximo número disponible (ver carpetas existentes)
2. Preguntar tema, audiencia, ángulo
3. Crear carpeta `NN-slug/`
4. Generar `post.md` siguiendo el formato de los existentes:
   - Frontmatter completo
   - Copy en el tono de Walter (párrafos cortos, voseo, anécdotas industriales)
   - Sección de notas internas con estrategia
   - Hashtags relevantes (no repetir exactos entre posts)
5. Ejecutar la función correspondiente en `_assets/generate_images.py` para generar la imagen
   - O crear una nueva función siguiendo el patrón visual existente

### 4. Regenerar imagen

Cuando el usuario pida cambiar una imagen:

1. Editar la función correspondiente en `generate_images.py`
2. Ejecutar: `python3 _assets/generate_images.py`
3. Verificar resultado mostrando la imagen

### 5. Publicar (requiere Postiz o scheduler configurado)

Cuando el usuario diga "publicar" o "programar":

1. Verificar que el post tiene `estado: listo`
2. Confirmar con el usuario: mostrar copy + imagen + fecha
3. Si hay scheduler (Postiz) configurado:
   - Subir imagen vía API
   - Crear post con copy y programar fecha
   - Actualizar `estado: listo` → `estado: publicado`
   - Agregar `fecha_publicacion: [timestamp]` al frontmatter
4. Si NO hay scheduler:
   - Copiar copy al clipboard
   - Indicar que suba `imagen.png` manualmente a LinkedIn
   - Actualizar estado después de confirmar

### 6. Análisis post-publicación

Cuando el usuario pregunte por resultados:

1. Listar posts con `estado: publicado`
2. Si hay datos de engagement (guardados manualmente en frontmatter):
   - `likes`, `comentarios`, `compartidos`, `impresiones`
3. Sugerir ajustes para próximos posts basándose en qué funcionó

## Reglas de copy

- Máximo 3000 caracteres por post (límite LinkedIn)
- Hook en las primeras 2 líneas (lo que se ve antes de "...ver más")
- No más de 6 hashtags por post
- No repetir hashtags exactos entre posts consecutivos
- Usar ▸ en lugar de bullets tradicionales
- Incluir pregunta final como CTA (genera comentarios)
- No mencionar precios en posts de storytelling
- Mencionar precios solo en posts de producto con link directo

## Reglas de imágenes

- Formato: 1200×1200 px PNG (cuadrado, óptimo mobile)
- Paleta: fondo #0a0e1a, acento #00ff88, secundario #06b6d4
- Display: Bebas Neue (en /fonts/ o bajar de GitHub dharmatype)
- Cuerpo: DejaVu Sans (sistema)
- Marca: punto verde + "VERIDIAN" + tagline en cada imagen
- Grid sutil de fondo en todas las imágenes
- Corner tag con número de post y categoría

## Integración con Postiz (opcional)

Si el usuario configura Postiz:

```bash
# Variables de entorno necesarias
export POSTIZ_API_KEY=tu_api_key
```

Endpoint para crear post:
```
POST https://app.postiz.com/api/posts
Content-Type: application/json
Authorization: Bearer $POSTIZ_API_KEY

{
  "content": "copy del post",
  "integration_id": "id_de_linkedin",
  "schedule": "2026-06-01T13:00:00Z",
  "media": ["url_o_base64_de_imagen"]
}
```

Antes de publicar SIEMPRE mostrar preview y pedir confirmación explícita.
