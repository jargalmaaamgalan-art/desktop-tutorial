import gen15 as g
from playwright.sync_api import sync_playwright
b64 = g.b64; HERE = g.HERE
LOGO_W = g.LOGO
LOGO_D = 'data:image/png;base64,' + b64(HERE / 'logo_left_dark.png')
QR = g.QR
AC = '#ea580c'; AC2 = '#fb923c'; INK = '#1c1917'; TINT = '#fff4ea'; SOFT = '#ffe4cf'; NIGHT = '#17121f'
TOTAL = 13

# recolour hero illustrations into the orange palette
def hero_svg(k):
    s = g.H[k]
    if k == 'module': s = s.replace('>M1<', '>1<').replace('>800<', '>↑<').replace('>600<', '>↓<')
    return s.replace(g.GOLD, AC2).replace(g.CYD, AC).replace(g.CY, AC2).replace(g.DK, INK)

CSS = g.ff + f"""
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;font-family:M,sans-serif}}
.pg{{position:relative;width:1080px;height:1350px;overflow:hidden}}
.light{{background:{TINT};color:{INK}}}
.light:before{{content:'';position:absolute;inset:0;background-image:radial-gradient(rgba(234,88,12,.12) 2px,transparent 2px);background-size:36px 36px;
 -webkit-mask-image:linear-gradient(180deg,#000,transparent 45%)}}
.dark{{color:#fff;background:radial-gradient(ellipse 70% 45% at 80% 8%,rgba(234,88,12,.55),transparent 70%),radial-gradient(ellipse 60% 40% at 0% 100%,rgba(251,146,60,.28),transparent 70%),linear-gradient(165deg,#241a2c,{NIGHT} 60%)}}
.spine{{position:absolute;left:0;top:0;bottom:0;width:22px;background:linear-gradient(90deg,{AC},{AC2})}}
.hd{{position:absolute;top:40px;left:56px;right:56px;display:flex;justify-content:space-between;align-items:center;z-index:2}}
.hd img{{height:60px}}
.pn{{border:2.5px solid currentColor;border-radius:30px;padding:7px 20px;font-weight:800;font-size:23px;opacity:.85}}
.ft{{position:absolute;left:56px;right:56px;bottom:32px;display:flex;justify-content:space-between;font-size:21px;font-weight:600;opacity:.7}}
.mn{{position:absolute;top:150px;bottom:92px;left:56px;right:56px;display:flex;flex-direction:column;justify-content:center;gap:30px;z-index:2}}
.wm{{position:absolute;right:-30px;bottom:40px;font-size:430px;font-weight:800;letter-spacing:-20px;line-height:.8;z-index:1;pointer-events:none}}
.light .wm{{color:transparent;-webkit-text-stroke:4px rgba(234,88,12,.13)}}
.dark .wm{{color:transparent;-webkit-text-stroke:4px rgba(251,146,60,.22)}}
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
.cd[style*='#ea580c'] .s{{color:#ffe4cf}}
.cd[style*='#ea580c'] .pl{{background:#1c1917}}
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
    c = 'rgba(251,146,60,.16)' if dark else 'rgba(234,88,12,.10)'
    t = 'rgba(251,146,60,.28)' if dark else 'rgba(234,88,12,.20)'
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
<div class="ft"><span>@globalmathprep · globalmathprep.academy</span><span>{'Гүйлгээд үз →' if 1 < n < TOTAL else ''}</span></div></div></body></html>'''

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
S.append((f'''<div style="display:flex;justify-content:space-between;align-items:flex-start">
<div class="chip" style="color:{AC2}">МЭДЭЭЛЛИЙН ЦУВРАЛ #02</div></div>
<div style="font-size:320px;font-weight:800;line-height:.85;letter-spacing:-12px;color:{AC2};margin-top:10px">+115</div>
<div style="font-size:46px;font-weight:800;margin-top:-4px;line-height:1.2">оноо = 20 цаг дасгал хийсэн<br>сурагчдын дундаж өсөлт*</div>
<h1 style="font-size:104px;margin-top:16px">SAT оноогоо<br><em style="color:{AC2}">өсгөх 9 алхам</em></h1>
<div style="font-size:38px;font-weight:600;line-height:1.35;color:#e7dcd3">Илүү их биш. Илүү <b style="color:#fff">ухаалаг</b> бэлд.</div>
<div><span class="chip">Үнэгүй хэрэгсэл</span><span class="chip">Өдөр бүр 1 алхам</span><span class="chip">Хадгалаад ав</span></div>
<div style="display:flex;justify-content:space-between;align-items:center;margin-top:auto">
<div style="font-size:22px;color:#bfb3aa;font-weight:600">Jargalmaa Amgalan · Global Math Prep<br><span style="font-size:18px">*College Board, Khan Academy-ийн 2017 оны судалгаа: Khan Academy дээр 20 цаг дасгал хийсэн сурагчид дунджаар +115 оноо ахисан</span></div>
<div style="background:{AC};border-radius:34px;padding:16px 30px;font-size:28px;font-weight:800;white-space:nowrap;flex:none">Гүйлгээд үз →</div></div>''', True))

# 2 CONTENTS
toc = ['Түвшнээ мэд', 'Зорилгоо тоогоор тавь', 'Зөв материал сонго', 'Алдаагаа бичиж ав', 'Эхний модульд анхаар', 'Цагаа ухаалаг хуваа', 'Дүрэм ба үг', 'Math: уншаад бод', 'Өдөр бүр бага багаар']
tg = '<div class="grid" style="grid-template-columns:1fr 1fr 1fr;gap:16px">' + ''.join(
    f'<div class="cd" style="padding:24px 20px;min-height:200px"><div style="font-size:64px;font-weight:800;color:{AC};line-height:1">{i:02d}</div><div class="t" style="font-size:31px;margin-top:12px">{t}</div></div>' for i, t in enumerate(toc, 1)) + '</div>'
S.append((f'''<div class="stp">АГУУЛГА</div><h1 style="margin-top:0">Энэ цувралд<br><em>юу байгаа вэ?</em></h1>{tg}
{take('Нэг алхам = нэг хуудас. <b>Хадгалаад</b> өдөр бүр нэгийг хий.', 'ЗӨВЛӨГӨӨ')}''', False))

# 3 step 1
S.append((top(1, 'Эхлээд', 'түвшнээ мэд', 'test') +
 '<div class="grid" style="grid-template-columns:1fr 1fr 1fr">' + stat('98', 'асуулт') + stat('2ц 14м', 'нийт хугацаа') + stat('0₮', 'Bluebook тест') + '</div>' +
 '<div class="grid">' + cd('ХИЙХ', 'Bluebook апп дээр бүтэн тест өг', 'College Board-ын үнэгүй апп, шалгалттай ижил') + cd('ДҮРЭМ', 'Таймер тавь, утсаа холдуул', 'Бодит нөхцөл = бодит оноо') + '</div>' +
 take('Оноогоо мэдвэл юугаа сурахаа <b>тодорхой</b> ойлгоно.'), False))

# 4 step 2
bar = f'''<div class="cd" style="padding:26px 28px"><div class="pl">ЖИШЭЭ</div><div style="display:flex;align-items:flex-end;gap:16px;height:170px;margin-top:6px">
<div style="flex:1;text-align:center"><div style="height:110px;background:{SOFT};border:3px solid {INK};border-radius:14px 14px 0 0"></div><div class="t" style="font-size:30px;margin-top:8px">1150</div><div class="s" style="margin:0">одоо</div></div>
<div style="font-size:50px;font-weight:800;color:{AC};padding-bottom:70px">→</div>
<div style="flex:1;text-align:center"><div style="height:150px;background:{AC};border:3px solid {INK};border-radius:14px 14px 0 0"></div><div class="t" style="font-size:30px;margin-top:8px">1350</div><div class="s" style="margin:0">зорилго</div></div>
<div style="flex:1.2;text-align:left;padding-bottom:40px"><div class="big" style="font-size:70px">+200</div><div class="s">Math +100<br>Англи +100</div></div></div></div>'''
S.append((top(2, 'Зорилгоо', 'тоогоор тавь', 'target') + bar +
 '<div class="grid" style="grid-template-columns:1fr 1fr 1fr">' + cd('1', 'Хүсэж буй сургуулийн оноог хар', arrow=False) + cd('2', 'Одоогийн оноотойгоо харьцуул', arrow=False) + cd('3', 'Зөрүүг Math, Англид хуваа', arrow=False) + '</div>' +
 take('"Их сурна" биш, <b>"+200 оноо"</b> гэж тавь.'), False))

# 5 step 3
S.append((top(3, 'Зөв материал', 'сонго', 'app') +
 '<div class="grid">' + cd('ҮНЭГҮЙ', 'Bluebook', 'Бодит шалгалттай ижил бүтэн тестүүд', False) +
 cd('ҮНЭГҮЙ', 'Khan Academy', 'Ур чадвар бүрээр дасгал', False) +
 cd('ҮНЭГҮЙ', 'SAT Question Bank', 'Сул сэдвээ сонгоод дасгал хий', False) +
 cd('GLOBAL MATH PREP', '5,700+ асуулт', 'Бүрэн тайлбартай + 13 бүтэн тест', False,
    extra=' style="background:#ea580c;color:#fff;border-color:#1c1917"') + '</div>' +
 take('Оноогоо <b>Bluebook</b>-ээр шалга. Сул сэдвээ <b>тайлбартай</b> асуултаар нөх.'), False))

# 6 step 4
tbl = f'''<div class="cd" style="padding:0;overflow:hidden"><div style="display:grid;grid-template-columns:1fr 1.2fr 1.3fr;font-size:24px">
<div style="background:{INK};color:#fff;padding:14px 18px;font-weight:800">Асуулт</div><div style="background:{INK};color:#fff;padding:14px 18px;font-weight:800">Яагаад?</div><div style="background:{INK};color:#fff;padding:14px 18px;font-weight:800">Засвар</div>
<div style="padding:16px 18px;font-weight:700">Англи #12</div><div style="padding:16px 18px;font-weight:600">Буруу уншсан</div><div style="padding:16px 18px;font-weight:600">Асуултыг 2 удаа унш</div>
<div style="padding:16px 18px;font-weight:700;border-top:2px solid {SOFT}">Math #7</div><div style="padding:16px 18px;font-weight:600;border-top:2px solid {SOFT}">Томьёо мартсан</div><div style="padding:16px 18px;font-weight:600;border-top:2px solid {SOFT}">7 хоногийн дараа дахин бод</div></div></div>'''
chips = ''.join(f'<span class="chip" style="color:{AC};background:#fff">{c}</span>' for c in ['Мэдэхгүй байсан', 'Буруу уншсан', 'Цаг дутсан', 'Яарч алдсан'])
S.append((top(4, 'Алдаагаа', 'бичиж ав', 'log') + tbl +
 f'<div class="cd"><div class="pl">АЛДААНЫ 4 ШАЛТГААН</div><div>{chips}</div></div>' +
 take('Нэг алдаагаа <b>дахин давтахгүй</b> бол оноо өснө.'), False))

# 7 step 5
m = f'''<div class="cd" style="display:flex;align-items:center;gap:18px;padding:24px">
<div style="flex:none;width:130px;height:130px;border:3px solid {INK};border-radius:22px;display:flex;align-items:center;justify-content:center;font-size:30px;font-weight:800;text-align:center;line-height:1.15">1-р<br>модуль</div>
<div style="font-size:44px;color:{AC};font-weight:800">→</div>
<div style="flex:1;display:flex;flex-direction:column;gap:10px">
<div style="background:{AC};color:#fff;border:3px solid {INK};border-radius:16px;padding:10px 18px;font-size:26px;font-weight:800">Сайн хийвэл: 2-р модуль хэцүү, оноо өндөр</div>
<div style="background:{SOFT};border:3px solid {INK};border-radius:16px;padding:10px 18px;font-size:26px;font-weight:800">Муу хийвэл: 2-р модуль хялбар, оноо хязгаартай</div></div></div>'''
S.append((top(5, 'Эхний модульд', 'анхаар', 'module') + m +
 '<div class="grid">' + cd('1', 'Бүтэн унш', 'Дараа нь хариулт хар', False) + cd('2', 'Амархан асуултаа бүү алд', 'Хурдан биш, зөв бод', False) +
 cd('3', 'Тэмдэглээд алгас', 'Эргэлзсэнээ дараа нь шалга', False) + cd('4', 'Хоосон бүү орхи', 'Буруу хариултад оноо хасахгүй', False) + '</div>', False))

# 8 step 6
S.append((top(6, 'Цагаа', 'ухаалаг хуваа', 'clock') +
 '<div class="grid">' + stat('~71 сек', 'Англи · 1 асуултад<br>64 мин ÷ 54') + stat('~95 сек', 'Math · 1 асуултад<br>70 мин ÷ 44') + '</div>' +
 cd('ГАЦВАЛ', 'Тэмдэглээд дараагийнх руу яв', 'Нэг асуултад гацаж цагаа бүү алд') +
 cd('ДАСГАЛ', 'Дасгалаа үргэлж цаг тавьж хий', 'Модуль бүр өөрийн цагтай') +
 take('Сүүлийн 2-3 минутад <b>тэмдэглэсэн</b> асуултаа шалга.'), False))

# 9 step 7
bars = [('Мэдээлэл ба санаа', 26), ('Бүтэц ба үг', 28), ('Санаа илэрхийлэх', 20), ('Дүрэм', 26)]
bh = ''.join(f'<div style="display:flex;align-items:center;gap:14px;margin:10px 0"><div style="width:280px;font-size:25px;font-weight:700">{a}</div><div style="flex:1;height:30px;background:{SOFT};border-radius:15px;border:2.5px solid {INK}"><div style="width:{p*3.3:.0f}%;height:100%;border-radius:12px;background:{AC2}"></div></div><div style="width:70px;font-weight:800;font-size:28px;color:{AC}">{p}%</div></div>' for a, p in bars)
S.append((top(7, 'Англи:', 'дүрэм + үг', 'abc') + f'<div class="cd"><div class="pl">R&amp;W ХЭСЭГ</div>{bh}</div>' +
 '<div class="grid">' + cd('ХУРДАН', 'Дүрмийн асуулт', 'Дүрмээ мэдвэл хариу нь тодорхой') + cd('ӨДӨР БҮР', '20 шинэ үг цээжил, 20 мин унш', 'Бага ч гэсэн тогтмол') + '</div>' +
 take('Өдөрт 20 үг = сард <b>600 үг</b>.'), False))

# 10 step 8
md = '<div class="grid" style="grid-template-columns:1fr 1fr 1fr 1fr;gap:14px">' + ''.join(stat(p, l) for p, l in [('35%', 'Алгебр'), ('35%', 'Ахисан математик'), ('15%', 'Өгөгдөл'), ('15%', 'Геометр, тригонометр')]) + '</div>'
S.append((top(8, 'Math: уншаад,', 'дараа нь бод', 'calc') + md +
 cd('1', 'Юу асууж байна?', 'Олох ёстой зүйлээ цаасан дээрээ товч бич', False) +
 cd('2', 'Desmos график тооны машин ашигла', 'Math хэсгийн бүх асуултад зөвшөөрөгдөнө', False) +
 take('Олон алдаа мэдлэгээс биш, <b>асуултыг буруу уншсанаас</b> гардаг.', 'GMP'), False))

# 11 step 9
days = [('Да', 'Асуулт', 0), ('Мя', 'Асуулт', 0), ('Лх', 'Асуулт', 0), ('Пү', 'Асуулт', 0), ('Ба', 'Асуулт', 0), ('Бя', 'Тест', 1), ('Ня', 'Алдаа', 2)]
dh = '<div style="display:flex;gap:10px">' + ''.join(f'<div style="flex:1;text-align:center;border:3px solid {INK};border-radius:18px;padding:16px 4px;background:{[ "#fff", AC, SOFT][k]};color:{"#fff" if k==1 else INK}"><div style="font-weight:800;font-size:30px">{d}</div><div style="font-size:19px;font-weight:700;margin-top:6px">{t}</div></div>' for d, t, k in days) + '</div>'
S.append((top(9, 'Бага багаар,', 'өдөр бүр', 'cal') +
 '<div class="grid">' + stat('6–8 цаг', 'Khan Academy дасгал → дунджаар +90*') + stat('20 цаг', 'Khan Academy дасгал → дунджаар +115*') + '</div>' +
 f'<div class="cd"><div class="pl">7 ХОНОГИЙН ТӨЛӨВЛӨГӨӨ</div>{dh}<div class="s" style="margin-top:12px">Хичээлийн өдөр 30–45 минут хангалттай</div></div>' +
 take('Өдөр бүр <b>1%</b>-иар ахи.', '1%') + '<div style="font-size:20px;font-weight:600;color:#78716c">*College Board, Khan Academy, 2017</div>', False))

# 12 GMP method
S.append((f'<div class="stp">GLOBAL MATH PREP</div><h1 style="margin-top:0">Бид яг ингэж<br><em>бэлддэг</em></h1>' +
 '<div class="grid g4" style="grid-template-columns:1fr 1fr 1fr 1fr;gap:14px">' + stat('3,904', 'Math асуулт') + stat('1,802', 'Англи асуулт') + stat('13', 'бүтэн тест') + stat('3,717', 'үгийн сан (Vocab Hub)') + '</div>' +
 '<div class="grid">' + cd('7 ХОНОГ БҮР', 'Бүтэн тест', 'Хэсэг бүрийн оноогоо харна') + cd('АЛДАА', 'Багш дахин тайлбарлана', 'Алдсан сэдэв бүрээр') +
 cd('ЭЦЭГ ЭХЭД', 'Долоо хоногийн тайлан', 'Ахиц харагдана') + cd('ЖИЖИГ АНГИ', '2–6 сурагч', 'Zoom-ээр шууд') + '</div>', False))

# 13 BACK COVER
recap = ''.join(f'<span class="chip" style="font-size:20px;padding:6px 14px;margin:4px">{i}. {t}</span>' for i, t in enumerate(toc, 1))
S.append((f'''<div class="chip" style="color:{AC2};align-self:flex-start">ТӨГСГӨЛ · ОДОО ЧИНИЙ ЭЭЛЖ</div>
<h1 style="font-size:76px;margin-top:0">9 алхам бэлэн.<br><em style="color:{AC2}">Эхлэх үү?</em></h1>
<div style="line-height:1.2">{recap}</div>
<div class="glass" style="background:#2a2030;display:grid;grid-template-columns:1fr 1fr;overflow:hidden">
 <div style="padding:22px 28px;border-right:2px solid rgba(255,255,255,.15)"><div style="font-size:22px;font-weight:800;color:{AC2};letter-spacing:1px">АНГЛИ (R&amp;W)</div><div style="font-size:44px;font-weight:800;margin-top:6px">Мя · Пү · Бя</div><div style="font-size:24px;color:#e7dcd3;font-weight:600">20:00–21:20 УБ цаг</div></div>
 <div style="padding:22px 28px"><div style="font-size:22px;font-weight:800;color:{AC2};letter-spacing:1px">MATH</div><div style="font-size:44px;font-weight:800;margin-top:6px">Да · Лх · Ба</div><div style="font-size:24px;color:#e7dcd3;font-weight:600">20:00–21:20 УБ цаг</div></div></div>
<div style="display:flex;gap:20px;align-items:stretch">
 <div style="background:#fff;border-radius:26px;padding:16px;text-align:center"><img src="{QR}" style="width:250px;height:250px;display:block"><div style="color:{INK};font-weight:800;font-size:24px;margin-top:6px">Скан хийж бүртгүүл</div></div>
 <div class="glass" style="background:#2a2030;flex:1;padding:24px 28px;display:flex;flex-direction:column;justify-content:center;gap:16px;font-size:28px;font-weight:700">
  <div>Үнэгүй 20 минутын тест</div><div>2–6 сурагчтай анги</div><div>Эцэг эхэд 7 хоногийн тайлан</div><div style="color:{AC2}">Суудал хязгаартай</div></div></div>
<div style="background:{AC};border-radius:24px;padding:18px;text-align:center;font-size:30px;font-weight:800">WhatsApp +1 428 880 1826</div>
<div style="text-align:center;font-size:27px;font-weight:700;color:#fff">Хуваарь, мэдээлэл авах бол <b style="color:#fb923c">"SAT"</b> гэж коммент бич</div>''', True))

if __name__ == '__main__':
    assert len(S) == TOTAL
    out = HERE / 'out16'; out.mkdir(exist_ok=True)
    for f in out.glob('*.png'): f.unlink()
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page(viewport={'width': 1080, 'height': 1350})
        for i, (body, dark) in enumerate(S, 1):
            pg.set_content(page(i, body, dark)); pg.wait_for_timeout(300)
            ov = pg.evaluate("()=>{const m=document.querySelector('.mn');let b=0;for(const c of m.children){b=Math.max(b,c.getBoundingClientRect().bottom)}const r=m.getBoundingClientRect();return [Math.round(b),Math.round(r.bottom),false]}")
            fn = out / f'SAT-9-Alkham-{i:02d}-of-{TOTAL}.png'
            pg.screenshot(path=str(fn)); print(fn.name, ov, 'OK' if ov[0] <= ov[1] and not ov[2] else 'OVERFLOW')
        br.close()
