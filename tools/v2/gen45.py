"""SAT Math: absolute value inequalities. Less than gives one interval; greater than gives two. One post, 6 slides.
Content verbatim from sat-math/course/ch18-absolute-value.html (GMP module), lesson 18-3:
lesson text (|A|<k -> -k<A<k; |A|>k -> A>k or A<-k; greater than never gives a double inequality),
the |2x-1|<7 example (-7<2x-1<7, -6<2x<8, -3<x<4) and chapter question 7 (|x+4|>2, answer x>-2 or x<-6)."""
import sys
import base64
import gen24, gen29, gen30, gen31, gen32, gen33

def _b(f): return 'data:image/png;base64,' + base64.b64encode(open(f, 'rb').read()).decode()
ROUND, WORD = _b('gmp-round.png'), _b('gmp-name-dark.png')

AC, SOFT, TINT = '#047857', '#d9f2e8', '#f3fbf7'   # emerald (new colour, not used by recent posts)
GREEN = '#15803d'; RED = '#c62828'; INK = '#1e1e1e'

EXTRA = gen33.EXTRA.replace('#be185d', AC) + """
.lead{font-size:40px!important;line-height:1.35!important}
.rule{font-size:36px!important;padding:24px 30px!important}
.big{font-size:36px!important}
.chips span{font-size:32px!important;padding:12px 24px!important}
.swipe{font-size:30px!important}
.tag{font-size:28px!important;padding:6px 16px!important}
.eqc{font-size:52px!important}
.k{width:64px!important;height:64px!important;font-size:34px!important}
.e{font-size:46px!important;width:auto!important;min-width:400px;white-space:nowrap}
.st .d{font-size:32px!important}
.st{padding:16px 0!important}
.bxs{font-size:44px!important;line-height:1.35!important;margin-top:24px!important}
.bxc div{font-size:36px!important;padding:10px 18px!important}
.ok{font-size:50px!important}
.pill{font-size:28px!important}
.wr{font-size:30px!important} .wr .w{font-size:32px!important;width:290px!important;white-space:nowrap}
.card[style*="font-size:27px"]{font-size:31px!important;white-space:nowrap}
.st .d{font-family:M,sans-serif!important;font-weight:700!important;color:#445!important}
.card .d{font-size:32px!important;margin-top:6px;color:#333;font-weight:700}
.brand{position:absolute;top:34px;left:56px;right:56px;display:flex;align-items:center;gap:18px;z-index:3}
.brand .r{width:112px;height:112px;border-radius:50%;box-shadow:0 4px 14px rgba(15,30,80,.25)}
.brand .w{height:36px;display:block}
.brand .tx{display:flex;flex-direction:column;gap:12px}
.brand .jg{font-family:S,serif;font-weight:700;font-size:27px;letter-spacing:5px;color:#af7f22;line-height:1}
.brand .n{margin-left:auto;font-weight:800;font-size:26px;letter-spacing:2px;color:""" + AC + """;border:2.5px solid """ + AC + """;border-radius:30px;padding:8px 18px}
.ft b{color:#1e2a5a}
"""

def css():
    return gen30.css(AC, SOFT, TINT) + EXTRA

m = gen31.m
X = '<i>x</i>'


def line(inside, labels=('−k', '0', 'k')):
    """Number line with open circles at -k and k. inside=True shades between, False shades both outer rays."""
    W, Y, a, c, b = 968, 60, 250, 484, 718
    s = f'<svg viewBox="0 0 {W} 120" style="display:block;width:100%;height:auto">'
    s += f'<line x1="20" y1="{Y}" x2="{W-20}" y2="{Y}" stroke="{INK}" stroke-width="3"/>'
    if inside:
        s += f'<line x1="{a}" y1="{Y}" x2="{b}" y2="{Y}" stroke="{AC}" stroke-width="12" stroke-linecap="round"/>'
    else:
        s += f'<line x1="30" y1="{Y}" x2="{a}" y2="{Y}" stroke="{AC}" stroke-width="12"/><polygon points="14,{Y} 36,{Y-14} 36,{Y+14}" fill="{AC}"/>'
        s += f'<line x1="{b}" y1="{Y}" x2="{W-30}" y2="{Y}" stroke="{AC}" stroke-width="12"/><polygon points="{W-14},{Y} {W-36},{Y-14} {W-36},{Y+14}" fill="{AC}"/>'
    if labels[1]:
        s += f'<line x1="{c}" y1="{Y-12}" x2="{c}" y2="{Y+12}" stroke="{INK}" stroke-width="3"/>'
    for x in (a, b):
        s += f'<circle cx="{x}" cy="{Y}" r="14" fill="#fff" stroke="{AC}" stroke-width="5"/>'
    for x, t in zip((a, c, b), labels):
        s += f'<text x="{x}" y="{Y+52}" text-anchor="middle" font-family="Georgia,serif" font-size="32" font-weight="700" fill="{INK}">{t}</text>'
    return s + '</svg>'


def mcq(qnum, stem, choices, win=None, cut=()):
    ch = ''.join(f'<div class="{"cut" if i in cut else ""}{" win" if i == win else ""}"><span class="l">{l}</span><span>{c}</span></div>' for i, (l, c) in enumerate(zip('ABCD', choices)))
    return f'''<div class="bx"><div class="bxh"><div><div class="s1">Section 2, Module 1: Math</div><div class="s2">Directions &#8964;</div></div>
<div class="tm">31:24<br><span class="hide">Hide</span></div>
<div class="tl"><div>{gen24.ICAL}<br>Calculator</div><div>{gen24.IREF}<br>Reference</div><div>{gen24.IMORE}<br>More</div></div></div><div class="dash"></div>
<div class="bxb"><div class="qrow"><div class="n">{qnum}</div>{gen24.BOOK}<span class="mr">Mark for Review</span></div>
<div class="bxs">{stem}</div><div class="bxc">{ch}</div></div>
<div class="dash"></div><div class="bxf"><span>Global Math Prep</span><span class="qx">Question {qnum} of 22 &#8963;</span><div class="bt"><span>Back</span><span>Next</span></div></div></div>'''


STEM = f'Which is equivalent to {m(f"|{X}+4|&gt;2")} ?'
CH = [m(f'{X}&gt;−2 or {X}&lt;−6'), m(f'−6&lt;{X}&lt;−2'), m(f'{X}&gt;2 or {X}&lt;−2'), m(f'−2&lt;{X}&lt;6')]

PAGES = [
    # 1. cover
    gen30.cover('SAT MATH · ABSOLUTE VALUE',
                f'{m(f"|{X}+4|&gt;2")}<br>нэг завсар уу?<br><span class="blue">Үгүй, 2 хэсэг.</span>',
                '&lt; бол хариу дунд нь хавчигдана. &gt; бол хоёр тийш салж явна.',
                ['&lt; → 1 завсар', '&gt; → 2 хэсэг'], '1f4cf').replace('font-size:104px', 'font-size:92px'),
    # 2. the idea
    f'''<div class="pill">ГОЛ САНАА</div><div class="h" style="font-size:66px">Зай бага уу,<br><span class="blue">зай их үү?</span></div>
<div class="card" style="padding:18px 26px"><div class="tag n" style="background:{AC}">БАГА · 1 ЗАВСАР</div><div class="eqc">{m("|A| &lt; k &nbsp;→&nbsp; −k &lt; A &lt; k")}</div>{line(True)}</div>
<div class="card" style="padding:18px 26px"><div class="tag n" style="background:{INK}">ИХ · 2 ХЭСЭГ</div><div class="eqc">{m("|A| &gt; k &nbsp;→&nbsp; A &gt; k <span style=font-family:M,sans-serif;font-size:34px;font-weight:800>эсвэл</span> A &lt; −k")}</div>{line(False)}</div>
<div class="rule">{m("−k &gt; A &gt; k")} гэж бичвэл утгагүй: k-аас их, −k-аас бага тоо байхгүй.</div>''',
    # 3. worked example
    f'''<div class="pill">ЖИШЭЭ · АЛХАМ АЛХМААР</div><div class="h" style="font-size:66px">{m(f"|2{X}−1|&lt;7")}<br><span class="blue">{X}&nbsp; хаана байх вэ?</span></div>
<div class="card" style="padding:8px 26px"><div class="steps">
<div class="st"><div class="k">1</div><div class="e">−7 &lt; 2<i>x</i>−1 &lt; 7</div><div class="d">Бага → 1 завсар</div></div>
<div class="st"><div class="k">2</div><div class="e">−6 &lt; 2<i>x</i> &lt; 8</div><div class="d">3 хэсэгт 1 нэм</div></div>
<div class="st"><div class="k">3</div><div class="e">−3 &lt; <i>x</i> &lt; 4</div><div class="d">3 хэсгийг 2-т хуваа</div></div></div></div>
<div class="card" style="padding:18px 26px">{line(True, ('−3', '', '4'))}</div>
<div class="rule">Үйлдлийг 3 хэсэгт зэрэг хий</div>''',
    # 4. question
    f'''<div class="pill">ДАСГАЛ · ЭХЛЭЭД ӨӨРӨӨ БОД</div>{mcq(7, STEM, CH)}
<div class="card big" style="padding:16px 24px">Тэмдэг нь &lt; уу, &gt; уу? 1 завсар уу, 2 хэсэг үү?</div>''',
    # 5. answer
    f'''<div class="pill">ХАРИУ</div>
<div class="okrow"><div class="ok">A</div><div class="h" style="font-size:50px">{m(f"{X} &gt; −2 or {X} &lt; −6")}</div></div>
<div class="card" style="padding:8px 26px"><div class="steps">
<div class="st"><div class="k">1</div><div class="e"><i>x</i>+4 &gt; 2 <span style="font-family:M,sans-serif;font-size:30px;font-weight:800">эсвэл</span> <i>x</i>+4 &lt; −2</div></div>
<div class="st"><div class="k">2</div><div class="e"><i>x</i> &gt; −2 <span style="font-family:M,sans-serif;font-size:30px;font-weight:800">эсвэл</span> <i>x</i> &lt; −6</div></div></div></div>
<div class="card" style="padding:8px 26px">
<div class="wr"><span class="w">B) −6 &lt; <i>x</i> &lt; −2</span><span>Энэ бол {m(f"|{X}+4|&lt;2")}-ын хариу.</span></div>
<div class="wr"><span class="w">C) <i>x</i> &gt; 2 or <i>x</i> &lt; −2</span><span>+4-ийг мартсан.</span></div>
<div class="wr"><span class="w">D) −2 &lt; <i>x</i> &lt; 6</span><span>Энэ 1 завсар. &gt; тэмдэгт 2 хэсэг гарна.</span></div></div>
<div class="rule">Их → 2 хэсэг, “эсвэл” (or)-оор холбоно</div>''',
    # 6. end
    gen30.endp('Шинэ сэдэв удахгүй'),
]


def page(C, n, T, body):
    return f'''<!doctype html><html lang="mn"><head><meta charset="utf-8"><style>{C}</style></head><body><div class="pg">
<div class="brand"><img class="r" src="{ROUND}"><div class="tx"><img class="w" src="{WORD}"><div class="jg">JARGALMAA AMGALAN</div></div><span class="n">{n:02d} / {T:02d}</span></div>
<div class="mn">{body}</div>
<div class="ft"><span><b>globalmathprep.academy</b> · SAT MATH · ABSOLUTE VALUE</span><span>{"Гүйлгээд үз →" if n < T else "@globalmathprep"}</span></div></div></body></html>'''


if __name__ == '__main__':
    gen32.render('--video' in sys.argv, key='Abs-Inequalities', prefix='GMP-Math-Abs-Inequalities', pages=PAGES, cssf=css, pagef=page)
