"""GMP enrolment poster v2: full-bleed photo, editorial right column."""
import base64, sys
sys.argv = [sys.argv[0]]
from gen41 import F
from PIL import Image
from playwright.sync_api import sync_playwright

T, G, CREAM = '#1b3b48', '#f3b045', '#fff8ea'
src = Image.open('/root/.claude/uploads/7b9b247d-7185-5faa-ae2d-e13a2742cc61/b972ed30-image.jpg')
src.crop((0, 320, 1344, 2000)).resize((1080, 1350), Image.LANCZOS).save('/home/claude/preview/jg-bg.jpg', quality=92)
PHOTO = 'data:image/jpeg;base64,' + base64.b64encode(open('/home/claude/preview/jg-bg.jpg', 'rb').read()).decode()
LOGO = 'data:image/png;base64,' + base64.b64encode(open('/home/claude/preview/gmp-logo.png', 'rb').read()).decode()

CHK = f'<svg viewBox="0 0 24 24" width="26" height="26"><circle cx="12" cy="12" r="11" fill="{G}"/><path d="M7 12.5l3.2 3L17 9" fill="none" stroke="{T}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>'
FEATS = ['College Board-ийн албан ёсны асуултууд', 'Долоо хоног бүр ахицын тайлан эцэг эхэд', 'Цөөн сурагчтай бүлэг', 'Англи, Монгол хэлээр, Канадаас онлайнаар']
feats = ''.join(f'<li>{CHK}<span>{t}</span></li>' for t in FEATS)

HTML = f'''<!doctype html><html><head><meta charset="utf-8"><style>
{F('SS', 'source-serif-4', [700, 800])}{F('IN', 'inter', [400, 600, 800])}
*{{box-sizing:border-box;margin:0}}
body{{width:1080px;height:1350px;font-family:IN,sans-serif;color:#fff;overflow:hidden;position:relative;background:{T} url({PHOTO}) left top/cover no-repeat}}
.veil{{position:absolute;inset:0;background:linear-gradient(90deg,rgba(27,59,72,0) 30%,rgba(27,59,72,.86) 50%,rgba(27,59,72,.97) 62%),linear-gradient(180deg,rgba(27,59,72,.55) 0,rgba(27,59,72,0) 22%,rgba(27,59,72,0) 70%,rgba(27,59,72,.95) 88%)}}
.logo{{position:absolute;left:34px;top:30px;height:100px;background:rgba(27,59,72,.82);padding:10px 18px;border-radius:16px}}
.col{{position:absolute;right:48px;top:150px;width:520px}}
.kick{{color:{G};font-weight:800;font-size:19px;letter-spacing:4px;text-transform:uppercase}}
h1{{font-family:SS,serif;font-size:74px;font-weight:800;line-height:1.02;margin:10px 0 6px}}
h1 em{{font-style:normal;color:{G}}}
.lead{{font-size:22px;color:#cfdde4;line-height:1.35;margin-bottom:30px}}
.sch{{border-left:5px solid {G};padding-left:22px;display:flex;flex-direction:column;gap:22px;margin-bottom:32px}}
.sc .n{{font-family:SS,serif;font-size:40px;font-weight:800;line-height:1}}.sc .n b{{color:{G}}}
.sc .d{{display:flex;align-items:center;gap:10px;margin-top:8px;font-size:21px}}
.sc .d span{{background:{CREAM};color:{T};font-weight:800;font-size:18px;padding:4px 12px;border-radius:8px}}
.sc .d i{{font-style:normal;font-family:SS,serif;font-weight:800;color:{G};font-size:30px;margin-left:6px}}
.tz{{font-size:16px;color:#9fb6c2;margin-top:4px}}
.res{{display:flex;align-items:center;gap:20px;background:rgba(255,248,234,.08);border:1.5px solid rgba(243,176,69,.5);border-radius:18px;padding:16px 22px;margin-bottom:30px}}
.res .big{{font-family:SS,serif;font-size:76px;font-weight:800;color:{G};line-height:.95}}
.res .t{{font-size:17px;line-height:1.35;color:#dbe6ec}}.res .t b{{color:#fff;font-size:19px;display:block;margin-bottom:4px}}
ul{{list-style:none;display:flex;flex-direction:column;gap:12px;margin-bottom:34px}}
li{{display:flex;align-items:center;gap:12px;font-size:21px;font-weight:600}}
.cta{{display:inline-block;background:{G};color:{T};font-weight:800;font-size:30px;padding:20px 44px;border-radius:60px;letter-spacing:1px;box-shadow:0 8px 0 #b47d1f}}
.who{{position:absolute;left:40px;bottom:56px;width:470px}}
.who h2{{font-family:SS,serif;font-size:38px;font-weight:800;line-height:1.05}}
.who .r{{color:{G};font-weight:800;font-size:16px;letter-spacing:1.5px;margin:8px 0 8px;text-transform:uppercase}}
.who p{{font-size:17px;line-height:1.4;color:#cfdde4;max-width:430px}}
.foot{{position:absolute;right:48px;bottom:56px;text-align:right;font-size:19px;font-weight:600;line-height:1.7}}
.disc{{position:absolute;left:40px;right:48px;bottom:18px;font-size:11px;color:#8aa3b0;text-align:center}}
</style></head><body><div class="veil"></div>
<img class="logo" src="{LOGO}">
<div class="col">
<div class="kick">Digital SAT бэлтгэл</div>
<h1>Канадаас,<br><em>онлайнаар</em></h1>
<div class="lead">Хичээл бүр Монголын цагаар орой 20:00 - 21:20</div>
<div class="sch">
<div class="sc"><div class="n">SAT <b>Математик</b></div><div class="d"><span>Да</span><span>Лх</span><span>Ба</span></div></div>
<div class="sc"><div class="n">SAT <b>Англи хэл</b></div><div class="d"><span>Мя</span><span>Пү</span><span>Ня</span></div></div>
</div>
<div class="res"><div class="big">1560</div><div class="t"><b>Сурагчийн оноо · 2026 оны 5-р сар</b>Унших, бичих 770 · Математик 790 · Дээд оноо 1600</div></div>
<ul>{feats}</ul>
<div class="cta">ЭЛСЭЛТ НЭЭЛТТЭЙ →</div>
</div>
<div class="who"><h2>Жаргалмаа Амгалан</h2><div class="r">Математикийн багш · 2010 оноос</div><p>Цогц сургалтын төвийн багш. 2025 оноос хойш Канад улсаас онлайнаар хичээл зааж байна.</p></div>
<div class="foot">globalmathprep.academy<br>WhatsApp +1 428 880 1826</div>
<div class="disc">SAT® is a trademark registered by the College Board, which is not affiliated with, and does not endorse, this content.</div>
</body></html>'''
open('/home/claude/preview/promo2.html', 'w').write(HTML)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1350})
    pg.goto('file:///home/claude/preview/promo2.html'); pg.wait_for_timeout(300)
    pg.screenshot(path='/home/claude/preview/promo2.png'); b.close()
print('ok')
