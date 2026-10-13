"""SAT Math: tolerance word problems. Midpoint inside the bars, half-width outside. One post, 6 slides.
Content from sat-math/course/ch18-absolute-value.html (GMP module), lesson 18-4:
lesson text (16 to 18 ounces -> |w-17|<1, check backwards, midpoint not endpoint) and practice Q2 (tape 400 to 410 feet) with its why-notes."""
import sys
import gen29, gen30, gen31, gen32, gen33

AC, SOFT, TINT = '#c2410c', '#fde3d3', '#fff7f2'   # burnt orange (not used by recent posts)
GREEN = '#15803d'; RED = '#c62828'

EXTRA = gen33.EXTRA.replace('#be185d', AC)

def css():
    return gen30.css(AC, SOFT, TINT) + EXTRA

m = gen31.m
L = '<i>l</i>'; W = '<i>w</i>'

STEM = f'A roll of tape must contain between {m("400")} and {m("410")} feet. Which inequality expresses the acceptable lengths {m(L)} ?'
CH = [m(f'|{L}−405|&lt;5'), m(f'|{L}−400|&lt;10'), m(f'|{L}−405|&gt;5'), m(f'|{L}+405|&lt;5')]

PAGES = [
    # 1. cover
    gen30.cover('SAT MATH · ABSOLUTE VALUE',
                f'16-аас 18-ын<br>хооронд<br><span class="blue">= {m(f"|{W}−17|&lt;1")}</span>',
                'Хоёр тооны хоорондох мужийг нэг модультай тэнцэтгэл бишээр бичих арга.',
                ['Дотор нь: дунд цэг', 'Гадна нь: хагас өргөн'], '1f4e6').replace('font-size:104px', 'font-size:90px'),
    # 2. the idea
    f'''<div class="pill">ГОЛ САНАА</div><div class="h" style="font-size:62px">{m("|<i>x</i>−дунд цэг|&lt;хагас өргөн")}</div>
<div class="lead">Савлагааны жин 16-аас 18 унцын хооронд. Дунд цэг нь 17, хоёр тийшээ 1 зайтай.</div>
<div class="card" style="padding:8px 26px"><div class="steps">
<div class="st"><div class="k">1</div><div class="e">(16+18) ÷ 2 = 17</div><div class="d">Дунд цэг: 2 захын дундаж</div></div>
<div class="st"><div class="k">2</div><div class="e">(18−16) ÷ 2 = 1</div><div class="d">Хагас өргөн: зөрүүний хагас</div></div>
<div class="st"><div class="k">3</div><div class="e">{m(f"|{W}−17|&lt;1")}</div><div class="d">Дунд цэг дотор, хагас өргөн гадна</div></div></div>
{gen33.twoside(17, 1).replace('#be185d', AC)}</div>
<div class="rule">Шалгах: {m(f"−1&lt;{W}−17&lt;1")} → {m(f"16&lt;{W}&lt;18")} ✓</div>''',
    # 3. question
    f'''<div class="pill">ДАСГАЛ · ЭХЛЭЭД ӨӨРӨӨ БОД</div>{gen33.mcq(2, STEM, CH)}
<div class="card big" style="padding:16px 24px">Эхлээд дунд цэг, хагас өргөнөө ол. Дараа нь хариугаа задалж шалга.</div>''',
    # 4. answer
    f'''<div class="pill">ХАРИУ</div>
<div class="okrow"><div class="ok">A) {m(f"|{L}−405|&lt;5")}</div></div>
<div class="card" style="padding:8px 26px"><div class="steps">
<div class="st"><div class="k">1</div><div class="e">(400+410) ÷ 2 = 405</div><div class="d">Дунд цэг</div></div>
<div class="st"><div class="k">2</div><div class="e">(410−400) ÷ 2 = 5</div><div class="d">Хагас өргөн</div></div>
<div class="st"><div class="k">3</div><div class="e">400 &lt; {L} &lt; 410</div><div class="d">Задлаад шалгав ✓</div></div></div></div>
<div class="card" style="padding:8px 26px">
<div class="wr"><span class="w">✗ B)</span><span>Задлахад {m(f"390&lt;{L}&lt;410")} гарна. Хэт өргөн.</span></div>
<div class="wr"><span class="w">✗ C)</span><span>"Их" тэмдэг нь шаардлага хангаагүй ороомгийг заана.</span></div>
<div class="wr"><span class="w">✗ D)</span><span>Модулийн дотор хасах тэмдэг байх ёстой.</span></div></div>''',
    # 5. trap
    f'''<div class="pill">УРХИ</div><div class="h" style="font-size:68px">Дотор нь <span class="blue">дунд цэг</span>,<br>зах биш</div>
<div class="card"><div class="tag n">БУРУУ</div><div class="eqc">{m(f"|{W}−16|&lt;2")} → {m(f"14&lt;{W}&lt;18")}</div></div>
<div class="card"><div class="tag y">ЗӨВ</div><div class="eqc">{m(f"|{W}−17|&lt;1")} → {m(f"16&lt;{W}&lt;18")}</div></div>
<div class="rule">Сонголтод 3 хувилбар бүгд гардаг. Задлахад анхны муж гарвал л зөв.</div>''',
    # 6. end
    gen30.endp('Шинэ сэдэв удахгүй'),
]


def page(C, n, T, body):
    return f'''<!doctype html><html lang="mn"><head><meta charset="utf-8"><style>{C}</style></head><body><div class="pg">
<div class="top"><img src="{gen29.LOGO}"><span>{n:02d} / {T:02d}</span></div>
<div class="mn">{body}</div>
<div class="ft"><span>SAT MATH · ABSOLUTE VALUE</span><span>{"Гүйлгээд үз →" if n < T else "@globalmathprep"}</span></div></div></body></html>'''


if __name__ == '__main__':
    gen32.render('--video' in sys.argv, key='Tolerance', prefix='GMP-Math-Tolerance', pages=PAGES, cssf=css, pagef=page)
