import gen15 as g
from playwright.sync_api import sync_playwright
b64 = g.b64; HERE = g.HERE
LOGO_W = g.LOGO
LOGO_D = 'data:image/png;base64,' + b64(HERE / 'logo_left_dark.png')
QR = g.QR
AC = '#e11d48'; AC2 = '#fb7185'; INK = '#1c1917'; TINT = '#fff1f2'; SOFT = '#ffe4e6'; NIGHT = '#1c0d18'
TOTAL = 6

# recolour hero illustrations into the rose palette
def hero_svg(k):
    s = g.H[k]
    return s.replace(g.GOLD, AC2).replace(g.CYD, AC).replace(g.CY, AC2).replace(g.DK, INK)

CSS = g.ff + f"""
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;font-family:M,sans-serif}}
.pg{{position:relative;width:1080px;height:1350px;overflow:hidden}}
.light{{background:{TINT};color:{INK}}}
.light:before{{content:'';position:absolute;inset:0;background-image:radial-gradient(rgba(225,29,72,.12) 2px,transparent 2px);background-size:36px 36px;
 -webkit-mask-image:linear-gradient(180deg,#000,transparent 45%)}}
.dark{{color:#fff;background:radial-gradient(ellipse 70% 45% at 80% 8%,rgba(225,29,72,.55),transparent 70%),radial-gradient(ellipse 60% 40% at 0% 100%,rgba(251,113,133,.28),transparent 70%),linear-gradient(165deg,#33142a,{NIGHT} 60%)}}
.spine{{position:absolute;left:0;top:0;bottom:0;width:22px;background:linear-gradient(90deg,{AC},{AC2})}}
.hd{{position:absolute;top:40px;left:56px;right:56px;display:flex;justify-content:space-between;align-items:center;z-index:2}}
.hd img{{height:60px}}
.pn{{border:2.5px solid currentColor;border-radius:30px;padding:7px 20px;font-weight:800;font-size:23px;opacity:.85}}
.ft{{position:absolute;left:56px;right:56px;bottom:32px;display:flex;justify-content:space-between;font-size:21px;font-weight:600;opacity:.7}}
.mn{{position:absolute;top:150px;bottom:92px;left:56px;right:56px;display:flex;flex-direction:column;justify-content:center;gap:30px;z-index:2}}
.wm{{position:absolute;right:-30px;bottom:40px;font-size:430px;font-weight:800;letter-spacing:-20px;line-height:.8;z-index:1;pointer-events:none}}
.light .wm{{color:transparent;-webkit-text-stroke:4px rgba(225,29,72,.13)}}
.dark .wm{{color:transparent;-webkit-text-stroke:4px rgba(251,113,133,.22)}}
.bub{{position:absolute;left:40px;right:40px;top:130px;bottom:100px;z-index:1;opacity:.55}}
.light:before{{display:none}}
.mn>*{{flex-shrink:0}}
.dark .mn{{gap:22px}}
.g4 .big{{font-size:60px}}
.top{{display:flex;align-items:center;gap:30px}}
.top .tx{{flex:1}}
.tile{{flex:none;width:230px;height:230px;border-radius:40px;background:{INK};display:flex;align-items:center;justify-content:center;box-shadow:0 18px 40px rgba(28,25,23,.25);transform:rotate(3deg)}}
.tile svg{{width:180px;height:180px}}
.stp{{align-self:flex-start;display:inline-flex;align-items:center;gap:12px;border:3px solid {AC};color:{AC};border-radius:30px;padding:8px 22px;font-weight:800;font-size:27px;letter-spacing:1px}}
.dots{{display:inline-flex;gap:6px;margin-left:6px}}
.dots i{{width:12px;height:12px;border-radius:50%;background:{SOFT}}}
.dots i.on{{background:{AC}}}
h1{{font-size:86px;font-weight:800;line-height:1.02;letter-spacing:-1.5px;margin-top:14px}}
h1 em{{font-style:normal;color:{AC}}}
.grid{{display:grid;grid-template-columns:1fr 1fr;gap:18px}}
.cd{{background:#fff;border:3px solid {INK};border-radius:28px;padding:26px 28px;box-shadow:6px 6px 0 {INK};position:relative}}
.cd .pl{{display:inline-block;background:{AC};color:#fff;font-weight:800;font-size:22px;letter-spacing:1px;border-radius:20px;padding:5px 14px;margin-bottom:10px}}
.cd .t{{font-size:37px;font-weight:800;line-height:1.2}}
.cd .s{{font-size:28px;font-weight:600;line-height:1.3;color:#57534e;margin-top:6px}}
.cd[style*='#e11d48'] .s{{color:#ffe4e6}}
.cd[style*='#e11d48'] .pl{{background:#1c1917}}
.cd .ar{{position:absolute;right:20px;top:20px;width:40px;height:40px;border-radius:50%;background:{SOFT};color:{AC};font-weight:800;font-size:24px;display:flex;align-items:center;justify-content:center}}
.big{{font-size:80px;font-weight:800;color:{AC};line-height:1}}
.take{{background:{INK};color:#fff;border-radius:28px;padding:26px 30px;display:flex;align-items:center;gap:22px;font-size:32px;font-weight:700;line-height:1.3}}
.take .k{{flex:none;background:{AC};border-radius:18px;padding:9px 16px;font-size:22px;font-weight:800;letter-spacing:1px}}
.take b{{color:{AC2}}}
.hl{{background:linear-gradient(transparent 55%,{SOFT} 55%)}}
.chip{{display:inline-block;border:2.5px solid currentColor;border-radius:30px;padding:8px 20px;font-size:24px;font-weight:700;margin:5px}}
.glass{{background:linear-gradient(160deg,rgba(255,255,255,.13),rgba(255,255,255,.04));border:2px solid rgba(255,255,255,.22);border-radius:28px;box-shadow:inset 0 1px 0 rgba(255,255,255,.25),0 20px 50px rgba(0,0,0,.3)}}
"""

def bubbles(dark):
    c = 'rgba(251,113,133,.16)' if dark else 'rgba(225,29,72,.10)'
    t = 'rgba(251,113,133,.28)' if dark else 'rgba(225,29,72,.20)'
    out = ''
    for r in range(15):
        y = 30 + r * 76
        out += f'<text x="0" y="{y+9}" font-family="M" font-weight="800" font-size="24" fill="{t}">{r+1}</text>'
        for j, L in enumerate('ABCD'):
            x = 70 + j * 62
            out += f'<circle cx="{x}" cy="{y}" r="21" fill="none" stroke="{c}" stroke-width="3"/><text x="{x}" y="{y+8}" text-anchor="middle" font-family="M" font-weight="700" font-size="20" fill="{t}">{L}</text>'
        for j, L in enumerate('ABCD'):
            x = 720 + j * 62
            out += f'<circle cx="{x}" cy="{y}" r="21" fill="none" stroke="{c}" stroke-width="3"/><text x="{x}" y="{y+8}" text-anchor="middle" font-family="M" font-weight="700" font-size="20" fill="{t}">{L}</text>'
    return f'<svg class="bub" viewBox="0 0 1000 1120" preserveAspectRatio="xMidYMid slice">{out}</svg>'

def page(n, body, dark=False):
    cls = 'dark' if dark else 'light'
    return f'''<!doctype html><html lang="mn"><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="pg {cls}">
{'<div class="spine"></div>' if dark else ''}
<div class="hd"><img src="{LOGO_W if dark else LOGO_D}"><div class="pn">{n}/{TOTAL}</div></div>
{bubbles(dark)}<div class="wm">SAT</div>
<div class="mn">{body}</div>
<div class="ft"><span>@globalmathprep · globalmathprep.academy</span><span>{'Гүйлгээд үз →' if n < TOTAL else n}</span></div></div></body></html>'''

def top(step, a, b, icon):
    dots = ''.join(f'<i class="{"on" if i <= step else ""}"></i>' for i in range(1, 10))
    return f'''<div class="top"><div class="tx"><div class="stp">АЛХАМ {step}/9<span class="dots">{dots}</span></div>
<h1>{a}<br><em>{b}</em></h1></div><div class="tile">{hero_svg(icon)}</div></div>'''

def cd(pl, t, s='', arrow=True, extra=''):
    return f'<div class="cd"{extra}>{f"<div class=pl>{pl}</div>" if pl else ""}{"<div class=ar>→</div>" if arrow else ""}<div class="t">{t}</div>{f"<div class=s>{s}</div>" if s else ""}</div>'
def take(t, k='ГОЛ САНАА'): return f'<div class="take"><div class="k">{k}</div><div>{t}</div></div>'
def stat(n, l): return f'<div class="cd" style="text-align:center;padding:22px 10px"><div class="big">{n}</div><div class="s" style="font-size:23px;margin-top:8px">{l}</div></div>'


S = []
# 1 COVER
card = f"""<div style="position:relative;align-self:center;width:620px;margin:10px 0">
<div class="glass" style="padding:30px 36px;transform:rotate(-3deg)">
 <div style="display:flex;justify-content:space-between;font-size:22px;font-weight:700;color:#e9d5dc"><span>SAT SCORE REPORT</span><span>Total</span></div>
 <div style="font-size:150px;font-weight:800;line-height:1;margin-top:10px;filter:blur(9px);color:{AC2}">1520</div>
 <div style="display:flex;gap:12px;margin-top:14px"><div style="flex:1;height:14px;border-radius:7px;background:rgba(255,255,255,.2)"></div><div style="flex:.6;height:14px;border-radius:7px;background:rgba(255,255,255,.2)"></div></div></div>
<div style="position:absolute;right:-30px;bottom:-26px;background:{AC};border-radius:22px;padding:14px 24px;font-size:30px;font-weight:800;transform:rotate(4deg);box-shadow:0 12px 30px rgba(0,0,0,.35)">Энэ оноо хэнийх вэ?</div></div>"""
S.append((f"""<div class="chip" style="color:{AC2};align-self:flex-start">ОЛОН ХҮНИЙ АСУУДАГ АСУУЛТ</div>
<h1 style="font-size:80px;margin-top:0">Бид яагаад<br>сурагчдынхаа оноог<br><em style="color:{AC2}">зарладаггүй вэ?</em></h1>
{card}
<div style="font-size:36px;font-weight:700;line-height:1.35;margin-top:14px">Товчхондоо: <b style="color:{AC2}">тэр оноо сурагчийн өөрийнх нь амжилт.</b></div>
<div style="display:flex;justify-content:space-between;align-items:center;margin-top:auto">
<div style="font-size:22px;color:#d9c4cc;font-weight:600">Jargalmaa Amgalan · Global Math Prep</div>
<div style="background:{AC};border-radius:34px;padding:16px 30px;font-size:28px;font-weight:800">Гүйлгээд үз →</div></div>""", True))

# 2 who did the work
who = [('Өглөө эрт босч хичээлээ хийсэн', 'СУРАГЧ'), ('Мянга мянган бодлого бодсон', 'СУРАГЧ'), ('Алдаагаа засч, дахин бодсон', 'СУРАГЧ'), ('Шалгалтаа өөрөө өгсөн', 'СУРАГЧ')]
wh = ''.join(f'<div class="cd" style="display:flex;align-items:center;justify-content:space-between;padding:14px 26px"><div class="t" style="font-size:32px">{a}</div><div style="flex:none;background:{AC};color:#fff;border:3px solid {INK};border-radius:18px;padding:6px 20px;font-size:26px;font-weight:800">{b}</div></div>' for a, b in who)
S.append((f'<div class="stp">1 · ХЭН ХӨДӨЛМӨРЛӨСӨН БЭ?</div><h1 style="margin-top:0;font-size:74px">Өндөр оноо бол<br><em>хөдөлмөрийн үр дүн</em></h1>' + wh +
 take('Шалгалтыг багш биш, <b>сурагч өөрөө</b> өгдөг. Тиймээс оноо нь ч сурагчийнх.'), False))

# 3 teacher role
S.append((f'<div class="stp">2 · БАГШ ЮУ ХИЙДЭГ ВЭ?</div><h1 style="margin-top:0">Бид зам заана,<br><em>туулдаг нь сурагч</em></h1>' +
 '<div class="grid">' + cd('ТАЙЛБАР', 'Энгийнээр тайлбарлана', 'Хүнд сэдвийг ойлгомжтой болгоно', False) + cd('ЗАСВАР', 'Алдааг олж засна', 'Яагаад алдсаныг хамт ойлгоно', False) +
 cd('ТӨЛӨВЛӨГӨӨ', 'Хувийн төлөвлөгөө гаргана', 'Юуг, хэзээ, хэр их хийх вэ', False) + cd('ДЭМЖЛЭГ', 'Урам зориг өгнө', 'Хэцүү үед ч хажууд нь байна', False) + '</div>' +
 take('Бид зөвхөн <b>хөтөч</b>. Гол баатар нь сурагч өөрөө.'), False))

# 4 why we don't advertise
S.append((f'<div class="stp">3 · ЯАГААД ЗАРЛАДАГГҮЙ ВЭ?</div><h1 style="margin-top:0">Шударга байх<br><em>нь чухал</em></h1>' +
 '<div class="grid">' + cd('ШУДАРГА', 'Хөдөлмөр нь сурагчийнх', 'Бид сурагчийн оноогоор өөрсдийгөө магтахгүй', False) +
 cd('СУУРЬ', 'Зарим нь суурь сайтай ирдэг', 'Тэдний амжилтыг өөрийнхөөрөө тооцохгүй', False) +
 cd('ХУВИЙН', 'Оноо бол хувийн мэдээлэл', 'Зарлах эсэхийг сурагч өөрөө шийднэ', False) +
 cd('ҮНЭН', 'Оноо амладаггүй', 'Хүн бүрийн эхлэл, хурд өөр өөр', False) + '</div>' +
 f'<div class="cd" style="background:{SOFT};text-align:center;padding:26px"><div class="t" style="font-size:38px">"Би чадлаа!" гэж хэлэх эрх<br><span style="color:{AC}">зөвхөн сурагчид бий.</span></div></div>', False))

# 5 what we show instead
steps = ['Долоо хоног бүр сорил', 'Хэсэг тус бүрийн дүн', 'Гэрийн даалгавар, ирц', 'Эцэг эхэд тайлан']
sg = '<div class="grid">' + ''.join(f'<div class="cd" style="display:flex;align-items:center;gap:18px;padding:22px 24px"><div style="flex:none;width:58px;height:58px;border-radius:50%;background:{AC};color:#fff;border:3px solid {INK};display:flex;align-items:center;justify-content:center;font-weight:800;font-size:28px">{i}</div><div class="t" style="font-size:31px">{t}</div></div>' for i, t in enumerate(steps, 1)) + '</div>'
S.append((f'<div class="stp">4 · БИД ЮУГ ХАРУУЛДАГ ВЭ?</div><h1 style="margin-top:0">Оноо биш,<br><em>ахицыг харуулна</em></h1>' + sg +
 f'<div class="cd" style="text-align:center;padding:30px"><div class="t" style="font-size:40px;line-height:1.25">Асуух шаардлагагүй.<br><span style="color:{AC}">Өөрөө харж болно.</span></div><div class="s" style="font-size:27px;margin-top:10px">Ахицыг зөвхөн сурагч болон эцэг эх нь харна</div></div>' +
 take('Бид оноогоор биш, сурагч <b style="white-space:nowrap">өдөр бүр 1%-иар</b> ахиж байгаагаар баярладаг.'), False))

# 6 BACK COVER
S.append((f"""<div class="chip" style="color:{AC2};align-self:flex-start">ТӨГСГӨЛ</div>
<h1 style="font-size:92px;margin-top:0">Чиний хөдөлмөр,<br><em style="color:{AC2}">чиний амжилт.</em></h1>
<div style="font-size:34px;font-weight:600;line-height:1.4;color:#f3e3e8">Бид үргэлж хажууд чинь байна.</div>
<div class="glass" style="display:grid;grid-template-columns:1fr 1fr;overflow:hidden">
 <div style="padding:22px 28px;border-right:2px solid rgba(255,255,255,.15)"><div style="font-size:22px;font-weight:800;color:{AC2};letter-spacing:1px">АНГЛИ (R&amp;W)</div><div style="font-size:44px;font-weight:800;margin-top:6px">Мя · Пү · Бя</div><div style="font-size:24px;color:#e9d5dc;font-weight:600">18:30–19:50 УБ цаг</div></div>
 <div style="padding:22px 28px"><div style="font-size:22px;font-weight:800;color:{AC2};letter-spacing:1px">MATH</div><div style="font-size:44px;font-weight:800;margin-top:6px">Да · Лх · Ба</div><div style="font-size:24px;color:#e9d5dc;font-weight:600">18:30–19:50 УБ цаг</div></div></div>
<div style="display:flex;gap:20px;align-items:stretch">
 <div style="background:#fff;border-radius:26px;padding:16px;text-align:center"><img src="{QR}" style="width:260px;height:260px;display:block"><div style="color:{INK};font-weight:800;font-size:24px;margin-top:6px">Скан хийж бүртгүүл</div></div>
 <div class="glass" style="flex:1;padding:24px 28px;display:flex;flex-direction:column;justify-content:center;gap:16px;font-size:28px;font-weight:700">
  <div>Үнэгүй түвшин тогтоох тест</div><div>2–5 хүүхэдтэй жижиг анги</div><div>Эцэг эхэд долоо хоног бүр тайлан</div></div></div>
<div style="background:{AC};border-radius:24px;padding:18px;text-align:center;font-size:30px;font-weight:800">WhatsApp +1 428 880 1826</div>""", True))

if __name__ == '__main__':
    assert len(S) == TOTAL
    out = HERE / 'out17'; out.mkdir(exist_ok=True)
    for f in out.glob('*.png'): f.unlink()
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page(viewport={'width': 1080, 'height': 1350})
        for i, (body, dark) in enumerate(S, 1):
            pg.set_content(page(i, body, dark)); pg.wait_for_timeout(300)
            ov = pg.evaluate("()=>{const m=document.querySelector('.mn');let b=0,t=1e9;for(const c of m.children){const r=c.getBoundingClientRect();b=Math.max(b,r.bottom);t=Math.min(t,r.top)}return [Math.round(t),Math.round(b)]}")
            fn = out / f'GMP-Bidnii-Zarchim-{i}-of-{TOTAL}.png'
            pg.screenshot(path=str(fn)); print(fn.name, ov, 'OK' if ov[0] >= 145 and ov[1] <= 1258 else 'OVERFLOW')
        br.close()
