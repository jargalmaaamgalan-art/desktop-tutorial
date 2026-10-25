"""SAT Math: graphs of absolute value. The V never goes below the x-axis; the vertex is where the inside is zero. One post, 6 slides.
Content verbatim from sat-math/course/ch18-absolute-value.html (GMP module), lesson 18-5:
lesson text (y=|x| is y=x with the part below the axis reflected up; the graph never dips below the axis;
test an easy point), worked example 8 (y=|2x-1|: y>=0, (0,1), one x-intercept x=1/2, vertex (1/2,0))
and chapter question 11 (graph of y=|x-5|, answer: a V with vertex at (5,0))."""
import sys
import base64
import gen24, gen30, gen31, gen32, gen33

def _b(f): return 'data:image/png;base64,' + base64.b64encode(open(f, 'rb').read()).decode()
ROUND, WORD = _b('gmp-round.png'), _b('gmp-name-dark.png')

AC, SOFT, TINT = '#6d28d9', '#ece4fb', '#f9f6ff'   # violet (new colour, not used by recent posts)
GREEN = '#15803d'; RED = '#c62828'; INK = '#1e1e1e'

EXTRA = gen33.EXTRA.replace('#be185d', AC) + """
.lead{font-size:38px!important;line-height:1.35!important}
.rule{font-size:36px!important;padding:24px 30px!important}
.big{font-size:36px!important}
.chips span{font-size:32px!important;padding:12px 24px!important}
.swipe{font-size:30px!important}
.tag{font-size:26px!important;padding:6px 16px!important}
.k{width:64px!important;height:64px!important;font-size:34px!important}
.e{font-size:42px!important;width:auto!important;min-width:330px;white-space:nowrap}
.st .d{font-size:32px!important;font-family:M,sans-serif!important;font-weight:700!important;color:#445!important}
.st{padding:14px 0!important}
.bxs{font-size:44px!important;line-height:1.35!important;margin-top:24px!important}
.bxc div{font-size:36px!important;padding:10px 18px!important}
.ok{font-size:50px!important}
.pill{font-size:28px!important}
.wr{font-size:30px!important} .wr .w{font-size:32px!important;width:250px!important;white-space:nowrap}
.card[style*="font-size:27px"]{font-size:31px!important;white-space:nowrap}
.two{display:flex;gap:20px} .two .card{flex:1;padding:16px 18px;text-align:center}
.cap{font-family:S,serif;font-size:40px;margin-top:4px}
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
Y = '<i>y</i>'


def graph(f, x0, x1, y0, y1, u=60, pts=(), ghost=None, disp=None):
    """Coordinate grid with the graph of f (solid, accent) and an optional ghost function (dashed red, the part below the axis)."""
    W, H = (x1 - x0) * u, (y1 - y0) * u
    sx = lambda x: (x - x0) * u
    sy = lambda y: (y1 - y) * u
    s = f'<svg viewBox="-10 -10 {W+20} {H+20}" style="display:block;width:{f'{disp}px' if disp else '100%'};height:auto;margin:0 auto">'
    for i in range(x0, x1 + 1):
        s += f'<line x1="{sx(i)}" y1="0" x2="{sx(i)}" y2="{H}" stroke="#e4e1ee" stroke-width="2"/>'
    for j in range(y0, y1 + 1):
        s += f'<line x1="0" y1="{sy(j)}" x2="{W}" y2="{sy(j)}" stroke="#e4e1ee" stroke-width="2"/>'
    s += f'<line x1="0" y1="{sy(0)}" x2="{W}" y2="{sy(0)}" stroke="{INK}" stroke-width="3"/>'
    s += f'<line x1="{sx(0)}" y1="0" x2="{sx(0)}" y2="{H}" stroke="{INK}" stroke-width="3"/>'
    s += f'<text x="{W-6}" y="{sy(0)-12}" text-anchor="end" font-family="Georgia,serif" font-style="italic" font-size="30" fill="{INK}">x</text>'
    s += f'<text x="{sx(0)+12}" y="26" font-family="Georgia,serif" font-style="italic" font-size="30" fill="{INK}">y</text>'

    def path(fn, color, dash=''):
        n = 240; p = []
        for k in range(n + 1):
            x = x0 + (x1 - x0) * k / n; yv = fn(x)
            yv = max(min(yv, y1 + 1), y0 - 1)
            p.append(f'{sx(x):.1f},{sy(yv):.1f}')
        return f'<polyline points="{" ".join(p)}" fill="none" stroke="{color}" stroke-width="7" stroke-linejoin="round" {dash}/>'
    s += f'<clipPath id="c"><rect x="0" y="0" width="{W}" height="{H}"/></clipPath><g clip-path="url(#c)">'
    if ghost:
        s += path(ghost, RED, 'stroke-dasharray="14 10" opacity=".8"')
    s += path(f, AC) + '</g>'
    for (px, py, lab, anchor) in pts:
        s += f'<circle cx="{sx(px)}" cy="{sy(py)}" r="12" fill="{INK}" stroke="#fff" stroke-width="3"/>'
        dx, dy, a = {'start': (18, -16, 'start'), 'end': (-26, -10, 'end'), 'below': (18, 44, 'start')}[anchor]
        s += f'<text x="{sx(px)+dx}" y="{sy(py)+dy}" text-anchor="{a}" font-family="Georgia,serif" font-size="32" font-weight="700" fill="{INK}" stroke="#fff" stroke-width="9" paint-order="stroke" stroke-linejoin="round">{lab}</text>'
    return s + '</svg>'


def mcq(qnum, stem, choices):
    ch = ''.join(f'<div><span class="l">{l}</span><span>{c}</span></div>' for l, c in zip('ABCD', choices))
    return f'''<div class="bx"><div class="bxh"><div><div class="s1">Section 2, Module 1: Math</div><div class="s2">Directions &#8964;</div></div>
<div class="tm">31:24<br><span class="hide">Hide</span></div>
<div class="tl"><div>{gen24.ICAL}<br>Calculator</div><div>{gen24.IREF}<br>Reference</div><div>{gen24.IMORE}<br>More</div></div></div><div class="dash"></div>
<div class="bxb"><div class="qrow"><div class="n">{qnum}</div>{gen24.BOOK}<span class="mr">Mark for Review</span></div>
<div class="bxs">{stem}</div><div class="bxc">{ch}</div></div>
<div class="dash"></div><div class="bxf"><span>Global Math Prep</span><span class="qx">Question {qnum} of 22 &#8963;</span><div class="bt"><span>Back</span><span>Next</span></div></div></div>'''


STEM = f'Which describes the graph of {m(f"{Y}=|{X}−5|")} ?'
CH = [f'a V with vertex at {m("(5, 0)")}', f'a V with vertex at {m("(−5, 0)")}',
      f'a V with vertex at {m("(0, 5)")}', f'a V with vertex at {m("(0, −5)")}']

G_LINE = graph(lambda x: x, -3, 3, -3, 3, u=70, ghost=None)
G_ABS = graph(lambda x: abs(x), -3, 3, -3, 3, u=70, ghost=lambda x: x, pts=[(0, 0, '(0, 0)', 'below')])
G_EX = graph(lambda x: abs(2 * x - 1), -2, 3, -1, 4, u=70, disp=380, pts=[(0, 1, '(0, 1)', 'end'), (0.5, 0, '(½, 0)', 'below')])

PAGES = [
    # 1. cover
    gen30.cover('SAT MATH · ABSOLUTE VALUE',
                f'{m(f"{Y}=|{X}−5|")}<br>V-ийн орой хаана?<br><span class="blue">(0, 5) биш.</span>',
                'Абсолют утгын графикийг 2 энгийн шалгуураар таних арга.',
                ['V хэлбэр', f'{Y} ≥ 0', 'Дотор = 0 → орой'], '1f4d0').replace('font-size:104px', 'font-size:90px'),
    # 2. the idea
    f'''<div class="pill">ГОЛ САНАА</div><div class="h" style="font-size:66px"><i>x</i> тэнхлэгээс доош<br><span class="blue">хэзээ ч ордоггүй</span></div>
<div class="two"><div class="card">{G_LINE}<div class="cap">{m(f"{Y}={X}")}</div></div><div class="card">{G_ABS}<div class="cap">{m(f"{Y}=|{X}|")}</div></div></div>
<div class="lead">{m(f"{Y}={X}")} шулууны <i>x</i> тэнхлэгээс доорх хэсгийг дээш нугалахад V үүснэ.</div>
<div class="rule"><i>x</i> тэнхлэгээс доош орсон график → шууд хас</div>''',
    # 3. worked example
    f'''<div class="pill">ЖИШЭЭ · АЛХАМ АЛХМААР</div><div class="h" style="font-size:62px">{m(f"{Y}=|2{X}−1|")}<br><span class="blue">ямар график вэ?</span></div>
<div class="card" style="padding:6px 26px"><div class="steps">
<div class="st"><div class="k">1</div><div class="e">{Y} ≥ 0</div><div class="d"><i>x</i> тэнхлэгээс доош орохгүй</div></div>
<div class="st"><div class="k">2</div><div class="e">{X}=0 → {Y}=|−1|=1</div><div class="d">(0, 1) цэгийг дайрна</div></div>
<div class="st"><div class="k">3</div><div class="e">2{X}−1=0 → {X}=½</div><div class="d">Орой нь (½, 0)</div></div></div></div>
<div class="card" style="padding:14px 26px">{G_EX}</div>''',
    # 4. question
    f'''<div class="pill">ДАСГАЛ · ЭХЛЭЭД ӨӨРӨӨ БОД</div>{mcq(11, STEM, CH)}
<div class="card big" style="padding:16px 24px">{m(f"|{X}−5|")} доторх хэсэг хэзээ 0 болох вэ?</div>''',
    # 5. answer
    f'''<div class="pill">ХАРИУ</div>
<div class="okrow"><div class="ok">A</div><div class="h" style="font-size:52px">Орой нь {m("(5, 0)")}</div></div>
<div class="card" style="padding:6px 26px"><div class="steps">
<div class="st"><div class="k">1</div><div class="e">{X}−5=0 → {X}=5</div><div class="d">Дотор нь 0 болох цэг</div></div>
<div class="st"><div class="k">2</div><div class="e">{Y}=|0|=0</div><div class="d">Орой: (5, 0)</div></div></div></div>
<div class="card" style="padding:6px 26px">
<div class="wr"><span class="w">B) (−5, 0)</span><span>Тэмдгийг андуурсан: <i>x</i>−5=0 бол <i>x</i>=5.</span></div>
<div class="wr"><span class="w">C) (0, 5)</span><span>Энэ цэг график дээр бий, гэхдээ орой биш.</span></div>
<div class="wr"><span class="w">D) (0, −5)</span><span>График <i>x</i> тэнхлэгээс доош ордоггүй.</span></div></div>
<div class="rule">Орой = | | доторх хэсэг 0 болох цэг</div>''',
    # 6. end
    gen30.endp('Шинэ сэдэв удахгүй'),
]


def page(C, n, T, body):
    return f'''<!doctype html><html lang="mn"><head><meta charset="utf-8"><style>{C}</style></head><body><div class="pg">
<div class="brand"><img class="r" src="{ROUND}"><div class="tx"><img class="w" src="{WORD}"><div class="jg">JARGALMAA AMGALAN</div></div><span class="n">{n:02d} / {T:02d}</span></div>
<div class="mn">{body}</div>
<div class="ft"><span><b>globalmathprep.academy</b> · SAT MATH · ABSOLUTE VALUE</span><span>{"Гүйлгээд үз →" if n < T else "@globalmathprep"}</span></div></div></body></html>'''


if __name__ == '__main__':
    gen32.render('--video' in sys.argv, key='Abs-Graphs', prefix='GMP-Math-Abs-Graphs', pages=PAGES, cssf=css, pagef=page)
