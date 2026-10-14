"""SAT Math: systems with no solution or infinitely many. One post, 6 slides.
Content from sat-math/course/ch09-systems-of-equations.html (GMP module), lesson 9-3:
lesson text (3x+2y=5 vs 3x+2y=-4 no solution; vs 6x+4y=10 infinitely many; scale, match both variables,
then the constant decides) and Worked Example 1 (-ax-12y=15, 4x+3y=-2, no solution -> a=16)."""
import sys
import gen29, gen30, gen31, gen32, gen33

AC, SOFT, TINT = '#1d4ed8', '#dbe5fd', '#f5f8ff'   # royal blue (not used by recent posts)

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
.sys{font-family:S,serif;font-size:50px;line-height:1.5;text-align:center;margin:14px 0}
"""

def css():
    return gen30.css(AC, SOFT, TINT) + EXTRA

m = gen31.m
X, Y, A = '<i>x</i>', '<i>y</i>', '<i>a</i>'

def mini(kind):
    ax = '<line x1="10" y1="110" x2="150" y2="110" stroke="#1e1e1e" stroke-width="2"/><line x1="20" y1="120" x2="20" y2="8" stroke="#1e1e1e" stroke-width="2"/>'
    if kind == 'one':
        l = '<line x1="25" y1="100" x2="150" y2="20" stroke="#1e1e1e" stroke-width="4"/><line x1="25" y1="25" x2="150" y2="100" stroke="#1e1e1e" stroke-width="4"/><circle cx="87" cy="61" r="7" fill="#1e1e1e"/>'
    elif kind == 'none':
        l = '<line x1="25" y1="80" x2="140" y2="15" stroke="#1e1e1e" stroke-width="4"/><line x1="45" y1="105" x2="150" y2="46" stroke="#1e1e1e" stroke-width="4"/>'
    else:
        l = '<line x1="25" y1="100" x2="150" y2="20" stroke="#1e1e1e" stroke-width="9"/><line x1="25" y1="100" x2="150" y2="20" stroke="#fff" stroke-width="3" stroke-dasharray="8 8"/>'
    return f'<svg viewBox="0 0 160 125">{ax}{l}</svg>'

SYS = f'<div class="sys">{m(f"−{A}{X} − 12{Y} = 15")}<br>{m(f"4{X} + 3{Y} = −2")}</div>'
STEM = (f'In the given system of equations, {m(A)} is a constant. If the system has no solution, what is the value of {m(A)} ?{SYS}')

PAGES = [
    # 1. cover
    gen30.cover('SAT MATH · SYSTEMS',
                f'Систем<br><span class="blue">шийдгүй</span> бол<br>{m(A)} = ?',
                'Бодохгүйгээр олно. Коэффициентээ тэнцүүлээд, тогтмол тоог хараарай.',
                ['Шийдгүй', 'Хязгааргүй олон', 'Нэг шийд'], '1f6a7').replace('font-size:104px', 'font-size:100px'),
    # 2. three cases with pictures
    f'''<div class="pill">ГОЛ САНАА</div><div class="h" style="font-size:66px">Шийдийн тоо =<br><span class="blue">огтлолцлын тоо</span></div>
<div class="cs"><div>{mini('one')}<b>1 шийд</b><span>Нэг цэгт огтлолцоно</span></div>
<div>{mini('none')}<b>Шийдгүй</b><span>Параллель, огт таарахгүй</span></div>
<div>{mini('inf')}<b>Хязгааргүй</b><span>Нэг шулуун давхардана</span></div></div>
<div class="rule">Коэффициент ижил, тогтмол өөр бол шийдгүй. Бүгд ижил бол хязгааргүй олон.</div>''',
    # 3. examples
    f'''<div class="pill">ЖИШЭЭ</div><div class="h" style="font-size:60px">Зүүн тал ижил,<br><span class="blue">тогтмол нь шийднэ</span></div>
<div class="card"><div class="tag n">ШИЙДГҮЙ</div><div class="eqc">{m(f"3{X}+2{Y}=5")}<br>{m(f"3{X}+2{Y}=−4")}</div></div>
<div class="card"><div class="tag y">ХЯЗГААРГҮЙ ОЛОН</div><div class="eqc">{m(f"3{X}+2{Y}=5")}<br>{m(f"6{X}+4{Y}=10")}</div></div>
<div class="rule">2-р систем: эхнийхийг 2-оор үржүүлэхэд яг ижил тэгшитгэл гарна</div>''',
    # 4. question
    f'''<div class="pill">ДАСГАЛ · ЭХЛЭЭД ӨӨРӨӨ БОД</div>{gen31.spr(7, STEM)}
<div class="card big" style="padding:16px 24px">{m(Y)}-ийн коэффициентийг эхлээд тэнцүүлээрэй.</div>''',
    # 5. answer
    f'''<div class="pill">ХАРИУ</div>
<div class="okrow"><div class="ok">{m(f"{A} = 16")}</div></div>
<div class="card" style="padding:8px 26px"><div class="steps">
<div class="st"><div class="k">1</div><div class="e">2-р тэгшитгэл × (−4)</div><div class="d">{m("3×(−4)=−12")}: {m(Y)} таарна</div></div>
<div class="st"><div class="k">2</div><div class="e">{m(f"−16{X}−12{Y}=8")}</div><div class="d">Бүх гишүүнийг үржүүлнэ</div></div>
<div class="st"><div class="k">3</div><div class="e">{m(f"−{A}=−16")}</div><div class="d">{m(X)}-ийн коэф. ч таарна</div></div>
<div class="st"><div class="k">4</div><div class="e">{m("15 ≠ 8")}</div><div class="d">Тогтмол өөр: шийдгүй ✓</div></div></div></div>
<div class="rule">Хэрэв 15-ын оронд 8 байсан бол хязгааргүй олон шийдтэй болно</div>''',
    # 6. end
    gen30.endp('Шинэ сэдэв удахгүй'),
]


def page(C, n, T, body):
    return f'''<!doctype html><html lang="mn"><head><meta charset="utf-8"><style>{C}</style></head><body><div class="pg">
<div class="top"><img src="{gen29.LOGO}"><span>{n:02d} / {T:02d}</span></div>
<div class="mn">{body}</div>
<div class="ft"><span>SAT MATH · SYSTEMS</span><span>{"Гүйлгээд үз →" if n < T else "@globalmathprep"}</span></div></div></body></html>'''


if __name__ == '__main__':
    gen32.render('--video' in sys.argv, key='Systems-NoSolution', prefix='GMP-Math-Systems-No-Solution', pages=PAGES, cssf=css, pagef=page)
