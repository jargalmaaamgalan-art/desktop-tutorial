from gen18 import *
AC = '#d97706'; SOFT = '#fde68a'; BG = '#fffbeb'; GRID = 'rgba(217,119,6,.09)'
GREEN = '#15803d'; RED = '#dc2626'
C = css(AC, SOFT, BG, GRID) + f"""
.v{{font-style:italic}}
.stem{{font-family:S,serif;font-size:30px;line-height:1.4}}
.chs{{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:16px}}
.chx{{border:2.5px solid {INK};border-radius:14px;padding:10px 12px;font-family:S,serif;font-size:30px;display:flex;align-items:center;gap:10px;background:#fff}}
.chx .l{{flex:none;width:36px;height:36px;border:2.5px solid {INK};border-radius:50%;display:flex;align-items:center;justify-content:center;font-family:M;font-size:18px;font-weight:800}}
.chx.ok{{border-color:{GREEN};background:#ecfdf3;color:{GREEN};font-weight:700}}
.chx.ok .l{{background:{GREEN};border-color:{GREEN};color:#fff}}
.chx.bad{{border-color:{RED};color:{RED}}}
.rule{{font-size:28px;font-weight:700;line-height:1.35}}
.rule .row{{display:flex;align-items:center;gap:14px;padding:10px 0;border-top:2px dashed #eadfc6}}
.rule .row:first-child{{border-top:0}}
.m{{font-family:S,serif;font-weight:600;font-size:31px}}
.trap{{background:{INK};color:#fff;border-radius:26px;padding:20px 26px;font-size:28px;font-weight:700;line-height:1.35;display:flex;gap:16px;align-items:center}}
.trap .k{{flex:none;background:{RED};border-radius:14px;padding:6px 12px;font-size:20px;font-weight:800;letter-spacing:1px}}
.trap b{{color:{SOFT}}}
"""
R2 = '<math style="margin-left:-2px"><msqrt><mn>2</mn></msqrt></math>'

def parab(fx, x0, x1, X, Y, n=60):
    pts = []
    for i in range(n + 1):
        x = x0 + (x1 - x0) * i / n
        pts.append(f'{X(x):.1f},{Y(fx(x)):.1f}')
    return 'M' + ' L'.join(pts)

def svg(w, h, inner):
    return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" style="display:block;font-family:S,serif">{inner}</svg>'

def axes(w, h, ox, oy):
    return (f'<line x1="10" y1="{oy}" x2="{w-10}" y2="{oy}" stroke="{INK}" stroke-width="2.5"/><polygon points="{w-10},{oy} {w-22},{oy-7} {w-22},{oy+7}" fill="{INK}"/>'
            f'<line x1="{ox}" y1="{h-10}" x2="{ox}" y2="10" stroke="{INK}" stroke-width="2.5"/><polygon points="{ox},10 {ox-7},22 {ox+7},22" fill="{INK}"/>')

# 1 lines: one / none / infinite
def mini(kind):
    s = f'<rect x="1" y="1" width="118" height="78" rx="10" fill="#fff" stroke="{INK}" stroke-width="2"/>'
    if kind == 'one': s += f'<line x1="15" y1="65" x2="105" y2="15" stroke="{INK}" stroke-width="4"/><line x1="15" y1="18" x2="105" y2="62" stroke="{AC}" stroke-width="4"/>'
    if kind == 'none': s += f'<line x1="15" y1="55" x2="105" y2="15" stroke="{INK}" stroke-width="4"/><line x1="15" y1="70" x2="105" y2="30" stroke="{AC}" stroke-width="4"/>'
    if kind == 'inf': s += f'<line x1="15" y1="62" x2="105" y2="18" stroke="{AC}" stroke-width="9"/><line x1="15" y1="62" x2="105" y2="18" stroke="{INK}" stroke-width="3"/>'
    return svg(120, 80, s)

def fig_sq():
    w, h, ox, oy = 420, 330, 210, 200
    X = lambda x: ox + x * 38; Y = lambda y: oy - y * 38
    return svg(w, h, axes(w, h, ox, oy) + f'<path d="{parab(lambda x:x*x,-2.4,2.4,X,Y)}" fill="none" stroke="{INK}" stroke-width="4"/>'
               f'<line x1="20" y1="{oy+80}" x2="{w-20}" y2="{oy+80}" stroke="{AC}" stroke-width="4" stroke-dasharray="12 8"/>'
               f'<text x="{w-24}" y="{oy+70}" text-anchor="end" font-size="26" fill="{AC}" font-style="italic">y = −841</text>'
               f'<text x="{ox+70}" y="40" font-size="26" font-style="italic">y = x²</text>'
               f'<text x="{ox}" y="{oy+124}" text-anchor="middle" font-size="22" font-family="M" font-weight="700" fill="{RED}">огтлолцохгүй</text>')

def fig_mid():
    w, h = 420, 330; oy = 90
    X = lambda x: 210 + (x - 45) * 110; Y = lambda y: oy - y * 70
    f = lambda x: (x - 44) * (x - 46)
    s = f'<line x1="10" y1="{oy}" x2="{w-10}" y2="{oy}" stroke="{INK}" stroke-width="2.5"/>'
    s += f'<path d="{parab(f,43.35,46.65,X,Y)}" fill="none" stroke="{INK}" stroke-width="4"/>'
    s += f'<line x1="{X(45)}" y1="30" x2="{X(45)}" y2="{Y(-1)+10}" stroke="{AC}" stroke-width="3" stroke-dasharray="10 7"/>'
    for r in (44, 46):
        s += f'<circle cx="{X(r)}" cy="{oy}" r="8" fill="{INK}"/><text x="{X(r)}" y="{oy-18}" text-anchor="middle" font-size="28">{r}</text>'
    s += f'<circle cx="{X(45)}" cy="{Y(-1)}" r="10" fill="{AC}"/><text x="{X(45)}" y="{Y(-1)+46}" text-anchor="middle" font-size="30" font-weight="700" fill="{AC}">x = 45</text>'
    s += f'<text x="{X(45)}" y="{Y(-1)+80}" text-anchor="middle" font-size="22" font-family="M" font-weight="700">яг дунд нь</text>'
    return svg(w, h, s)

def fig_shift():
    w, h = 440, 330; oy = 250
    X = lambda x: 360 + (x + 8) * 20; Y = lambda y: oy - y * 5.2
    f = lambda x: 4 * x * x + 64 * x + 262
    s = f'<line x1="10" y1="{oy}" x2="{w-10}" y2="{oy}" stroke="{INK}" stroke-width="2.5"/>'
    s += f'<path d="{parab(f,-11.2,-4.8,X,Y)}" fill="none" stroke="{INK}" stroke-width="4"/>'
    s += f'<path d="{parab(lambda x:f(x+5),-16.2,-9.8,X,Y)}" fill="none" stroke="{AC}" stroke-width="4"/>'
    vy = Y(6); ay = vy - 46
    s += f'<circle cx="{X(-8)}" cy="{vy}" r="8" fill="{INK}"/><circle cx="{X(-13)}" cy="{vy}" r="8" fill="{AC}"/>'
    s += f'<line x1="{X(-8)}" y1="{ay}" x2="{X(-13)+16}" y2="{ay}" stroke="{AC}" stroke-width="4"/><polygon points="{X(-13)+2},{ay} {X(-13)+18},{ay-9} {X(-13)+18},{ay+9}" fill="{AC}"/><line x1="{X(-8)}" y1="{vy-10}" x2="{X(-8)}" y2="{ay}" stroke="{INK}" stroke-width="2" stroke-dasharray="5 4"/><line x1="{X(-13)}" y1="{vy-10}" x2="{X(-13)}" y2="{ay}" stroke="{AC}" stroke-width="2" stroke-dasharray="5 4"/>'
    s += f'<text x="{(X(-8)+X(-13))/2}" y="{ay-16}" text-anchor="middle" font-size="26" font-family="M" font-weight="800" fill="{AC}">5</text>'
    s += f'<text x="{X(-8)}" y="{oy+36}" text-anchor="middle" font-size="26">−8</text><text x="{X(-13)}" y="{oy+36}" text-anchor="middle" font-size="26" fill="{AC}" font-weight="700">−13</text>'
    s += f'<text x="{X(-8)+40}" y="40" font-size="26" font-style="italic">f</text><text x="{X(-13)-50}" y="40" font-size="26" font-style="italic" fill="{AC}">g</text>'
    return svg(w, h, s)

def fig_tri():
    w, h = 420, 330
    A, B, Cc = (70, 280), (70, 60), (290, 280)
    s = f'<polygon points="{A[0]},{A[1]} {B[0]},{B[1]} {Cc[0]},{Cc[1]}" fill="none" stroke="{INK}" stroke-width="4"/>'
    s += f'<polyline points="{A[0]},{A[1]-26} {A[0]+26},{A[1]-26} {A[0]+26},{A[1]}" fill="none" stroke="{INK}" stroke-width="2.5"/>'
    s += f'<text x="{A[0]-18}" y="{(A[1]+B[1])/2+10}" text-anchor="end" font-size="34" font-style="italic">a</text>'
    s += f'<text x="{(A[0]+Cc[0])/2}" y="{A[1]+40}" text-anchor="middle" font-size="34" font-style="italic">a</text>'
    s += f'<text x="{(B[0]+Cc[0])/2+28}" y="{(B[1]+Cc[1])/2-10}" font-size="34" font-style="italic" fill="{AC}" font-weight="700">a√2</text>'
    s += f'<text x="{Cc[0]-60}" y="{Cc[1]-12}" font-size="22">45°</text><text x="{B[0]+10}" y="{B[1]+56}" font-size="22">45°</text>'
    return svg(w, h, s)

def trick(n, emo, title_a, title_b, stem, choices, ok, bad, fig, rule, trap):
    cols = 2 if max(len(c) for c in choices) > 8 and 'math' not in ''.join(choices) else 4
    chs = f'<div class="chs" style="grid-template-columns:repeat({cols},1fr)">' + ''.join(f'<div class="chx{" ok" if l==ok else (" bad" if l==bad else "")}"><span class="l">{l}</span>{c}</div>' for l, c in zip('ABCD', choices)) + '</div>'
    return (f'''<div style="display:flex;align-items:center;justify-content:space-between"><div><div class="pill">ТРИК {n}/5</div>
<h1 style="font-size:66px;margin-top:14px">{title_a}<br><em>{title_b}</em></h1></div>{E(emo,140,"wig")}</div>
<div class="card" style="padding:22px 26px"><div style="font-size:20px;font-weight:800;letter-spacing:1px;opacity:.6;margin-bottom:8px">SAT АСУУЛТ · COLLEGE BOARD QUESTION BANK</div><div class="stem">{stem}</div>{chs}</div>
<div class="card" style="display:flex;gap:18px;align-items:center;padding:18px 22px"><div style="flex:none">{fig}</div><div class="rule" style="flex:1">{rule}</div></div>
<div class="trap"><span class="k">УРХИ</span><div>{trap}</div></div>''', '')

def rows(items): return ''.join(f'<div class="row"><span>{a}</span></div>' for a in items)

P = []
P.append((f'''<div class="pill">SAT MATH · ТРИК</div>
<h1 style="font-size:104px;margin-top:8px">Бодохоос<br>өмнө мэдэх<br><em>5 трик</em></h1>
<div class="card" style="padding:22px 28px"><div style="font-size:30px;font-weight:800">Шалгаад үз: <span class="m">g(x) = f(x + 5)</span> график</div>
<div style="display:flex;gap:16px;margin-top:14px"><div style="flex:1;border:3px solid {INK};border-radius:16px;padding:12px;text-align:center;font-size:30px;font-weight:800">баруун тийш →</div><div style="flex:1;border:3px solid {INK};border-radius:16px;padding:12px;text-align:center;font-size:30px;font-weight:800">← зүүн тийш</div></div>
<div style="font-size:24px;font-weight:700;opacity:.7;margin-top:12px">Хариу нь 5-р хуудсанд 👉</div></div>
<div style="display:flex;justify-content:space-between;align-items:center">
 <div style="font-size:24px;font-weight:700;opacity:.75">Жинхэнэ SAT асуултууд · Хадгалаад ав</div>
 <div style="background:{INK};color:#fff;border-radius:34px;padding:14px 28px;font-size:28px;font-weight:800;box-shadow:6px 6px 0 {AC}">Гүйлгээд үз →</div></div>'''.replace('👉', ''),
 f'''<div style="position:absolute;right:60px;top:200px;z-index:1">{E("1f9e0",190,"fl")}</div>
<div style="position:absolute;right:110px;top:440px;z-index:1" class="pop">{E("1f9ee",120,"wig")}</div>'''))

P.append(trick(1, '1f914', 'Шийдгүй бол', 'x-ийн коэффициент = 0',
    '<div style="text-align:center;font-size:36px;margin-bottom:6px">(<span class="v">b</span> − 2)<span class="v">x</span> = 8</div>In the given equation, <span class="v">b</span> is a constant. If the equation has no solution, what is the value of <span class="v">b</span>?',
    ['2', '4', '6', '10'], 'A', 'D',
    '<div style="display:flex;flex-direction:column;gap:10px">' + mini('one') + mini('none') + mini('inf') + '</div>',
    rows(['<span class="m">a ≠ c</span> → <b>1 шийд</b>', '<span class="m">a = c, b ≠ d</span> → <b style="color:#dc2626">шийдгүй</b>', '<span class="m">a = c, b = d</span> → <b style="color:#d97706">хязгааргүй олон</b>']) + '<div style="font-size:22px;opacity:.7;margin-top:6px">Хэлбэр: <span class="m" style="font-size:24px">ax + b = cx + d</span></div>',
    '<b>b = 10</b> гэж бодох. 8-тай тэнцүүлэх биш, <b>b − 2 = 0</b> болгоно: 0 · x = 8 хэзээ ч үнэн биш.'))

P.append(trick(2, '1f62e', 'Квадрат хэзээ ч', 'сөрөг биш',
    '<div style="text-align:center;font-size:36px;margin-bottom:6px"><span class="v">x</span><sup>2</sup> = −841</div>How many distinct real solutions does the given equation have?',
    ['Exactly one', 'Exactly two', 'Infinitely many', 'Zero'], 'D', 'B', fig_sq(),
    rows(['<span class="m">x² = эерэг</span> → <b>2 шийд</b>', '<span class="m">x² = 0</span> → <b>1 шийд</b>', '<span class="m">x² = сөрөг</span> → <b style="color:#dc2626">0 шийд</b>']),
    '√841 = 29 гэж тооцоод <b>“Two”</b> сонгох. Тоо нь сөрөг, тэгэхээр бодох ч хэрэггүй.'))

P.append(trick(3, '1f9d0', 'Орой нь язгууруудын', 'яг дунд',
    '<div style="text-align:center;font-size:36px;margin-bottom:6px"><span class="v">f</span>(<span class="v">x</span>) = (<span class="v">x</span> − 44)(<span class="v">x</span> − 46)</div>The function <span class="v">f</span> is defined by the given equation. For what value of <span class="v">x</span> does <span class="v">f</span>(<span class="v">x</span>) reach its minimum?',
    ['46', '45', '44', '−1'], 'B', 'C', fig_mid(),
    rows(['Язгуур: <span class="m">44</span> ба <span class="m">46</span>', 'Орой: <span class="m">(44 + 46) ÷ 2 = 45</span>', 'Үржих хэлбэрт байвал <b>задлах хэрэггүй</b>']),
    '<b>44</b> эсвэл <b>46</b> сонгох. Эдгээр нь графикийн тэнхлэгтэй огтлолцох цэгүүд, орой биш.'))

P.append(trick(4, '1f92f', 'f(x + 5) нь', 'зүүн тийш 5',
    '<div style="text-align:center;font-size:36px;margin-bottom:6px"><span class="v">f</span>(<span class="v">x</span>) = 4<span class="v">x</span><sup>2</sup> + 64<span class="v">x</span> + 262</div>The function <span class="v">g</span> is defined by <span class="v">g</span>(<span class="v">x</span>) = <span class="v">f</span>(<span class="v">x</span> + 5). For what value of <span class="v">x</span> does <span class="v">g</span>(<span class="v">x</span>) reach its minimum?',
    ['−13', '−8', '−5', '−3'], 'A', 'D', fig_shift(),
    rows(['<i>f</i>-ийн орой: <span class="m">−64 ÷ 8 = −8</span>', '<span class="m">f(x + 5)</span> → <b>зүүн</b> тийш 5', '<span class="m">−8 − 5 = −13</span>']) + '<div style="font-size:22px;opacity:.75;margin-top:6px">Орой: <span class="m" style="font-size:24px">x = −b ÷ 2a</span></div>',
    '“+5” гэж харж <b>баруун</b> тийш шилжүүлэх: −8 + 5 = <b>−3</b>. Нэмэх нь зүүн тийш!'))

P.append(trick(5, '1f4d0', '45-45-90:', 'гипотенуз = катет × √2',
    f'The perimeter of an isosceles right triangle is <span style="white-space:nowrap">18 + 18{R2}</span> inches. What is the length, in inches, of the hypotenuse of this triangle?',
    ['9', f'9{R2}', '18', f'18{R2}'], 'C', 'D', fig_tri(),
    rows(['Периметр: <span class="m">a + a + a√2</span>', '<span class="m">a(2 + √2) = 18 + 18√2</span>', '<span class="m">a = 9√2</span> → гипотенуз <span class="m">= 18</span>']),
    'Асуултад харагдсан <b>18√2</b>-ыг сонгох. Асуусан зүйлээ дахин унш: гипотенуз!'))

# cheat sheet
cs = [('Шийдгүй', '<span class="m">a = c</span>, <span class="m">b ≠ d</span>'), ('Квадрат', '<span class="m">x² = сөрөг</span> → 0 шийд'), ('Орой', 'язгууруудын дундаж'),
      ('Шилжилт', '<span class="m">f(x + k)</span> → зүүн тийш'), ('45-45-90', 'гипотенуз = <span class="m">a√2</span>')]
csr = ''.join(f'<div style="display:flex;align-items:center;gap:18px;padding:16px 22px;{"border-top:2px dashed #eadfc6;" if i else ""}"><div style="flex:none;width:52px;height:52px;border-radius:50%;background:{AC};color:#fff;border:3px solid {INK};display:flex;align-items:center;justify-content:center;font-size:26px;font-weight:800">{i+1}</div><div style="flex:none;width:210px;font-size:30px;font-weight:800">{a}</div><div style="font-size:29px;font-weight:600">{b}</div></div>' for i, (a, b) in enumerate(cs))
P.append((f'<div style="display:flex;align-items:center;justify-content:space-between"><div><div class="pill">ХАДГАЛАХ ХУУДАС</div><h1 style="margin-top:14px">5 трик,<br><em>нэг дор</em></h1></div>{E("1f4dd",150,"wig")}</div>'
          f'<div class="card" style="padding:6px 0">{csr}</div>'
          f'<div class="trap" style="background:{INK}"><span class="k" style="background:{AC}">ДААЛГАВАР</span><div>Аль трик нь чамд хамгийн шинэ байв? <b>Комментод</b> дугаараа бич!</div></div>', ''))

P.append((end_page(AC, SOFT, 'Math-ыг', 'бодож сурна', 'GMP-ийн асуултын санд <b>3,904 Math асуулт</b>, бүгд алхам алхмаар тайлбартай.',
                   sched_cell('MATH', 'Да · Лх · Ба', AC) + sched_cell('АНГЛИ (R&amp;W)', 'Мя · Пү · Бя', AC, True),
                   [('1f9ee', '3,904 Math асуулт'), ('1f4dd', 'Долоо хоног бүр сорил'), ('1f331', 'Үнэгүй түвшин тогтоох тест')]), ''))

if __name__ == '__main__':
    import sys
    render(C, P, HERE / 'out22', 'GMP-SAT-Math-Trik', video_first=('--video' in sys.argv))
