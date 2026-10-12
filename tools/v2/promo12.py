"""GMP ad v12: premium duotone portrait, one idea, restraint."""
import base64, sys
sys.argv = [sys.argv[0]]
from gen41 import F
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
from playwright.sync_api import sync_playwright

T, G, CREAM = '#1b3b48', '#f3b045', '#f6f1e7'
src = Image.open('/root/.claude/uploads/7b9b247d-7185-5faa-ae2d-e13a2742cc61/b972ed30-image.jpg')
im = src.crop((420, 560, 1500, 1910)).resize((1080, 1350), Image.LANCZOS)
g = ImageOps.grayscale(im)
g = ImageEnhance.Contrast(g).enhance(1.25)
duo = ImageOps.colorize(g, black=(8, 26, 36), mid=(34, 74, 90), white=(246, 238, 220), midpoint=118)
duo = duo.filter(ImageFilter.GaussianBlur(1.5)); duo.save('/home/claude/preview/jg-duo.jpg', quality=94)
CUT = 'data:image/png;base64,' + base64.b64encode(open('/home/claude/preview/jg-cut2.png', 'rb').read()).decode()
PHOTO = 'data:image/jpeg;base64,' + base64.b64encode(open('/home/claude/preview/jg-duo.jpg', 'rb').read()).decode()
LOGO = 'data:image/png;base64,' + base64.b64encode(open('/home/claude/preview/gmp-logo.png', 'rb').read()).decode()

HTML = f'''<!doctype html><html><head><meta charset="utf-8"><style>
{F('SS', 'source-serif-4', [600, 800])}{F('IN', 'inter', [400, 600, 800])}
*{{box-sizing:border-box;margin:0}}
body{{width:1080px;height:1350px;font-family:IN,sans-serif;color:#fff;overflow:hidden;position:relative;background:{T} url({PHOTO}) center/cover}}
.veil{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,30,40,.5) 0,rgba(10,30,40,0) 22%,rgba(10,30,40,0) 50%,rgba(10,30,40,.85) 74%,rgba(10,30,40,.97) 100%),linear-gradient(90deg,rgba(10,30,40,.8) 0,rgba(10,30,40,.45) 45%,rgba(10,30,40,.1) 70%)}}
.logo{{position:absolute;left:64px;top:56px;height:84px}}
.cut{{position:absolute;right:0px;bottom:120px;width:560px;filter:drop-shadow(0 30px 40px rgba(0,0,0,.6))}}
.tag{{position:absolute;right:64px;top:64px;color:{G};font-weight:800;font-size:16px;letter-spacing:4px;text-transform:uppercase;border-bottom:2px solid {G};padding-bottom:8px}}
.blk{{position:absolute;left:64px;width:520px;bottom:150px}}
.h0{{font-family:SS,serif;font-weight:800;font-size:104px;line-height:.95;color:{G};letter-spacing:-3px}}
h1{{font-family:SS,serif;font-weight:600;font-size:36px;line-height:1.2;margin-top:18px}}
.sub{{font-size:19px;color:#cfdde4;margin-top:16px;line-height:1.55}}
.row{{display:flex;align-items:center;gap:22px;margin-top:28px;flex-wrap:wrap}}
.btn{{background:{G};color:{T};font-weight:800;font-size:22px;padding:18px 30px;border-radius:50px}}
.hint{{font-size:18px;color:#9fb6c2}}
.foot{{position:absolute;left:64px;right:64px;bottom:60px;display:flex;justify-content:space-between;font-size:17px;letter-spacing:2px;text-transform:uppercase;color:#9fb6c2;font-weight:600;border-top:1px solid rgba(255,255,255,.18);padding-top:22px}}
.foot b{{color:#fff}}
.disc{{position:absolute;left:64px;right:64px;bottom:22px;font-size:10px;color:#6f8793}}
</style></head><body><div class="veil"></div>
<img class="cut" src="{CUT}"><img class="logo" src="{LOGO}">
<div class="tag">Элсэлт нээлттэй</div>
<div class="blk">
<div class="h0">Канадаас<br>шууд.</div>
<h1>Digital SAT Math + English,<br>нэг багштай, нэг дор.</h1>
<div class="sub">15 жилийн туршлагатай багш<br>College Board-ийн асуултууд<br>Долоо хоног бүр ахицын тайлан</div>
<div class="row"><div class="btn">Үнэгүй SAT тест авах →</div></div><div class="hint" style="margin-top:12px">"SAT" гэж коммент бичээрэй</div>
</div>
<div class="foot"><span><b>Математик</b> Да · Лх · Ба</span><span><b>Англи хэл</b> Мя · Пү · Ня</span><span><b>20:00 - 21:20</b> Монголын цагаар</span></div>
<div class="disc">SAT® is a trademark registered by the College Board, which is not affiliated with, and does not endorse, this content.</div>
</body></html>'''
open('/home/claude/preview/promo12.html', 'w').write(HTML)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1350})
    pg.goto('file:///home/claude/preview/promo12.html'); pg.wait_for_timeout(300)
    pg.screenshot(path='/home/claude/preview/promo12.png'); b.close()
print('ok')
