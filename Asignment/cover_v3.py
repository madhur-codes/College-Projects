import math
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, Color
from reportlab.lib.units import mm
from reportlab.pdfbase.pdfmetrics import stringWidth

W, H = A4

NAVY      = HexColor("#152A4E")
NAVY_SOFT = HexColor("#5B6B85")
GOLD      = HexColor("#B8933F")
GOLD_SOFT = HexColor("#D8B96A")
LINE_GREY = HexColor("#E3E6EC")
WHITE     = HexColor("#FFFFFF")
TEXT_GREY = HexColor("#6B7688")

c = canvas.Canvas("cover_page_v3.pdf", pagesize=A4)

# ---------- Background ----------
c.setFillColor(WHITE)
c.rect(0, 0, W, H, fill=1, stroke=0)

# ---------- Faint hexagon texture (very light, decorative only) ----------
def hexagon_path(cx, cy, r):
    p = c.beginPath()
    for k in range(6):
        ang = math.radians(60 * k - 30)
        pt = (cx + r * math.cos(ang), cy + r * math.sin(ang))
        if k == 0:
            p.moveTo(*pt)
        else:
            p.lineTo(*pt)
    p.close()
    return p

c.saveState()
c.setStrokeColor(LINE_GREY)
c.setLineWidth(0.5)
hr = 9 * mm
hstep_x = hr * math.sqrt(3)
hstep_y = hr * 1.5
row = 0
y = -hr
while y < H + hr:
    x_off = (hstep_x / 2) if row % 2 else 0
    x = -hr + x_off
    while x < W + hr:
        c.drawPath(hexagon_path(x, y, hr))
        x += hstep_x
    y += hstep_y
    row += 1
c.restoreState()

# ---------- Outer decorative border ----------
margin = 9 * mm
c.setStrokeColor(GOLD)
c.setLineWidth(1.1)
c.rect(margin, margin, W - 2 * margin, H - 2 * margin, fill=0, stroke=1)

gap = 2.3 * mm
c.setStrokeColor(NAVY)
c.setLineWidth(0.5)
c.rect(margin + gap, margin + gap, W - 2 * (margin + gap), H - 2 * (margin + gap), fill=0, stroke=1)


def circuit_corner(x, y, sx, sy, scale=1.0):
    c.saveState()
    c.setStrokeColor(GOLD)
    c.setFillColor(GOLD)
    c.setLineWidth(1.0)
    segs = [
        (0, 0, 12 * sx, 0),
        (12 * sx, 0, 12 * sx, 9 * sy),
        (12 * sx, 9 * sy, 20 * sx, 9 * sy),
        (0, 0, 0, 12 * sy),
        (0, 12 * sy, 8 * sx, 12 * sy),
    ]
    for (x1, y1, x2, y2) in segs:
        c.line(x + x1 * scale, y + y1 * scale, x + x2 * scale, y + y2 * scale)
    for (nx, ny) in [(0, 0), (12 * sx, 0), (12 * sx, 9 * sy), (20 * sx, 9 * sy), (0, 12 * sy), (8 * sx, 12 * sy)]:
        c.circle(x + nx * scale, y + ny * scale, 1.2, fill=1, stroke=0)
    c.restoreState()

cm = margin + gap + 3 * mm
circuit_corner(cm, H - cm, 1, -1, 1.1)
circuit_corner(W - cm, H - cm, -1, -1, 1.1)
circuit_corner(cm, cm, 1, 1, 1.1)
circuit_corner(W - cm, cm, -1, 1, 1.1)

def curved_text(text, cx, cy, radius, font="Helvetica-Bold", size=13,
                 color=NAVY, letter_spacing=2.2, center_angle=90):
    """Draws text along an upward-arcing circular path, upright and centred
    on center_angle (90 = straight up)."""
    widths = [stringWidth(ch, font, size) for ch in text]
    angles = [ (w + letter_spacing) / radius for w in widths ]
    total_angle = sum(angles)
    start_angle = math.radians(center_angle) + total_angle / 2
    c.saveState()
    c.setFillColor(color)
    c.setFont(font, size)
    cur = start_angle
    for ch, a in zip(text, angles):
        cur -= a / 2
        x = cx + radius * math.cos(cur)
        y = cy + radius * math.sin(cur)
        rot = math.degrees(cur) - 90
        c.saveState()
        c.translate(x, y)
        c.rotate(rot)
        c.drawCentredString(0, 0, ch)
        c.restoreState()
        cur -= a / 2
    c.restoreState()


# ---------- Header: college name as BIG curved bold heading ----------
bx, by = W / 2, H * 0.71
R = 17 * mm  # logo radius

curve_r = 60 * mm
curved_text("JANTA COLLEGE BAKEWAR", bx, by, curve_r,
            font="Helvetica-Bold", size=24, color=NAVY, letter_spacing=4.2, center_angle=90)

# small diamond + line flourish under the curved heading, above the logo
# (small flourish removed — the curved heading is now the header accent)

# ---------- Center emblem: actual college logo, circular ----------
logo_path = "/home/risx/First Sem Projects/Asignment/logo.png"
c.saveState()
p = c.beginPath()
p.circle(bx, by, R)
c.clipPath(p, stroke=0, fill=0)
c.drawImage(logo_path, bx - R, by - R, width=2 * R, height=2 * R,
            mask='auto', preserveAspectRatio=True)
c.restoreState()

# thin ring around logo
c.setStrokeColor(GOLD)
c.setLineWidth(1.3)
c.circle(bx, by, R, fill=0, stroke=1)
c.setStrokeColor(NAVY)
c.setLineWidth(0.6)
c.circle(bx, by, R + 1.6 * mm, fill=0, stroke=1)

# tiny orbiting ticks around the ring
n = 24
for k in range(n):
    ang = math.radians((360 / n) * k)
    r1 = R + 3.2 * mm
    r2 = R + 4.6 * mm
    x1, y1 = bx + r1 * math.cos(ang), by + r1 * math.sin(ang)
    x2, y2 = bx + r2 * math.cos(ang), by + r2 * math.sin(ang)
    c.setStrokeColor(LINE_GREY if k % 3 else GOLD_SOFT)
    c.setLineWidth(0.7)
    c.line(x1, y1, x2, y2)

# ---------- Title ----------
title_y = by - R - 15 * mm
c.setFillColor(NAVY)
c.setFont("Helvetica-Bold", 25)
c.drawCentredString(W / 2, title_y, "Computer Fundamentals")
c.drawCentredString(W / 2, title_y - 11.5 * mm, "& Python Programming")

# ---------- (subtitle removed) ----------

# ---------- Details card (bordered, white, gold corner ticks) ----------
card_w, card_h = 108 * mm, 38 * mm
card_x = W / 2 - card_w / 2
card_y = 58 * mm

c.setFillColor(WHITE)
c.setStrokeColor(LINE_GREY)
c.setLineWidth(1)
c.roundRect(card_x, card_y, card_w, card_h, 4.5 * mm, fill=1, stroke=1)

tick = 4 * mm
c.setStrokeColor(GOLD)
c.setLineWidth(1.2)
for (cxp, cyp, sx_, sy_) in [
    (card_x, card_y + card_h, 1, -1),
    (card_x + card_w, card_y + card_h, -1, -1),
    (card_x, card_y, 1, 1),
    (card_x + card_w, card_y, -1, 1),
]:
    c.line(cxp, cyp, cxp + tick * sx_, cyp)
    c.line(cxp, cyp, cxp, cyp + tick * sy_)

rows = [("NAME", "Madhur"), ("ROLL NO.", "15"), ("CLASS", "B.Sc. First Sem")]
label_x = card_x + 12 * mm
value_x = card_x + 40 * mm
row_y0 = card_y + card_h - 11 * mm
row_gap = 12 * mm
for i, (label, value) in enumerate(rows):
    ry = row_y0 - i * row_gap
    c.setFont("Helvetica-Bold", 9.5)
    c.setFillColor(GOLD)
    c.drawString(label_x, ry, label)
    c.setFont("Helvetica-Bold", 12.5)
    c.setFillColor(NAVY)
    c.drawString(value_x, ry, value)
    if i < len(rows) - 1:
        c.setStrokeColor(LINE_GREY)
        c.setLineWidth(0.6)
        c.line(label_x, ry - 5 * mm, card_x + card_w - 10 * mm, ry - 5 * mm)

# ---------- Footer ----------
foot_y = 24 * mm
c.setStrokeColor(GOLD)
c.setLineWidth(0.9)
c.line(W / 2 - 28 * mm, foot_y, W / 2 + 28 * mm, foot_y)
c.setFillColor(GOLD)
c.saveState()
c.translate(W / 2, foot_y)
c.rotate(45)
c.rect(-1.3 * mm, -1.3 * mm, 2.6 * mm, 2.6 * mm, fill=1, stroke=0)
c.restoreState()

c.setFont("Helvetica-Bold", 10.5)
c.setFillColor(NAVY)
c.drawCentredString(W / 2, foot_y - 7 * mm, "ACADEMIC YEAR 2026 - 27")

c.setFont("Helvetica", 8)
c.setFillColor(TEXT_GREY)
c.drawCentredString(W / 2, foot_y - 12.5 * mm, "Submitted in partial fulfilment of the requirements of the course")

c.showPage()
c.save()
print("cover_page_v3.pdf created")