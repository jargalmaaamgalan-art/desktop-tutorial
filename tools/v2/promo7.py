"""GMP ad v7: NBCC-style. Photo, big stat block on the right, label boxes, teal info strip."""
import base64, sys
sys.argv = [sys.argv[0]]
from gen41 import F
from PIL import Image
from playwright.sync_api import sync_playwright

T, G = '#1b3b48', '#f3b045'
src = Image.open('/root/.claude/uploads/7b9b247d-7185-5faa-ae2d-e13a2742cc61/b972ed30-image.jpg')
src.crop((0, 520, 1400, 2000)).resize((1080, 1142), Image.LANCZOS).save('/home/claude/preview/jg-v7.jpg', quality=93)
PHOTO = 'data:image/jpeg;base64,' + base64.b64encode(open('/home/claude/preview/jg-v7.jpg', 'rb').read()).decode()
LOGO = 'data:image/png;base64,' + base64.b64encode(open('/home/claude/preview/gmp-logo.png', 'rb').read()).decode()

HTML = f'''<!doctype html><html><head><meta charset="utf-8"><style>
{F('OS', 'oswald', [500, 700])}{F('IN', 'inter', [400, 600, 800])}
*{{box-sizing:border-box;margin:0}}
body{{width:1080px;height:1350px;font-family:OS,sans-serif;color:#fff;overflow:hidden;position:relative;background:{T}}}
.ph{{position:absolute;left:0;top:0;width:1080px;height:1240px;background:url({PHOTO}) center top/cover}}
.ph:after{{content:'';position:absolute;inset:0;background:linear-gradient(90deg,rgba(14,36,46,0) 40%,rgba(14,36,46,.8) 58%,rgba(14,36,46,.92) 100%)}}
.tag{{position:absolute;right:48px;top:48px;background:#fff;color:{T};font-weight:700;font-size:24px;letter-spacing:3px;padding:10px 20px;text-transform:uppercase}}
.blk{{position:absolute;left:560px;right:48px;top:250px}}
.blk img{{height:96px;margin-left:-4px}}
.stat{{font-weight:700;font-size:250px;line-height:.9;letter-spacing:-6px;margin-top:10px}}.stat small{{font-size:110px;letter-spacing:0;vertical-align:baseline;margin-left:6px}}
.sl{{font-weight:500;font-size:34px;line-height:1.15;margin-top:12px;max-width:440px}}
.box{{display:inline-block;background:#fff;color:{T};font-weight:700;font-size:28px;padding:12px 18px;margin-top:22px;line-height:1.2}}
.who{{position:absolute;left:48px;bottom:140px;font-family:IN,sans-serif}}
.who b{{display:block;font-size:30px;font-weight:800;text-shadow:0 2px 10px rgba(0,0,0,.6)}}.who span{{font-size:16px;color:{G};font-weight:600;letter-spacing:1.5px;text-transform:uppercase}}
.strip{{position:absolute;left:0;right:0;bottom:0;height:110px;background:#0f6b88;display:flex;align-items:center;justify-content:center;font-weight:500;font-size:24px;letter-spacing:1.5px;text-transform:uppercase;white-space:nowrap}}
.strip i{{font-style:normal;width:2px;height:44px;background:rgba(255,255,255,.55);margin:0 22px}}
.disc{{position:absolute;left:0;right:0;bottom:112px;text-align:center;font-family:IN,sans-serif;font-size:10.5px;color:#b8cbd5;background:rgba(14,36,46,.6);padding:5px 0}}
</style></head><body>
<div class="ph"></div>
<div class="tag">Элсэлт нээлттэй</div>
<div class="blk"><img src="{LOGO}">
<div class="stat">15<small>+</small></div>
<div class="sl">жилийн математикийн багшийн туршлага.</div>
<div class="box">Digital SAT бэлтгэл Канадаас шууд онлайнаар.</div></div>
<div class="who"><b>Жаргалмаа Амгалан</b><span>Математикийн багш</span></div>
<div class="disc">SAT® is a trademark registered by the College Board, which is not affiliated with, and does not endorse, this content.</div>
<div class="strip">Бүртгүүлэх<i></i>Монголын цагаар 20:00 - 21:20<i></i>WhatsApp +1 428 880 1826</div>
</body></html>'''
open('/home/claude/preview/promo7.html', 'w').write(HTML)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1350})
    pg.goto('file:///home/claude/preview/promo7.html'); pg.wait_for_timeout(300)
    pg.screenshot(path='/home/claude/preview/promo7.png'); b.close()
print('ok')
