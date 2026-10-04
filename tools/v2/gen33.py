"""SAT Math: absolute value equations have two cases; the minus goes on the number. One post, 6 slides.
Content verbatim from sat-math/course/ch18-absolute-value.html (GMP module), lesson 18-2:
lesson text (|x-2|=10 -> 12 or -8; minus applies to the whole right side), practice Q2 (|2x-6|=8 -> 7 and -1) with its why-notes."""
import sys
import gen29, gen30, gen24, gen31, gen32
from playwright.sync_api import sync_playwright

AC, SOFT, TINT = '#be185d', '#fbe1ec', '#fff5f9'   # raspberry pink (not used by recent posts)
GREEN = '#15803d'; RED = '#c62828'; INK = '#1e1e1e'

EXTRA = gen31.EXTRA.replace('#0f766e', AC) + f"""
.okrow .ok{{font-size:48px!important}}
.eqc{{font-family:S,serif;font-size:46px;text-align:center}} .eqc i{{font-style:italic}}
.tag{{display:inline-block;border-radius:10px;padding:3px 12px;font-size:20px;font-weight:800;color:#fff;margin-bottom:8px;letter-spacing:1px}}
.tag.y{{background:{GREEN}}} .tag.n{{background:{RED}}}
.st .e{{width:360px!important}}
.wr .w{{text-decoration:none!important;color:#c62828!important}}
.st .d{{font-family:S,serif;font-size:34px!important;color:#1e1e1e!important;font-weight:400!important}}
"""

def css():
    return gen30.css(AC, SOFT, TINT) + EXTRA

m = gen31.m
X = '<i>x</i>'

def twoside(c, k):
    """Number line showing c-k and c+k, both k units from the centre c."""
    W, L, R, Y = 968, 60, 908, 80
    lo, hi = c - k - 2, c + k + 2
    sx = lambda v: L + (v - lo) * (R - L) / (hi - lo)
    s = f'<svg viewBox="0 0 {W} 150" style="display:block;width:100%;height:auto">'
    s += f'<line x1="{L-30}" y1="{Y}" x2="{R+30}" y2="{Y}" stroke="{INK}" stroke-width="3"/>'
    for a, b in ((c - k, c), (c, c + k)):
        s += f'<path d="M{sx(a)} {Y-14} Q{(sx(a)+sx(b))/2} {Y-70} {sx(b)} {Y-14}" fill="none" stroke="{AC}" stroke-width="4"/>'
        s += f'<text x="{(sx(a)+sx(b))/2}" y="{Y-50}" text-anchor="middle" font-family="Georgia,serif" font-size="30" font-weight="700" fill="{AC}">{k}</text>'
    for v in (c - k, c, c + k):
        lab = '−' + str(-v) if v < 0 else str(v)
        s += f'<line x1="{sx(v)}" y1="{Y-10}" x2="{sx(v)}" y2="{Y+10}" stroke="{INK}" stroke-width="3"/>'
        s += f'<text x="{sx(v)}" y="{Y+48}" text-anchor="middle" font-family="Georgia,serif" font-size="32" font-weight="700" fill="{INK if v == c else AC}">{lab}</text>'
        if v != c:
            s += f'<circle cx="{sx(v)}" cy="{Y}" r="12" fill="{AC}"/>'
    return s + '</svg>'

def mcq(qnum, stem, choices):
    ch = ''.join(f'<div><span class="l">{l}</span><span>{c}</span></div>' for l, c in zip('ABCD', choices))
    return f'''<div class="bx"><div class="bxh"><div><div class="s1">Section 2, Module 1: Math</div><div class="s2">Directions &#8964;</div></div>
<div class="tm">31:24<br><span class="hide">Hide</span></div>
<div class="tl"><div>{gen24.ICAL}<br>Calculator</div><div>{gen24.IREF}<br>Reference</div><div>{gen24.IMORE}<br>More</div></div></div><div class="dash"></div>
<div class="bxb"><div class="qrow"><div class="n">{qnum}</div>{gen24.BOOK}<span class="mr">Mark for Review</span><span class="abc">ABC</span></div>
<div class="bxs">{stem}</div><div class="bxc">{ch}</div></div>
<div class="dash"></div><div class="bxf"><span>Global Math Prep</span><span class="qx">Question {qnum} of 22 &#8963;</span><div class="bt"><span>Back</span><span>Next</span></div></div></div>'''

STEM = f'What are the solutions to {m(f"|2{X}−6|=8")} ?'
CH = [m('7') + ' and ' + m('−1'), m('7') + ' and ' + m('1'), m('−7') + ' and ' + m('1'), m('7') + ' only']

PAGES = [
    # 1. cover
    gen30.cover('SAT MATH · ABSOLUTE VALUE',
                f'{m(f"|{X}−2|=10")}<br>{m(f"{X}=12")} гэвэл<br><span class="blue">хагас нь л зөв.</span>',
                'Ижил зайд 2 тоо байдаг. Тиймээс 2 тэгшитгэл бодно.',
                ['|A| = k', 'k > 0: A = k эсвэл A = −k'], '1f914').replace('font-size:104px', 'font-size:92px'),
    # 2. the idea
    f'''<div class="pill">ГОЛ САНАА</div><div class="h" style="font-size:72px">{m("|<i>A</i>|=<i>k</i>")} бол<br><span class="blue">2 тохиолдол</span></div>
<div class="lead">{m("<i>k</i>")} эерэг бол {m("<i>A</i>=<i>k</i>")} эсвэл {m("<i>A</i>=−<i>k</i>")}. Ижил зайд 2 тоо байдаг.</div>
<div class="card" style="padding:8px 26px"><div class="steps">
<div class="st"><div class="k">1</div><div class="e">{X}−2 = 10</div><div class="d">→ {m(f"{X}=12")}</div></div>
<div class="st"><div class="k">2</div><div class="e">{X}−2 = −10</div><div class="d">→ {m(f"{X}=−8")}</div></div></div>
{twoside(2, 10)}</div>
<div class="rule">12 ба −8 хоёулаа 2-оос яг 10 зайтай</div>''',
    # 3. question
    f'''<div class="pill">ДАСГАЛ · ЭХЛЭЭД ӨӨРӨӨ БОД</div>{mcq(2, STEM, CH)}
<div class="card big" style="padding:16px 24px">Баруун тал эерэг тоо байна. Хэдэн тохиолдол бодох вэ?</div>''',
    # 4. answer
    f'''<div class="pill">ХАРИУ</div>
<div class="okrow"><div class="ok">A) 7 and −1</div><div class="h" style="font-size:52px">2 шийд</div></div>
<div class="card" style="padding:8px 26px"><div class="steps">
<div class="st"><div class="k">1</div><div class="e">2{X}−6 = 8</div><div class="d">2{X} = 14 → {m(f"{X}=7")}</div></div>
<div class="st"><div class="k">2</div><div class="e">2{X}−6 = −8</div><div class="d">2{X} = −2 → {m(f"{X}=−1")}</div></div></div></div>
<div class="card" style="padding:8px 26px">
<div class="wr"><span class="w">✗ B) 7 and 1</span><span>2 дахь тохиолдол 2{X}−6=−8 тул {X}=−1.</span></div>
<div class="wr"><span class="w">✗ C) −7 and 1</span><span>Эхний тохиолдол 2{X}=14 тул {X}=7.</span></div>
<div class="wr"><span class="w">✗ D) 7 only</span><span>Шийд 2 байна, 1 биш.</span></div></div>''',
    # 5. trap
    f'''<div class="pill">УРХИ</div><div class="h" style="font-size:72px">Хасах тэмдэг<br><span class="blue">тоон дээр</span> очно</div>
<div class="card"><div class="tag n">БУРУУ</div><div class="eqc">{m(f"<span style='background:#fde2e2;color:#c62828;border-radius:8px;padding:0 8px'>−</span>2{X}−6=8")}</div></div>
<div class="card"><div class="tag y">ЗӨВ</div><div class="eqc">{m(f"2{X}−6=−8")}</div></div>
<div class="rule">Хасах тэмдгийг баруун талын тоон дээр тавина. Модулийн доторх илэрхийлэл дээр биш.</div>''',
    # 6. end
    gen30.endp('Шинэ сэдэв удахгүй'),
]


def page(C, n, T, body):
    return f'''<!doctype html><html lang="mn"><head><meta charset="utf-8"><style>{C}</style></head><body><div class="pg">
<div class="top"><img src="{gen29.LOGO}"><span>{n:02d} / {T:02d}</span></div>
<div class="mn">{body}</div>
<div class="ft"><span>SAT MATH · ABSOLUTE VALUE</span><span>{"Гүйлгээд үз →" if n < T else "@globalmathprep"}</span></div></div></body></html>'''


if __name__ == '__main__':
    gen32.render('--video' in sys.argv, key='Abs-Value-Two-Cases', prefix='GMP-Math-Abs-Value-Two-Cases', pages=PAGES, cssf=css, pagef=page)
