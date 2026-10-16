"""SAT Math: exponential vs linear growth, rate is not the factor. One post, 6 slides.
Content from sat-math/course/ch03-exponential-vs-linear.html lesson 3-1 (y=ab^t, b=1+p/100, 6% is 1.06 not 0.06) and Worked Example 1 (250 insects, 8% a week).
"""
import sys
import base64
import gen29, gen30, gen31, gen32, gen33

def _b(f): return 'data:image/png;base64,' + base64.b64encode(open(f, 'rb').read()).decode()
ROUND, WORD = _b('gmp-round.png'), _b('gmp-name-dark.png')

AC, SOFT, TINT = '#4d7c0f', '#e6f0d2', '#f8fbef'   # olive green (new colour)

EXTRA = gen33.EXTRA.replace('#be185d', AC) + """
.lead{font-size:44px!important;line-height:1.35!important}
.rule{font-size:38px!important;padding:24px 30px!important}
.big{font-size:40px!important}
.chips span{font-size:34px!important;padding:12px 26px!important}
.swipe{font-size:30px!important}
.tag{font-size:30px!important;padding:6px 16px!important}
.eqc{font-size:62px!important}
.k{width:64px!important;height:64px!important;font-size:34px!important}
.e{font-size:46px!important;width:auto!important;min-width:420px;white-space:nowrap}
.st .d{font-size:34px!important}
.st{padding:18px 0!important}
.bxs{font-size:46px!important;line-height:1.35!important}
.spr{font-size:30px!important}.bxin{width:260px!important;height:72px!important}
.ok{font-size:64px!important}
.pill{font-size:28px!important}
.card[style*="font-size:27px"]{font-size:31px!important;white-space:nowrap}
.cs{display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px}
.cs div{background:#fff;border:2px solid #e3e5f5;border-radius:18px;padding:18px 12px;text-align:center}
.cs svg{width:100%;height:auto;display:block}
.cs b{display:block;font-size:34px;margin-top:10px;color:#1e1e1e}
.cs span{display:block;font-size:26px;color:#556;font-weight:600;margin-top:4px;line-height:1.25}
.brand{position:absolute;top:34px;left:56px;right:56px;display:flex;align-items:center;gap:18px;z-index:3}
.brand .r{width:112px;height:112px;border-radius:50%;box-shadow:0 4px 14px rgba(15,30,80,.25)}
.brand .w{height:36px;display:block}
.brand .tx{display:flex;flex-direction:column;gap:12px}
.brand .jg{font-family:S,serif;font-weight:700;font-size:27px;letter-spacing:5px;color:#af7f22;line-height:1}
.brand .n{margin-left:auto;font-weight:800;font-size:26px;letter-spacing:2px;color:"""+AC+""";border:2.5px solid """+AC+""";border-radius:30px;padding:8px 18px}
.ft b{color:#1e2a5a}
.sys{font-family:S,serif;font-size:50px;line-height:1.5;text-align:center;margin:14px 0}
.mt{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.mt div{background:#fff;border:2px solid #dfe8cc;border-radius:16px;padding:20px 18px;text-align:center}
.mt b{display:block;font-size:38px;color:#445;font-weight:700}
.mt span{display:block;font-family:S,serif;font-size:66px;color:"""+AC+""";font-weight:700;margin-top:4px}
.card .d{font-size:34px!important;margin-top:8px;color:#333;font-weight:700}
.card .eqc{font-size:60px!important}
"""

def css():
    return gen30.css(AC, SOFT, TINT) + EXTRA

m = gen31.m
X, Y, A = '<i>x</i>', '<i>y</i>', '<i>a</i>'

m = gen31.m
STEM = (f'A colony of {m("250")} insects grows by {m("8%")} each week. According to the model, how many insects will there be after {m("2")} weeks? (Round to the nearest whole number.)')

PAGES = [
    gen30.cover('SAT MATH · EXPONENTIAL',
                f'6%-иар өсөнө<br>гэвэл {m("b = 0.06")}?<br><span class="blue">Буруу.</span>',
                'Өсөлтийн хувь ба үржүүлэгч нь өөр тоо. Хувь дээр 1 нэмнэ.',
                ['b = 1.06', 'y = a·bᵗ', 'Нэмэхгүй, үржүүлнэ'], '1f4c8').replace('font-size:104px', 'font-size:88px'),
    f'''<div class="pill">ГОЛ САНАА</div><div class="h" style="font-size:66px">Нэмдэг үү,<br><span class="blue">үржүүлдэг үү?</span></div>
<div class="card"><div class="tag n">ЛИНЕЙН</div><div class="eqc">{m("250, 270, 290, 310")}</div><div class="d">Үе бүр <b>ижил тоо нэмнэ</b> (+20)</div></div>
<div class="card"><div class="tag y">ЭКСПОНЕНЦИАЛ</div><div class="eqc">{m("250, 270, 291.6")}</div><div class="d">Үе бүр <b>ижил тоогоор үржүүлнэ</b> (×1.08)</div></div>
<div class="rule">Загвар: {m("y = a·b<sup>t</sup>")}. {m("a")} нь эхний утга, {m("b")} нь үе бүрийн үржүүлэгч.</div>''',
    f'''<div class="pill">ҮРЖҮҮЛЭГЧ ОЛОХ</div><div class="h" style="font-size:62px">Хувь → <span class="blue">b</span></div>
<div class="mt"><div><b>8% өсөлт</b><span>1.08</span></div><div><b>12% бууралт</b><span>0.88</span></div>
<div><b>2 дахин</b><span>2</span></div><div><b>хагас болно</b><span>0.5</span></div></div>
<div class="card" style="padding:18px 26px"><div class="tag n">ДУТУУ ХАРИУ</div><div class="eqc">{m("6% → b = 0.06")}</div><div class="d">Энэ нь үе бүр 94% алдана гэсэн үг.</div></div>
<div class="rule">Зөв нь {m("6% → b = 1.06")}. Буруу хувилбар сонголтод байнга гардаг.</div>''',
    f'''<div class="pill">ДАСГАЛ · ЭХЛЭЭД ӨӨРӨӨ БОД</div>{gen31.spr(8, STEM)}
<div class="card big" style="padding:16px 24px">Эхлээд {m("a")} ба {m("b")}-ээ ол, дараа нь {m("t = 2")} тавь.</div>''',
    f'''<div class="pill">ХАРИУ</div>
<div class="okrow"><div class="ok">292</div><div class="h" style="font-size:52px">290 биш</div></div>
<div class="card" style="padding:8px 26px"><div class="steps">
<div class="st"><div class="k">1</div><div class="e">a = 250</div><div class="d">Эхний тоо</div></div>
<div class="st"><div class="k">2</div><div class="e">b = 1 + 0.08 = 1.08</div><div class="d">8% өсөлт</div></div>
<div class="st"><div class="k">3</div><div class="e">y = 250(1.08)<sup>t</sup></div><div class="d">Загвар бичнэ</div></div>
<div class="st"><div class="k">4</div><div class="e">250(1.08)² = 291.6</div><div class="d">Ойролцоогоор 292</div></div></div></div>
<div class="rule">Линейн бол 250 + 2(20) = 290. Хоёр дахь долоо хоног том суурь дээр өсдөг.</div>''',
    gen30.endp('Шинэ сэдэв удахгүй'),
]


def page(C, n, T, body):
    return f'''<!doctype html><html lang="mn"><head><meta charset="utf-8"><style>{C}</style></head><body><div class="pg">
<div class="brand"><img class="r" src="{ROUND}"><div class="tx"><img class="w" src="{WORD}"><div class="jg">JARGALMAA AMGALAN</div></div><span class="n">{n:02d} / {T:02d}</span></div>
<div class="mn">{body}</div>
<div class="ft"><span><b>globalmathprep.academy</b> · SAT MATH · EXPONENTIAL</span><span>{"Гүйлгээд үз →" if n < T else "@globalmathprep"}</span></div></div></body></html>'''


if __name__ == '__main__':
    gen32.render('--video' in sys.argv, key='Exponential-Factor', prefix='GMP-Math-Exponential-Factor', pages=PAGES, cssf=css, pagef=page)
