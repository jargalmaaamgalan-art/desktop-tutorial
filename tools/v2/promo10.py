"""GMP ad v9: magazine cover. Cut-out teacher in front of giant 'SAT' type, flat teal, gold accents."""
import base64, sys
sys.argv = [sys.argv[0]]
from gen41 import F
from playwright.sync_api import sync_playwright

T, T2, G, CREAM = '#1b3b48', '#0e2832', '#f3b045', '#f6f1e7'
CUT = 'data:image/png;base64,' + base64.b64encode(open('/home/claude/preview/jg-cut2.png', 'rb').read()).decode()
LOGO = 'data:image/png;base64,' + base64.b64encode(open('/home/claude/preview/gmp-logo.png', 'rb').read()).decode()

HTML = f'''<!doctype html><html><head><meta charset="utf-8"><style>
{F('SS', 'source-serif-4', [600, 800])}{F('IN', 'inter', [400, 600, 800])}{F('OS', 'oswald', [500])}
*{{box-sizing:border-box;margin:0}}
body{{width:1080px;height:1350px;font-family:IN,sans-serif;color:#fff;overflow:hidden;position:relative;background:radial-gradient(900px 700px at 30% 85%,#24505f 0,{T} 45%,{T2} 100%)}}
.grid{{display:none}}
.logo{{position:absolute;left:48px;top:40px;height:96px}}
.tag{{position:absolute;right:48px;top:52px;border:2px solid {G};color:{G};font-family:OS,sans-serif;font-size:21px;letter-spacing:3px;padding:9px 18px;text-transform:uppercase;border-radius:50px}}
.big{{position:absolute;left:0;right:0;top:250px;text-align:center;font-family:SS,serif;font-weight:800;font-size:470px;line-height:.8;letter-spacing:-10px;color:{G}}}
.big b{{color:{G}}}
.cut{{position:absolute;left:40px;bottom:130px;width:560px;filter:drop-shadow(0 24px 30px rgba(0,0,0,.6)) drop-shadow(-6px 0 0 rgba(120,190,220,.0))}}
.floor{{position:absolute;left:60px;bottom:120px;width:540px;height:40px;border-radius:50%;background:radial-gradient(closest-side,rgba(0,0,0,.55),rgba(0,0,0,0))}}
.col{{position:absolute;right:48px;top:660px;width:470px}}
.kick{{color:{G};font-weight:800;font-size:17px;letter-spacing:3px;text-transform:uppercase;white-space:nowrap}}
h1{{font-family:SS,serif;font-weight:600;font-size:42px;line-height:1.1;margin:12px 0 16px;white-space:nowrap}}
.chips{{display:flex;flex-direction:column;gap:10px;margin:6px 0 4px}}.ch{{display:flex;align-items:center;gap:12px;font-size:19px;color:#dbe6ec;line-height:1.25}}.ch i{{flex:none;font-style:normal;font-family:SS,serif;font-weight:800;font-size:20px;color:{G};width:54px;height:54px;border:2px solid rgba(243,176,69,.6);border-radius:50%;display:flex;align-items:center;justify-content:center}}.hint{{margin-top:10px;font-size:16px;color:#9fb6c2}}
.btn{{display:inline-block;margin-top:18px;background:{G};color:{T};font-weight:800;font-size:24px;padding:18px 32px;border-radius:50px}}
.strip{{position:absolute;left:0;right:0;bottom:0;height:130px;background:{CREAM};color:{T};display:flex;align-items:center;justify-content:space-around;padding:0 40px 14px}}
.s{{text-align:center}}.s b{{display:block;font-family:SS,serif;font-size:34px;font-weight:800;line-height:1}}.s span{{font-family:OS,sans-serif;font-size:17px;letter-spacing:2.5px;text-transform:uppercase;color:#55707c}}
.sep{{width:1.5px;height:70px;background:#d9cdb6}}
.who{{display:none}}
.who b{{display:block;font-size:24px;font-weight:800}}.who span{{font-size:14px;color:{G};letter-spacing:1.5px;text-transform:uppercase;font-weight:600}}
.disc{{position:absolute;left:0;right:0;bottom:6px;text-align:center;font-size:10px;color:#8a9aa3;z-index:2}}
</style></head><body><div class="grid"></div>
<img class="logo" src="{LOGO}">
<div class="tag">Элсэлт нээлттэй</div>
<div class="big">S<b>A</b>T</div>
<div class="floor"></div><img class="cut" src="{CUT}">
<div class="col"><div class="kick">Digital SAT · Канадаас онлайн</div>
<h1>Math + English<br>нэг багштай, нэг дор.</h1>
<div class="chips"><div class="ch"><i>15+</i>жилийн багшлах туршлага</div><div class="ch"><i>CB</i>College Board-ийн албан ёсны асуултууд</div><div class="ch"><i>7</i>хоног бүр ахицын тайлан эцэг эхэд</div></div>
<div class="btn">Үнэгүй SAT тест авах →</div><div class="hint">"SAT" гэж коммент бичээрэй</div></div>
<div class="who"><b>Жаргалмаа Амгалан</b><span>Математикийн багш</span></div>
<div class="disc">SAT® is a trademark registered by the College Board, which is not affiliated with, and does not endorse, this content.</div>
<div class="strip"><div class="s"><b>Да · Лх · Ба</b><span>Математик</span></div><div class="sep"></div><div class="s"><b>Мя · Пү · Ня</b><span>Англи хэл</span></div><div class="sep"></div><div class="s"><b>20:00 - 21:20</b><span>Монголын цагаар</span></div></div>
</body></html>'''
open('/home/claude/preview/promo10.html', 'w').write(HTML)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1350})
    pg.goto('file:///home/claude/preview/promo10.html'); pg.wait_for_timeout(300)
    pg.screenshot(path='/home/claude/preview/promo10.png'); b.close()
print('ok')
