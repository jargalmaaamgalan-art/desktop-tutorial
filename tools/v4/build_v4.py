"""GMP design v4: five series looks so the grid stops looking the same.
Each content pillar gets its own background, layout and type, not just a tint.
Run: python3 build_v4.py  -> PNG covers in ./out (1080x1350)."""
import pathlib, sys
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).resolve().parent
T = HERE.parent
OUT = HERE / 'out'; OUT.mkdir(exist_ok=True)

def fonts():
    css = ''
    mf = T / 'poster/fonts/package/files'
    for w in (500, 600, 700, 800, 900):
        for sub in ('latin', 'latin-ext', 'cyrillic', 'cyrillic-ext'):
            p = mf / f'montserrat-{sub}-{w}-normal.woff2'
            if p.exists():
                css += f"@font-face{{font-family:M;font-weight:{w};src:url('{p.as_uri()}')}}\n"
    sf = T / 'poster/fonts/serif/package/files'
    for w in (600, 700, 800, 900):
        for st in ('normal', 'italic'):
            for sub in ('latin', 'latin-ext', 'cyrillic', 'cyrillic-ext'):
                p = sf / f'source-serif-4-{sub}-{w}-{st}.woff2'
                if p.exists():
                    css += f"@font-face{{font-family:S;font-weight:{w};font-style:{st};src:url('{p.as_uri()}')}}\n"
    pf = T / 'fonts2/fontsource-playfair-display-5.3.0/package/files'
    for sub in ('latin', 'latin-ext', 'cyrillic'):
        for st in ('normal', 'italic'):
            p = pf / f'playfair-display-{sub}-900-{st}.woff2'
            if p.exists():
                css += f"@font-face{{font-family:P;font-weight:900;font-style:{st};src:url('{p.as_uri()}')}}\n"
    return css

LOGO_LIGHT = (T / 'v2/hdr_logo.png').as_uri()        # white text, for dark grounds
LOGO_DARK = (T / 'v2/hdr_logo_dark.png').as_uri()    # navy text, for light grounds
ROUND = (T / 'v2/gmp-round.png').as_uri()

BASE = """
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px;overflow:hidden}
body{font-family:M,sans-serif;position:relative}
.logo{position:absolute;left:64px;top:52px;height:64px}
.foot{position:absolute;left:64px;right:64px;bottom:48px;display:flex;justify-content:space-between;align-items:center;font-weight:700;font-size:24px;letter-spacing:.5px}
.swipe{display:inline-flex;align-items:center;gap:12px;padding:16px 28px;border-radius:999px;font-weight:800;font-size:26px}
.ser{font-family:S,serif}
"""

def page(css, body):
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{fonts()}{BASE}{css}</style></head><body>{body}</body></html>"

ARROW = "<svg width='30' height='30' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'><path d='M5 12h14M13 6l6 6-6 6'/></svg>"

# A. COLLEGE BOARD NEWS: black ground, yellow ticker, newspaper headline
def news():
    css = """
body{background:#0d0d0f;color:#fff}
.tick{position:absolute;left:0;right:0;top:160px;height:70px;background:#ffd23f;color:#0d0d0f;display:flex;align-items:center;gap:26px;padding-left:64px;font-weight:900;font-size:30px;letter-spacing:3px;white-space:nowrap;overflow:hidden}
.tick i{font-style:normal;opacity:.45}
.date{position:absolute;left:64px;top:262px;font-size:26px;font-weight:700;color:#9a9aa3;letter-spacing:2px}
.h{position:absolute;left:64px;right:64px;top:300px;font-family:P,serif;font-weight:900;font-size:138px;line-height:1.0;letter-spacing:-2px}
.h em{font-style:normal;color:#ffd23f}
.list{position:absolute;left:64px;right:64px;top:770px;border-top:3px solid #ffd23f}
.row{display:flex;gap:26px;align-items:baseline;padding:22px 0;border-bottom:1px solid #2c2c33;font-size:34px;font-weight:700}
.row b{font-family:P,serif;font-size:44px;color:#ffd23f;width:44px}
.row.fade{opacity:.35;filter:blur(1.5px)}
.foot{color:#9a9aa3}
.swipe{background:#ffd23f;color:#0d0d0f}
"""
    rows = [("1", "Windows 11 шаардлагатай"), ("2", "Chromebook: зөвхөн verified mode"), ("3", "Тооны машиныг томруулж болно")]
    r = ''.join(f"<div class='row'><b>{n}</b>{t}</div>" for n, t in rows)
    r += "<div class='row fade'><b>4</b>Reference sheet шинэ загвартай</div>"
    body = f"""<img class='logo' src='{LOGO_LIGHT}'>
<div class='tick'>COLLEGE BOARD МЭДЭЭ <i>●</i> SAT NEWS <i>●</i> COLLEGE BOARD МЭДЭЭ <i>●</i> SAT NEWS</div>
<div class='date'>ЭХ СУРВАЛЖ: SATSUITE.COLLEGEBOARD.ORG</div>
<div class='h'>Bluebook<br><em>өөрчлөгдлөө.</em><br>5 шинэчлэл</div>
<div class='list'>{r}</div>
<div class='foot'><span>@globalmathprep</span><span class='swipe'>Бүгдийг харах {ARROW}</span></div>"""
    return page(css, body)

# B. SAT MATH QUESTION OF THE DAY: graph paper, big equation, Desmos-blue frame
def math():
    css = """
body{background:#fbfbf7;color:#101828;
background-image:linear-gradient(#e3e7ef 1.5px,transparent 1.5px),linear-gradient(90deg,#e3e7ef 1.5px,transparent 1.5px);background-size:54px 54px}
.tag{position:absolute;left:64px;top:160px;display:flex;gap:14px}
.tag span{padding:12px 22px;border-radius:12px;font-weight:800;font-size:24px;letter-spacing:1px}
.t1{background:#2f6fec;color:#fff}.t2{background:#fff;border:3px solid #101828}
.no{position:absolute;right:64px;top:132px;font-family:P,serif;font-weight:900;font-size:150px;color:#2f6fec;line-height:1}
.h{position:absolute;left:64px;right:64px;top:320px;font-weight:900;font-size:112px;line-height:1.04;letter-spacing:-2px}
.h .vs{color:#ff6a3d}
.card{position:absolute;left:64px;right:64px;top:650px;background:#fff;border:4px solid #101828;border-radius:28px;box-shadow:12px 12px 0 #2f6fec;padding:38px 40px}
.q{font-family:S,serif;font-size:38px;line-height:1.35}
.q i{font-style:italic}
.opts{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:30px}
.o{border:3px solid #cfd5e1;border-radius:16px;padding:18px 22px;font-family:S,serif;font-size:38px;display:flex;gap:18px;align-items:center}
.o b{font-family:M;font-size:24px;width:44px;height:44px;border-radius:50%;border:3px solid #101828;display:grid;place-items:center}
.timer{position:absolute;left:64px;top:1150px;display:flex;align-items:center;gap:14px;font-weight:800;font-size:30px}
.timer s{text-decoration:none;background:#ff6a3d;color:#fff;padding:10px 20px;border-radius:12px}
.foot{color:#5b6475}
.swipe{background:#101828;color:#fff}
"""
    opts = [("A", "5 − 3<i>t</i>"), ("B", "3<i>t</i> − 5"), ("C", "3(<i>t</i> − 5)"), ("D", "3<i>t</i> + 5")]
    o = ''.join(f"<div class='o'><b>{a}</b><span>{t}</span></div>" for a, t in opts)
    body = f"""<img class='logo' src='{LOGO_DARK}'>
<div class='tag'><span class='t1'>SAT MATH</span><span class='t2'>ӨДРИЙН АСУУЛТ</span></div>
<div class='no'>#001</div>
<div class='h'>3t − 5 үү,<br><span class='vs'>5 − 3t</span> үү?</div>
<div class='card'><div class='q'>Which expression is “five less than three times a number <i>t</i>”?</div><div class='opts'>{o}</div></div>
<div class='timer'><s>60 сек</s> Хариугаа бичээд, дараа нь гүйлгэ</div>
<div class='foot'><span>@globalmathprep</span><span class='swipe'>Хариу {ARROW}</span></div>"""
    return page(css, body)

# C. SAT ENGLISH CHALLENGE: editorial, deep plum, big serif text with the blank
def english():
    css = """
body{background:#3a0b2c;color:#fbeee6}
.tag{position:absolute;left:64px;top:160px;font-weight:800;font-size:24px;letter-spacing:4px;color:#ff9fb7}
.big{position:absolute;left:40px;top:150px;font-family:P,serif;font-size:420px;color:#5a1846;line-height:1}
.h{position:absolute;left:64px;right:64px;top:300px;font-family:P,serif;font-weight:900;font-size:110px;line-height:1.02}
.h em{font-style:normal;color:#ff9fb7}
.pass{position:absolute;left:64px;right:64px;top:640px;font-family:S,serif;font-style:normal;font-weight:600;font-size:44px;line-height:1.4;color:#f2d9cf}
.blank{display:inline-block;width:240px;border-bottom:5px solid #ff9fb7;margin:0 6px}
.chips{position:absolute;left:64px;top:930px;display:flex;flex-wrap:wrap;gap:14px;width:900px}
.chips span{border:3px solid #ff9fb7;border-radius:999px;padding:12px 26px;font-family:S,serif;font-weight:700;font-size:34px;color:#fbeee6}
.meta{position:absolute;left:64px;top:1120px;font-weight:700;font-size:28px;color:#ff9fb7}
.foot{color:#c9a6b8}
.swipe{background:#ff9fb7;color:#3a0b2c}
"""
    ch = ''.join(f"<span>{w}</span>" for w in ("uncontroversial", "individualistic", "theoretical", "homogeneous"))
    body = f"""<img class='logo' src='{LOGO_LIGHT}'>
<div class='big'>“</div>
<div class='tag'>SAT ENGLISH · CHALLENGE 1.02</div>
<div class='h'>Худал итгэлийг<br><em>аль үг нэрлэх вэ?</em></div>
<div class='pass'>Disproving the common misconception of Native art as <span class='blank'></span>, the painters whose work appears in the collection…</div>
<div class='chips'>{ch}</div>
<div class='meta'>4 сонголт · 90 секунд · Words in Context</div>
<div class='foot'><span>@globalmathprep</span><span class='swipe'>Задаргаа {ARROW}</span></div>"""
    return page(css, body)

# D. DATA GUIDE: cream, giant number, real bar chart
def data():
    css = """
body{background:#f4efe6;color:#1b1b1b}
.tag{position:absolute;left:64px;top:160px;background:#1b1b1b;color:#f4efe6;padding:12px 22px;border-radius:10px;font-weight:800;font-size:24px;letter-spacing:2px}
.h{position:absolute;left:64px;right:64px;top:250px;font-weight:900;font-size:68px;line-height:1.05;letter-spacing:-1.5px}
.num{position:absolute;left:52px;top:410px;font-family:P,serif;font-weight:900;font-size:300px;line-height:1;color:#e4572e;letter-spacing:-6px}
.num small{font-size:120px}
.sub{position:absolute;left:600px;right:64px;top:470px;font-weight:700;font-size:34px;line-height:1.3}
.sub b{color:#e4572e}
.chart{position:absolute;left:64px;right:64px;top:780px}
.bar{display:flex;align-items:center;gap:20px;margin-bottom:16px;font-weight:800;font-size:28px}
.bar .l{width:96px}
.bar .t{flex:1;height:44px;background:#e5dccd;border-radius:10px;overflow:hidden}
.bar .f{height:100%;background:#1b1b1b;border-radius:10px}
.bar.hi .f{background:#e4572e}
.bar .v{width:70px;text-align:right}
.src{position:absolute;left:64px;top:1150px;font-size:22px;font-weight:600;color:#7b7266}
.foot{color:#7b7266}
.swipe{background:#1b1b1b;color:#f4efe6}
"""
    rows = [(1000, 47), (1100, 62), (1200, 75), (1300, 85), (1400, 93), (1500, 97)]
    b = ''.join(f"<div class='bar{' hi' if s == 1400 else ''}'><span class='l'>{s}</span><div class='t'><div class='f' style='width:{p}%'></div></div><span class='v'>{p}</span></div>" for s, p in rows)
    body = f"""<img class='logo' src='{LOGO_DARK}'>
<div class='tag'>ТОО ЯРЬЖ БАЙНА</div>
<div class='h'>1400 гэдэг сайн оноо уу?</div>
<div class='num'>93<small>%</small></div>
<div class='sub'>100 сурагчаас <b>93</b> нь ижил буюу доогуур оноотой</div>
<div class='chart'>{b}</div>
<div class='src'>SAT User Percentile · research.collegeboard.org</div>
<div class='foot'><span>@globalmathprep</span><span class='swipe'>Гүйлгээд үз {ARROW}</span></div>"""
    return page(css, body)

# E. DEADLINE: full-bleed red-orange, calendar tile, countdown
def deadline():
    css = """
body{background:#ff4d2e;color:#fff}
.tag{position:absolute;left:64px;top:160px;font-weight:900;font-size:26px;letter-spacing:4px;color:#2a0a04}
.cal{position:absolute;left:64px;top:240px;width:420px;background:#fff;border-radius:34px;overflow:hidden;box-shadow:0 30px 60px rgba(60,10,0,.25);transform:rotate(-4deg)}
.cal .top{background:#2a0a04;color:#fff;text-align:center;font-weight:900;font-size:40px;letter-spacing:6px;padding:22px 0}
.cal .d{color:#2a0a04;text-align:center;font-family:P,serif;font-weight:900;font-size:230px;line-height:1.05;padding:10px 0 26px}
.cnt{position:absolute;left:560px;right:64px;top:250px}
.cnt b{display:block;font-family:P,serif;font-weight:900;font-size:230px;line-height:1}
.cnt span{display:block;margin-top:24px;font-weight:900;font-size:58px;line-height:1.05}
.h{position:absolute;left:64px;right:64px;top:790px;font-weight:900;font-size:76px;line-height:1.05;letter-spacing:-1.5px}
.h em{font-style:normal;color:#2a0a04}
.note{position:absolute;left:64px;right:64px;top:1080px;font-weight:700;font-size:30px;line-height:1.35;color:#ffe2da}
.foot{color:#ffe2da}
.swipe{background:#2a0a04;color:#fff}
"""
    body = f"""<img class='logo' src='{LOGO_LIGHT}'>
<div class='tag'>SAT ХУАНЛИ · 12/5-НЫ ШАЛГАЛТ</div>
<div class='cal'><div class='top'>НОЯ</div><div class='d'>20</div></div>
<div class='cnt'><b>13</b><span>хоног<br>үлдлээ</span></div>
<div class='h'>SAT шалгалтад<br><em>бүртгүүлэх</em> сүүлийн өдөр</div>
<div class='note'>УБ цагаар 11/21-ний 12:59 хүртэл · College Board-ийн сайтаар</div>
<div class='foot'><span>@globalmathprep</span><span class='swipe'>Алхам алхмаар {ARROW}</span></div>"""
    return page(css, body)

# F. SAT WORDS: lime ground, one giant word, meaning in Mongolian
def words():
    css = """
body{background:#c8f169;color:#0f1a0a}
.tag{position:absolute;left:64px;top:160px;display:flex;gap:14px;align-items:center}
.tag span{background:#0f1a0a;color:#c8f169;padding:12px 22px;border-radius:10px;font-weight:800;font-size:24px;letter-spacing:2px}
.tag b{font-weight:900;font-size:26px}
.k{position:absolute;left:64px;right:64px;top:290px;font-weight:900;font-size:68px;line-height:1.08}
.w{position:absolute;left:58px;top:480px;font-weight:900;font-size:146px;letter-spacing:-5px;line-height:1}
.ipa{position:absolute;left:64px;top:660px;font-family:S,serif;font-style:italic;font-size:38px;color:#3b5a1f}
.mn{position:absolute;left:64px;top:740px;background:#0f1a0a;color:#fff;padding:22px 34px;border-radius:22px;font-weight:900;font-size:64px}
.next{position:absolute;left:64px;right:64px;top:930px;display:flex;flex-wrap:wrap;gap:14px}
.next span{border:3px solid #0f1a0a;border-radius:999px;padding:12px 24px;font-weight:800;font-size:30px}
.foot{color:#3b5a1f}
.swipe{background:#0f1a0a;color:#c8f169}
"""
    nx = ''.join(f"<span>{w}</span>" for w in ("underscore", "corroborate", "reconcile", "ambivalent"))
    body = f"""<img class='logo' src='{LOGO_DARK}'>
<div class='tag'><span>SAT ҮГС</span><b>1 / 5</b></div>
<div class='k'>SAT-д байнга<br>гардаг 5 үг</div>
<div class='w'>undermine</div>
<div class='ipa'>verb · /ˌʌndərˈmaɪn/</div>
<div class='mn'>= сулруулах</div>
<div class='next'>{nx}</div>
<div class='foot'><span>@globalmathprep</span><span class='swipe'>Дараагийн үг {ARROW}</span></div>"""
    return page(css, body)

SETS = {'A-news': news, 'B-math': math, 'C-english': english, 'D-data': data, 'E-deadline': deadline, 'F-words': words}

if __name__ == '__main__':
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={'width': 1080, 'height': 1350})
        for name, fn in SETS.items():
            html = HERE / f'{name}.html'
            html.write_text(fn())
            pg.goto(html.as_uri()); pg.wait_for_timeout(400)
            over = pg.evaluate("""()=>[...document.querySelectorAll('body *')].filter(e=>{const r=e.getBoundingClientRect();return r.width>0&&(r.right>1080.5||r.bottom>1350.5||r.left<-0.5)}).map(e=>e.className||e.tagName)""")
            if over: print('OVERFLOW', name, over)
            pg.screenshot(path=str(OUT / f'{name}.png'))
            print('ok', name)
        b.close()
