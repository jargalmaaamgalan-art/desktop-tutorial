"""GMP ad v9: magazine cover. Cut-out teacher in front of giant 'SAT' type, flat teal, gold accents."""
import base64, sys
sys.argv = [sys.argv[0]]
from gen41 import F
from playwright.sync_api import sync_playwright

T, T2, G, CREAM = '#1b3b48', '#0e2832', '#f3b045', '#f6f1e7'
CUT = 'data:image/png;base64,' + base64.b64encode(open('/home/claude/preview/jg-cut.png', 'rb').read()).decode()
LOGO = 'data:image/png;base64,' + base64.b64encode(open('/home/claude/preview/gmp-logo.png', 'rb').read()).decode()

HTML = f'''<!doctype html><html><head><meta charset="utf-8"><style>
{F('SS', 'source-serif-4', [600, 800])}{F('IN', 'inter', [400, 600, 800])}{F('OS', 'oswald', [500])}
*{{box-sizing:border-box;margin:0}}
body{{width:1080px;height:1350px;font-family:IN,sans-serif;color:#fff;overflow:hidden;position:relative;background:radial-gradient(900px 700px at 30% 85%,#24505f 0,{T} 45%,{T2} 100%)}}
.grid{{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.045) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.045) 1px,transparent 1px);background-size:60px 60px}}
.logo{{position:absolute;left:48px;top:40px;height:96px}}
.tag{{position:absolute;right:48px;top:52px;background:{G};color:{T};font-family:OS,sans-serif;font-size:22px;letter-spacing:3px;padding:10px 18px;text-transform:uppercase}}
.big{{position:absolute;left:40px;top:150px;font-family:SS,serif;font-weight:800;font-size:430px;line-height:.8;letter-spacing:-14px;color:transparent;-webkit-text-stroke:3px rgba(243,176,69,.55)}}
.big b{{color:{G};-webkit-text-stroke:0}}
.cut{{position:absolute;left:10px;bottom:150px;width:540px;filter:drop-shadow(0 30px 40px rgba(0,0,0,.55))}}
.col{{position:absolute;right:48px;top:560px;width:440px}}
.kick{{color:{G};font-weight:800;font-size:18px;letter-spacing:4px;text-transform:uppercase}}
h1{{font-family:SS,serif;font-weight:600;font-size:50px;line-height:1.1;margin:14px 0 18px}}
.pt{{font-size:22px;line-height:1.5;color:#cfdde4}}.pt b{{color:#fff;font-weight:800}}
.btn{{display:inline-block;margin-top:26px;background:{G};color:{T};font-weight:800;font-size:26px;padding:20px 38px;border-radius:50px}}
.strip{{position:absolute;left:0;right:0;bottom:0;height:150px;background:{CREAM};color:{T};display:flex;align-items:center;justify-content:space-around;padding:0 40px 14px}}
.s{{text-align:center}}.s b{{display:block;font-family:SS,serif;font-size:40px;font-weight:800;line-height:1}}.s span{{font-family:OS,sans-serif;font-size:17px;letter-spacing:2.5px;text-transform:uppercase;color:#55707c}}
.sep{{width:1.5px;height:70px;background:#d9cdb6}}
.who{{position:absolute;left:48px;bottom:166px;background:rgba(14,40,50,.85);border-left:5px solid {G};padding:10px 16px}}
.who b{{display:block;font-size:24px;font-weight:800}}.who span{{font-size:14px;color:{G};letter-spacing:1.5px;text-transform:uppercase;font-weight:600}}
.disc{{position:absolute;left:0;right:0;bottom:6px;text-align:center;font-size:10px;color:#8a9aa3;z-index:2}}
</style></head><body><div class="grid"></div>
<img class="logo" src="{LOGO}">
<div class="tag">Элсэлт нээлттэй</div>
<div class="big">S<b>A</b>T</div>
<img class="cut" src="{CUT}">
<div class="col"><div class="kick">Digital SAT · Онлайн</div>
<h1>Math + English багш, Канадаас шууд онлайнаар.</h1>
<div class="pt"><b>15 жилийн</b> туршлагатай багш<br><b>Цөөн сурагчтай</b> бүлэг<br>Англи, Монгол хэлээр</div>
<div class="btn">Бүртгүүлэх →</div></div>
<div class="who"><b>Жаргалмаа Амгалан</b><span>Математикийн багш</span></div>
<div class="disc">SAT® is a trademark registered by the College Board, which is not affiliated with, and does not endorse, this content.</div>
<div class="strip"><div class="s"><b>Да · Лх · Ба</b><span>Математик</span></div><div class="sep"></div><div class="s"><b>Мя · Пү · Ня</b><span>Англи хэл</span></div><div class="sep"></div><div class="s"><b>20:00 - 21:20</b><span>Монголын цагаар</span></div></div>
</body></html>'''
open('/home/claude/preview/promo9.html', 'w').write(HTML)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1350})
    pg.goto('file:///home/claude/preview/promo9.html'); pg.wait_for_timeout(300)
    pg.screenshot(path='/home/claude/preview/promo9.png'); b.close()
print('ok')
