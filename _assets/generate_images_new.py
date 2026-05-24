"""
Generador de imágenes para posts 07-15 — Veridian LinkedIn
Mismo estilo que generate_images.py original.
Ejecutar desde la raíz del proyecto:
  python3 _assets/generate_images_new.py
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os, sys
sys.stdout.reconfigure(encoding='utf-8')

# ── Paths ─────────────────────────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DIR    = os.path.join(SCRIPT_DIR, "..")          # veridian-linkedin/
FONTS_DIR  = os.path.join(SCRIPT_DIR, "..", "fonts") # optional

# ── Brand palette ─────────────────────────────────────────────────────────────
BG        = (10, 14, 26)
BG_ALT    = (15, 23, 42)
PANEL     = (17, 24, 39)
GRID      = (30, 41, 59)
ACCENT    = (0, 255, 136)
ACCENT_DIM= (0, 200, 110)
CYAN      = (6, 182, 212)
WHITE     = (255, 255, 255)
GRAY      = (148, 163, 184)
GRAY_DARK = (71, 85, 105)
RED_HOT   = (239, 68, 68)
AMBER     = (251, 191, 36)

W, H = 1200, 1200

# ── Font loader ───────────────────────────────────────────────────────────────
def font(name, size):
    paths = {
        "bebas":      os.path.join(FONTS_DIR, "BebasNeue-Regular.ttf"),
        "bebas_bold": os.path.join(FONTS_DIR, "BebasNeue-Bold.ttf"),
        "sans":       "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "sans_bold":  "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "mono":       "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
        "mono_bold":  "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf",
    }
    try:
        return ImageFont.truetype(paths[name], size)
    except Exception:
        try:
            return ImageFont.truetype(paths["sans"], size)
        except Exception:
            return ImageFont.load_default()

def new_canvas():
    return Image.new("RGB", (W, H), BG)

def draw_grid(draw, spacing=60, color=GRID):
    for x in range(0, W, spacing):
        draw.line([(x, 0), (x, H)], fill=color, width=1)
    for y in range(0, H, spacing):
        draw.line([(0, y), (W, y)], fill=color, width=1)

def draw_glow_blob(img, center, radius, color, alpha_max=80):
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    for i in range(30, 0, -1):
        a = int(alpha_max * (i / 30) ** 2 * 0.15)
        r = int(radius * i / 30)
        od.ellipse([center[0]-r, center[1]-r, center[0]+r, center[1]+r],
                   fill=(color[0], color[1], color[2], a))
    overlay = overlay.filter(ImageFilter.GaussianBlur(20))
    img.paste(overlay, (0, 0), overlay)

def draw_brand_mark(draw, x=60, y=H-90):
    draw.ellipse([x, y+12, x+18, y+30], fill=ACCENT)
    f = font("bebas_bold", 38)
    draw.text((x+30, y), "VERIDIAN", font=f, fill=WHITE)
    f2 = font("sans", 14)
    draw.text((x+30, y+44), "Software para empresas que producen", font=f2, fill=GRAY)

def draw_corner_tag(draw, text, color=ACCENT):
    f = font("mono_bold", 16)
    bbox = draw.textbbox((0, 0), text, font=f)
    tw = bbox[2] - bbox[0]
    x = W - 60 - tw
    draw.rectangle([x-12, 90, x-4, 98], fill=color)
    draw.text((x, 60), text, font=f, fill=WHITE)

def save(img, folder, filename="imagen.png"):
    path = os.path.join(OUT_DIR, folder, filename)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    img.save(path, "PNG", optimize=True)
    print(f"✓ {folder}/{filename}")


# ─────────────────────────────────────────────────────────────────────────────
# 07 — DOCKER TIP
# ─────────────────────────────────────────────────────────────────────────────
def image_07_docker():
    img = new_canvas()
    draw = ImageDraw.Draw(img)
    draw_grid(draw)
    draw_glow_blob(img, (900, 300), 500, CYAN, alpha_max=70)
    draw_glow_blob(img, (200, 900), 400, ACCENT, alpha_max=50)
    draw = ImageDraw.Draw(img)
    draw_corner_tag(draw, "07 / TIP TÉCNICO", color=CYAN)

    f_h = font("bebas_bold", 100)
    draw.text((60, 110), "NODE + POSTGRES", font=f_h, fill=WHITE)
    f_h2 = font("bebas_bold", 170)
    draw.text((60, 200), "EN 3 MIN", font=f_h2, fill=ACCENT)
    f_sub = font("bebas_bold", 80)
    draw.text((60, 370), "CON DOCKER.", font=f_sub, fill=CYAN)

    # Terminal panel
    py = 500
    draw.rounded_rectangle([60, py, 1140, py+580], radius=14, fill=PANEL, outline=GRID, width=2)
    for i, c in enumerate([(239,68,68),(250,204,21),(74,222,128)]):
        draw.ellipse([80+i*22, py+18, 94+i*22, py+32], fill=c)
    draw.text((160, py+16), "docker-compose.yml", font=font("mono", 14), fill=GRAY)

    f_c = font("mono_bold", 22)
    f_cm = font("mono", 22)
    lines = [
        [("services:", ACCENT)],
        [("  app:", WHITE)],
        [("    image: ", GRAY), ("node:20", CYAN)],
        [("    ports: ", GRAY), ("'3000:3000'", ACCENT)],
        [("    depends_on: ", GRAY), ("- db", WHITE)],
        [],
        [("  db:", WHITE)],
        [("    image: ", GRAY), ("postgres:15", CYAN)],
        [("    volumes:", GRAY)],
        [("      - ", GRAY), ("pgdata:/var/lib/postgresql/data", ACCENT)],
        [],
        [("volumes:", ACCENT)],
        [("  pgdata:", WHITE)],
    ]
    ly = py + 60
    for line in lines:
        lx = 90
        for txt, col in line:
            draw.text((lx, ly), txt, font=f_c, fill=col)
            bb = draw.textbbox((lx, ly), txt, font=f_c)
            lx = bb[2]
        ly += 38

    draw_brand_mark(draw)
    save(img, "07-docker-tip")


# ─────────────────────────────────────────────────────────────────────────────
# 08 — STOCK FANTASMA
# ─────────────────────────────────────────────────────────────────────────────
def image_08_stock():
    img = new_canvas()
    draw = ImageDraw.Draw(img)
    draw_grid(draw)
    draw_glow_blob(img, (300, 400), 600, RED_HOT, alpha_max=60)
    draw_glow_blob(img, (1000, 900), 400, ACCENT, alpha_max=50)
    draw = ImageDraw.Draw(img)
    draw_corner_tag(draw, "08 / CASO DE DOLOR", color=RED_HOT)

    f_h = font("bebas_bold", 115)
    draw.text((60, 110), "EL REPUESTO", font=f_h, fill=WHITE)
    draw.text((60, 220), "QUE EXISTE", font=f_h, fill=WHITE)
    draw.text((60, 330), "Y NO EXISTE.", font=f_h, fill=RED_HOT)

    # Inventory card — sistema dice que hay stock
    cx, cy = 60, 530
    draw.rounded_rectangle([cx, cy, cx+500, cy+260], radius=12,
                           fill=PANEL, outline=RED_HOT, width=2)
    f_label = font("mono_bold", 14)
    draw.text((cx+20, cy+16), "SISTEMA: stock disponible", font=f_label, fill=RED_HOT)
    f_item = font("sans_bold", 22)
    draw.text((cx+20, cy+60), "Rodamiento SKF 6205", font=f_item, fill=WHITE)
    f_qty = font("bebas_bold", 90)
    draw.text((cx+20, cy+90), "3", font=f_qty, fill=ACCENT)
    f_unit = font("sans", 18)
    draw.text((cx+100, cy+130), "unidades en depósito", font=f_unit, fill=GRAY)
    # warning
    f_warn = font("mono_bold", 18)
    draw.text((cx+20, cy+200), "⚠  técnico fue a buscarlos — NO ESTÁN", font=f_warn, fill=RED_HOT)

    # Real situation
    rx, ry = 620, 530
    draw.rounded_rectangle([rx, ry, rx+500, ry+260], radius=12,
                           fill=PANEL, outline=GRAY_DARK, width=2)
    draw.text((rx+20, ry+16), "REALIDAD: depósito vacío", font=f_label, fill=GRAY_DARK)
    f_zero = font("bebas_bold", 90)
    draw.text((rx+20, ry+90), "0", font=f_zero, fill=GRAY_DARK)
    draw.text((rx+100, ry+130), "unidades reales", font=f_unit, fill=GRAY_DARK)
    f_cost = font("sans", 16)
    draw.text((rx+20, ry+195), "→ Parada de línea. Compra de urgencia.", font=f_cost, fill=RED_HOT)

    # Bottom message
    f_msg = font("bebas_bold", 56)
    draw.text((60, 850), "EL REGISTRO TIENE QUE SER", font=f_msg, fill=WHITE)
    draw.text((60, 910), "TAN FÁCIL QUE NO HAYA EXCUSA.", font=f_msg, fill=ACCENT)

    draw_brand_mark(draw)
    save(img, "08-stock-fantasma")


# ─────────────────────────────────────────────────────────────────────────────
# 09 — ERP PRODUCCIÓN REAL
# ─────────────────────────────────────────────────────────────────────────────
def image_09_produccion():
    img = new_canvas()
    draw = ImageDraw.Draw(img)
    draw_grid(draw)
    draw_glow_blob(img, (600, 400), 600, ACCENT, alpha_max=70)
    draw = ImageDraw.Draw(img)
    draw_corner_tag(draw, "09 / ERP EN PRODUCCIÓN")

    f_h = font("bebas_bold", 100)
    draw.text((60, 110), "NO ES UN MVP", font=f_h, fill=GRAY_DARK)
    draw.text((60, 205), "EN MI LAPTOP.", font=f_h, fill=GRAY_DARK)
    f_h2 = font("bebas_bold", 120)
    draw.text((60, 340), "ES PRODUCCIÓN.", font=f_h2, fill=ACCENT)

    # Server architecture diagram
    dy = 530
    nodes = [
        (180,  dy,      "REACT 18",    "Frontend",   CYAN),
        (560,  dy,      "EXPRESS API",  "Node.js",    ACCENT),
        (940,  dy,      "POSTGRESQL",  "Database",   ACCENT),
        (180,  dy+280,  "REDIS",       "Cache",      CYAN),
        (560,  dy+280,  "DOCKER",      "Containers", GRAY),
        (940,  dy+280,  "RAILWAY",     "Deploy",     CYAN),
    ]
    bw, bh = 260, 200
    for nx, ny, name, role, col in nodes:
        draw.rounded_rectangle([nx-bw//2, ny, nx+bw//2, ny+bh],
                               radius=12, fill=PANEL, outline=col, width=2)
        draw.rectangle([nx-bw//2, ny, nx+bw//2, ny+4], fill=col)
        f_n = font("bebas_bold", 44)
        draw.text((nx-bw//2+20, ny+20), name, font=f_n, fill=WHITE)
        f_r = font("mono", 16)
        draw.text((nx-bw//2+20, ny+80), role.upper(), font=f_r, fill=col)
        # status dot
        draw.ellipse([nx+bw//2-34, ny+18, nx+bw//2-20, ny+32], fill=ACCENT)

    # Connector lines between columns
    for x1, x2, y_mid in [(180+bw//2, 560-bw//2, dy+100),
                           (560+bw//2, 940-bw//2, dy+100),
                           (180+bw//2, 560-bw//2, dy+380),
                           (560+bw//2, 940-bw//2, dy+380)]:
        draw.line([(x1, y_mid), (x2, y_mid)], fill=GRID, width=2)

    draw_brand_mark(draw)
    save(img, "09-authkit-caso-real")


# ─────────────────────────────────────────────────────────────────────────────
# 10 — POSTGRESQL VS MONGODB
# ─────────────────────────────────────────────────────────────────────────────
def image_10_postgres():
    img = new_canvas()
    draw = ImageDraw.Draw(img)
    draw_grid(draw)
    draw_glow_blob(img, (300, 600), 600, ACCENT, alpha_max=60)
    draw = ImageDraw.Draw(img)
    draw_corner_tag(draw, "10 / TIP TÉCNICO", color=CYAN)

    f_h = font("bebas_bold", 110)
    draw.text((60, 110), "POR QUÉ", font=f_h, fill=WHITE)
    draw.text((60, 215), "POSTGRESQL", font=f_h, fill=ACCENT)
    draw.text((60, 320), "PARA DATOS INDUSTRIALES.", font=font("bebas_bold", 70), fill=WHITE)

    # VS comparison
    col_w = 510
    left_x, right_x, card_y = 60, 630, 480
    card_h = 540

    # Postgres card
    draw.rounded_rectangle([left_x, card_y, left_x+col_w, card_y+card_h],
                           radius=12, fill=PANEL, outline=ACCENT, width=2)
    draw.rectangle([left_x, card_y, left_x+col_w, card_y+4], fill=ACCENT)
    f_title = font("bebas_bold", 52)
    draw.text((left_x+20, card_y+18), "POSTGRESQL", font=f_title, fill=ACCENT)
    f_tag = font("mono_bold", 13)
    draw.rounded_rectangle([left_x+20, card_y+80, left_x+120, card_y+100],
                           radius=10, fill=ACCENT)
    draw.text((left_x+30, card_y+82), "ELEGIDO", font=f_tag, fill=BG)

    reasons_pg = [
        "JOINs nativos e indexados",
        "Transacciones ACID reales",
        "Migraciones de schema versionadas",
        "Window functions para reportes",
        "Full-text search sin Elastic",
        "30 años de optimización",
    ]
    f_r = font("sans", 18)
    ry = card_y + 120
    for r in reasons_pg:
        draw.text((left_x+20, ry), "▸ " + r, font=f_r, fill=WHITE)
        ry += 36

    # MongoDB card
    draw.rounded_rectangle([right_x, card_y, right_x+col_w, card_y+card_h],
                           radius=12, fill=PANEL, outline=GRAY_DARK, width=2)
    draw.rectangle([right_x, card_y, right_x+col_w, card_y+4], fill=GRAY_DARK)
    draw.text((right_x+20, card_y+18), "MONGODB", font=f_title, fill=GRAY_DARK)
    draw.rounded_rectangle([right_x+20, card_y+80, right_x+155, card_y+100],
                           radius=10, fill=GRAY_DARK)
    draw.text((right_x+30, card_y+82), "OTRO CONTEXTO", font=f_tag, fill=WHITE)

    reasons_mongo = [
        "JOINs a mano en JavaScript",
        "Sin schema → migraciones manuales",
        "Ideal para logs y catálogos",
        "Datos semi-estructurados",
        "No para relaciones industriales",
        "No para 10 años de historial",
    ]
    ry = card_y + 120
    for r in reasons_mongo:
        draw.text((right_x+20, ry), "▸ " + r, font=f_r, fill=GRAY_DARK)
        ry += 36

    # VS badge
    f_vs = font("bebas_bold", 80)
    draw.text((556, 700), "VS", font=f_vs, fill=GRID)

    draw_brand_mark(draw)
    save(img, "10-postgres-vs-mongo")


# ─────────────────────────────────────────────────────────────────────────────
# 11 — CAMBIO DE TURNO
# ─────────────────────────────────────────────────────────────────────────────
def image_11_turno():
    img = new_canvas()
    draw = ImageDraw.Draw(img)
    draw_grid(draw, spacing=80)
    draw_glow_blob(img, (600, 600), 700, RED_HOT, alpha_max=50)
    draw = ImageDraw.Draw(img)
    draw_corner_tag(draw, "11 / CASO DE DOLOR", color=RED_HOT)

    f_h = font("bebas_bold", 105)
    draw.text((60, 110), "EL CAMBIO DE", font=f_h, fill=WHITE)
    draw.text((60, 210), "TURNO MÁS", font=f_h, fill=WHITE)
    draw.text((60, 310), "CARO DEL MUNDO.", font=font("bebas_bold", 80), fill=RED_HOT)

    # The quote
    quote_y = 470
    draw.rounded_rectangle([60, quote_y, 1140, quote_y+160], radius=14,
                           fill=PANEL, outline=RED_HOT, width=2)
    f_quote = font("bebas_bold", 70)
    draw.text((100, quote_y+20), '"CHE, LA PRENSA 3', font=f_quote, fill=WHITE)
    draw.text((100, quote_y+85), 'ESTÁ RARA. FIJATE."', font=f_quote, fill=RED_HOT)

    # The cost breakdown
    cost_y = 700
    f_label = font("mono_bold", 15)
    draw.text((60, cost_y), "LO QUE ESE 'FIJATE' INFORMAL CUESTA:", font=f_label, fill=GRAY)
    costs = [
        ("→", "Turno entrante arranca desde cero"),
        ("→", "Diagnóstico duplicado si vuelve a fallar"),
        ("→", "Decisiones sin historial ni contexto"),
        ("→", "Horas-hombre perdidas investigando lo mismo"),
        ("→", "Jefe sin respuesta cuando pregunta qué pasó"),
    ]
    f_cost = font("sans", 22)
    cy2 = cost_y + 50
    for arrow, text in costs:
        draw.text((60, cy2), arrow, font=f_cost, fill=RED_HOT)
        draw.text((100, cy2), text, font=f_cost, fill=WHITE)
        cy2 += 44

    # Solution hint
    f_sol = font("bebas_bold", 56)
    draw.text((60, 1010), "LA SOLUCIÓN:", font=f_sol, fill=ACCENT)
    draw.text((380, 1010), "REGISTRARLO ANTES DE TOCAR NADA.", font=font("bebas_bold", 40), fill=GRAY)

    draw_brand_mark(draw)
    save(img, "11-cambio-turno")


# ─────────────────────────────────────────────────────────────────────────────
# 12 — QUÉ RESUELVE EL ERP
# ─────────────────────────────────────────────────────────────────────────────
def image_12_erp_scope():
    img = new_canvas()
    draw = ImageDraw.Draw(img)
    draw_grid(draw)
    draw_glow_blob(img, (900, 300), 500, ACCENT, alpha_max=60)
    draw = ImageDraw.Draw(img)
    draw_corner_tag(draw, "12 / ERP COMPLETO")

    f_h = font("bebas_bold", 100)
    draw.text((60, 110), "QUÉ RESUELVE", font=f_h, fill=WHITE)
    draw.text((60, 210), "VERIDIAN ERP.", font=font("bebas_bold", 120), fill=ACCENT)

    # Two columns: SI / NO
    col_w = 510
    lx, rx, cy = 60, 630, 400

    # SÍ column
    draw.rounded_rectangle([lx, cy, lx+col_w, cy+560], radius=12, fill=PANEL, outline=ACCENT, width=2)
    draw.rectangle([lx, cy, lx+col_w, cy+4], fill=ACCENT)
    f_col = font("bebas_bold", 52)
    draw.text((lx+20, cy+16), "SÍ RESUELVE", font=f_col, fill=ACCENT)
    si_items = [
        "Órdenes de trabajo",
        "Mantenimiento preventivo",
        "Inventario de repuestos",
        "Personal y turnos",
        "Dashboard ejecutivo",
        "Historial por equipo",
    ]
    f_item = font("sans", 20)
    iy = cy + 90
    for item in si_items:
        draw.text((lx+20, iy), "✓  " + item, font=f_item, fill=WHITE)
        iy += 44

    # NO column
    draw.rounded_rectangle([rx, cy, rx+col_w, cy+560], radius=12, fill=PANEL, outline=GRAY_DARK, width=2)
    draw.rectangle([rx, cy, rx+col_w, cy+4], fill=GRAY_DARK)
    draw.text((rx+20, cy+16), "TODAVÍA NO", font=f_col, fill=GRAY_DARK)
    no_items = [
        "Contabilidad avanzada",
        "Liquidación de sueldos",
        "CRM de ventas",
        "Logística de distribución",
        "",
        "",
    ]
    iy = cy + 90
    for item in no_items:
        if item:
            draw.text((rx+20, iy), "—  " + item, font=f_item, fill=GRAY_DARK)
        iy += 44

    # Target
    f_target = font("bebas_bold", 44)
    draw.text((60, 1010), "PARA PYMÉS INDUSTRIALES DE 10 A 200 PERSONAS.", font=f_target, fill=GRAY)

    draw_brand_mark(draw)
    save(img, "12-workkit-teaser")


# ─────────────────────────────────────────────────────────────────────────────
# 13 — MIGRATIONS TIP
# ─────────────────────────────────────────────────────────────────────────────
def image_13_migrations():
    img = new_canvas()
    draw = ImageDraw.Draw(img)
    draw_grid(draw)
    draw_glow_blob(img, (900, 300), 500, CYAN, alpha_max=60)
    draw_glow_blob(img, (200, 1000), 400, ACCENT, alpha_max=50)
    draw = ImageDraw.Draw(img)
    draw_corner_tag(draw, "13 / TIP TÉCNICO", color=CYAN)

    f_h = font("bebas_bold", 105)
    draw.text((60, 110), "MIGRACIONES EN", font=f_h, fill=WHITE)
    draw.text((60, 210), "PRODUCCIÓN", font=f_h, fill=CYAN)
    draw.text((60, 310), "SIN DRAMA.", font=f_h, fill=WHITE)

    # Terminal with migration code
    py = 460
    draw.rounded_rectangle([60, py, 1140, py+640], radius=14, fill=PANEL, outline=GRID, width=2)
    for i, c in enumerate([(239,68,68),(250,204,21),(74,222,128)]):
        draw.ellipse([80+i*22, py+18, 94+i*22, py+32], fill=c)
    draw.text((160, py+16), "20260601_add_serial_number.js", font=font("mono", 14), fill=GRAY)

    f_c = font("mono_bold", 21)
    code_lines = [
        [("module.exports = {", WHITE)],
        [],
        [("  async ", CYAN), ("up", ACCENT), ("(queryInterface, Sequelize) {", WHITE)],
        [("    await ", CYAN), ("queryInterface.sequelize", WHITE), (".transaction(", GRAY)],
        [("      async ", CYAN), ("(t) ", WHITE), ("=> {", GRAY)],
        [("        await ", CYAN), ("queryInterface", WHITE), (".addColumn(", GRAY)],
        [("          'equipments', 'serial_number',", ACCENT)],
        [("          { type: Sequelize.", WHITE), ("STRING", CYAN), (" }, { transaction: t }", GRAY)],
        [("        );", GRAY)],
        [("      });", GRAY)],
        [("  },", WHITE)],
        [],
        [("  async ", CYAN), ("down", RED_HOT), ("(queryInterface) {", WHITE)],
        [("    await ", CYAN), ("queryInterface", WHITE), (".removeColumn(", GRAY)],
        [("          'equipments', 'serial_number'", ACCENT)],
        [("    );", GRAY)],
        [("  }", WHITE)],
        [("};", WHITE)],
    ]
    ly = py + 60
    for line in code_lines:
        lx = 90
        for txt, col in line:
            draw.text((lx, ly), txt, font=f_c, fill=col)
            bb = draw.textbbox((lx, ly), txt, font=f_c)
            lx = bb[2]
        ly += 32

    draw_brand_mark(draw)
    save(img, "13-migrations-tip")


# ─────────────────────────────────────────────────────────────────────────────
# 14 — EL TÉCNICO QUE SABE TODO
# ─────────────────────────────────────────────────────────────────────────────
def image_14_tecnico():
    img = new_canvas()
    draw = ImageDraw.Draw(img)
    draw_grid(draw, spacing=80)
    draw_glow_blob(img, (600, 500), 700, AMBER, alpha_max=50)
    draw_glow_blob(img, (1000, 900), 400, RED_HOT, alpha_max=40)
    draw = ImageDraw.Draw(img)
    draw_corner_tag(draw, "14 / CASO DE DOLOR", color=AMBER)

    f_h = font("bebas_bold", 105)
    draw.text((60, 110), "EL TÉCNICO QUE", font=f_h, fill=WHITE)
    draw.text((60, 210), "SABE TODO.", font=f_h, fill=AMBER)

    # Asset vs Risk
    ax, ay, aw, ah = 60, 380, 500, 200
    draw.rounded_rectangle([ax, ay, ax+aw, ay+ah], radius=12, fill=PANEL, outline=ACCENT, width=2)
    draw.text((ax+20, ay+16), "ACTIVO", font=font("mono_bold", 14), fill=ACCENT)
    f_big = font("bebas_bold", 62)
    draw.text((ax+20, ay+50), "INVALUABLE", font=f_big, fill=WHITE)
    draw.text((ax+20, ay+130), "20 años de experiencia", font=font("sans", 20), fill=GRAY)

    rx2, ry2 = 620, 380
    draw.rounded_rectangle([rx2, ry2, rx2+aw, ry2+ah], radius=12, fill=PANEL, outline=RED_HOT, width=2)
    draw.text((rx2+20, ry2+16), "RIESGO", font=font("mono_bold", 14), fill=RED_HOT)
    draw.text((rx2+20, ry2+50), "OPERACIONAL", font=f_big, fill=WHITE)
    draw.text((rx2+20, ry2+130), "Conocimiento solo en su cabeza", font=font("sans", 20), fill=GRAY)

    # Arrow down
    mid_x = W // 2
    draw.line([(ax+aw//2, ay+ah), (ax+aw//2, ay+ah+60)], fill=GRID, width=3)
    draw.line([(rx2+aw//2, ry2+ah), (rx2+aw//2, ry2+ah+60)], fill=GRID, width=3)

    # What happens when he leaves
    f_sub = font("bebas_bold", 55)
    draw.text((60, 640), "EL DÍA QUE SE VA:", font=f_sub, fill=RED_HOT)
    consequences = [
        "El equipo nuevo arranca desde cero",
        "No hay registro de qué falló en cada máquina",
        "Diagnósticos equivocados, paradas evitables",
        "15 años de historia — perdidos",
    ]
    f_c = font("sans", 22)
    cy3 = 710
    for c in consequences:
        draw.text((60, cy3), "→  " + c, font=f_c, fill=WHITE)
        cy3 += 48

    # Solution
    f_sol = font("bebas_bold", 55)
    draw.text((60, 940), "EL CONOCIMIENTO TIENE QUE", font=f_sol, fill=WHITE)
    draw.text((60, 1000), "VIVIR EN EL SISTEMA, NO EN UNA PERSONA.", font=font("bebas_bold", 40), fill=ACCENT)

    draw_brand_mark(draw)
    save(img, "14-conocimiento-rehenes")


# ─────────────────────────────────────────────────────────────────────────────
# 15 — 3 SEMANAS
# ─────────────────────────────────────────────────────────────────────────────
def image_15_tres_semanas():
    img = new_canvas()
    draw = ImageDraw.Draw(img)
    draw_grid(draw)
    draw_glow_blob(img, (600, 600), 700, ACCENT, alpha_max=60)
    draw = ImageDraw.Draw(img)
    draw_corner_tag(draw, "15 / REFLEXIÓN")

    f_h = font("bebas_bold", 100)
    draw.text((60, 110), "3 SEMANAS", font=f_h, fill=ACCENT)
    draw.text((60, 205), "CONSTRUYENDO", font=f_h, fill=WHITE)
    draw.text((60, 300), "VERIDIAN EN PÚBLICO.", font=font("bebas_bold", 75), fill=WHITE)

    # Three learnings
    lessons = [
        (ACCENT, "01", "Los posts de dolor", "funcionan más que los técnicos"),
        (CYAN,   "02", "La historia personal", "conecta más que las features"),
        (WHITE,  "03", "Building in public", "obliga a claridad real"),
    ]
    ly2 = 470
    for col, num, title, sub in lessons:
        # Number
        f_num = font("bebas_bold", 80)
        draw.text((60, ly2), num, font=f_num, fill=col)
        # Title
        f_t2 = font("bebas_bold", 55)
        draw.text((160, ly2+5), title.upper(), font=f_t2, fill=WHITE)
        # Sub
        f_s2 = font("sans", 20)
        draw.text((160, ly2+65), sub, font=f_s2, fill=GRAY)
        # Divider
        draw.rectangle([60, ly2+105, 1140, ly2+108], fill=GRID)
        ly2 += 140

    # CTA block
    cta_y = 960
    draw.rounded_rectangle([60, cta_y, 1140, cta_y+160], radius=14,
                           fill=PANEL, outline=ACCENT, width=2)
    f_cta = font("bebas_bold", 52)
    draw.text((100, cta_y+20), "¿TU EMPRESA GESTIONA PLANTA EN PLANILLAS?", font=f_cta, fill=WHITE)
    f_cta2 = font("sans_bold", 22)
    draw.text((100, cta_y+90), "Escribime por DM — hacemos una demo sin formularios.", font=f_cta2, fill=ACCENT)

    draw_brand_mark(draw)
    save(img, "15-tres-semanas")


# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("Generando imágenes posts 07-15...\n")
    image_07_docker()
    image_08_stock()
    image_09_produccion()
    image_10_postgres()
    image_11_turno()
    image_12_erp_scope()
    image_13_migrations()
    image_14_tecnico()
    image_15_tres_semanas()
    print("\n✓ Todas las imágenes generadas.")
