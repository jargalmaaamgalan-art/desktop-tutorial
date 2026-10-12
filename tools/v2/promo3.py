"""GMP enrolment poster v3: photo banner on top, cream info section with a weekly timetable."""
import base64, sys
sys.argv = [sys.argv[0]]
from gen41 import F
from PIL import Image
from playwright.sync_api import sync_playwright

T, G, CREAM, INK = '#1b3b48', '#f3b045', '#fbf5e9', '#1b3b48'
src = Image.open('/root/.claude/uploads/7b9b247d-7185-5faa-ae2d-e13a2742cc61/b972ed30-image.jpg')
src.crop((0, 560, 1500, 1560)).resize((1080, 800), Image.LANCZOS).save('/home/claude/preview/jg-ban.jpg', quality=92)
PHOTO = 'data:image/jpeg;base64,' + base64.b64encode(open('/home/claude/preview/jg-ban.jpg', 'rb').read()).decode()
LOGO = 'data:image/png;base64,' + base64.b64encode(open('/home/claude/preview/gmp-logo.png', 'rb').read()).decode()

DAYS = ['Да', 'Мя', 'Лх', 'Пү', 'Ба', 'Бя', 'Ня']
MATH, ENG = {'Да', 'Лх', 'Ба'}, {'Мя', 'Пү', 'Ня'}
def cell(d):
    if d in MATH: return f'<div class="c m"><b>{d}</b><span>Математик</span></div>'
    if d in ENG: return f'<div class="c e"><b>{d}</b><span>Англи хэл</span></div>'
    return f'<div class="c o"><b>{d}</b><span>амралт</span></div>'
grid = ''.join(cell(d) for d in DAYS)

def ic(k):
    s = 'fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"'
    d = {'doc': '<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M9 8h6M9 12h6M9 16h4"/>',
         'chart': '<path d="M4 20h16M7 16v-5M12 16V7M17 16v-9"/>',
         'group': '<circle cx="9" cy="8" r="3"/><circle cx="16" cy="9" r="2.5"/><path d="M3 19c0-3 3-5 6-5s6 2 6 5M14 19c0-2 2-4 4-4s3 1 3 3"/>',
         'globe': '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>'}[k]
    return f'<svg viewBox="0 0 24 24" width="28" height="28" {s}>{d}</svg>'
FE = [('doc', 'College Board-ийн', 'албан ёсны асуултууд'), ('chart', 'Долоо хоног бүр', 'ахицын тайлан эцэг эхэд'),
      ('group', 'Цөөн сурагчтай', 'бүлэг, хүүхэд бүрд анхаарна'), ('globe', 'Англи, Монгол хэлээр', 'Канадаас онлайнаар')]
feats = ''.join(f'<div class="f"><i>{ic(k)}</i><div><b>{a}</b><span>{b}</span></div></div>' for k, a, b in FE)

HTML = f'''<!doctype html><html><head><meta charset="utf-8"><style>
{F('SS', 'source-serif-4', [700, 800])}{F('IN', 'inter', [400, 600, 800])}
*{{box-sizing:border-box;margin:0}}
body{{width:1080px;height:1350px;font-family:IN,sans-serif;color:{INK};background:{CREAM};overflow:hidden;position:relative}}
.ban{{height:720px;background:{T} url({PHOTO}) center top/cover no-repeat;position:relative;color:#fff}}
.ban:before{{content:'';position:absolute;inset:0;background:linear-gradient(90deg,rgba(27,59,72,.05) 35%,rgba(27,59,72,.82) 58%,rgba(27,59,72,.95) 100%)}}
.ban:after{{content:'';position:absolute;left:0;right:0;bottom:0;height:10px;background:{G}}}
.logo{{position:absolute;left:34px;top:30px;height:88px;background:rgba(27,59,72,.85);padding:8px 16px;border-radius:14px}}
.hd{{position:absolute;right:52px;top:170px;width:440px}}
.kick{{color:{G};font-weight:800;font-size:18px;letter-spacing:4px;text-transform:uppercase}}
h1{{font-family:SS,serif;font-size:68px;font-weight:800;line-height:1.02;margin:10px 0 14px}}h1 em{{font-style:normal;color:{G}}}
.lead{{font-size:21px;color:#dbe6ec;line-height:1.4}}
.res{{display:flex;align-items:center;gap:16px;margin-top:26px;border-top:2px solid rgba(243,176,69,.5);padding-top:18px}}
.res .big{{font-family:SS,serif;font-size:72px;font-weight:800;color:{G};line-height:.95}}
.res .t{{font-size:16px;line-height:1.35;color:#dbe6ec}}.res .t b{{color:#fff;font-size:18px;display:block;margin-bottom:3px}}
.who{{position:absolute;left:34px;bottom:34px;background:rgba(27,59,72,.88);border-left:6px solid {G};padding:14px 20px;max-width:470px;border-radius:0 14px 14px 0}}
.who h2{{font-family:SS,serif;font-size:30px;font-weight:800;line-height:1.05}}
.who .r{{color:{G};font-weight:800;font-size:14px;letter-spacing:1.5px;margin-top:6px;text-transform:uppercase}}
.body{{padding:40px 52px 0}}
.st{{font-family:SS,serif;font-size:34px;font-weight:800;line-height:1;margin-bottom:6px}}
.sub{{font-size:18px;color:#5a7380;margin-bottom:18px}}.sub b{{color:{INK};font-family:SS,serif;font-size:26px;margin-left:4px}}
.wk{{display:grid;grid-template-columns:repeat(7,1fr);gap:10px;margin-bottom:38px}}
.c{{border-radius:18px;padding:20px 6px 16px;text-align:center;border:2px solid transparent}}
.c b{{display:block;font-family:SS,serif;font-size:30px;font-weight:800;line-height:1}}.c span{{display:block;font-size:12.5px;font-weight:600;margin-top:8px;letter-spacing:.2px}}
.c.m{{background:{T};color:#fff}}.c.e{{background:{G};color:{T}}}.c.o{{background:transparent;border-color:#d8ccb8;color:#9aa9b0}}
.fl{{display:grid;grid-template-columns:1fr 1fr;gap:22px 24px;margin-bottom:38px}}
.f{{display:flex;align-items:center;gap:14px}}
.f i{{flex:none;width:58px;height:58px;border-radius:50%;background:{T};color:{G};display:flex;align-items:center;justify-content:center}}
.f b{{display:block;font-size:21px;line-height:1.2}}.f span{{font-size:17px;color:#5a7380}}
.cta{{display:flex;align-items:center;justify-content:space-between;background:{T};color:#fff;border-radius:24px;padding:22px 30px}}
.cta .b{{background:{G};color:{T};font-weight:800;font-size:28px;padding:16px 34px;border-radius:50px;letter-spacing:1px}}
.cta .k{{font-size:19px;font-weight:600;line-height:1.6}}.cta .k b{{color:{G}}}
.disc{{position:absolute;left:52px;right:52px;bottom:16px;font-size:11px;color:#8a9aa3;text-align:center}}
</style></head><body>
<div class="ban"><img class="logo" src="{LOGO}">
<div class="hd"><div class="kick">Digital SAT бэлтгэл</div><h1>Канадаас,<br><em>онлайнаар</em></h1>
<div class="lead">Хичээл бүр Монголын цагаар орой <span style="white-space:nowrap">20:00 - 21:20</span>.<br>Англи, Монгол хэлээр.</div>
<div class="res"><div class="big">1560</div><div class="t"><b>Сурагчийн оноо · 2026 оны 5-р сар</b>Унших, бичих 770 · Математик 790<br>Дээд оноо 1600</div></div></div>
<div class="who"><h2>Жаргалмаа Амгалан</h2><div class="r">Математикийн багш · 2010 оноос · Цогц сургалтын төв</div></div>
</div>
<div class="body">
<div class="st">Долоо хоногийн хуваарь</div>
<div class="sub">Монголын цагаар <b>20:00 - 21:20</b></div>
<div class="wk">{grid}</div>
<div class="fl">{feats}</div>
<div class="cta"><div class="k"><b>globalmathprep.academy</b><br>WhatsApp +1 428 880 1826</div><div class="b">ЭЛСЭЛТ НЭЭЛТТЭЙ →</div></div>
</div>
<div class="disc">SAT® is a trademark registered by the College Board, which is not affiliated with, and does not endorse, this content.</div>
</body></html>'''
open('/home/claude/preview/promo3.html', 'w').write(HTML)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1350})
    pg.goto('file:///home/claude/preview/promo3.html'); pg.wait_for_timeout(300)
    pg.screenshot(path='/home/claude/preview/promo3.png'); b.close()
print('ok')
