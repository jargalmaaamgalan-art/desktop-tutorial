import math
import gen22 as B
from gen18 import *
AC, SOFT, INK, GREEN, RED = B.AC, B.SOFT, B.INK if hasattr(B, 'INK') else '#16121f', B.GREEN, B.RED
R2 = B.R2
DC = {'red': '#c74440', 'blue': '#2d70b3', 'green': '#388c46', 'purple': '#6042a6', 'black': '#000000', 'orange': '#fa7e19'}

C = B.C + f"""
.bb{{background:#fff;border:3px solid {INK};border-radius:24px;box-shadow:7px 7px 0 {INK};overflow:hidden}}
.bbh{{display:flex;align-items:center;justify-content:space-between;padding:14px 24px;border-bottom:2px dashed #b9b9b9;background:#f7f8fc;font-family:Arial,sans-serif}}
.bbh .sec{{font-size:22px;font-weight:700}}
.bbh .tm{{font-size:30px;font-weight:700;letter-spacing:1px}}
.bbh .tools{{display:flex;gap:22px;font-size:17px;color:#333;text-align:center}}
.bbq{{padding:18px 30px 22px}}
.bbbar{{display:flex;align-items:center;gap:14px;background:#f0f0f0;margin:0 -30px;padding:8px 30px;font-family:Arial,sans-serif;font-size:21px}}
.bbbar .qn{{background:#000;color:#fff;font-weight:700;font-size:24px;width:44px;height:40px;display:flex;align-items:center;justify-content:center}}
.bbbar .abc{{margin-left:auto;border:2px solid #000;border-radius:5px;padding:1px 6px;font-size:16px;font-weight:700;text-decoration:line-through}}
.bbstem{{font-family:S,serif;font-size:33px;line-height:1.45;margin-top:18px}}
.bbdisp{{text-align:center;font-family:S,serif;font-size:38px;margin:14px 0 6px}}
.bbch{{display:flex;flex-direction:column;gap:14px;margin-top:20px}}
.bbc{{display:flex;align-items:center;gap:18px;border:2px solid #1b1b1b;border-radius:12px;padding:12px 18px;font-family:S,serif;font-size:32px}}
.bbc .l{{flex:none;width:40px;height:40px;border:2px solid #1b1b1b;border-radius:50%;display:flex;align-items:center;justify-content:center;font-family:Arial,sans-serif;font-size:20px;font-weight:700}}
.bbf{{display:flex;align-items:center;justify-content:space-between;padding:12px 24px;border-top:2px dashed #b9b9b9;background:#f7f8fc;font-family:Arial,sans-serif;font-size:20px;font-weight:700}}
.bbf .qx{{background:#1b1b1b;color:#fff;border-radius:8px;padding:6px 14px}}
.bbf .nx{{background:#324dc7;color:#fff;border-radius:22px;padding:8px 26px}}
.ds{{display:flex;background:#fff;border:3px solid {INK};border-radius:24px;box-shadow:7px 7px 0 {INK};overflow:hidden}}
.dsl{{flex:none;width:360px;border-right:2px solid #d8d8d8;background:#fff}}
.dsr{{display:flex;align-items:stretch;border-bottom:1px solid #e3e3e3;min-height:66px}}
.dsr .g{{flex:none;width:44px;background:#f2f2f2;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;font-family:Arial;font-size:13px;color:#888}}
.dsr .dot{{width:22px;height:22px;border-radius:50%}}
.dsr .x{{flex:1;display:flex;align-items:center;justify-content:space-between;padding:8px 12px;font-family:S,serif;font-size:28px;line-height:1.25}}
.dsr .val{{font-family:Arial;font-size:19px;color:#555;background:#f2f2f2;border-radius:6px;padding:2px 8px}}
.dshd{{height:36px;background:#e8e8e8;border-bottom:1px solid #d0d0d0;display:flex;align-items:center;padding:0 12px;font-family:Arial;font-size:15px;color:#555;font-weight:700;letter-spacing:.5px}}
.lead2{{display:flex;align-items:center;gap:20px}}
.tag{{display:inline-flex;align-items:center;gap:8px;border:2.5px solid {INK};border-radius:30px;padding:6px 16px;font-size:22px;font-weight:800;background:#fff;margin-right:8px}}
.tag.h{{background:{INK};color:#fff}}
.okchip{{flex:none;background:{GREEN};color:#fff;border:3px solid {INK};border-radius:18px;padding:10px 18px;font-size:30px;font-weight:800;text-align:center;line-height:1.1}}
.okchip small{{display:block;font-size:17px;font-weight:700;opacity:.9}}
"""

def nice(span, target=6):
    raw = span / target
    p = 10 ** math.floor(math.log10(raw))
    for m in (1, 2, 5, 10):
        if raw <= m * p: return m * p
    return 10 * p

def fmt(v):
    if abs(v - round(v)) < 1e-9: v = int(round(v))
    s = f'{v:g}' if not isinstance(v, int) else str(v)
    return s.replace('-', '−')

def desmos(exprs, items, xr, yr, W=598, H=490):
    x0, x1 = xr; y0, y1 = yr
    X = lambda x: (x - x0) / (x1 - x0) * W
    Y = lambda y: H - (y - y0) / (y1 - y0) * H
    sx = nice(x1 - x0); sy = nice(y1 - y0, 5)
    s = f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;font-family:Arial,sans-serif"><defs><clipPath id="cp"><rect width="{W}" height="{H}"/></clipPath></defs><rect width="{W}" height="{H}" fill="#fff"/>'
    for step, col, sw, fac in ((sx / 5 if str(sx)[0] != '2' else sx / 4, '#ececec', 1, 1), (sx, '#cfcfcf', 1.3, 0)):
        k = math.ceil(x0 / step)
        while k * step <= x1:
            xv = k * step; s += f'<line x1="{X(xv):.1f}" y1="0" x2="{X(xv):.1f}" y2="{H}" stroke="{col}" stroke-width="{sw}"/>'; k += 1
    for step, col, sw in ((sy / 5 if str(sy)[0] != '2' else sy / 4, '#ececec', 1), (sy, '#cfcfcf', 1.3)):
        k = math.ceil(y0 / step)
        while k * step <= y1:
            yv = k * step; s += f'<line x1="0" y1="{Y(yv):.1f}" x2="{W}" y2="{Y(yv):.1f}" stroke="{col}" stroke-width="{sw}"/>'; k += 1
    ax_y = min(max(Y(0), 0), H); ax_x = min(max(X(0), 0), W)
    if y0 <= 0 <= y1: s += f'<line x1="0" y1="{Y(0):.1f}" x2="{W}" y2="{Y(0):.1f}" stroke="#222" stroke-width="2"/>'
    if x0 <= 0 <= x1: s += f'<line x1="{X(0):.1f}" y1="0" x2="{X(0):.1f}" y2="{H}" stroke="#222" stroke-width="2"/>'
    halo = 'paint-order="stroke" stroke="#fff" stroke-width="5" stroke-linejoin="round"'
    k = math.ceil(x0 / sx)
    while k * sx <= x1:
        xv = k * sx
        if abs(xv) > 1e-9 and 14 < X(xv) < W - 14:
            ty = min(max(ax_y + 22, 22), H - 8)
            s += f'<text x="{X(xv):.1f}" y="{ty:.1f}" text-anchor="middle" font-size="17" fill="#333" {halo}>{fmt(xv)}</text>'
        k += 1
    k = math.ceil(y0 / sy)
    while k * sy <= y1:
        yv = k * sy
        if abs(yv) > 1e-9 and 12 < Y(yv) < H - 12:
            tx = min(max(ax_x - 8, 40), W - 8)
            s += f'<text x="{tx:.1f}" y="{Y(yv)+6:.1f}" text-anchor="end" font-size="17" fill="#333" {halo}>{fmt(yv)}</text>'
        k += 1
    if x0 <= 0 <= x1 and y0 <= 0 <= y1:
        s += f'<text x="{X(0)-8:.1f}" y="{Y(0)+22:.1f}" text-anchor="end" font-size="17" fill="#333" {halo}>0</text>'
    s += '<g clip-path="url(#cp)">'
    for it in items:
        if it[0] == 'f':
            _, fn, col = it; pts = []
            for i in range(401):
                xv = x0 + (x1 - x0) * i / 400; yv = fn(xv)
                pts.append(f'{X(xv):.1f},{max(min(Y(yv), H + 400), -400):.1f}')
            s += f'<path d="M{" L".join(pts)}" fill="none" stroke="{DC[col]}" stroke-width="4" stroke-linejoin="round"/>'
        if it[0] == 'curve':
            _, pts, col = it
            s += f'<polyline points="{" ".join(f"{X(a):.1f},{Y(b):.1f}" for a, b in pts)}" fill="none" stroke="{DC[col]}" stroke-width="4" stroke-linejoin="round"/>'
        if it[0] == 'poly':
            _, pts, col = it
            s += f'<polygon points="{" ".join(f"{X(a):.1f},{Y(b):.1f}" for a, b in pts)}" fill="{DC[col]}" fill-opacity=".25" stroke="{DC[col]}" stroke-width="3.5"/>'
    for it in items:
        if it[0] == 'pt':
            _, xv, yv, col, lab, anchor = it
            s += f'<circle cx="{X(xv):.1f}" cy="{Y(yv):.1f}" r="7" fill="{DC[col]}" stroke="#fff" stroke-width="2"/>'
            dx, dy, ta = {'ne': (12, -12, 'start'), 'nw': (-12, -12, 'end'), 'se': (12, 28, 'start'), 'sw': (-12, 28, 'end'), 's': (0, 32, 'middle'), 'n': (0, -16, 'middle'), 'E': (46, 7, 'start'), 'W': (-46, 7, 'end'), 'N': (0, -24, 'middle'), 'S': (0, 62, 'middle')}[anchor]
            s += f'<text x="{X(xv)+dx:.1f}" y="{Y(yv)+dy:.1f}" text-anchor="{ta}" font-size="19" fill="#555" {halo}>{lab}</text>'
        if it[0] == 'note':
            _, xv, yv, txt, col = it
            s += f'<text x="{X(xv):.1f}" y="{Y(yv):.1f}" text-anchor="middle" font-size="21" font-weight="700" fill="{col}" {halo}>{txt}</text>'
    s += '</g></svg>'
    rows = ''.join(f'<div class="dsr"><div class="g">{i}<div class="dot" style="background:{DC[c]}"></div></div><div class="x"><span>{t}</span>{f"<span class=val>= {v}</span>" if v else ""}</div></div>' for i, (c, t, v) in enumerate(exprs, 1))
    return f'<div class="ds"><div class="dsl"><div class="dshd">DESMOS-Д ИНГЭЖ БИЧ</div>{rows}</div><div>{s}</div></div>'

v = lambda t: f'<i>{t}</i>'

def bluebook(n, qnum, disp, stem, choices, secs='1:35'):
    ch = ''.join(f'<div class="bbc"><span class="l">{l}</span><span>{c}</span></div>' for l, c in zip('ABCD', choices))
    return f'''<div class="bb"><div class="bbh"><div class="sec">Section 2, Module 1: Math</div><div class="tm">{secs}</div><div class="tools"><div>{E("1f9ee",30)}<br>Calculator</div><div>{E("1f4d0",30)}<br>Reference</div></div></div>
<div class="bbq"><div class="bbbar"><div class="qn">{qnum}</div>{B.BOOK if hasattr(B,"BOOK") else ""}<span>Mark for Review</span><span class="abc">ABC</span></div>
{f'<div class="bbdisp">{disp}</div>' if disp else ''}<div class="bbstem">{stem}</div><div class="bbch">{ch}</div></div>
<div class="bbf"><span>GMP · Practice</span><span class="qx">Question {qnum} of 22 ⌃</span><span class="nx">Next</span></div></div>'''

BOOK = '<svg width="22" height="26" viewBox="0 0 24 28" fill="none" stroke="#000" stroke-width="2.4"><path d="M4 2h16v24l-8-6-8 6z"/></svg>'
B.BOOK = BOOK

def qslide(n, diff, dom, qnum, disp, stem, choices, emo):
    tag = f'<span class="tag{" h" if diff=="Hard" else ""}">{E("1f525" if diff=="Hard" else "1f60e",30)} {diff}</span><span class="tag">{dom}</span><span class="tag">{E("23f1",28)} ~95 сек</span>'
    return (f'''<div style="display:flex;align-items:center;justify-content:space-between"><div><div class="pill">ТРИК {n}/5 · ЭХЛЭЭД ӨӨРӨӨ БОД</div><div style="margin-top:14px">{tag}</div></div>{E(emo,120,"wig")}</div>
{bluebook(n, qnum, disp, stem, choices)}
<div class="trap" style="background:{INK}"><span class="k" style="background:{AC}">ДАРААГИЙН ХУУДАС</span><div>Хариу + <b>Desmos</b>-оор 10 секундэд шалгах арга 👉</div></div>'''.replace(' 👉', ''), '')

def aslide(n, title_a, title_b, ok, okv, dsm, rule, trap):
    return (f'''<div><div class="pill">ТРИК {n}/5 · ХАРИУ</div><h1 style="font-size:64px;margin-top:14px">{title_a}<br><em>{title_b}</em></h1></div>
{dsm}
<div class="card lead2" style="padding:18px 22px"><div class="okchip"><small>ЗӨВ ХАРИУ</small>{ok}) {okv}</div><div class="rule" style="font-size:27px">{rule}</div></div>
<div class="trap"><span class="k">УРХИ</span><div>{trap}</div></div>''', '')

f4 = lambda x: 4 * x * x + 64 * x + 262
a5 = 9 * math.sqrt(2)
P = []
P.append((B.P[0][0].replace('Хариу нь 5-р хуудсанд', 'Хариу нь 9-р хуудсанд'), B.P[0][1]))

P.append(qslide(1, 'Medium', 'Algebra', 4, f'({v("b")} − 2){v("x")} = 8', f'In the given equation, {v("b")} is a constant. If the equation has no solution, what is the value of {v("b")}?', ['2', '4', '6', '10'], '1f914'))
P.append(aslide(1, 'Шийдгүй бол', 'шулуунууд параллель',
    'A', '2',
    desmos([('black', f'{v("b")} = 2', ''), ('red', f'{v("y")} = ({v("b")} − 2){v("x")}', ''), ('blue', f'{v("y")} = 8', '')],
           [('f', lambda x: 0 * x, 'red'), ('f', lambda x: 8 + 0 * x, 'blue'), ('note', 0, 4.6, 'огтлолцохгүй = шийдгүй', DC['red'])], (-10, 10), (-3, 12)),
    '<b>b − 2 = 0</b> үед 0 · x = 8 болно: хэзээ ч үнэн биш. Desmos: <b>b</b>-г 2 болгоход хоёр шулуун параллель.',
    '<b>b − 2 = 8</b> гэж бодоод <b>b = 10</b> сонгох. Энэ нь “нэг шийдтэй” тохиолдол.'))

P.append(qslide(2, 'Medium', 'Advanced Math', 9, f'{v("x")}<sup>2</sup> = −841', 'How many distinct real solutions does the given equation have?', ['Exactly one', 'Exactly two', 'Infinitely many', 'Zero'], '1f62e'))
P.append(aslide(2, 'Квадрат хэзээ ч', 'сөрөг биш',
    'D', 'Zero',
    desmos([('red', f'{v("y")} = {v("x")}<sup>2</sup>', ''), ('blue', f'{v("y")} = −841', '')],
           [('f', lambda x: x * x, 'red'), ('f', lambda x: -841 + 0 * x, 'blue'), ('note', 0, -600, 'огтлолцох цэг алга', DC['blue'])], (-40, 40), (-1100, 1700)),
    '<b>x² ≥ 0</b> үргэлж. Сөрөг тоотой тэнцэх боломжгүй → <b>0 шийд</b>. x² = 0 → 1 шийд, x² = эерэг → 2 шийд.',
    '√841 = 29 гэж бодоод <b>“Exactly two”</b> сонгох. Хасах тэмдгийг анзаар!'))

P.append(qslide(3, 'Hard', 'Advanced Math', 14, f'{v("f")}({v("x")}) = ({v("x")} − 44)({v("x")} − 46)', f'The function {v("f")} is defined by the given equation. For what value of {v("x")} does {v("f")}({v("x")}) reach its minimum?', ['46', '45', '44', '−1'], '1f9d0'))
P.append(aslide(3, 'Орой нь язгууруудын', 'яг дунд',
    'B', '45',
    desmos([('red', f'{v("y")} = ({v("x")} − 44)({v("x")} − 46)', '')],
           [('f', lambda x: (x - 44) * (x - 46), 'red'), ('pt', 44, 0, 'red', '(44, 0)', 'nw'), ('pt', 46, 0, 'red', '(46, 0)', 'ne'), ('pt', 45, -1, 'red', '(45, −1)', 's')], (42, 48), (-2.2, 4)),
    'Язгуур 44 ба 46 → орой <b>(44 + 46) ÷ 2 = 45</b>. Desmos-д графикаа бичээд хамгийн доод цэг дээр дар.',
    '<b>44</b> эсвэл <b>46</b> сонгох: эдгээр нь тэг цэгүүд. <b>−1</b> нь хамгийн бага <b>утга</b>, x биш.'))

P.append(qslide(4, 'Hard', 'Advanced Math', 18, f'{v("f")}({v("x")}) = 4{v("x")}<sup>2</sup> + 64{v("x")} + 262', f'The function {v("g")} is defined by {v("g")}({v("x")}) = {v("f")}({v("x")} + 5). For what value of {v("x")} does {v("g")}({v("x")}) reach its minimum?', ['−13', '−8', '−5', '−3'], '1f92f'))
P.append(aslide(4, 'f(x + 5) нь', 'зүүн тийш 5',
    'A', '−13',
    desmos([('red', f'{v("f")}({v("x")}) = 4{v("x")}<sup>2</sup> + 64{v("x")} + 262', ''), ('blue', f'{v("g")}({v("x")}) = {v("f")}({v("x")} + 5)', '')],
           [('f', f4, 'red'), ('f', lambda x: f4(x + 5), 'blue'), ('pt', -8, 6, 'red', '(−8, 6)', 'se'), ('pt', -13, 6, 'blue', '(−13, 6)', 'sw')], (-20, 2), (-8, 42)),
    '<b>f</b>-ийн орой x = −64 ÷ 8 = <b>−8</b>. <b>f(x + 5)</b> → зүүн тийш 5 → <b>−13</b>.',
    '“+5” гэж харж баруун тийш шилжүүлэх: −8 + 5 = <b>−3</b>. Нэмэх = зүүн!'))

P.append(qslide(5, 'Hard', 'Geometry &amp; Trig', 21, '', f'The perimeter of an isosceles right triangle is <span style="white-space:nowrap">18 + 18{R2}</span> inches. What is the length, in inches, of the hypotenuse of this triangle?', ['9', f'9{R2}', '18', f'18{R2}'], '1f4d0'))
P.append(aslide(5, '45-45-90:', 'гипотенуз = катет × √2',
    'C', '18',
    desmos([('black', f'{v("a")} = 9√2', '12.7279'), ('green', f'polygon((0,0),({v("a")},0),(0,{v("a")}))', ''), ('purple', f'distance(({v("a")},0),(0,{v("a")}))', '18')],
           [('poly', [(0, 0), (a5, 0), (0, a5)], 'green'), ('pt', a5, 0, 'green', '(12.73, 0)', 'n'), ('pt', 0, a5, 'green', '(0, 12.73)', 'ne'), ('note', 8.8, 7.8, 'гипотенуз = 18', DC['purple'])], (-3, 25), (-3, -3 + 28 * 490 / 598)),
    'a + a + a√2 = <b>a(2 + √2)</b> = 18 + 18√2 → a = 9√2 → гипотенуз <b>a√2 = 18</b>.',
    'Асуултад харагдсан <b>18√2</b>-ыг сонгох. Асуусан зүйлээ дахин унш: гипотенуз!'))

P.append(B.P[6])
P.append(B.P[7])

if __name__ == '__main__':
    import sys
    render(C, P, HERE / 'out23', 'GMP-SAT-Math-Desmos', video_first=('--video' in sys.argv))
