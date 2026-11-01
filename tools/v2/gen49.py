"""SAT Math: absolute value equations. The two solutions are symmetric about the centre, so their sum is twice the centre. One post, 6 slides.
Content verbatim from sat-math/course/ch18-absolute-value.html (GMP module), lesson 18-2:
lesson text 'Sums and products of the solutions' (|x-2|=10 -> 2+-10, sum 2x2=4), worked example 3 (a-d),
chapter question 3 (|x-5|=9, sum of the two values = 10, 'The sum is twice the centre')
and practice Q7 (|3x|=12 -> 4 and -4, sum 0, 'Solutions symmetric about zero always sum to zero')."""
import sys
import gen30, gen31, gen32, gen33, gen47

AC, SOFT, TINT = '#0e7490', '#dcf1f6', '#f3fafc'   # ocean cyan (new colour, not used by recent posts)
GREEN = '#15803d'; RED = '#c62828'
gen33.AC = AC   # number line colour

EXTRA = gen47.EXTRA.replace('#6d28d9', AC) + """
.spr{font-size:30px!important}.bxin{width:260px!important;height:72px!important}
.bxs{margin-bottom:10px}
.h .m{font-size:1em!important}
.st .e{font-size:44px!important}
.lead{font-size:40px!important}
"""


def css():
    return gen30.css(AC, SOFT, TINT) + EXTRA


m = gen31.m
X = '<i>x</i>'

STEM = f'If {m(f"|{X}−5|=9")}, what is the sum of the two possible values of {m(X)} ?'

PAGES = [
    # 1. cover
    gen30.cover('SAT MATH · ABSOLUTE VALUE',
                f'Шийдүүдийн<br>нийлбэрийг асуувал<br><span class="blue">богино зам бий</span>',
                '|x−c|=k (k>0) тэгшитгэлийн 2 шийд c цэгээс ижил зайд байрладаг.',
                ['|A| = k', 'Нийлбэр = 2 × төв'], '2795').replace('font-size:104px', 'font-size:84px'),
    # 2. the idea
    f'''<div class="pill">ГОЛ САНАА</div><div class="h" style="font-size:70px">2 шийд<br><span class="blue">төвийн 2 талд</span></div>
<div class="lead">2 шийд нь | | доторхыг 0 болгох цэгээс (төвөөс) 2 тийш яг ижил зайд байна.</div>
<div class="card" style="padding:14px 26px"><div class="cap" style="text-align:center">{m(f"|{X}−2|=10")} · төв = 2</div>{gen33.twoside(2, 10)}</div>
<div class="rule">2 ± 10 → нийлбэр = 2 × 2 = 4</div>''',
    # 3. worked example
    f'''<div class="pill">ЖИШЭЭ · АЛХАМ АЛХМААР</div><div class="h" style="font-size:70px">{m(f"|{X}−2|=10")}<br><span class="blue"><i>x</i>-ийн 2 утгын нийлбэр?</span></div>
<div class="card" style="padding:6px 26px"><div class="steps">
<div class="st"><div class="k">a</div><div class="e">{X}−2=10 эсвэл {X}−2=−10</div></div>
<div class="st"><div class="k">b</div><div class="e">{X}=12 эсвэл {X}=−8</div></div>
<div class="st"><div class="k">c</div><div class="e">12+(−8)=4</div><div class="d">Асуусан нийлбэр</div></div>
<div class="st"><div class="k">d</div><div class="e">2×2=4</div><div class="d">Богино зам: төвийн 2 дахин</div></div></div></div>
<div class="rule">2 зам, 1 хариу. d зам илүү хурдан.</div>''',
    # 4. question
    f'''<div class="pill">ДАСГАЛ · ЭХЛЭЭД ӨӨРӨӨ БОД</div>{gen31.spr(3, STEM)}
<div class="card big" style="padding:16px 24px">{m(f"|{X}−5|")} доторх хэсэг хэзээ 0 болох вэ? Тэр бол төв.</div>''',
    # 5. answer
    f'''<div class="pill">ХАРИУ</div>
<div class="okrow"><div class="ok">10</div><div class="h" style="font-size:52px">Төв 5, нийлбэр 2 × 5</div></div>
<div class="card" style="padding:6px 26px"><div class="steps">
<div class="st"><div class="k">1</div><div class="e">{X}=14 эсвэл {X}=−4</div></div>
<div class="st"><div class="k">2</div><div class="e">14+(−4)=10=2×5</div></div></div></div>
<div class="card"><div class="tag y">БАС НЭГ ЖИШЭЭ</div><div class="big">{m(f"|3{X}|=12")} → {m(f"{X}=4")} эсвэл {m(f"{X}=−4")}. Төв нь 0 тул нийлбэр нь <b class="hl">0</b>.</div></div>
<div class="rule">Нийлбэр = төвийн 2 дахин</div>''',
    # 6. end
    gen30.endp('Шинэ сэдэв удахгүй').replace('Дараагийн хичээл', 'Дараагийн пост').replace('<div style="color:#556">WhatsApp', '<div style="color:#556">Улаанбаатарын цагаар</div><div style="color:#556">WhatsApp'),
]


def page(C, n, T, body):
    return gen47.page(C, n, T, body)


if __name__ == '__main__':
    gen32.render('--video' in sys.argv, key='Abs-Sum', prefix='GMP-Math-Abs-Sum-of-Solutions', pages=PAGES, cssf=css, pagef=page)
