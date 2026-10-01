import math
import gen26 as H, gen25 as D, gen23 as G
from gen18 import *
AC = G.AC; INK = '#16121f'
C = H.C + f"""
.co{{position:absolute;z-index:5;width:54px;height:54px;border-radius:50%;background:{AC};color:#fff;border:4px solid #fff;box-shadow:0 0 0 3px {INK},0 6px 14px rgba(0,0,0,.3);display:flex;align-items:center;justify-content:center;font-size:28px;font-weight:800;font-family:M}}
.ring{{position:absolute;z-index:4;width:64px;height:64px;border-radius:50%;border:5px solid {AC};margin:-32px 0 0 -32px;animation:pulse 1.4s ease-in-out infinite}}
.st3{{display:grid;grid-template-columns:1fr 1fr 1.05fr;gap:14px}}
.st3>div{{background:#fff;border:3px solid {INK};border-radius:20px;box-shadow:5px 5px 0 {INK};padding:14px 16px}}
.st3 .h{{display:flex;align-items:center;gap:10px;font-size:24px;font-weight:800;color:{AC}}}
.st3 .h span{{width:40px;height:40px;border-radius:50%;background:{AC};color:#fff;display:flex;align-items:center;justify-content:center;font-size:22px}}
.st3 .t{{font-size:25px;font-weight:700;line-height:1.3;margin-top:8px}}
.st3 .ans{{background:#ecfdf3!important;border-color:#15803d!important;box-shadow:5px 5px 0 #15803d!important}}
.st3 .ans .h{{color:#15803d}} .st3 .ans .h span{{background:#15803d}}
.st3 .ans .t{{font-size:34px;color:#15803d;font-family:S,serif}}
.why{{font-size:27px;font-weight:700;line-height:1.35;background:#fff;border:3px solid {INK};border-radius:20px;padding:16px 22px;box-shadow:5px 5px 0 {INK}}}
.why b{{color:{AC}}}
"""
GH = 278

def dmc(title, exprs, items, xr, yr, pt, ring=True):
    html = D.dm(title, exprs, items, xr, yr, H=GH)
    W = 962; x0, x1 = xr; y0, y1 = yr
    px = (pt[0] - x0) / (x1 - x0) * W; py = 54 + GH - (pt[1] - y0) / (y1 - y0) * GH
    rows_top = 54 + GH + 52
    over = f'<div class="co" style="left:{W - 80}px;top:{rows_top + 6}px">1</div>'
    if ring: over += f'<div class="ring" style="left:{px:.0f}px;top:{py:.0f}px"></div>'
    over += f'<div class="co" style="left:{min(px + 30, W - 70):.0f}px;top:{max(py - 84, 60):.0f}px">2</div>'
    return f'<div style="position:relative">{html}{over}</div>'

def aslide(n, title, sub, dmhtml, s1, s2, ans, why, trap):
    return (f'''<div><div class="pill">ХАРИУ {n}/5</div><h1 style="font-size:52px;margin-top:8px">{title}<br><em>{sub}</em></h1></div>
{dmhtml}
<div class="st3"><div><div class="h"><span>1</span>БИЧ</div><div class="t">{s1}</div></div><div><div class="h"><span>2</span>ДАР</div><div class="t">{s2}</div></div><div class="ans"><div class="h"><span>✓</span>ХАРИУ</div><div class="t">{ans}</div></div></div>
<div class="why">{why}</div>
<div class="trap"><span class="k">УРХИ</span><div>{trap}</div></div>''', '')

v = G.v; f4 = H.f4
P = list(H.P)
P[2] = aslide(1, 'Шулуунууд огтлолцохгүй', '= шийдгүй',
    dmc('Хэцүү асуулт 1', [('red', 'wave', f'−12{v("x")} + 14{v("y")} = 36', ''), ('blue', 'wave', f'−6{v("x")} + 7{v("y")} = −18', '')],
        [('f', lambda x: (36 + 12 * x) / 14, 'red'), ('f', lambda x: (-18 + 6 * x) / 7, 'blue')], (-14, 14), (-7, 8), (4, 2), ring=False),
    'Хоёр тэгшитгэлээ бич', 'Шулуунуудыг хар: огтлолцохгүй', 'D) Zero',
    'Огтлолцох цэг = шийд. <b>Цэг байхгүй бол шийд байхгүй.</b>',
    'C (Infinitely many) гэж бодох урхи. Шулуунууд давхцахгүй, <b>зэрэгцээ</b>.')
P[4] = aslide(2, 'Огтлолцох цэг', '= хариу',
    dmc('Хэцүү асуулт 2', [('red', 'wave', f'{v("x")} − {v("y")} = 1', ''), ('blue', 'wave', f'{v("x")} + {v("y")} = {v("x")}<sup>2</sup> − 3', '')],
        [('f', lambda x: x - 1, 'red'), ('f', lambda x: x * x - 3 - x, 'blue'), ('pt', 1 + math.sqrt(3), math.sqrt(3), 'black', '(2.732, 1.732)', 'E'), ('pt', 1 - math.sqrt(3), -math.sqrt(3), 'black', '(−0.732, −1.732)', 'nw')], (-6, 7), (-4.5, 5.5), (1 + math.sqrt(3), math.sqrt(3))),
    'Хоёр тэгшитгэлээ бич', 'Огтлолцох цэг: (2.732, 1.732)', '(1 + √3, √3)',
    '1 + √3 ≈ <b>2.732</b>, √3 ≈ <b>1.732</b>. Тоо яг таарч байна → <b>A</b>.',
    'Сонголтын √-ийг тооцоолуураар шалга. 1 + √5 ≈ 3.24 таарахгүй.')
P[6] = aslide(3, 'x тэнхлэгтэй огтлолцол', '= t', 
    dmc('Хэцүү асуулт 3', [('red', 'wave', f'{v("h")}({v("x")}) = 2({v("x")} − 4)<sup>2</sup> − 32', '')],
        [('f', lambda x: 2 * (x - 4) ** 2 - 32, 'red'), ('pt', 0, 0, 'red', '(0, 0)', 'nw'), ('pt', 8, 0, 'red', '(8, 0)', 'S'), ('pt', 4, -32, 'red', '(4, −32)', 's')], (-5, 13), (-40, 20), (8, 0)),
    'h(x)-ээ бич', '2 дахь огтлолцол: (8, 0)', 'D) 8',
    'Асуулт графикийн <b>x тэнхлэгтэй огтлолцох</b> 2 дахь цэгийг асууж байна: <b>(8, 0)</b>.',
    '<b>4</b> бол оройн цэг, t биш.')
P[8] = aslide(4, 'g-ийн хамгийн доод цэг', '= хариу',
    dmc('Хэцүү асуулт 4', [('red', 'wave', f'{v("f")}({v("x")}) = 4{v("x")}<sup>2</sup> + 64{v("x")} + 262', ''), ('blue', 'wave', f'{v("g")}({v("x")}) = {v("f")}({v("x")} + 5)', '')],
        [('f', f4, 'red'), ('f', lambda x: f4(x + 5), 'blue'), ('pt', -8, 6, 'red', '(−8, 6)', 'N'), ('pt', -13, 6, 'blue', '(−13, 6)', 'W')], (-22, 4), (-10, 50), (-13, 6)),
    'f ба g(x) = f(x + 5)-ыг бич', 'Цэнхэр графикийн доод цэг: (−13, 6)', 'A) −13',
    'Desmos g-г өөрөө зурна. <b>Цэнхэр</b> графикийн хамгийн доод цэг = <b>−13</b>.',
    '<b>−8</b> бол улаан f-ийн цэг. Асуулт g-г асууж байна.')
P[10] = aslide(5, 'Тойргийн голыг', 'хар', 
    dmc('Хэцүү асуулт 5', [('purple', 'wave', f'{v("x")}<sup>2</sup> + 20{v("x")} + {v("y")}<sup>2</sup> + 16{v("y")} = −20', ''), ('black', 'pt', '(−10, −8)', '')],
        [('curve', H.circle, 'purple'), ('pt', -10, -8, 'black', '(−10, −8)', 'S')], (-10 - 30 * 962 / 278 / 2, -10 + 30 * 962 / 278 / 2), (-23, 7), (-10, -8)),
    'Тэгшитгэлээ шууд бич', 'Голд нь цэг тавьж шалга', 'B) (−10, −8)',
    'Desmos тойргийг зурна. Гол нь яг <b>(−10, −8)</b> дээр.',
    '<b>(10, 8)</b>: тэмдэг эсрэгээрээ. Графикаа хар!')

if __name__ == '__main__':
    import sys
    render(C, P, HERE / 'out27', 'GMP-SAT-Math-Desmos-Easy', video_first=('--video' in sys.argv))
