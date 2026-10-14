"""GMP math Reel in the 'paper + zoom + arrow + handwriting' style. 1080x1920, 10 s, 30 fps."""
import base64, os, subprocess, sys, shutil
sys.path.insert(0, '/home/claude/desktop-tutorial/tools/v2')
sys.argv = [sys.argv[0]] + sys.argv[1:]
from gen41 import F
from playwright.sync_api import sync_playwright

D = '/home/claude/mascot'
def b(f): return 'data:image/png;base64,' + base64.b64encode(open(f, 'rb').read()).decode()
ROUND = b(f'{D}/gmp-round.png')
DUR = 10

HTML = f'''<!doctype html><html><head><meta charset="utf-8"><style>
{F('C', 'caveat', [700])}{F('N', 'nunito', [800, 900])}{F('S', 'source-serif-4', [600, 700])}
*{{box-sizing:border-box;margin:0}}
body{{width:1080px;height:1920px;overflow:hidden;position:relative;background:#eeece6}}
.paper{{position:absolute;inset:0;background:#f1efe9}}
.paper:after{{content:'';position:absolute;inset:0;opacity:.35;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2'/><feColorMatrix values='0 0 0 0 .4  0 0 0 0 .4  0 0 0 0 .4  0 0 0 .5 0'/></filter><rect width='300' height='300' filter='url(%23n)'/></svg>")}}
.cam{{position:absolute;inset:0;transform-origin:540px 760px}}
.num{{position:absolute;left:82px;top:470px;width:100px;height:100px;background:#16285e;color:#fff;font:600 54px/100px S,serif;text-align:center}}
.bar{{position:absolute;left:182px;right:0;top:470px;height:100px;background:#cfd2d4}}
.q{{position:absolute;left:0;right:0;top:640px;text-align:center;font-family:S,serif;color:#111}}
.q .t{{font-size:84px;font-weight:600}}
.q .e{{font-size:120px;font-weight:600;margin-top:20px;font-style:normal}}
.q i{{font-style:italic}}
.q sup{{font-size:.55em}}
.arrow{{position:absolute;left:640px;top:880px;width:300px;height:420px}}
.arrow path{{fill:none;stroke:#f5cf1b;stroke-width:26;stroke-linecap:round;stroke-linejoin:round}}
.hand{{position:absolute;left:90px;right:90px;top:1330px;font-family:C,cursive;font-weight:700;font-size:92px;line-height:1.1;color:#1f5fbf;text-align:center}}
.hand span{{display:inline-block}}
.cta{{position:absolute;left:50%;top:1590px;transform:translateX(-50%);background:#16285e;color:#fff;border-radius:60px;padding:22px 44px;font:900 40px N,sans-serif;white-space:nowrap}}
.wm{{position:absolute;right:56px;top:1010px;text-align:right;font:800 30px/1.25 N,sans-serif;color:#9aa0a6}}
.brand{{position:absolute;left:56px;top:150px;display:flex;align-items:center;gap:18px}}
.brand img{{width:96px;height:96px;border-radius:50%}}
.brand div{{font:900 34px/1.15 N,sans-serif;color:#16285e;letter-spacing:1px}}.brand small{{display:block;font:800 24px N,sans-serif;color:#af7f22;letter-spacing:3px}}
/* timeline */
.cam{{animation:cam {DUR}s cubic-bezier(.45,0,.2,1) both}}
@keyframes cam{{0%{{transform:scale(1.9) translate(-150px,40px)}}22%{{transform:scale(1.9) translate(110px,40px)}}34%{{transform:scale(1) translate(0,0)}}100%{{transform:scale(1) translate(0,0)}}}}
.arrow path{{stroke-dasharray:900;animation:draw {DUR}s linear both}}
@keyframes draw{{0%,36%{{stroke-dashoffset:900}}50%{{stroke-dashoffset:0}}100%{{stroke-dashoffset:0}}}}
.hand .l1{{animation:w1 {DUR}s linear both}}.hand .l2{{animation:w2 {DUR}s linear both}}
@keyframes w1{{0%,50%{{clip-path:inset(0 100% 0 0)}}64%,100%{{clip-path:inset(0 0 0 0)}}}}
@keyframes w2{{0%,64%{{clip-path:inset(0 100% 0 0)}}76%,100%{{clip-path:inset(0 0 0 0)}}}}
.cta{{animation:pop {DUR}s ease-out both}}
@keyframes pop{{0%,80%{{opacity:0;transform:translateX(-50%) scale(.6)}}85%{{opacity:1;transform:translateX(-50%) scale(1.06)}}88%,100%{{opacity:1;transform:translateX(-50%) scale(1)}}}}
</style></head><body>
<div class="paper"></div>
<div class="cam">
 <div class="num">20</div><div class="bar"></div>
 <div class="q"><div class="t">Solve for <i>x</i>:</div><div class="e"><i>x</i><sup>8</sup> = (<i>x</i> − 2)<sup>8</sup></div></div>
 <div class="wm">Global Math Prep<br>globalmathprep.academy</div>
</div>
<div class="brand"><img src="{ROUND}"><div>GLOBAL MATH PREP<small>JARGALMAA AMGALAN</small></div></div>
<svg class="arrow" viewBox="0 0 300 420"><path d="M210,400 C260,300 230,150 60,40 M60,40 L150,40 M60,40 L80,125"/></svg>
<div class="hand"><span class="l1">Ихэнх сурагч энд</span><br><span class="l2">алддаг. Та чадах уу?</span></div>
<div class="cta">Хариугаа коммент дээр бичээрэй 👇</div>
</body></html>'''

if __name__ == '__main__':
    open(f'{D}/reel.html', 'w').write(HTML)
    video = '--video' in sys.argv
    fr = f'{D}/rframes'; shutil.rmtree(fr, ignore_errors=True); os.makedirs(fr)
    times = [i * 1000 / 30 for i in range(DUR * 30)] if video else [500, 3000, 5200, 9500]
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page(viewport={'width': 1080, 'height': 1920})
        pg.goto(f'file://{D}/reel.html'); pg.wait_for_timeout(400)
        for i, t in enumerate(times):
            pg.evaluate(f'document.getAnimations().forEach(a=>{{a.pause();a.currentTime={t}}})')
            pg.screenshot(path=f'{fr}/{i:04d}.png')
        br.close()
    if video:
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', '30', '-i', f'{fr}/%04d.png', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', f'{D}/GMP-Reel-Solve-x8.mp4'], check=True)
        shutil.copy(f'{fr}/0285.png', f'{D}/GMP-Reel-Solve-x8-cover.png')
    print('ok')
