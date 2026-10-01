import math
import gen25 as D, gen24, gen23 as G
from gen18 import *
C = D.C + '''
.bxs{font-size:30px!important;margin-top:14px!important}
.bxd{font-size:33px!important;margin:14px 0 0!important}
.bxc{gap:11px!important;margin-top:16px!important}
.bxc div{padding:9px 16px!important;font-size:29px!important}
.mn{gap:22px}
'''
v = G.v
AC, SOFT, GREEN, RED = G.AC, G.SOFT, G.GREEN, G.RED

def rad(n): return f'<math style="margin-left:-2px"><msqrt><mn>{n}</mn></msqrt></math>'

def qslide(n, dom, qnum, disp, stem, choices, emo):
    tag = f'<span class="tag h">{E("1f525",30)} Hard</span><span class="tag">{dom}</span><span class="tag">{E("23f1",28)} Гараар удаан</span>'
    return (f'''<div style="display:flex;align-items:center;justify-content:space-between"><div><div class="pill">ХЭЦҮҮ АСУУЛТ {n}/5 · ЭХЛЭЭД ӨӨРӨӨ БОД</div><div style="margin-top:14px">{tag}</div></div>{E(emo,96,"wig")}</div>
{gen24.bluebook(n, qnum, disp, stem, choices)}
<div class="trap"><span class="k" style="background:{AC}">ДАРААГИЙН ХУУДАС</span><div>Desmos-оор хэдхэн секундэд хэрхэн бодохыг харна</div></div>''', '')

def aslide(n, ta, tb, ok, okv, dmhtml, steps, check, trap):
    st = ''.join(f'<div style="display:flex;align-items:center;gap:10px;font-size:25px;font-weight:700;line-height:1.25"><span style="flex:none;width:36px;height:36px;border-radius:50%;background:{AC};color:#fff;display:flex;align-items:center;justify-content:center;font-size:19px;font-weight:800">{i}</span><span>{t}</span></div>' for i, t in enumerate(steps, 1))
    return (f'''<div><div class="pill">ХАРИУ {n}/5 · DESMOS</div><h1 style="font-size:52px;margin-top:10px">{ta}<br><em>{tb}</em></h1></div>
{dmhtml}
<div class="card" style="display:flex;gap:20px;align-items:center;padding:18px 22px"><div class="okchip"><small>ЗӨВ ХАРИУ</small>{ok}) {okv}</div><div style="display:flex;flex-direction:column;gap:8px">{st}<div style="font-size:22px;font-weight:600;opacity:.8">Гараар шалгах: {check}</div></div></div>
<div class="trap"><span class="k">УРХИ</span><div>{trap}</div></div>''', '')

f4 = lambda x: 4 * x * x + 64 * x + 262
circle = [(-10 + 12 * math.cos(t / 100 * 2 * math.pi), -8 + 12 * math.sin(t / 100 * 2 * math.pi)) for t in range(101)]
P = []
P.append((f'''<div class="pill">SAT MATH · DESMOS</div>
<h1 style="font-size:100px;margin-top:8px">Хэцүү<br>5 асуулт,<br><em>Desmos-оор хялбар</em></h1>
<div class="card" style="padding:22px 28px;font-size:30px;font-weight:700;line-height:1.4">Bluebook-т <span class="hl">Desmos</span> тооны машин Math хэсэг бүхэлдээ нээлттэй. Ихэнх сурагч үүнийг бүрэн ашигладаггүй.</div>
<div style="display:flex;gap:14px;flex-wrap:wrap"><span class="tag h">{E("1f525",30)} 5 Hard</span><span class="tag">College Board Question Bank</span><span class="tag">Алхам алхмаар</span></div>
<div style="display:flex;justify-content:space-between;align-items:center">
 <div style="font-size:24px;font-weight:700;opacity:.75">Хадгалаад ав · Найздаа илгээ</div>
 <div style="background:#16121f;color:#fff;border-radius:34px;padding:14px 28px;font-size:28px;font-weight:800;box-shadow:6px 6px 0 {AC}">Гүйлгээд үз →</div></div>''',
 f'''<div style="position:absolute;right:60px;top:200px;z-index:1">{E("1f92f",190,"fl")}</div>
<div style="position:absolute;right:110px;top:440px;z-index:1" class="pop">{E("1f4c8",120,"wig")}</div>'''))

# 1 system zero
P.append(qslide(1, 'Algebra', 12, f'<div>−12{v("x")} + 14{v("y")} = 36</div><div>−6{v("x")} + 7{v("y")} = −18</div>', 'How many solutions does the given system of equations have?', ['Exactly one', 'Exactly two', 'Infinitely many', 'Zero'], '1f914'))
P.append(aslide(1, 'Огтлолцохгүй бол', 'шийдгүй', 'D', 'Zero',
    D.dm('Хэцүү асуулт 1', [('red', 'wave', f'−12{v("x")} + 14{v("y")} = 36', ''), ('blue', 'wave', f'−6{v("x")} + 7{v("y")} = −18', '')],
         [('f', lambda x: (36 + 12 * x) / 14, 'red'), ('f', lambda x: (-18 + 6 * x) / 7, 'blue'), ('note', 6.5, -4.5, 'параллель: огтлолцохгүй', G.DC['red'])], (-14, 14), (-7, 8)),
    ['Хоёр тэгшитгэлээ хуулж бич', 'Шулуунууд параллель гарна', 'Огтлолцол 0 → шийд 0'],
    '2-р тэгшитгэлийг 2-оор үржүүлбэл −12x + 14y = −36. Зүүн тал ижил, баруун тал өөр.',
    'Коэффициент ижил харагдаад <b>“Infinitely many”</b> сонгох. Баруун талыг шалга: 36 ≠ −36.'))

# 2 nonlinear system
P.append(qslide(2, 'Advanced Math', 17, f'<div>{v("x")} − {v("y")} = 1</div><div>{v("x")} + {v("y")} = {v("x")}<sup>2</sup> − 3</div>', 'Which ordered pair is a solution to the system of equations above?',
    [f'(1 + {rad(3)}, {rad(3)})', f'({rad(3)}, −{rad(3)})', f'(1 + {rad(5)}, {rad(5)})', f'({rad(5)}, −1 + {rad(5)})'], '1f9d0'))
P.append(aslide(2, 'Системийн шийд =', 'огтлолцох цэг', 'A', '(1+√3, √3)',
    D.dm('Хэцүү асуулт 2', [('red', 'wave', f'{v("x")} − {v("y")} = 1', ''), ('blue', 'wave', f'{v("x")} + {v("y")} = {v("x")}<sup>2</sup> − 3', '')],
         [('f', lambda x: x - 1, 'red'), ('f', lambda x: x * x - 3 - x, 'blue'), ('pt', 1 + math.sqrt(3), math.sqrt(3), 'black', '(2.732, 1.732)', 'se'), ('pt', 1 - math.sqrt(3), -math.sqrt(3), 'black', '(−0.732, −1.732)', 'nw')], (-6, 7), (-4.5, 5.5)),
    ['Хоёр тэгшитгэлээ бич', 'Огтлолцох цэг дээр дар', '1 + √3 ≈ 2.732, √3 ≈ 1.732'],
    'y = x − 1-ийг орлуулбал x² − 2x − 2 = 0 → x = 1 ± √3.',
    '√5 бүхий хариу руу хазайх. Desmos-оор тоон утгыг нь тулгаад шалга: 1 + √5 ≈ 3.24.'))

# 3 h(x)
P.append(qslide(3, 'Advanced Math', 19, f'{v("h")}({v("x")}) = 2({v("x")} − 4)<sup>2</sup> − 32',
    f'The quadratic function {v("h")} is defined as shown. In the {v("xy")}-plane, the graph of {v("y")} = {v("h")}({v("x")}) intersects the {v("x")}-axis at the points (0, 0) and ({v("t")}, 0), where {v("t")} is a constant. What is the value of {v("t")}?',
    ['1', '2', '4', '8'], '1f62e'))
P.append(aslide(3, 'x-тэнхлэгтэй огтлолцол', '= язгуур', 'D', '8',
    D.dm('Хэцүү асуулт 3', [('red', 'wave', f'{v("h")}({v("x")}) = 2({v("x")} − 4)<sup>2</sup> − 32', '')],
         [('f', lambda x: 2 * (x - 4) ** 2 - 32, 'red'), ('pt', 0, 0, 'red', '(0, 0)', 'nw'), ('pt', 8, 0, 'red', '(8, 0)', 'ne'), ('pt', 4, -32, 'red', '(4, −32)', 's')], (-5, 13), (-40, 20)),
    ['Функцээ хуулж бич', 'x-тэнхлэгтэй огтлолцол дээр дар', '(8, 0) → t = 8'],
    'Орой x = 4. Тэг цэгүүд тэгш хэмтэй: 0 ба 4 + 4 = 8.',
    'Оройн x = <b>4</b>-ийг сонгох. Асуулт тэнхлэгтэй огтлолцох <b>хоёр дахь</b> цэгийг асууж байна.'))

# 4 shift
P.append(qslide(4, 'Advanced Math', 21, f'{v("f")}({v("x")}) = 4{v("x")}<sup>2</sup> + 64{v("x")} + 262',
    f'The function {v("g")} is defined by {v("g")}({v("x")}) = {v("f")}({v("x")} + 5). For what value of {v("x")} does {v("g")}({v("x")}) reach its minimum?', ['−13', '−8', '−5', '−3'], '1f92f'))
P.append(aslide(4, 'Desmos-д f(x + 5)', 'гэж шууд бич', 'A', '−13',
    D.dm('Хэцүү асуулт 4', [('red', 'wave', f'{v("f")}({v("x")}) = 4{v("x")}<sup>2</sup> + 64{v("x")} + 262', ''), ('blue', 'wave', f'{v("g")}({v("x")}) = {v("f")}({v("x")} + 5)', '')],
         [('f', f4, 'red'), ('f', lambda x: f4(x + 5), 'blue'), ('pt', -8, 6, 'red', '(−8, 6)', 'se'), ('pt', -13, 6, 'blue', '(−13, 6)', 'sw')], (-22, 4), (-10, 50)),
    ['f-ээ, дараа нь g(x) = f(x + 5)-ыг бич', 'Цэнхэр графикийн доод цэг дээр дар', '(−13, 6) → x = −13'],
    'f-ийн орой −64 ÷ 8 = −8. f(x + 5) нь зүүн тийш 5 → −13.',
    '“+5” гэж харж баруун тийш шилжүүлэх: −8 + 5 = <b>−3</b>. Нэмэх нь зүүн тийш!'))

# 5 circle
P.append(qslide(5, 'Geometry &amp; Trig', 22, f'{v("x")}<sup>2</sup> + 20{v("x")} + {v("y")}<sup>2</sup> + 16{v("y")} = −20',
    f'The equation above defines a circle in the {v("xy")}-plane. What are the coordinates of the center of the circle?', ['(−20, −16)', '(−10, −8)', '(10, 8)', '(20, 16)'], '1f50d'))
yspan = 30
P.append(aslide(5, 'Тойргийн тэгшитгэлийг', 'шууд бич', 'B', '(−10, −8)',
    D.dm('Хэцүү асуулт 5', [('purple', 'wave', f'{v("x")}<sup>2</sup> + 20{v("x")} + {v("y")}<sup>2</sup> + 16{v("y")} = −20', ''), ('black', 'pt', '(−10, −8)', '')],
         [('curve', circle, 'purple'), ('pt', -10, -8, 'black', '(−10, −8)', 'sw')], (-10 - yspan * 962 / 290 / 2, -10 + yspan * 962 / 360 / 2), (-8 - yspan / 2, -8 + yspan / 2)),
    ['Тэгшитгэлээ шууд хуулж бич', 'Төвийн цэгээ бичээд шалга', 'Яг голд нь → (−10, −8)'],
    'Төв = (−20 ÷ 2, −16 ÷ 2) = (−10, −8). Радиус 12.',
    '<b>(10, 8)</b> сонгох: тэмдэг эсрэгээрээ! Төв нь коэффициентийн хагасын <b>эсрэг тэмдэгтэй</b>.'))

cs = [('Шийдийн тоо', 'огтлолцлын тоо'), ('Системийн шийд', 'огтлолцох цэг'), ('Язгуур', 'x-тэнхлэгтэй огтлолцол'), ('Min / max', 'доод, дээд цэг дээр дар'), ('Тойрог', 'шууд бичээд төвөө шалга')]
csr = ''.join(f'<div style="display:flex;align-items:center;gap:18px;padding:16px 22px;{"border-top:2px dashed #eadfc6;" if i else ""}"><div style="flex:none;width:52px;height:52px;border-radius:50%;background:{AC};color:#fff;border:3px solid #16121f;display:flex;align-items:center;justify-content:center;font-size:26px;font-weight:800">{i+1}</div><div style="flex:none;width:280px;font-size:30px;font-weight:800">{a}</div><div style="font-size:29px;font-weight:600">= {b}</div></div>' for i, (a, b) in enumerate(cs))
P.append((f'<div style="display:flex;align-items:center;justify-content:space-between"><div><div class="pill">ХАДГАЛАХ ХУУДАС</div><h1 style="margin-top:14px">Desmos-ын<br><em>5 нууц</em></h1></div>{E("1f4dd",150,"wig")}</div>'
          f'<div class="card" style="padding:6px 0">{csr}</div>'
          f'<div class="trap"><span class="k" style="background:{AC}">ДААЛГАВАР</span><div>Аль нь чамд шинэ байв? Дугаараа <b>комментод</b> бич!</div></div>', ''))
P.append(G.P[-1])

if __name__ == '__main__':
    import sys
    render(C, P, HERE / 'out26', 'GMP-SAT-Math-Hard-Desmos', video_first=('--video' in sys.argv))
