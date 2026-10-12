"""GMP enrolment poster v4: conference-ad style (headline block, photo, info strip)."""
import base64, sys
sys.argv = [sys.argv[0]]
from gen41 import F
from PIL import Image
from playwright.sync_api import sync_playwright

T, G = '#1b3b48', '#f3b045'
src = Image.open('/root/.claude/uploads/7b9b247d-7185-5faa-ae2d-e13a2742cc61/b972ed30-image.jpg')
src.crop((0, 720, 1500, 1748)).resize((1080, 740), Image.LANCZOS).save('/home/claude/preview/jg-wide.jpg', quality=92)
PHOTO = 'data:image/jpeg;base64,' + base64.b64encode(open('/home/claude/preview/jg-wide.jpg', 'rb').read()).decode()
LOGO = 'data:image/png;base64,' + base64.b64encode(open('/home/claude/preview/gmp-logo.png', 'rb').read()).decode()

HTML = f'''<!doctype html><html><head><meta charset="utf-8"><style>
{F('IN', 'inter', [400, 600, 800])}
*{{box-sizing:border-box;margin:0}}
body{{width:1080px;height:1350px;font-family:IN,sans-serif;color:#fff;background:{T};overflow:hidden;position:relative}}
.top{{height:520px;background:linear-gradient(180deg,#0c2530 0%,#1b3b48 60%,#1f4556 100%);text-align:center;padding-top:44px;position:relative}}
.top img{{height:120px}}
.l1{{font-size:40px;font-weight:800;margin-top:30px;letter-spacing:-.3px}}
.l2{{font-size:104px;font-weight:800;color:{G};line-height:1.05;margin-top:8px;letter-spacing:-2px}}
.l3{{font-size:58px;font-weight:600;margin-top:4px;letter-spacing:-.5px}}
.ph{{height:700px;background:url({PHOTO}) center/cover;position:relative}}
.ph:before{{content:'';position:absolute;left:0;right:0;top:0;height:90px;background:linear-gradient(180deg,#1f4556,rgba(31,69,86,0))}}
.tag{{position:absolute;left:40px;bottom:34px;background:rgba(27,59,72,.9);padding:14px 22px;border-left:6px solid {G};border-radius:0 12px 12px 0}}
.tag b{{display:block;font-size:26px;font-weight:800}}.tag span{{font-size:16px;color:{G};font-weight:600;letter-spacing:1px;text-transform:uppercase}}
.strip{{height:90px;background:{G};color:{T};display:flex;align-items:center;justify-content:center;gap:0;font-size:26px;font-weight:800}}
.strip i{{font-style:normal;font-weight:400;opacity:.55;margin:0 14px;font-size:30px}}
.strip small{{font-weight:600;font-size:19px;margin-left:8px}}
.bar{{height:0}}
.disc{{height:40px;display:flex;align-items:center;justify-content:center;font-size:11px;color:#9fb6c2;background:#0c2530}}
</style></head><body>
<div class="top"><img src="{LOGO}">
<div class="l1">SAT Математик · SAT Англи хэл · Онлайн</div>
<div class="l2">Элсэлт нээлттэй!</div>
<div class="l3">Монголын цагаар 20:00 - 21:20</div></div>
<div class="ph"><div class="tag"><b>Жаргалмаа Амгалан</b><span>Математикийн багш · Канадаас онлайнаар</span></div></div>
<div class="strip">Да · Лх · Ба<small>Математик</small><i>|</i>Мя · Пү · Ня<small>Англи хэл</small><i>|</i>WhatsApp +1 428 880 1826</div>
<div class="disc">globalmathprep.academy · SAT® is a trademark registered by the College Board, which is not affiliated with, and does not endorse, this content.</div>
</body></html>'''
open('/home/claude/preview/promo4.html', 'w').write(HTML)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1350})
    pg.goto('file:///home/claude/preview/promo4.html'); pg.wait_for_timeout(300)
    pg.screenshot(path='/home/claude/preview/promo4.png'); b.close()
print('ok')
