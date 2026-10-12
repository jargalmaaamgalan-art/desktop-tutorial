"""GMP ad v8: HubSpot diagonal block + NBCC tag and strip."""
import base64, sys
sys.argv = [sys.argv[0]]
from gen41 import F
from PIL import Image
from playwright.sync_api import sync_playwright

T, G, CREAM = '#1b3b48', '#f3b045', '#f6f1e7'
src = Image.open('/root/.claude/uploads/7b9b247d-7185-5faa-ae2d-e13a2742cc61/b972ed30-image.jpg')
from PIL import ImageEnhance
im = src.crop((0, 700, 1230, 1700)).resize((1080, 878), Image.LANCZOS)
im = ImageEnhance.Contrast(im).enhance(1.08); im = ImageEnhance.Color(im).enhance(0.92)
im.save('/home/claude/preview/jg-v8.jpg', quality=94)
Image.open('/home/claude/desktop-tutorial/tools/v2/logo_left_dark.png').crop((0, 0, 430, 86)).save('/home/claude/preview/gmp-logo-dark.png')
PHOTO = 'data:image/jpeg;base64,' + base64.b64encode(open('/home/claude/preview/jg-v8.jpg', 'rb').read()).decode()
LOGO = 'data:image/png;base64,' + base64.b64encode(open('/home/claude/preview/gmp-logo-dark.png', 'rb').read()).decode()

HTML = f'''<!doctype html><html><head><meta charset="utf-8"><style>
{F('CG', 'cormorant-garamond', [600])}{F('OS', 'oswald', [500])}{F('IN', 'inter', [400, 600, 800])}
*{{box-sizing:border-box;margin:0}}
body{{width:1080px;height:1350px;font-family:IN,sans-serif;color:{T};overflow:hidden;position:relative;background:{CREAM}}}
.ph{{position:absolute;left:0;top:0;width:1080px;height:880px;background:url({PHOTO}) center top/cover}}
.ph:after{{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(14,36,46,.35),rgba(14,36,46,0) 30%)}}
.gold{{position:absolute;left:0;top:640px;width:1080px;height:600px;background:{G};clip-path:polygon(0 110px,1080px 0,1080px 12px,0 122px)}}
.tag{{position:absolute;right:48px;top:48px;background:#fff;color:{T};font-family:OS,sans-serif;font-weight:500;font-size:23px;letter-spacing:3px;padding:10px 20px 10px 16px;text-transform:uppercase;display:flex;align-items:center;gap:12px}}.tag:before{{content:'';width:12px;height:12px;border-radius:50%;background:{G}}}
.blk{{position:absolute;left:0;top:640px;width:1080px;height:600px;background:{CREAM};clip-path:polygon(0 122px,1080px 12px,1080px 100%,0 100%)}}
h1{{position:absolute;left:56px;top:776px;font-family:CG,serif;font-weight:600;font-size:84px;line-height:1.0;color:{T};letter-spacing:-.5px}}
.sub{{position:absolute;left:58px;top:1064px;font-size:22px;color:#55707c;font-weight:500;letter-spacing:.2px}}
.row{{position:absolute;left:56px;right:56px;top:1128px;display:flex;align-items:center;justify-content:space-between}}
.row img{{height:86px}}
.btn{{background:{G};color:{T};font-weight:800;font-size:28px;padding:22px 44px;border-radius:12px;box-shadow:0 6px 18px rgba(243,176,69,.35)}}
.strip{{position:absolute;left:0;right:0;bottom:0;height:96px;background:{T};color:#fff;display:flex;align-items:center;justify-content:center;font-family:OS,sans-serif;font-weight:500;font-size:23px;letter-spacing:1.5px;text-transform:uppercase;white-space:nowrap}}
.strip i{{width:1.5px;height:36px;background:rgba(255,255,255,.35);margin:0 26px}}
.disc{{position:absolute;left:0;right:0;bottom:104px;text-align:center;font-size:10.5px;color:#9aa9b0}}
</style></head><body>
<div class="ph"></div>
<div class="tag">Элсэлт нээлттэй</div>
<div class="gold"></div><div class="blk"></div>
<h1>Digital SAT бэлтгэл<br>Канадаас шууд<br>онлайнаар</h1>
<div class="sub">15 жилийн туршлагатай багш · Цөөн сурагчтай бүлэг · Англи, Монгол хэлээр</div>
<div class="row"><img src="{LOGO}"><div class="btn">Бүртгүүлэх →</div></div>
<div class="disc">SAT® is a trademark registered by the College Board, which is not affiliated with, and does not endorse, this content.</div>
<div class="strip">Математик Да · Лх · Ба<i></i>Англи хэл Мя · Пү · Ня<i></i>Монголын цагаар 20:00 - 21:20</div>
</body></html>'''
open('/home/claude/preview/promo8.html', 'w').write(HTML)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1350})
    pg.goto('file:///home/claude/preview/promo8.html'); pg.wait_for_timeout(300)
    pg.screenshot(path='/home/claude/preview/promo8.png'); b.close()
print('ok')
