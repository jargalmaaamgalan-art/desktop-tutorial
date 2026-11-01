"""SAT Math: absolute value equations, the two special cases. |A|=0 has one solution; |A|=negative has none. One post, 6 slides.
Content verbatim from sat-math/course/ch18-absolute-value.html (GMP module), lesson 18-2:
lesson text 'The two special cases' and the 'Solving |A|=k' table, practice Q1 (|x|=5 -> 2), Q3 (|x+3|=0 -> 1), Q4 (|x-4|=-2 -> 0)
and chapter question 5 (|x+8|=-3, answer: none; 'Check the sign on the right first')."""
import sys
import gen30, gen31, gen32, gen47

AC, SOFT, TINT = '#be123c', '#fde4e9', '#fff6f8'   # rose (new colour, not used by recent posts)
GREEN = '#15803d'; RED = '#c62828'

EXTRA = gen47.EXTRA.replace('#6d28d9', AC) + """
.h .m{font-size:1em!important}
.kt{display:flex;align-items:center;gap:20px;padding:16px 0;border-top:2px dashed #e0e3ef}
.kt:first-child{border-top:0}
.kt .a{flex:none;width:200px;font-family:S,serif;font-size:44px}
.kt .b{flex:1;font-family:S,serif;font-size:40px}
.kt .c{flex:none;font-size:32px;font-weight:900;color:""" + AC + """}
.ex3{display:flex;flex-direction:column;gap:18px}
.ex3 .card{display:flex;align-items:center;gap:20px;padding:18px 26px}
.ex3 .q{flex:1;font-family:S,serif;font-size:54px}
.ex3 .r{font-size:33px;font-weight:700;color:#445;text-align:right;line-height:1.3}
.ex3 .r b{display:block;font-size:40px;color:""" + AC + """}
"""


def css():
    return gen30.css(AC, SOFT, TINT) + EXTRA


m = gen31.m
X = '<i>x</i>'
A = '<i>A</i>'
K = '<i>k</i>'

STEM = f'How many solutions does {m(f"|{X}+8|=−3")} have?'
CH = ['none', 'one', 'two', 'infinitely many']

PAGES = [
    # 1. cover
    gen30.cover('SAT MATH · ABSOLUTE VALUE',
                f'{m(f"|{X}+8|=−3")}<br>хэдэн шийдтэй вэ?<br><span class="blue">Бодох ч хэрэггүй.</span>',
                'Баруун талын тэмдгийг эхлээд шалга. Хариу шууд харагдана.',
                ['|A| = k', 'k-ийн тэмдгийг хар'], '1f9d0').replace('font-size:104px', 'font-size:88px'),
    # 2. the idea: the table
    f'''<div class="pill">ГОЛ САНАА</div><div class="h" style="font-size:70px">{m(f"|{A}|={K}")} хэдэн шийдтэй вэ?<br><span class="blue">{m(K)}-аас хамаарна</span></div>
<div class="card" style="padding:6px 26px">
<div class="kt"><span class="a">{m(f"{K}>0")}</span><span class="b">{m(f"{A}={K}")} эсвэл {m(f"{A}=−{K}")}</span><span class="c">2 шийд</span></div>
<div class="kt"><span class="a">{m(f"{K}=0")}</span><span class="b">{m(f"{A}=0")}</span><span class="c">1 шийд</span></div>
<div class="kt"><span class="a">{m(f"{K}<0")}</span><span class="b">боломжгүй</span><span class="c">Шийдгүй</span></div></div>
<div class="lead">0-ээс 0 зайтай тоо ганц: 0 өөрөө. Абсолют утга хэзээ ч сөрөг байдаггүй.</div>''',
    # 3. three examples
    f'''<div class="pill">3 ЖИШЭЭ</div><div class="h" style="font-size:66px">Баруун тал тоо бол<br><span class="blue">тэмдгийг нь хар</span></div>
<div class="ex3">
<div class="card"><span class="q">{m(f"|{X}|=5")}</span><span class="r"><b>2 шийд</b>{m(f"{X}=5")} эсвэл {m(f"{X}=−5")}</span></div>
<div class="card"><span class="q">{m(f"|{X}+3|=0")}</span><span class="r"><b>1 шийд</b>{m(f"{X}+3=0")} → {m(f"{X}=−3")}</span></div>
<div class="card"><span class="q">{m(f"|{X}−4|=−2")}</span><span class="r"><b>Шийдгүй</b>{m(f"|{X}−4|≥0")} үргэлж</span></div></div>
<div class="rule">Эерэг → 2 · Тэг → 1 · Сөрөг → 0</div>''',
    # 4. question
    f'''<div class="pill">ДАСГАЛ · ЭХЛЭЭД ӨӨРӨӨ БОД</div>{gen47.mcq(5, STEM, CH)}
<div class="card big" style="padding:16px 24px">Тооцоо хийхээсээ өмнө баруун талын тэмдгийг хар.</div>''',
    # 5. answer
    f'''<div class="pill">ХАРИУ</div>
<div class="okrow"><div class="ok">A) none</div><div class="h" style="font-size:52px">Шийдгүй</div></div>
<div class="card" style="padding:6px 26px"><div class="steps">
<div class="st"><div class="k">1</div><div class="e">{m(f"|{X}+8|≥0")}</div><div class="d">Абсолют утга хэзээ ч сөрөг биш</div></div>
<div class="st"><div class="k">2</div><div class="e">{m(f"|{X}+8|≠−3")}</div><div class="d">Тиймээс −3-тай хэзээ ч тэнцэхгүй</div></div></div></div>
<div class="card" style="padding:6px 26px">
<div class="wr"><span class="w">B) one</span><span>|A|=k хэлбэрт 1 шийд зөвхөн k=0 үед гарна.</span></div>
<div class="wr"><span class="w">C) two</span><span>|A|=k хэлбэрт 2 шийд зөвхөн k>0 үед гарна.</span></div>
<div class="wr"><span class="w">D) infinitely many</span><span>Нэг ч {X} тэгшитгэлийг үнэн болгохгүй.</span></div></div>
<div class="rule">Эхлээд баруун талын тэмдгийг шалга</div>''',
    # 6. end
    gen30.endp('Шинэ сэдэв удахгүй').replace('Дараагийн хичээл', 'Дараагийн пост').replace('<div style="color:#556">WhatsApp', '<div style="color:#556">Улаанбаатарын цагаар</div><div style="color:#556">WhatsApp'),
]


def page(C, n, T, body):
    return gen47.page(C, n, T, body)


if __name__ == '__main__':
    gen32.render('--video' in sys.argv, key='Abs-No-Solution', prefix='GMP-Math-Abs-No-Solution', pages=PAGES, cssf=css, pagef=page)
