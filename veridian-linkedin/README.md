# Veridian — Serie de LinkedIn "Construyendo Veridian"

Vault con 6 publicaciones listas para LinkedIn, con imágenes de marca y notas internas de estrategia.

## Estructura del vault

```
veridian-linkedin/
├── README.md                        ← este archivo
├── 01-hero-marca/
│   ├── post.md                      ← copy listo para pegar en LinkedIn
│   └── imagen.png                   ← imagen para subir
├── 02-erp-modular/
├── 03-origen-industrial/
├── 04-authkit-velocidad/
├── 05-dolor-mantenimiento/
├── 06-stack-confianza/
└── _assets/
    └── generate_images.py           ← script generador (reutilizable)
```

## Calendario sugerido de publicación

| # | Post | Tipo | Audiencia | Día sugerido |
|---|------|------|-----------|--------------|
| 01 | Manifiesto: sin licencias eternas | Hook | PyMEs en general | Martes 10 AM |
| 02 | ERP no necesita 200 módulos | Producto | Gerentes operativos | Viernes 10 AM (3 días después) |
| 03 | 15 años en planta | Historia personal | Todos | Martes siguiente |
| 04 | AuthKit en 5 minutos | Producto / venta | Devs / CTOs | Jueves |
| 05 | Excel = grito de auxilio | Dolor | Mantenimiento | Martes siguiente |
| 06 | Stack que corre en planta | Cierre técnico | Compradores técnicos | Jueves |

**Cadencia**: 2 posts por semana (martes y jueves o viernes). 3 semanas de contenido. Después: medir, iterar.

## Cómo usar este vault

### Si usás Obsidian
1. Abrí Obsidian y "Open folder as vault" → seleccioná `veridian-linkedin/`
2. Cada `post.md` tiene frontmatter con `tags`, `estado` y `fecha_sugerida`
3. Cambiá `estado: draft` → `estado: publicado` cuando lo publiques
4. Las imágenes se ven embebidas con `![[imagen.png]]`

### Si solo usás carpetas
1. Cada subcarpeta es una publicación autocontenida
2. Abrí `post.md` con cualquier editor (es markdown plano)
3. La imagen está al lado lista para subir a LinkedIn

### Flujo de publicación
1. Abrí la subcarpeta del post que toca
2. Copiá el copy desde "Copy (listo para pegar en LinkedIn)" hasta el último hashtag
3. Subí `imagen.png` a LinkedIn primero
4. Pegá el copy
5. Publicá
6. Marcá `estado: publicado` y agregá `fecha_real:` al frontmatter

## Identidad visual

Todas las imágenes comparten:

- **Tamaño**: 1200×1200 px (cuadrado, óptimo para feed mobile)
- **Fondo**: `#0a0e1a` (mismo dark theme de la landing)
- **Acento principal**: `#00ff88` (verde tech Veridian)
- **Acento secundario**: `#06b6d4` (cyan)
- **Display**: Bebas Neue (igual que la landing en producción)
- **Cuerpo**: DejaVu Sans (sustituto cercano a Inter)
- **Marca**: punto verde + "VERIDIAN" + tagline en cada imagen

## Regenerar imágenes

Si querés modificar copy, colores o layout:

```bash
cd veridian-linkedin
python3 _assets/generate_images.py
```

Las funciones `image_01_hero()` a `image_06_stack()` son independientes — podés correr una sola y regenerar solo esa.

## Recomendaciones operativas

- **Responder comentarios en las primeras 2 horas** del post para empujar alcance
- **No publicar dos posts el mismo día** — pierden alcance entre sí
- **Pinear el post 06** una vez publicado: es el que mejor convierte a DM
- **Trackear DMs y clicks a Gumroad** antes/después de cada publicación
- **No copiar/pegar literal** los hashtags entre posts — LinkedIn castiga la repetición exacta

## Próximos pasos sugeridos (después de estos 6)

- Post de caso real (cuando haya un cliente con permiso de mencionar)
- Behind-the-scenes: pantalla de Antigravity usándolo para WorkKit
- Comparativa honesta: Veridian vs ERP "líder" (sin nombres, con tabla)
- Post de error: qué rompí y qué aprendí construyendo esto
- Live demo del ERP completo en video corto

## Subir a GitHub

Para versionar en `github.com/veridian-ware` (según tu preferencia):

```bash
cd veridian-linkedin
git init
git add .
git commit -m "Serie inicial: 6 posts Construyendo Veridian"
git branch -M main
git remote add origin git@github.com:veridian-ware/linkedin-content.git
git push -u origin main
```

(El repo `linkedin-content` lo tenés que crear vos en GitHub primero — yo no tengo permisos para crear repos en tu org. Una vez creado, los comandos de arriba lo dejan sincronizado.)
