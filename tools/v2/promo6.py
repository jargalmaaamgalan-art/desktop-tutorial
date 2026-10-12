"""GMP ad v6: Coursera-style. Full-bleed photo, teal logo on top, serif caps headline, white card, button."""
import base64, sys
sys.argv = [sys.argv[0]]
from gen41 import F
from PIL import Image
from playwright.sync_api import sync_playwright

T, G = '#1b3b48', '#f3b045'
src = Image.open('/root/.claude/uploads/7b9b247d-7185-5faa-ae2d-e13a2742cc61/b972ed30-image.jpg')
src.crop((0, 400, 1400, 2000)).resize((1080, 1234), Image.LANCZOS).save('/home/claude/preview/jg-full.jpg', quality=93)
PHOTO = 'data:image/jpeg;base64,' + base64.b64encode(open('/home/claude/preview/jg-full.jpg', 'rb').read()).decode()
LOGO = 'data:image/png;base64,' + base64.b64encode(open('/home/claude/preview/gmp-round.png', 'rb').read()).decode()

HTML = f'''<!doctype html><html><head><meta charset="utf-8"><style>
{F('CG', 'cormorant-garamond', [600, 700])}{F('IN', 'inter', [400, 600, 800])}
*{{box-sizing:border-box;margin:0}}
body{{width:1080px;height:1350px;font-family:IN,sans-serif;color:#fff;overflow:hidden;position:relative;background:{T} url({PHOTO}) center bottom/cover no-repeat}}
.veil{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(14,36,46,.96) 0,rgba(14,36,46,.9) 34%,rgba(14,36,46,.55) 44%,rgba(27,59,72,0) 56%,rgba(27,59,72,0) 72%,rgba(14,36,46,.95) 100%)}}
.lg{{position:absolute;left:0;right:0;top:36px;text-align:center}}.lg img{{height:190px;filter:drop-shadow(0 6px 16px rgba(0,0,0,.35))}}.lg .n{{font-family:CG,serif;font-weight:700;font-size:38px;letter-spacing:5px;margin-top:8px}}
.hd{{position:absolute;left:60px;right:60px;top:300px;text-align:center}}
.kick{{font-family:CG,serif;font-weight:700;font-size:52px;color:{G};letter-spacing:1px}}
h1{{font-family:CG,serif;font-weight:700;font-size:92px;line-height:1.02;letter-spacing:2px;text-transform:uppercase;margin-top:6px;text-shadow:0 3px 6px rgba(0,0,0,.5),0 10px 40px rgba(0,0,0,.5)}}
.card{{position:absolute;right:56px;bottom:200px;width:540px;background:#fff;color:{T};border-radius:22px;padding:24px 30px;box-shadow:0 10px 0 {G}}}
.card .t{{font-family:CG,serif;font-weight:700;font-size:42px;line-height:1.1;margin-bottom:10px}}
.card .l{{font-size:25px;line-height:1.5;color:{T};font-weight:500}}.card .l b{{color:{T};font-weight:800}}
.row{{position:absolute;left:56px;right:56px;bottom:62px;display:flex;align-items:flex-end;justify-content:space-between}}
.who b{{display:block;font-size:34px;font-weight:800;text-shadow:0 2px 8px rgba(0,0,0,.5)}}.who span{{font-size:18px;color:{G};font-weight:600;letter-spacing:1.5px;text-transform:uppercase}}
.btn{{background:{G};color:{T};font-weight:800;font-size:30px;padding:22px 44px;border-radius:50px}}
.disc{{position:absolute;left:0;right:0;bottom:14px;text-align:center;font-size:10.5px;color:#9fb6c2}}
</style></head><body><div class="veil"></div>
<div class="lg"><img src="{LOGO}"><div class="n">GLOBAL MATH PREP</div></div>
<div class="hd"><div class="kick">Digital SAT бэлтгэл</div><h1>Канадаас<br>шууд онлайнаар</h1></div>
<div class="card"><div class="t">Элсэлт нээлттэй</div>
<div class="l"><b>Математик</b> · Да, Лх, Ба<br><b>Англи хэл</b> · Мя, Пү, Ня<br>Монголын цагаар 20:00 - 21:20</div></div>
<div class="row"><div class="who"><b>Жаргалмаа Амгалан</b><span>Математикийн багш · 15 жилийн туршлага</span></div><div class="btn">Бүртгүүлэх →</div></div>
<div class="disc">globalmathprep.academy · WhatsApp +1 428 880 1826 · SAT® is a trademark registered by the College Board, which is not affiliated with, and does not endorse, this content.</div>
</body></html>'''
open('/home/claude/preview/promo6.html', 'w').write(HTML)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1350})
    pg.goto('file:///home/claude/preview/promo6.html'); pg.wait_for_timeout(300)
    pg.screenshot(path='/home/claude/preview/promo6.png'); b.close()
print('ok')
