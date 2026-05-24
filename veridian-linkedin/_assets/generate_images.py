"""
Generador de imágenes para publicaciones de LinkedIn — Marca Veridian
Estilo: dark theme, acento verde tech, tipografía Bebas Neue (display) + DejaVu Sans (cuerpo)
Tamaño: 1200x1200 (óptimo para feed mobile de LinkedIn)
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
import math
import random

# Paths
FONTS_DIR = "/home/claude/fonts"
OUT_DIR = "/home/claude/veridian-linkedin"

# Brand palette - Veridian
BG = (10, 14, 26)               # #0a0e1a deep dark blue-black
BG_ALT = (15, 23, 42)           # #0f172a
PANEL = (17, 24, 39)            # #111827
GRID = (30, 41, 59)             # #1e293b subtle grid
ACCENT = (0, 255, 136)          # #00ff88 brand green
ACCENT_DIM = (0, 200, 110)      # darker variant
CYAN = (6, 182, 212)            # #06b6d4
WHITE = (255, 255, 255)
GRAY = (148, 163, 184)          # #94a3b8
GRAY_DARK = (71, 85, 105)       # #475569
RED_HOT = (239, 68, 68)         # for "pain" visuals

# Canvas
W, H = 1200, 1200

def font(name, size):
    """Load font from /home/claude/fonts or fall back to DejaVu."""
    paths = {
        "bebas":      f"{FONTS_DIR}/BebasNeue-Regular.ttf",
        "bebas_bold": f"{FONTS_DIR}/BebasNeue-Bold.ttf",
        "sans":       "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "sans_bold":  "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "mono":       "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
        "mono_bold":  "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf",
    }
    return ImageFont.truetype(paths[name], size)

def new_canvas():
    img = Image.new("RGB", (W, H), BG)
    return img

def draw_grid(draw, spacing=60, color=GRID, opacity_alpha=None):
    """Draw subtle grid background."""
    for x in range(0, W, spacing):
        draw.line([(x, 0), (x, H)], fill=color, width=1)
    for y in range(0, H, spacing):
        draw.line([(0, y), (W, y)], fill=color, width=1)

def draw_glow_blob(img, center, radius, color, alpha_max=80):
    """Draw a soft radial glow blob using a separate alpha layer."""
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    steps = 30
    for i in range(steps, 0, -1):
        a = int(alpha_max * (i / steps) ** 2 * 0.15)
        r = int(radius * i / steps)
        od.ellipse([center[0]-r, center[1]-r, center[0]+r, center[1]+r],
                   fill=(color[0], color[1], color[2], a))
    overlay = overlay.filter(ImageFilter.GaussianBlur(20))
    img.paste(overlay, (0, 0), overlay)

def draw_brand_mark(draw, x=60, y=H-90):
    """Small VERIDIAN brand mark - bottom of every image."""
    # Logo dot
    draw.ellipse([x, y+12, x+18, y+30], fill=ACCENT)
    # Wordmark
    f = font("bebas_bold", 38)
    draw.text((x+30, y), "VERIDIAN", font=f, fill=WHITE)
    # Tagline
    f2 = font("sans", 14)
    draw.text((x+30, y+44), "Software para empresas que producen", font=f2, fill=GRAY)

def draw_corner_tag(draw, text, color=ACCENT):
    """Top-right small tag like 'CASE 01 / SOFTWARE'."""
    f = font("mono_bold", 16)
    bbox = draw.textbbox((0, 0), text, font=f)
    tw = bbox[2] - bbox[0]
    x = W - 60 - tw
    y = 60
    # underline accent
    draw.rectangle([x-12, y+30, x-4, y+38], fill=color)
    draw.text((x, y), text, font=f, fill=WHITE)

def wrap_text(text, fnt, max_width, draw):
    """Wrap text into lines fitting max_width."""
    words = text.split()
    lines = []
    cur = ""
    for w in words:
        test = (cur + " " + w).strip()
        bbox = draw.textbbox((0, 0), test, font=fnt)
        if bbox[2] - bbox[0] <= max_width:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

# ─────────────────────────────────────────────────────────────────────────────
# IMAGE 01 — HERO / MARCA
# Mensaje: "Software empresarial sin licencias eternas"
# ─────────────────────────────────────────────────────────────────────────────
def image_01_hero():
    img = new_canvas()
    draw = ImageDraw.Draw(img)
    draw_grid(draw)

    # Ambient glows
    draw_glow_blob(img, (200, 200), 500, ACCENT)
    draw_glow_blob(img, (1000, 1050), 600, CYAN, alpha_max=60)

    draw = ImageDraw.Draw(img)  # re-acquire after paste

    # Faux terminal panel in background (decorative)
    panel_x, panel_y, panel_w, panel_h = 700, 700, 460, 420
    draw.rounded_rectangle([panel_x, panel_y, panel_x+panel_w, panel_y+panel_h],
                           radius=14, fill=PANEL, outline=GRID, width=2)
    # Window dots
    for i, c in enumerate([(239,68,68), (250,204,21), (74,222,128)]):
        draw.ellipse([panel_x+20+i*22, panel_y+18, panel_x+34+i*22, panel_y+32], fill=c)
    # Code lines (decorative)
    f_mono = font("mono", 14)
    lines = [
        ("$ ", ACCENT, "npm run deploy"),
        ("", WHITE, ""),
        ("→ ", CYAN, "Building Veridian ERP..."),
        ("✓ ", ACCENT, "auth module ready"),
        ("✓ ", ACCENT, "workorders module ready"),
        ("✓ ", ACCENT, "inventory module ready"),
        ("✓ ", ACCENT, "dashboard module ready"),
        ("", WHITE, ""),
        ("→ ", CYAN, "Tu PyME, online en minutos."),
    ]
    ly = panel_y + 60
    for prefix, pc, rest in lines:
        if prefix:
            draw.text((panel_x+24, ly), prefix, font=f_mono, fill=pc)
            bbox = draw.textbbox((0,0), prefix, font=f_mono)
            draw.text((panel_x+24+bbox[2]-bbox[0], ly), rest, font=f_mono, fill=GRAY)
        ly += 26

    # Corner tag
    draw_corner_tag(draw, "01 / MANIFIESTO")

    # Main headline
    f_huge = font("bebas_bold", 130)
    f_big = font("bebas_bold", 130)
    draw.text((60, 200), "SOFTWARE", font=f_huge, fill=WHITE)
    draw.text((60, 320), "EMPRESARIAL", font=f_huge, fill=WHITE)
    # Accent line
    draw.text((60, 440), "SIN LICENCIAS", font=f_huge, fill=ACCENT)
    draw.text((60, 560), "ETERNAS.", font=f_huge, fill=ACCENT)

    # Subhead
    f_sub = font("sans", 26)
    sub_lines = [
        "ERP modular, propio, desplegado en tu",
        "infraestructura. Pagás una vez. Es tuyo."
    ]
    sy = 720
    for ln in sub_lines:
        draw.text((60, sy), ln, font=f_sub, fill=GRAY)
        sy += 36

    draw_brand_mark(draw)
    img.save(f"{OUT_DIR}/01-hero-marca/imagen.png", "PNG", optimize=True)
    print("✓ 01-hero-marca/imagen.png")

# ─────────────────────────────────────────────────────────────────────────────
# IMAGE 02 — ERP MODULAR
# Mensaje: "Tu ERP no necesita 200 módulos. Solo los que usás."
# ─────────────────────────────────────────────────────────────────────────────
def image_02_modular():
    img = new_canvas()
    draw = ImageDraw.Draw(img)
    draw_grid(draw)

    draw_glow_blob(img, (900, 300), 500, ACCENT)
    draw = ImageDraw.Draw(img)

    draw_corner_tag(draw, "02 / PRODUCTO")

    # Headline
    f_h = font("bebas_bold", 110)
    draw.text((60, 110), "TU ERP NO NECESITA", font=f_h, fill=WHITE)
    f_acc = font("bebas_bold", 180)
    draw.text((60, 210), "200 MÓDULOS.", font=f_acc, fill=ACCENT)
    f_h2 = font("bebas_bold", 90)
    draw.text((60, 400), "SOLO LOS QUE", font=f_h2, fill=WHITE)
    draw.text((60, 485), "REALMENTE USÁS.", font=f_h2, fill=WHITE)

    # Modules grid - 4 columns x 2 rows of cards
    modules = [
        ("AUTH", "Roles & permisos", True),
        ("WORK", "Órdenes de trabajo", True),
        ("INV",  "Inventario", True),
        ("HR",   "Personal", True),
        ("BUY",  "Compras", False),
        ("DASH", "Dashboard", False),
        ("AUTO", "Automatización", False),
        ("MON",  "Monitoreo", False),
    ]
    grid_y = 660
    card_w, card_h = 250, 200
    gap = 30
    start_x = 60
    for i, (code, name, active) in enumerate(modules):
        col = i % 4
        row = i // 4
        x = start_x + col * (card_w + gap)
        y = grid_y + row * (card_h + gap)
        # Card
        fill = PANEL if active else BG_ALT
        outline = ACCENT if active else GRID
        draw.rounded_rectangle([x, y, x+card_w, y+card_h], radius=12,
                               fill=fill, outline=outline, width=2)
        # Code
        f_code = font("bebas_bold", 60)
        c_color = ACCENT if active else GRAY_DARK
        draw.text((x+20, y+30), code, font=f_code, fill=c_color)
        # Name
        f_name = font("sans_bold", 16)
        n_color = WHITE if active else GRAY_DARK
        draw.text((x+20, y+115), name, font=f_name, fill=n_color)
        # Status dot
        sc = ACCENT if active else GRAY_DARK
        draw.ellipse([x+card_w-32, y+20, x+card_w-20, y+32], fill=sc)
        # Status text
        f_st = font("mono", 11)
        st_text = "ACTIVO" if active else "OPCIONAL"
        draw.text((x+20, y+card_h-30), st_text, font=f_st, fill=sc)

    draw_brand_mark(draw)
    img.save(f"{OUT_DIR}/02-erp-modular/imagen.png", "PNG", optimize=True)
    print("✓ 02-erp-modular/imagen.png")

# ─────────────────────────────────────────────────────────────────────────────
# IMAGE 03 — ORIGEN INDUSTRIAL
# Mensaje: "15 años en la planta. Ahora construyo el software que faltaba."
# ─────────────────────────────────────────────────────────────────────────────
def image_03_origen():
    img = new_canvas()
    draw = ImageDraw.Draw(img)
    draw_grid(draw, spacing=80)

    draw_glow_blob(img, (1000, 1000), 700, ACCENT, alpha_max=70)
    draw_glow_blob(img, (200, 1100), 400, CYAN, alpha_max=50)
    draw = ImageDraw.Draw(img)

    draw_corner_tag(draw, "03 / ORIGEN")

    # Big number
    f_huge = font("bebas_bold", 460)
    # outline effect
    draw.text((60, 80), "15", font=f_huge, fill=ACCENT)
    # Year unit
    f_unit = font("bebas_bold", 90)
    draw.text((430, 200), "AÑOS", font=f_unit, fill=WHITE)
    draw.text((430, 290), "EN PLANTA.", font=f_unit, fill=WHITE)

    # divider
    draw.rectangle([60, 580, 1140, 584], fill=GRID)

    # Subhead
    f_h2 = font("bebas_bold", 80)
    draw.text((60, 620), "AHORA CONSTRUYO", font=f_h2, fill=WHITE)
    draw.text((60, 700), "EL SOFTWARE", font=f_h2, fill=WHITE)
    draw.text((60, 780), "QUE", font=f_h2, fill=WHITE)
    draw.text((196, 780), "FALTABA.", font=f_h2, fill=ACCENT)

    # Three timeline points
    timeline_y = 920
    points = [
        ("MANTENIMIENTO", "Industrial"),
        ("FULLSTACK DEV", "React + Node"),
        ("VERIDIAN", "Producto propio"),
    ]
    for i, (title, sub) in enumerate(points):
        x = 60 + i * 380
        # Dot
        is_last = i == len(points) - 1
        dot_color = ACCENT if is_last else WHITE
        draw.ellipse([x, timeline_y, x+24, timeline_y+24], fill=dot_color)
        # Connector
        if i < len(points) - 1:
            draw.rectangle([x+24, timeline_y+10, x+380, timeline_y+14], fill=GRID)
        # Text
        f_t = font("bebas_bold", 32)
        draw.text((x, timeline_y+40), title, font=f_t,
                  fill=ACCENT if is_last else WHITE)
        f_s = font("sans", 16)
        draw.text((x, timeline_y+80), sub, font=f_s, fill=GRAY)

    draw_brand_mark(draw)
    img.save(f"{OUT_DIR}/03-origen-industrial/imagen.png", "PNG", optimize=True)
    print("✓ 03-origen-industrial/imagen.png")

# ─────────────────────────────────────────────────────────────────────────────
# IMAGE 04 — AUTHKIT VELOCIDAD
# Mensaje: "JWT + RBAC listo en 5 minutos. No 5 semanas."
# ─────────────────────────────────────────────────────────────────────────────
def image_04_velocidad():
    img = new_canvas()
    draw = ImageDraw.Draw(img)
    draw_grid(draw)

    draw_glow_blob(img, (900, 400), 500, ACCENT)
    draw = ImageDraw.Draw(img)

    draw_corner_tag(draw, "04 / AUTHKIT EXPRESS")

    # Top label
    f_t = font("bebas_bold", 50)
    draw.text((60, 130), "JWT + RBAC PARA EXPRESS.JS", font=f_t, fill=GRAY)

    # ── Big winner row: "5 MIN" all in one line, all green
    # Use a single font size so baseline is consistent
    f_main = font("bebas_bold", 240)
    draw.text((60, 200), "5 MIN.", font=f_main, fill=ACCENT)

    # Tag pill: AHORA
    f_pill = font("mono_bold", 18)
    pill_text = "AHORA"
    pbox = draw.textbbox((0,0), pill_text, font=f_pill)
    pw = pbox[2]-pbox[0]+24
    draw.rounded_rectangle([60, 470, 60+pw, 470+34], radius=17,
                           fill=ACCENT)
    draw.text((72, 477), pill_text, font=f_pill, fill=BG)

    # ── Loser row: "5 SEMANAS" all grayed
    draw.text((60, 540), "5 SEMANAS.", font=f_main, fill=GRAY_DARK)
    # Strike line - measure actual text width
    sbbox = draw.textbbox((60, 540), "5 SEMANAS.", font=f_main)
    strike_y = (sbbox[1] + sbbox[3]) // 2 + 10
    draw.line([(sbbox[0]-10, strike_y), (sbbox[2]+10, strike_y)], fill=RED_HOT, width=10)

    # Tag pill: ANTES
    pill_text2 = "ANTES"
    pbox2 = draw.textbbox((0,0), pill_text2, font=f_pill)
    pw2 = pbox2[2]-pbox2[0]+24
    draw.rounded_rectangle([60, 810, 60+pw2, 810+34], radius=17,
                           fill=GRAY_DARK)
    draw.text((72, 817), pill_text2, font=f_pill, fill=WHITE)

    # ── Code snippet panel at bottom
    panel_y = 890
    draw.rounded_rectangle([60, panel_y, 1140, panel_y+220], radius=14,
                           fill=PANEL, outline=GRID, width=2)
    # window dots
    for i, c in enumerate([(239,68,68), (250,204,21), (74,222,128)]):
        draw.ellipse([80+i*20, panel_y+16, 92+i*20, panel_y+28], fill=c)
    f_filename = font("mono", 14)
    draw.text((180, panel_y+15), "server.js", font=f_filename, fill=GRAY)

    # Code — render token by token using actual measured width
    f_code = font("mono_bold", 24)
    line_y = panel_y + 60
    x = 90
    tokens = [
        ("const ", CYAN),
        ("auth ", WHITE),
        ("= ", GRAY),
        ("require(", GRAY),
        ("'@veridian/authkit'", ACCENT),
        (")", GRAY),
    ]
    for txt, col in tokens:
        draw.text((x, line_y), txt, font=f_code, fill=col)
        bb = draw.textbbox((x, line_y), txt, font=f_code)
        x = bb[2]

    line_y += 40
    draw.text((90, line_y), "app.use(", font=f_code, fill=WHITE)
    bb = draw.textbbox((90, line_y), "app.use(", font=f_code)
    draw.text((bb[2], line_y), "auth.middleware()", font=f_code, fill=ACCENT)
    bb2 = draw.textbbox((bb[2], line_y), "auth.middleware()", font=f_code)
    draw.text((bb2[2], line_y), ")", font=f_code, fill=WHITE)

    line_y += 50
    draw.text((90, line_y), "// JWT + RBAC listo. Eso es todo.", font=f_code, fill=GRAY_DARK)

    draw_brand_mark(draw)
    img.save(f"{OUT_DIR}/04-authkit-velocidad/imagen.png", "PNG", optimize=True)
    print("✓ 04-authkit-velocidad/imagen.png")

# ─────────────────────────────────────────────────────────────────────────────
# IMAGE 05 — DOLOR MANTENIMIENTO
# Mensaje: "Excel para órdenes de trabajo es un grito de auxilio."
# ─────────────────────────────────────────────────────────────────────────────
def image_05_dolor():
    img = new_canvas()
    draw = ImageDraw.Draw(img)
    draw_grid(draw)

    draw_glow_blob(img, (300, 300), 500, RED_HOT, alpha_max=70)
    draw_glow_blob(img, (1000, 1000), 500, ACCENT, alpha_max=70)
    draw = ImageDraw.Draw(img)

    draw_corner_tag(draw, "05 / DIAGNÓSTICO", color=RED_HOT)

    # Headline
    f_h = font("bebas_bold", 110)
    draw.text((60, 130), "EXCEL PARA", font=f_h, fill=WHITE)
    draw.text((60, 230), "ÓRDENES DE", font=f_h, fill=WHITE)
    draw.text((60, 330), "TRABAJO", font=f_h, fill=WHITE)

    # red highlight
    f_h2 = font("bebas_bold", 130)
    draw.text((60, 440), "ES UN GRITO", font=f_h2, fill=RED_HOT)
    draw.text((60, 560), "DE AUXILIO.", font=f_h2, fill=RED_HOT)

    # Chaotic vs ordered visual
    # Left: chaotic Excel mock
    chaos_x, chaos_y = 60, 760
    draw.rounded_rectangle([chaos_x, chaos_y, chaos_x+520, chaos_y+280], radius=12,
                           fill=PANEL, outline=RED_HOT, width=2)
    f_title = font("mono_bold", 14)
    draw.text((chaos_x+20, chaos_y+15), "OT_MARZO_v8_FINAL_revisado(2).xlsx", font=f_title, fill=RED_HOT)
    # fake rows
    f_row = font("mono", 11)
    rows = [
        ("OT-001", "??? motor 3", "pendient", "Juan"),
        ("OT-002", "rev. bomba", "?", "?"),
        ("OT-?",  "TBD", "URGENTE!!", ""),
        ("",       "ver mail Juan", "", ""),
        ("OT-003", "filtro aceite", "ok", "Pedro"),
        ("???",    "???", "borrar", ""),
        ("OT-005", "ver chat WSP", "??", ""),
    ]
    ry = chaos_y + 50
    for r in rows:
        for i, cell in enumerate(r):
            draw.text((chaos_x+20+i*120, ry), cell, font=f_row, fill=GRAY)
        ry += 28
        draw.line([(chaos_x+15, ry-4), (chaos_x+510, ry-4)], fill=GRID, width=1)

    # Right: ordered Veridian mock
    ord_x = 620
    draw.rounded_rectangle([ord_x, chaos_y, ord_x+520, chaos_y+280], radius=12,
                           fill=PANEL, outline=ACCENT, width=2)
    draw.text((ord_x+20, chaos_y+15), "Veridian / Work Orders", font=f_title, fill=ACCENT)
    # status pills
    statuses = [
        ("OT-2401", "Motor línea 3",    "ABIERTA",   ACCENT),
        ("OT-2402", "Bomba sector B",   "EN CURSO",  CYAN),
        ("OT-2403", "Filtro aceite",    "CERRADA",   GRAY),
        ("OT-2404", "Rev. preventiva",  "PROGRAM.",  ACCENT),
        ("OT-2405", "Cambio rodam.",    "EN CURSO",  CYAN),
        ("OT-2406", "Calibración",      "ABIERTA",   ACCENT),
        ("OT-2407", "Lubricación",      "PROGRAM.",  ACCENT),
    ]
    ry = chaos_y + 50
    for code, desc, status, col in statuses:
        draw.text((ord_x+20, ry), code, font=f_row, fill=WHITE)
        draw.text((ord_x+110, ry), desc, font=f_row, fill=GRAY)
        # status pill
        f_pill = font("mono_bold", 10)
        bbox = draw.textbbox((0,0), status, font=f_pill)
        pw = bbox[2]-bbox[0]+16
        draw.rounded_rectangle([ord_x+520-pw-15, ry-2, ord_x+520-15, ry+16],
                               radius=8, outline=col, width=1)
        draw.text((ord_x+520-pw-7, ry), status, font=f_pill, fill=col)
        ry += 28
        draw.line([(ord_x+15, ry-4), (ord_x+510, ry-4)], fill=GRID, width=1)

    draw_brand_mark(draw)
    img.save(f"{OUT_DIR}/05-dolor-mantenimiento/imagen.png", "PNG", optimize=True)
    print("✓ 05-dolor-mantenimiento/imagen.png")

# ─────────────────────────────────────────────────────────────────────────────
# IMAGE 06 — STACK / CONFIANZA
# Mensaje: "El stack que corre en planta."
# ─────────────────────────────────────────────────────────────────────────────
def image_06_stack():
    img = new_canvas()
    draw = ImageDraw.Draw(img)
    draw_grid(draw)

    draw_glow_blob(img, (600, 600), 700, ACCENT, alpha_max=60)
    draw = ImageDraw.Draw(img)

    draw_corner_tag(draw, "06 / STACK")

    # Headline
    f_h = font("bebas_bold", 140)
    draw.text((60, 130), "EL STACK QUE", font=f_h, fill=WHITE)
    draw.text((60, 260), "CORRE EN", font=f_h, fill=WHITE)
    draw.text((60, 390), "PLANTA.", font=f_h, fill=ACCENT)

    # Subhead
    f_sub = font("sans", 24)
    draw.text((60, 540), "No es \"un MVP\". Es producción real,", font=f_sub, fill=GRAY)
    draw.text((60, 576), "con dolores resueltos, sobre tecnología sólida.", font=f_sub, fill=GRAY)

    # Stack badges - 2 rows x 4 cols
    stack = [
        ("REACT 18",      "Frontend"),
        ("NODE.JS",       "Runtime"),
        ("EXPRESS",       "API"),
        ("POSTGRESQL",    "Datos"),
        ("SEQUELIZE",     "ORM"),
        ("REDIS",         "Cache"),
        ("DOCKER",        "Containers"),
        ("RAILWAY",       "Deploy"),
    ]
    badge_w, badge_h = 250, 130
    gap = 30
    start_x = 60
    start_y = 680
    for i, (name, role) in enumerate(stack):
        col = i % 4
        row = i // 4
        x = start_x + col * (badge_w + gap)
        y = start_y + row * (badge_h + gap)
        draw.rounded_rectangle([x, y, x+badge_w, y+badge_h], radius=12,
                               fill=PANEL, outline=GRID, width=2)
        # Top accent line
        draw.rectangle([x, y, x+badge_w, y+4], fill=ACCENT)
        # Name
        f_n = font("bebas_bold", 38)
        draw.text((x+20, y+22), name, font=f_n, fill=WHITE)
        # Role
        f_r = font("mono", 14)
        draw.text((x+20, y+75), role.upper(), font=f_r, fill=ACCENT)
        # bottom mini line decoration
        draw.line([(x+20, y+105), (x+60, y+105)], fill=ACCENT, width=2)

    draw_brand_mark(draw)
    img.save(f"{OUT_DIR}/06-stack-confianza/imagen.png", "PNG", optimize=True)
    print("✓ 06-stack-confianza/imagen.png")

# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    image_01_hero()
    image_02_modular()
    image_03_origen()
    image_04_velocidad()
    image_05_dolor()
    image_06_stack()
    print("\nTodas las imágenes generadas.")
