"""SAT Math: percent as a multiplier; successive changes multiply, they do not add. One post, 6 slides.
Content from sat-math/course/ch02-percent.html (GMP module), lesson 2-1: lesson text (multiplier,
"percent of" vs "percent more than": 25% of 80 = 20, 25% more than 80 = 100) and Worked Example 1
(jacket $80, +25% then -10%: 100, 90, 12.5% increase, multiplier 1.125, not 1.15)."""
import sys
import gen29, gen30, gen31, gen32, gen33

AC, SOFT, TINT = '#4338ca', '#e0e1fb', '#f6f6ff'   # indigo (not used by recent posts)

EXTRA = gen33.EXTRA.replace('#be185d', AC) + """
.mt{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.mt div{background:#fff;border:2px solid #e3e5f5;border-radius:16px;padding:16px 18px;text-align:center}
.mt b{display:block;font-size:30px;color:#445;font-weight:700}
.mt span{display:block;font-family:S,serif;font-size:50px;color:""" + AC + """;font-weight:700;margin-top:4px}
/* bigger text (13 Oct feedback) */
.lead{font-size:44px!important;line-height:1.35!important}
.rule{font-size:40px!important;padding:24px 30px!important}
.big{font-size:42px!important}
.chips span{font-size:34px!important;padding:12px 26px!important}
.swipe{font-size:30px!important}
.mt b{font-size:40px!important}.mt span{font-size:68px!important}.mt div{padding:20px!important}
.tag{font-size:32px!important;padding:6px 16px!important}
.eqc{font-size:80px!important}
.k{width:64px!important;height:64px!important;font-size:34px!important}
.e{font-size:48px!important;width:auto!important;min-width:400px;white-space:nowrap}
.st .d{font-size:34px!important}
.d{font-size:40px!important}
.st{padding:18px 0!important}
.bxs{font-size:48px!important;line-height:1.35!important}
.spr{font-size:30px!important}.bxin{width:260px!important;height:72px!important}
.ok{font-size:60px!important}
.pill{font-size:28px!important}
.card[style*="font-size:27px"]{font-size:31px!important;white-space:nowrap}
.card[style*="font-size:27px"] span{font-size:inherit}
"""

def css():
    return gen30.css(AC, SOFT, TINT) + EXTRA

m = gen31.m

STEM = (f'A jacket is priced at {m("$80")}. Its price is raised by {m("25%")}, and the new price is later reduced by {m("10%")}. '
        f'By what percent is the final price greater than the original price?')

PAGES = [
    # 1. cover
    gen30.cover('SAT MATH · PERCENT',
                f'+25%, дараа нь −10%<br>= +15%?<br><span class="blue">Буруу.</span>',
                'Хувийг нэмж хасдаггүй. Үржүүлэгч болгоод үржүүлнэ.',
                ['×1.25', '×0.90', '= ×1.125'], '1f4c9').replace('font-size:104px', 'font-size:94px'),
    # 2. the idea
    f'''<div class="pill">ГОЛ САНАА</div><div class="h" style="font-size:72px">Өөрчлөлт бүр<br><span class="blue">үржүүлэгч</span></div>
<div class="lead">25%-иар өсгөх нь "25 нэмэх" биш, <b class="hl">1.25-аар үржүүлэх</b>. 25%-иар бууруулах нь 0.75-аар үржүүлэх.</div>
<div class="mt"><div><b>+25%</b><span>×1.25</span></div><div><b>−25%</b><span>×0.75</span></div>
<div><b>+10%</b><span>×1.10</span></div><div><b>−10%</b><span>×0.90</span></div></div>
<div class="rule">Хоёр өөрчлөлт дараалбал үржүүлэгчүүдийг үржүүлнэ</div>''',
    # 3. of vs more than
    f'''<div class="pill">АНХААР</div><div class="h" style="font-size:66px">"-ийн 25%" ба<br><span class="blue">"25%-иар их"</span></div>
<div class="card"><div class="tag y">80-ийн 25%</div><div class="eqc">{m("0.25 × 80 = 20")}</div></div>
<div class="card"><div class="tag y">80-аас 25%-иар их</div><div class="eqc">{m("1.25 × 80 = 100")}</div></div>
<div class="rule">Хоёр хариу хоёулаа сонголтод гардаг. Асуултаа эхлээд уншаарай.</div>''',
    # 4. question
    f'''<div class="pill">ДАСГАЛ · ЭХЛЭЭД ӨӨРӨӨ БОД</div>{gen31.spr(5, STEM)}
<div class="card big" style="padding:16px 24px">10%-ийг 80-аас биш, өссөн үнээс хасна.</div>''',
    # 5. answer
    f'''<div class="pill">ХАРИУ</div>
<div class="okrow"><div class="ok">12.5%</div><div class="h" style="font-size:52px">15% биш</div></div>
<div class="card" style="padding:8px 26px"><div class="steps">
<div class="st"><div class="k">1</div><div class="e">80 × 1.25 = 100</div><div class="d">25%-иар өссөн</div></div>
<div class="st"><div class="k">2</div><div class="e">100 × 0.90 = 90</div><div class="d">100-аас 10% хассан</div></div>
<div class="st"><div class="k">3</div><div class="e">(90 − 80) ÷ 80</div><div class="d">= 0.125 = 12.5% өсөлт</div></div>
<div class="st"><div class="k">4</div><div class="e">1.25 × 0.90 = 1.125</div><div class="d">Нэг үржүүлэгч: мөн 12.5%</div></div></div></div>
<div class="rule">10%-ийг 25% нэмэгдсэн том тооноос хассан тул 15% гарахгүй</div>''',
    # 6. end
    gen30.endp('Шинэ сэдэв удахгүй'),
]


def page(C, n, T, body):
    return f'''<!doctype html><html lang="mn"><head><meta charset="utf-8"><style>{C}</style></head><body><div class="pg">
<div class="top"><img src="{gen29.LOGO}"><span>{n:02d} / {T:02d}</span></div>
<div class="mn">{body}</div>
<div class="ft"><span>SAT MATH · PERCENT</span><span>{"Гүйлгээд үз →" if n < T else "@globalmathprep"}</span></div></div></body></html>'''


if __name__ == '__main__':
    gen32.render('--video' in sys.argv, key='Percent-Multiplier', prefix='GMP-Math-Percent-Multiplier', pages=PAGES, cssf=css, pagef=page)
