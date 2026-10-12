"""GMP ad v11: strictly organized. 64px margins, straight split, every element on the same left edge."""
import base64, sys
sys.argv = [sys.argv[0]]
from gen41 import F
from PIL import Image, ImageEnhance
from playwright.sync_api import sync_playwright

T, G, CREAM = '#1b3b48', '#f3b045', '#f6f1e7'
M = 64
src = Image.open('/root/.claude/uploads/7b9b247d-7185-5faa-ae2d-e13a2742cc61/b972ed30-image.jpg')
im = src.crop((0, 640, 1380, 1640)).resize((1080, 783), Image.LANCZOS)
im = ImageEnhance.Contrast(im).enhance(1.06); im = ImageEnhance.Color(im).enhance(0.9)
im.save('/home/claude/preview/jg-v11.jpg', quality=94)
Image.open('/home/claude/desktop-tutorial/tools/v2/logo_left_dark.png').crop((0, 0, 430, 86)).save('/home/claude/preview/gmp-logo-dark.png')
PHOTO = 'data:image/jpeg;base64,' + base64.b64encode(open('/home/claude/preview/jg-v11.jpg', 'rb').read()).decode()
LOGO = 'data:image/png;base64,' + base64.b64encode(open('/home/claude/preview/gmp-logo-dark.png', 'rb').read()).decode()

HTML = f'''<!doctype html><html><head><meta charset="utf-8"><style>
{F('SS', 'source-serif-4', [600])}{F('IN', 'inter', [400, 600, 800])}
*{{box-sizing:border-box;margin:0}}
body{{width:1080px;height:1350px;font-family:IN,sans-serif;color:{T};overflow:hidden;position:relative;background:{CREAM}}}
.ph{{position:absolute;left:0;top:0;width:1080px;height:780px;background:url({PHOTO}) center top/cover}}
.ph:after{{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(14,36,46,.45),rgba(14,36,46,0) 26%)}}
.tag{{position:absolute;right:{M}px;top:{M}px;background:#fff;color:{T};font-weight:800;font-size:18px;letter-spacing:3px;padding:12px 18px;text-transform:uppercase;border-radius:6px}}
.blk{{position:absolute;left:{M}px;right:{M}px;top:780px;bottom:112px;display:flex;flex-direction:column;justify-content:center;gap:0}}
.kick{{color:#b47d1f;font-weight:800;font-size:17px;letter-spacing:3px;text-transform:uppercase;margin-bottom:14px}}
h1{{font-family:SS,serif;font-weight:600;font-size:66px;line-height:1.06;letter-spacing:-.5px}}
.sub{{font-size:22px;line-height:1.5;color:#4a6572;margin-top:18px}}
.row{{display:flex;align-items:center;justify-content:space-between;margin-top:34px}}
.row img{{height:76px;margin-left:-8px}}
.btn{{background:{G};color:{T};font-weight:800;font-size:24px;padding:20px 36px;border-radius:10px}}
.strip{{position:absolute;left:0;right:0;bottom:0;height:112px;background:{T};color:#fff;display:grid;grid-template-columns:1fr 1fr 1fr;align-items:center;padding:0 {M}px}}
.c{{display:flex;flex-direction:column;gap:4px;border-left:1px solid rgba(255,255,255,.18);padding-left:20px}}.c:first-child{{border:0;padding-left:0}}
.c b{{font-family:SS,serif;font-size:28px;font-weight:600;line-height:1}}.c span{{font-size:13px;letter-spacing:2px;text-transform:uppercase;color:#9fb6c2;font-weight:600}}
.disc{{position:absolute;left:{M}px;right:{M}px;bottom:122px;font-size:10px;color:#9aa9b0}}
</style></head><body>
<div class="ph"></div>
<div class="tag">Элсэлт нээлттэй</div>
<div class="blk">
<div class="kick">Digital SAT · Канадаас онлайнаар</div>
<h1>Math + English,<br>нэг багштай, нэг дор.</h1>
<div class="sub">15 жилийн туршлагатай багш · College Board-ийн асуултууд · Долоо хоног бүр тайлан</div>
<div class="row"><img src="{LOGO}"><div class="btn">Үнэгүй SAT тест авах →</div></div>
</div>
<div class="disc">SAT® is a trademark registered by the College Board, which is not affiliated with, and does not endorse, this content.</div>
<div class="strip"><div class="c"><b>Да · Лх · Ба</b><span>Математик</span></div><div class="c"><b>Мя · Пү · Ня</b><span>Англи хэл</span></div><div class="c"><b>20:00 - 21:20</b><span>Монголын цагаар</span></div></div>
</body></html>'''
open('/home/claude/preview/promo11.html', 'w').write(HTML)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1350})
    pg.goto('file:///home/claude/preview/promo11.html'); pg.wait_for_timeout(300)
    pg.screenshot(path='/home/claude/preview/promo11.png'); b.close()
print('ok')
