"""GMP ad v5: HubSpot-Academy style. Photo top, calm block below with one serif headline, logo left, button right."""
import base64, sys
sys.argv = [sys.argv[0]]
from gen41 import F
from PIL import Image
from playwright.sync_api import sync_playwright

T, G, CREAM = '#1b3b48', '#f3b045', '#f6f1e7'
src = Image.open('/root/.claude/uploads/7b9b247d-7185-5faa-ae2d-e13a2742cc61/b972ed30-image.jpg')
src.crop((0, 640, 1500, 1690)).resize((1080, 756), Image.LANCZOS).save('/home/claude/preview/jg-top.jpg', quality=93)
Image.open('/home/claude/desktop-tutorial/tools/v2/logo_left_dark.png').crop((0, 0, 430, 86)).save('/home/claude/preview/gmp-logo-dark.png')
PHOTO = 'data:image/jpeg;base64,' + base64.b64encode(open('/home/claude/preview/jg-top.jpg', 'rb').read()).decode()
LOGO = 'data:image/png;base64,' + base64.b64encode(open('/home/claude/preview/gmp-logo-dark.png', 'rb').read()).decode()

HTML = f'''<!doctype html><html><head><meta charset="utf-8"><style>
{F('CG', 'cormorant-garamond', [600, 700])}{F('IN', 'inter', [400, 600, 800])}
*{{box-sizing:border-box;margin:0}}
body{{width:1080px;height:1350px;font-family:IN,sans-serif;color:{T};background:{CREAM};overflow:hidden;position:relative}}
.ph{{height:740px;background:url({PHOTO}) center/cover}}
.blk{{padding:56px 70px 0}}
.eye{{color:#b47d1f;font-weight:800;font-size:19px;letter-spacing:3px;text-transform:uppercase;margin-bottom:16px}}
h1{{font-family:CG,serif;font-weight:600;font-size:63px;line-height:1.1;letter-spacing:1px;text-transform:uppercase}}
.sub{{font-size:25px;color:#35505c;margin-top:22px;font-weight:500;line-height:1.55}}.sub b{{color:{T};font-weight:800}}
.row{{position:absolute;left:70px;right:70px;bottom:66px;display:flex;align-items:center;justify-content:space-between}}
.row img{{height:110px}}
.btn{{background:{G};color:{T};font-weight:800;font-size:27px;padding:22px 40px;border-radius:12px}}
.disc{{position:absolute;left:0;right:0;bottom:16px;text-align:center;font-size:11px;color:#7d8f99}}
</style></head><body>
<div class="ph"></div>
<div class="blk"><div class="eye">Элсэлт нээлттэй · 2026 оны намар</div><h1>Digital SAT бэлтгэл,<br>Канадаас шууд онлайнаар.</h1>
<div class="sub"><b>Математик</b> Да · Лх · Ба &nbsp;&nbsp;<b>Англи хэл</b> Мя · Пү · Ня<br>Монголын цагаар 20:00 - 21:20 · 15 жилийн туршлагатай багш</div></div>
<div class="row"><img src="{LOGO}"><div class="btn">Бүртгүүлэх →</div></div>
<div class="disc">globalmathprep.academy · WhatsApp +1 428 880 1826 · SAT® is a trademark registered by the College Board, which is not affiliated with, and does not endorse, this content.</div>
</body></html>'''
open('/home/claude/preview/promo5.html', 'w').write(HTML)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1350})
    pg.goto('file:///home/claude/preview/promo5.html'); pg.wait_for_timeout(300)
    pg.screenshot(path='/home/claude/preview/promo5.png'); b.close()
print('ok')
