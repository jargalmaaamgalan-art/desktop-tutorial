import base64, pathlib
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).parent
FD = HERE.parent / 'poster/fonts/package/files'
b64 = lambda p: base64.b64encode(p.read_bytes()).decode()
RNG = {'latin': 'U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+2074,U+20AC,U+2122,U+2190-21FF,U+2212,U+2215,U+FEFF,U+FFFD',
       'latin-ext': 'U+0100-024F,U+0259,U+1E00-1EFF,U+2020,U+20A0-20AB,U+20AD-20CF,U+2113,U+2C60-2C7F,U+A720-A7FF',
       'cyrillic': 'U+0301,U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116',
       'cyrillic-ext': 'U+0460-052F,U+1C80-1C88,U+20B4,U+2DE0-2DFF,U+A640-A69F,U+FE2E-FE2F'}
ff = ''
for w in (500, 600, 700, 800):
    for sub, r in RNG.items():
        ff += "@font-face{font-family:M;font-weight:%d;unicode-range:%s;src:url(data:font/woff2;base64,%s)}\n" % (w, r, b64(FD / f'montserrat-{sub}-{w}-normal.woff2'))
QR = 'data:image/svg+xml;base64,' + b64(HERE / 'qr_join.svg')
LOGO = 'data:image/png;base64,' + b64(HERE / 'logo_left.png')

GOLD = '#f6c343'; CY = '#8ff0f5'; PAPER = '#f7f1e3'; DK = '#10323d'; CYD = '#35b6c9'
TOTAL = 12

CSS = ff + f"""
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;font-family:M,sans-serif;color:#fff}}
.pg{{position:relative;width:1080px;height:1350px;overflow:hidden;
 background:radial-gradient(ellipse 80% 55% at 50% 22%,#1c5b6c 0%,rgba(28,91,108,0) 70%),linear-gradient(170deg,#154a59 0%,#0f3a48 45%,#0a2b37 100%)}}
.gr{{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.035) 1px,transparent 1px);background-size:54px 54px;
 -webkit-mask-image:radial-gradient(ellipse at 50% 40%,#000 30%,transparent 80%)}}
.hd{{position:absolute;top:44px;left:52px;right:52px;display:flex;justify-content:space-between;align-items:center}}
.hd img{{height:60px}}
.pn{{border:2px solid rgba(255,255,255,.25);background:rgba(255,255,255,.06);border-radius:30px;padding:8px 20px;font-weight:700;font-size:22px}}
.ft{{position:absolute;left:52px;right:52px;bottom:34px;display:flex;justify-content:space-between;font-size:21px;font-weight:600;color:#d6e7ec}}
.bar{{position:absolute;left:52px;right:52px;bottom:76px;height:4px;background:rgba(255,255,255,.12);border-radius:2px}}
.bar i{{display:block;height:100%;background:{GOLD};border-radius:2px}}
.mn{{position:absolute;top:140px;bottom:104px;left:52px;right:52px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:22px;text-align:center}}
.hero{{width:250px;height:250px;border-radius:44px;background:linear-gradient(160deg,rgba(255,255,255,.14),rgba(255,255,255,.04));border:2px solid rgba(255,255,255,.2);
 box-shadow:0 24px 60px rgba(0,0,0,.35),inset 0 1px 0 rgba(255,255,255,.25);display:flex;align-items:center;justify-content:center}}
.hero svg{{width:200px;height:200px}}
.pill{{background:{GOLD};color:{DK};font-weight:800;font-size:25px;letter-spacing:2px;padding:9px 26px;border-radius:30px}}
h1{{font-size:66px;font-weight:800;line-height:1.08;letter-spacing:-.5px;text-shadow:0 4px 18px rgba(0,0,0,.3)}}
h1 em{{font-style:normal;color:{CY}}}
.gl{{align-self:stretch;background:linear-gradient(160deg,rgba(255,255,255,.1),rgba(255,255,255,.035));border:2px solid rgba(255,255,255,.2);border-radius:28px;
 box-shadow:0 18px 50px rgba(0,0,0,.25),inset 0 1px 0 rgba(255,255,255,.2)}}
.lead{{padding:24px 34px;font-size:32px;font-weight:700;line-height:1.35}}
.lead span{{display:block;font-size:26px;font-weight:500;color:#cfe6ec;margin-top:6px}}
.rows{{text-align:left}}
.row{{display:flex;align-items:center;gap:22px;padding:18px 28px;border-top:1.5px solid rgba(255,255,255,.12)}}
.row:first-child{{border-top:0}}
.num{{flex:none;width:54px;height:54px;border-radius:50%;background:{GOLD};color:{DK};font-weight:800;font-size:27px;display:flex;align-items:center;justify-content:center;box-shadow:0 4px 12px rgba(0,0,0,.3)}}
.row .k{{flex:none;width:210px;font-weight:800;font-size:29px;color:{GOLD}}}
.row .v{{font-size:28px;font-weight:600;line-height:1.35}}
.row .v small{{display:block;font-size:22px;font-weight:500;color:#bcd9e0;margin-top:2px}}
.stats{{align-self:stretch;display:flex;gap:16px}}
.st{{flex:1;padding:20px 12px}}
.st b{{display:block;font-size:50px;font-weight:800;color:{GOLD};line-height:1.05}}
.st b.c{{color:{CY}}}
.st span{{display:block;font-size:21px;font-weight:600;color:#d6e9ee;margin-top:6px;line-height:1.25}}
.tip{{align-self:stretch;display:flex;align-items:center;gap:16px;text-align:left;background:rgba(246,195,67,.13);border:2px solid rgba(246,195,67,.45);border-radius:20px;padding:18px 26px;font-size:26px;font-weight:600;line-height:1.35}}
.tip b{{color:{GOLD}}}
.chip{{display:inline-block;border:2px solid rgba(255,255,255,.3);background:rgba(255,255,255,.08);border-radius:30px;padding:9px 20px;font-size:24px;font-weight:700;margin:4px}}
.note{{font-size:19px;color:#a9cbd3;font-weight:500}}
"""

def page(n, body, pct=None):
    pct = pct if pct is not None else n / TOTAL * 100
    return f'''<!doctype html><html lang="mn"><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="pg"><div class="gr"></div>
<div class="hd"><img src="{LOGO}"><div class="pn">{n}/{TOTAL}</div></div>
<div class="mn">{body}</div><div class="bar"><i style="width:{pct:.0f}%"></i></div>
<div class="ft"><span>@globalmathprep · globalmathprep.academy</span><span>{n}/{TOTAL}</span></div></div></body></html>'''

# ---------- hero illustrations (viewBox 200) ----------
def svg(x): return f'<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">{x}</svg>'
SH = '<ellipse cx="100" cy="182" rx="62" ry="7" fill="rgba(0,0,0,.25)"/>'
H = {}
H['test'] = svg(SH + f'''<rect x="42" y="30" width="116" height="146" rx="14" fill="{PAPER}"/><rect x="72" y="20" width="56" height="22" rx="8" fill="{DK}"/>
<rect x="60" y="62" width="62" height="10" rx="5" fill="{DK}"/><rect x="60" y="80" width="80" height="7" rx="3.5" fill="#c9c1ad"/>
<circle cx="66" cy="108" r="7" fill="none" stroke="{CYD}" stroke-width="4"/><rect x="80" y="104" width="58" height="7" rx="3.5" fill="#c9c1ad"/>
<circle cx="66" cy="130" r="7" fill="{GOLD}"/><rect x="80" y="126" width="46" height="7" rx="3.5" fill="#c9c1ad"/>
<circle cx="66" cy="152" r="7" fill="none" stroke="{CYD}" stroke-width="4"/><rect x="80" y="148" width="52" height="7" rx="3.5" fill="#c9c1ad"/>
<circle cx="150" cy="150" r="30" fill="{GOLD}"/><path d="M150 132v18l12 8" stroke="{DK}" stroke-width="6" fill="none" stroke-linecap="round"/>''')
H['target'] = svg(SH + f'''<circle cx="95" cy="105" r="70" fill="{PAPER}"/><circle cx="95" cy="105" r="52" fill="{CYD}"/><circle cx="95" cy="105" r="34" fill="{PAPER}"/><circle cx="95" cy="105" r="16" fill="{GOLD}"/>
<path d="M95 105L165 38" stroke="{DK}" stroke-width="7" stroke-linecap="round"/><path d="M152 30l20 -6 -6 20z" fill="{GOLD}" stroke="{DK}" stroke-width="4" stroke-linejoin="round"/>''')
H['app'] = svg(SH + f'''<rect x="30" y="38" width="140" height="104" rx="12" fill="{DK}"/><rect x="38" y="46" width="124" height="88" rx="6" fill="{PAPER}"/>
<rect x="50" y="58" width="50" height="9" rx="4.5" fill="{CYD}"/><rect x="50" y="76" width="100" height="6" rx="3" fill="#c9c1ad"/><rect x="50" y="90" width="84" height="6" rx="3" fill="#c9c1ad"/>
<rect x="50" y="106" width="40" height="16" rx="8" fill="{GOLD}"/><path d="M18 150h164l-12 18H30z" fill="#8fb3bd"/>
<circle cx="150" cy="60" r="0"/><path d="M130 100l10 10 20-24" stroke="#2f9e6e" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/>''')
H['log'] = svg(SH + f'''<rect x="40" y="26" width="120" height="150" rx="12" fill="{PAPER}"/><rect x="40" y="26" width="22" height="150" rx="10" fill="{CYD}"/>
<path d="M78 58l14 14M92 58L78 72" stroke="#e5534b" stroke-width="6" stroke-linecap="round"/><rect x="102" y="61" width="42" height="7" rx="3.5" fill="#c9c1ad"/>
<path d="M76 104l8 8 14-16" stroke="#2f9e6e" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/><rect x="104" y="101" width="40" height="7" rx="3.5" fill="#c9c1ad"/>
<rect x="76" y="134" width="68" height="7" rx="3.5" fill="#c9c1ad"/><path d="M150 120l26-26 10 10-26 26-14 4z" fill="{GOLD}" stroke="{DK}" stroke-width="4" stroke-linejoin="round"/>''')
H['module'] = svg(SH + f'''<rect x="22" y="56" width="62" height="86" rx="10" fill="{PAPER}"/><text x="53" y="108" text-anchor="middle" font-family="M" font-weight="800" font-size="28" fill="{DK}">M1</text>
<path d="M88 99c30 0 30-44 58-44M88 99c30 0 30 44 58 44" stroke="{CY}" stroke-width="6" fill="none" stroke-linecap="round"/>
<rect x="138" y="36" width="50" height="36" rx="9" fill="{GOLD}"/><text x="163" y="61" text-anchor="middle" font-family="M" font-weight="800" font-size="18" fill="{DK}">800</text>
<rect x="138" y="126" width="50" height="36" rx="9" fill="{PAPER}"/><text x="163" y="151" text-anchor="middle" font-family="M" font-weight="800" font-size="18" fill="{DK}">600</text>
<circle cx="88" cy="99" r="8" fill="{CY}"/>''')
H['clock'] = svg(SH + f'''<rect x="88" y="16" width="24" height="18" rx="5" fill="{GOLD}"/><circle cx="100" cy="104" r="70" fill="{PAPER}" stroke="{DK}" stroke-width="8"/>
<path d="M100 104 L100 34 A70 70 0 0 1 166 82 Z" fill="{CYD}" opacity=".85"/>
<path d="M100 104V58M100 104l30 18" stroke="{DK}" stroke-width="8" stroke-linecap="round"/><circle cx="100" cy="104" r="8" fill="{GOLD}"/>''')
H['abc'] = svg(SH + f'''<path d="M30 40c26-10 50-6 70 8v130c-20-14-44-18-70-8z" fill="{PAPER}"/><path d="M170 40c-26-10-50-6-70 8v130c20-14 44-18 70-8z" fill="#e9e0c9"/>
<text x="64" y="112" text-anchor="middle" font-family="M" font-weight="800" font-size="40" fill="{DK}">Aa</text>
<rect x="116" y="76" width="40" height="7" rx="3.5" fill="{CYD}"/><rect x="116" y="94" width="34" height="7" rx="3.5" fill="#c9c1ad"/><rect x="116" y="112" width="40" height="7" rx="3.5" fill="#c9c1ad"/>
<circle cx="160" cy="46" r="22" fill="{GOLD}"/><text x="160" y="54" text-anchor="middle" font-family="M" font-weight="800" font-size="20" fill="{DK}">20</text>''')
H['calc'] = svg(SH + f'''<rect x="26" y="30" width="148" height="140" rx="16" fill="{PAPER}"/><path d="M46 150V48M46 150h110" stroke="#9c9480" stroke-width="4"/>
<path d="M50 140C80 40 110 40 150 70" stroke="{CYD}" stroke-width="7" fill="none" stroke-linecap="round"/><path d="M50 60L150 140" stroke="{GOLD}" stroke-width="7" stroke-linecap="round"/>
<circle cx="84" cy="87" r="9" fill="{DK}"/><circle cx="138" cy="130" r="0"/>''')
H['cal'] = svg(SH + f'''<rect x="30" y="40" width="140" height="132" rx="16" fill="{PAPER}"/><rect x="30" y="40" width="140" height="34" rx="16" fill="{CYD}"/><rect x="30" y="58" width="140" height="16" fill="{CYD}"/>
<rect x="60" y="26" width="10" height="28" rx="5" fill="{DK}"/><rect x="130" y="26" width="10" height="28" rx="5" fill="{DK}"/>''' +
 ''.join(f'<rect x="{44+i%5*24}" y="{86+i//5*26}" width="18" height="18" rx="4" fill="{GOLD if i in (1,6,8,12) else "#d9d0bb"}"/>' for i in range(15)))
H['gmp'] = svg(SH + f'''<path d="M100 22l62 24v48c0 40-28 68-62 82-34-14-62-42-62-82V46z" fill="{PAPER}"/><path d="M100 38l46 18v38c0 30-20 52-46 64z" fill="#e9e0c9"/>
<path d="M70 100l20 20 40-44" stroke="#2f9e6e" stroke-width="12" fill="none" stroke-linecap="round" stroke-linejoin="round"/><circle cx="160" cy="44" r="18" fill="{GOLD}"/><text x="160" y="51" text-anchor="middle" font-family="M" font-weight="800" font-size="17" fill="{DK}">1%</text>''')
H['rocket'] = svg(SH + f'''<path d="M100 20c30 20 40 60 30 100H70C60 80 70 40 100 20z" fill="{PAPER}"/><circle cx="100" cy="70" r="16" fill="{CYD}" stroke="{DK}" stroke-width="5"/>
<path d="M70 120l-22 26 30-6zM130 120l22 26-30-6z" fill="{GOLD}"/><path d="M84 126h32l-6 32h-20z" fill="{GOLD}"/><path d="M92 158h16l-8 18z" fill="#ff9a52"/>''')

def hero(k): return f'<div class="hero">{H[k]}</div>'
def pill(t): return f'<div class="pill">{t}</div>'
def rows(items, numbered=True):
    out = ''
    for i, it in enumerate(items, 1):
        if isinstance(it, tuple) and not numbered:
            out += f'<div class="row"><div class="k">{it[0]}</div><div class="v">{it[1]}</div></div>'
        else:
            out += f'<div class="row"><div class="num">{i}</div><div class="v">{it}</div></div>'
    return f'<div class="gl rows">{out}</div>'
def stats(items): return '<div class="stats">' + ''.join(f'<div class="gl st"><b class="{c}">{a}</b><span>{b}</span></div>' for a, b, c in items) + '</div>'
def lead(a, b=''): return f'<div class="gl lead">{a}{f"<span>{b}</span>" if b else ""}</div>'
def tip(t): return f'<div class="tip"><div>{t}</div></div>'

S = []
# 1 COVER
S.append(hero('rocket') + f'''{pill('МЭДЭЭЛЛИЙН ЦУВРАЛ #02')}
<h1 style="font-size:86px">SAT оноогоо<br><em>өсгөх 9 алхам</em></h1>
<div class="gl" style="padding:26px 30px 22px;display:flex;align-items:center;gap:28px;text-align:left">
 <div style="font-size:150px;font-weight:800;color:{GOLD};line-height:.9;letter-spacing:-4px">+115</div>
 <div style="font-size:40px;font-weight:800;line-height:1.3">оноо<span style="display:block;font-size:27px;font-weight:500;color:#cfe6ec;margin-top:6px">20 цаг зөв дасгал хийсэн сурагчдын дундаж өсөлт*</span></div></div>
<div style="font-size:36px;font-weight:700;line-height:1.35">Илүү <span style="color:#ffb3a8;text-decoration:line-through">их</span> биш,<br>илүү <span style="color:{CY}">ЗӨВ</span> бэлдэх нь чухал.</div>
<div><span class="chip">Бодит судалгаа</span><span class="chip">Үнэгүй эх сурвалж</span><span class="chip">Хадгалаад ав</span></div>
<div class="note">*College Board × Khan Academy судалгаа, ~250,000 сурагч</div>
<div style="font-size:30px;font-weight:800;color:{GOLD}">Гүйлгээд үзээрэй →</div>''')
# 2 step 1
S.append(hero('test') + pill('SAT · АЛХАМ 1') + '<h1>Эхлээд одоогийн<br><em>түвшнээ мэд</em></h1>' +
 lead('Bluebook апп дээр бүтэн практик тестийг жинхэнэ шалгалт шиг өг.', 'Цаг хэмжин, завсарлагатай, утасгүй. Энэ оноо бол таны эхлэлийн цэг.') +
 stats([('98', 'асуулт', ''), ('2ц 14м', 'шалгалтын нийт хугацаа', 'c'), ('0₮', 'албан ёсны тест үнэгүй', '')]) +
 tip('Цаг бага байна уу? <b>GMP-ийн 20 минутын үнэгүй түвшин тогтоох тест</b>ийг өг.'))
# 3 step 2
S.append(hero('target') + pill('SAT · АЛХАМ 2') + '<h1>Зорилгоо<br><em>тоогоор тавь</em></h1>' +
 rows([('Зорилго', 'Хүсэж буй сургуулиудын элсэгчдийн SAT оноог судал.'),
       ('Зөрүү', 'Зорилго − одоогийн оноо = нөхөх оноо.'),
       ('Хуваах', 'Math, Англи хэсэгт тус тусад нь зорилт тавь.')], numbered=False) +
 f'<div class="gl" style="padding:20px 26px;font-size:30px;font-weight:800">Жишээ: 1150 → 1350 = <span style="color:{GOLD}">+200</span><span style="display:block;font-size:24px;font-weight:600;color:#cfe6ec;margin-top:6px">Math +100 · Англи +100 · Ойлгомжтой, хэмжигдэхүйц</span></div>')
# 4 step 3
S.append(hero('app') + pill('SAT · АЛХАМ 3') + '<h1>Албан ёсны<br><em>материалаар бэлд</em></h1>' +
 rows([('Bluebook', 'Бодит шалгалттай ижил, адаптив бүтэн тестүүд'),
       ('Khan Academy', 'Official SAT Practice: ур чадвар бүрээр, үнэгүй'),
       ('Question Bank', 'College Board-ийн асуултын сан: сул сэдвээрээ шүүж бод')], numbered=False) +
 tip('Албан бус тестүүдийн хүндрэл, оноо бодит шалгалтаас <b>зөрөх</b> тохиолдол бий.'))
# 5 step 4
S.append(hero('log') + pill('SAT · АЛХАМ 4') + '<h1>Алдаа бүр —<br><em>дараагийн оноо</em></h1>' +
 lead('Алдааны дэвтэр хөтөл: буруу хариулт бүрт 3 зүйл бич.', 'Яагаад алдсан · Зөв дүрэм, арга · 7 хоногийн дараа дахин бодох') +
 '<div class="gl" style="padding:18px 20px"><div style="font-size:23px;font-weight:700;color:#cfe6ec;margin-bottom:8px">Алдааны 4 шалтгаан</div>' +
 ''.join(f'<span class="chip">{c}</span>' for c in ['Мэдлэг дутсан', 'Буруу уншсан', 'Цаг хүрээгүй', 'Болгоомжгүй']) + '</div>' +
 tip('GMP: буруу хариулт бүрийг <b>Reteach</b>-ээр дахин тайлбарлаж, дахин бодуулдаг.'))
# 6 step 5
S.append(hero('module') + pill('SAT · АЛХАМ 5') + '<h1>Эхний модульд<br><em>нарийвчлал</em></h1>' +
 rows(['Асуултыг бүтэн уншаад, дараа нь хариултаа хар.',
       'Хялбар асуултаа <b style="color:#8ff0f5">алдахгүй</b> — хурдан биш, зөв бод.',
       'Эргэлзсэн асуултаа тэмдэглэ (flag), сүүлд нь эргэж ир.',
       'Хоосон бүү орхи: буруу хариултад оноо хасагдахгүй.']) +
 tip('Эхний модуль сайн бол хэцүү 2-р модуль нээгдэж, <b>өндөр оноо</b> боломжтой болно.'))
# 7 step 6
S.append(hero('clock') + pill('SAT · АЛХАМ 6') + '<h1>Цагаа<br><em>ухаалаг хуваа</em></h1>' +
 stats([('~71 сек', 'Англи: асуулт бүрт<br>(64 мин ÷ 54)', ''), ('~95 сек', 'Math: асуулт бүрт<br>(70 мин ÷ 44)', 'c')]) +
 rows(['Гацвал тэмдэглээд цааш яв — нэг асуултад цагаа бүү үр.',
       'Практик тест бүрийг таймертай өг.',
       'Эцсийн 2–3 минутад тэмдэглэсэн асуултаа шалга.']))
# 8 step 7
bars = [('Мэдээлэл ба санаа', 26), ('Бүтэц ба үг хэрэглээ', 28), ('Санаа илэрхийлэх', 20), ('Англи хэлний дүрэм', 26)]
bh = ''.join(f'<div style="display:flex;align-items:center;gap:14px;margin:9px 0"><div style="width:330px;text-align:left;font-size:23px;font-weight:600">{a}</div><div style="flex:1;height:26px;background:rgba(255,255,255,.1);border-radius:13px"><div style="width:{p*3}%;height:100%;border-radius:13px;background:{GOLD if a.startswith("Англи") else CYD}"></div></div><div style="width:70px;font-weight:800;font-size:25px;color:{GOLD}">{p}%</div></div>' for a, p in bars)
S.append(hero('abc') + pill('SAT · АЛХАМ 7') + '<h1>Англи: <em>дүрэм +<br>үгсийн сан</em></h1>' +
 f'<div class="gl" style="padding:18px 28px">{bh}</div>' +
 rows(['Дүрэм тодорхой хариутай — хамгийн <b style="color:#8ff0f5">хурдан өсдөг</b> хэсэг.',
       'Өдөрт 20 шинэ үг + 20 минут англиар унш.']) +
 tip('GMP Vocab Hub: <b>3,717 үг</b>, өдөрт 20 үгээр.'))
# 9 step 8
S.append(hero('calc') + pill('SAT · АЛХАМ 8') + '<h1>Math: <em>эхлээд уншаад,<br>дараа нь бод</em></h1>' +
 rows(['Асуулт яг <b style="color:#8ff0f5">юуг</b> асууж байгааг тодруулж, доогуур нь зур.',
       'Desmos график тооны машин Math хэсэг бүхэлд нь ашиглагдана — хариугаа шалга.',
       'Томьёоны хуудас шалгалтад өгөгдөнө — хаана юу байгааг урьдчилан мэд.']) +
 tip('“Алдсан онооны ихэнх нь алгебр биш — <b>асуугаагүй асуултад</b> хариулснаас.” — GMP'))
# 10 step 9
days = [('Да', 'Асуулт', ''), ('Мя', 'Асуулт', ''), ('Лх', 'Асуулт', ''), ('Пү', 'Асуулт', ''), ('Ба', 'Асуулт', ''), ('Бя', 'Бүтэн тест', 'g'), ('Ня', 'Алдаа засах', 'c')]
dh = '<div style="display:flex;gap:10px">' + ''.join(f'<div style="flex:1;border-radius:16px;padding:14px 4px;background:{"rgba(246,195,67,.9)" if k=="g" else ("rgba(143,240,245,.85)" if k=="c" else "rgba(255,255,255,.08)")};color:{DK if k else "#fff"};border:2px solid rgba(255,255,255,.2)"><div style="font-weight:800;font-size:27px">{d}</div><div style="font-size:17px;font-weight:700;margin-top:6px;line-height:1.2">{t}</div></div>' for d, t, k in days) + '</div>'
S.append(hero('cal') + pill('SAT · АЛХАМ 9') + '<h1>Бага багаар,<br><em>өдөр бүр</em></h1>' +
 stats([('6–8 цаг', 'дасгал → дунджаар<br>+90 оноо*', ''), ('20 цаг', 'дасгал → дунджаар<br>+115 оноо*', 'c')]) +
 f'<div class="gl" style="padding:18px">{dh}<div style="font-size:22px;font-weight:600;color:#cfe6ec;margin-top:12px">Ажлын өдөр 30–45 минут · Амралтын өдөр тест + дүгнэлт</div></div>' +
 '<div class="note">*College Board × Khan Academy судалгаа</div>')
# 11 GMP method
S.append(hero('gmp') + pill('GLOBAL MATH PREP-ИЙН АРГА') + '<h1>Асуулт бүрийг бодож,<br><em>өдөр бүр 1%-иар ахи</em></h1>' +
 stats([('3,904', 'Math асуулт', ''), ('1,802', 'Англи асуулт', 'c'), ('13', 'адаптив бүтэн тест', '')]) +
 rows(['Долоо хоног бүр практик тест — оноо хэсэг хэсгээр',
       'Асуулт бүр бүрэн тайлбартай, алдааг Reteach-ээр засна',
       'Эцэг эхэд долоо хоног бүрийн ахицын тайлан',
       '2–5 сурагчтай жижиг анги, Zoom-ээр шууд']))
# 12 END
sched = f'''<div class="gl" style="padding:8px 0">
<div class="row"><div class="k" style="width:230px">Англи (R&amp;W)</div><div class="v" style="font-size:29px;font-weight:800">Мя · Пү · Бя<small>18:30–19:50 (УБ цаг)</small></div></div>
<div class="row"><div class="k" style="width:230px">Math</div><div class="v" style="font-size:29px;font-weight:800">Да · Лх · Ба<small>18:30–19:50 (УБ цаг)</small></div></div></div>'''
S.append(pill('ОДОО ЭХЛЭЕ') + '<h1>SAT-ын бэлтгэл<br><em>эхэлж байна</em></h1>' + sched +
 f'''<div style="align-self:stretch;display:flex;gap:20px;align-items:stretch">
 <div style="background:#fff;border-radius:26px;padding:16px;display:flex;flex-direction:column;align-items:center"><img src="{QR}" style="width:260px;height:260px"><div style="color:{DK};font-weight:800;font-size:23px;margin-top:6px">Скан хийж бүртгүүл</div></div>
 <div class="gl" style="flex:1;padding:22px 26px;text-align:left;display:flex;flex-direction:column;justify-content:center;gap:14px;font-size:25px;font-weight:600;line-height:1.3">
  <div>Үнэгүй 20 минутын түвшин тогтоох тест</div><div>2–5 сурагчтай жижиг анги</div><div>Эцэг эхэд 7 хоног бүрийн тайлан</div>
  <div style="color:{GOLD};font-weight:800">Суудал хязгаартай</div></div></div>
<div style="align-self:stretch;background:{GOLD};color:{DK};border-radius:22px;padding:18px;font-size:29px;font-weight:800">WhatsApp: +1 428 880 1826 · globalmathprep.academy</div>
<div style="font-size:24px;font-weight:700;color:#cfe6ec">Хадгалаад, SAT өгөх найздаа хуваалцаарай</div>''')

if __name__ == '__main__':
    assert len(S) == TOTAL
    out = HERE / 'out15'; out.mkdir(exist_ok=True)
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page(viewport={'width': 1080, 'height': 1350})
        for i, body in enumerate(S, 1):
            pg.set_content(page(i, body)); pg.wait_for_timeout(300)
            ov = pg.evaluate("()=>{const m=document.querySelector('.mn');let t=1e9,b=0;for(const c of m.children){const x=c.getBoundingClientRect();t=Math.min(t,x.top);b=Math.max(b,x.bottom)}return [Math.round(t),Math.round(b)]}")
            fn = out / f'GMP-SAT-Onoo-Osgoh-{i:02d}-of-{TOTAL}.png'
            pg.screenshot(path=str(fn)); print(fn.name, ov, 'OK' if ov[0] >= 120 and ov[1] <= 1250 else 'OVERFLOW')
        br.close()
