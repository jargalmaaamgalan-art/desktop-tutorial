"""Animated GMP mascot intro, 1080x1350. Writes scene.html, poster PNG, and MP4 (6 s, 30 fps, loops)."""
import base64, os, subprocess, sys, shutil
sys.path.insert(0, '/home/claude/desktop-tutorial/tools/v2')
sys.argv = [sys.argv[0]] + sys.argv[1:]
from gen41 import F
import char
from playwright.sync_api import sync_playwright

D = '/home/claude/mascot'
def b(f): return 'data:image/png;base64,' + base64.b64encode(open(f, 'rb').read()).decode()
ROUND = b(f'{D}/gmp-round.png')
NAME = b('/home/claude/desktop-tutorial/tools/v2/gmp-name-dark.png')
SVG = char.svg().replace('<?xml version="1.0"?>', '')

DUR = 6
HTML = f'''<!doctype html><html><head><meta charset="utf-8"><style>
{F('M', 'nunito', [700, 800, 900])}{F('S', 'source-serif-4', [700])}
*{{box-sizing:border-box;margin:0}}
body{{width:1080px;height:1350px;overflow:hidden;position:relative;font-family:M,sans-serif;
 background:radial-gradient(900px 700px at 70% 75%,#fff4dc 0,#fdf8ef 45%,#f4f1ea 100%)}}
.top{{position:absolute;top:0;left:0;right:0;height:12px;background:#16285e}}
.brand{{position:absolute;top:56px;left:64px;display:flex;align-items:center;gap:20px}}
.brand .r{{width:118px;height:118px;border-radius:50%;box-shadow:0 6px 18px rgba(13,26,66,.25)}}
.brand .tx{{display:flex;flex-direction:column;gap:13px}}
.brand .w{{height:40px;display:block}}
.brand .jg{{font-family:S,serif;font-weight:700;font-size:29px;letter-spacing:5px;color:#af7f22;line-height:1}}
.ring{{position:absolute;left:150px;top:470px;width:860px;height:860px;border-radius:50%;background:radial-gradient(circle,#f8c95e 0,#f2a51f 62%,#e4900f 100%);opacity:.95}}
.ring2{{position:absolute;left:110px;top:430px;width:940px;height:940px;border-radius:50%;border:3px dashed rgba(22,40,94,.18)}}
.ch{{position:absolute;left:190px;top:440px;width:800px}}
.ch svg{{width:800px;height:auto;display:block}}
.bub{{position:absolute;left:56px;top:330px;background:#16285e;color:#fff;border-radius:34px;padding:26px 34px;font-weight:800;font-size:44px;line-height:1.2;box-shadow:0 14px 30px rgba(13,26,66,.25);transform-origin:80% 100%}}
.bub:after{{content:'';position:absolute;right:70px;bottom:-26px;border:18px solid transparent;border-top:26px solid #16285e}}
.bub span{{color:#f2a51f}}
.tag{{position:absolute;left:64px;top:208px;background:#fff;border:3px solid #16285e;color:#16285e;border-radius:50px;padding:14px 28px;font-weight:900;font-size:26px;letter-spacing:1.5px}}
.sp{{position:absolute;width:46px;height:46px}}
.sp path{{fill:#f2a51f}}
/* animation */
#all{{animation:bob 2s ease-in-out infinite alternate}}
#head{{transform-box:view-box;transform-origin:400px 520px;animation:tilt 3s ease-in-out infinite alternate}}
#pony{{transform-box:view-box;transform-origin:462px 180px;animation:swing 1.5s ease-in-out infinite alternate}}
#eyes{{transform-box:view-box;transform-origin:400px 350px;animation:blink 3s linear infinite}}
#arm{{transform-box:view-box;transform-origin:590px 640px;animation:thumb 1s ease-in-out infinite alternate}}
.bub{{animation:pop 6s ease-out infinite}}
.sp{{animation:tw 1.5s ease-in-out infinite}}
.s2{{animation-delay:.5s}}.s3{{animation-delay:1s}}
@keyframes bob{{from{{transform:translateY(0)}}to{{transform:translateY(-14px)}}}}
@keyframes tilt{{from{{transform:rotate(-3deg)}}to{{transform:rotate(3deg)}}}}
@keyframes swing{{from{{transform:rotate(-7deg)}}to{{transform:rotate(6deg)}}}}
@keyframes blink{{0%,90%,100%{{transform:scaleY(1)}}94%{{transform:scaleY(.08)}}}}
@keyframes thumb{{from{{transform:rotate(-3deg)}}to{{transform:rotate(5deg)}}}}
@keyframes pop{{0%{{transform:scale(0);opacity:0}}8%{{transform:scale(1.08);opacity:1}}12%{{transform:scale(1)}}100%{{transform:scale(1);opacity:1}}}}
@keyframes tw{{0%,100%{{transform:scale(.4) rotate(0);opacity:.2}}50%{{transform:scale(1) rotate(45deg);opacity:1}}}}
</style></head><body>
<div class="top"></div>
<div class="brand"><img class="r" src="{ROUND}"><div class="tx"><img class="w" src="{NAME}"><div class="jg">JARGALMAA AMGALAN</div></div></div>
<div class="ring2"></div><div class="ring"></div>
<div class="ch">{SVG}</div>
<svg class="sp" style="left:930px;top:560px" viewBox="0 0 40 40"><path d="M20 0 L24 16 L40 20 L24 24 L20 40 L16 24 L0 20 L16 16Z"/></svg>
<svg class="sp s2" style="left:990px;top:690px;width:30px" viewBox="0 0 40 40"><path d="M20 0 L24 16 L40 20 L24 24 L20 40 L16 24 L0 20 L16 16Z"/></svg>
<svg class="sp s3" style="left:860px;top:470px;width:34px" viewBox="0 0 40 40"><path d="M20 0 L24 16 L40 20 L24 24 L20 40 L16 24 L0 20 L16 16Z"/></svg>
<div class="bub">Сайн уу! <span>SAT</span>-д<br>хамт бэлдье!</div>
<div class="tag">DIGITAL SAT · MATH + ENGLISH</div>
</body></html>'''

if __name__ == '__main__':
    open(f'{D}/scene.html', 'w').write(HTML)
    video = '--video' in sys.argv
    fr = f'{D}/frames'; shutil.rmtree(fr, ignore_errors=True); os.makedirs(fr)
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page(viewport={'width': 1080, 'height': 1350})
        pg.goto(f'file://{D}/scene.html'); pg.wait_for_timeout(400)
        n = DUR * 30 if video else 1
        for i in range(n):
            t = 1800 if not video else i * 1000 / 30
            pg.evaluate(f'document.getAnimations().forEach(a=>{{a.pause();a.currentTime={t}}})')
            pg.screenshot(path=f'{fr}/{i:04d}.png')
        br.close()
    shutil.copy(f'{fr}/0000.png' if not video else f'{fr}/0054.png', f'{D}/GMP-Mascot-Intro.png')
    if video:
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', '30', '-i', f'{fr}/%04d.png', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', f'{D}/GMP-Mascot-Intro.mp4'], check=True)
    print('ok')
