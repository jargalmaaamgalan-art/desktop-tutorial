import base64, pathlib, subprocess, shutil
import gen15 as g
from playwright.sync_api import sync_playwright
HERE = g.HERE
b64 = g.b64
EM = HERE.parent / 'emoji' / 'e'
SD = HERE.parent / 'poster/fonts/serif/package/files'
serif = ''
for w in (400, 600, 700):
    for st in ('normal', 'italic'):
        serif += "@font-face{font-family:S;font-weight:%d;font-style:%s;src:url(data:font/woff2;base64,%s)}\n" % (w, st, b64(SD / f'source-serif-4-latin-{w}-{st}.woff2'))
LOGO_D = 'data:image/png;base64,' + b64(HERE / 'logo_left_dark.png')
QR = g.QR
INK = '#16121f'

def E(code, size=80, cls='', style=''):
    import os
    if code in os.environ.get('EMOJI_BLOCK', '').split(','): return ''
    return f'<img class="em {cls}" style="width:{size}px;height:{size}px;{style}" src="data:image/svg+xml;base64,{b64(EM / (code + ".svg"))}">'

def css(AC, SOFT, BG, GRID):
    return g.ff + serif + f"""
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;font-family:M,sans-serif;color:{INK}}}
.pg{{position:relative;width:1080px;height:1350px;overflow:hidden;background:{BG};
 background-image:linear-gradient({GRID} 1.5px,transparent 1.5px),linear-gradient(90deg,{GRID} 1.5px,transparent 1.5px);background-size:54px 54px}}
.hd{{position:absolute;top:40px;left:56px;right:56px;display:flex;justify-content:space-between;align-items:center;z-index:3}}
.hd img{{height:60px}}
.pn{{border:2.5px solid {INK};border-radius:30px;padding:7px 20px;font-weight:800;font-size:23px;background:#fff}}
.ft{{position:absolute;left:56px;right:56px;bottom:32px;display:flex;justify-content:space-between;font-size:21px;font-weight:700;opacity:.75;z-index:3}}
.mn{{position:absolute;top:150px;bottom:90px;left:56px;right:56px;display:flex;flex-direction:column;justify-content:center;gap:26px;z-index:2}}
.mn>*{{flex-shrink:0}}
.pill{{align-self:flex-start;display:inline-flex;align-items:center;gap:10px;background:{AC};color:#fff;border-radius:30px;padding:9px 22px;font-weight:800;font-size:24px;letter-spacing:1px}}
h1{{font-size:80px;font-weight:800;line-height:1.03;letter-spacing:-1.5px}}
h1 em{{font-style:normal;color:{AC}}}
.hl{{background:linear-gradient(transparent 58%,{SOFT} 58%);padding:0 6px}}
.grid{{display:grid;grid-template-columns:1fr 1fr;gap:20px}}
.card{{background:#fff;border:3px solid {INK};border-radius:28px;box-shadow:7px 7px 0 {INK};padding:24px 26px;position:relative}}
.em{{display:inline-block;vertical-align:middle}}
.take{{background:{INK};color:#fff;border-radius:26px;padding:22px 28px;display:flex;align-items:center;gap:18px;font-size:29px;font-weight:700;line-height:1.3}}
.take b{{color:{SOFT}}}
.chip{{display:inline-flex;align-items:center;gap:8px;border:2.5px solid {INK};background:#fff;border-radius:30px;padding:7px 18px;font-size:23px;font-weight:700;margin:4px}}
@keyframes fl{{0%,100%{{transform:translateY(0) rotate(-6deg)}}50%{{transform:translateY(-26px) rotate(6deg)}}}}
@keyframes pop{{0%{{transform:scale(0)}}60%{{transform:scale(1.18)}}100%{{transform:scale(1)}}}}
@keyframes wig{{0%,100%{{transform:rotate(-10deg)}}50%{{transform:rotate(10deg)}}}}
@keyframes pulse{{0%,100%{{transform:scale(1)}}50%{{transform:scale(1.08)}}}}
.fl{{animation:fl 3s ease-in-out infinite}}
.wig{{animation:wig 1.5s ease-in-out infinite}}
.pulse{{animation:pulse 2s ease-in-out infinite}}
.pop{{animation:pop .9s cubic-bezier(.3,1.6,.5,1) both}}
@keyframes up{{0%{{opacity:0;transform:translateY(40px)}}100%{{opacity:1;transform:none}}}}
.mn>*{{animation:up .6s ease-out both}}
.mn>*:nth-child(2){{animation-delay:.12s}} .mn>*:nth-child(3){{animation-delay:.24s}} .mn>*:nth-child(4){{animation-delay:.36s}} .mn>*:nth-child(5){{animation-delay:.48s}} .mn>*:nth-child(6){{animation-delay:.6s}} .mn>*:nth-child(7){{animation-delay:.72s}}
.grid>.card{{animation:pop .6s cubic-bezier(.3,1.6,.5,1) both}}
.grid>.card:nth-child(1){{animation-delay:.45s}} .grid>.card:nth-child(2){{animation-delay:.6s}} .grid>.card:nth-child(3){{animation-delay:.75s}} .grid>.card:nth-child(4){{animation-delay:.9s}}
"""

def page(C, n, total, body, extra=''):
    return f'''<!doctype html><html lang="mn"><head><meta charset="utf-8"><style>{C}</style></head><body><div class="pg">{extra}
<div class="hd"><img src="{LOGO_D}"><div class="pn">{n}/{total}</div></div>
<div class="mn">{body}</div>
<div class="ft"><span>@globalmathprep · globalmathprep.academy</span><span>{"Гүйлгээд үз →" if n < total else ""}</span></div></div></body></html>'''

def end_page(AC, SOFT, title_a, title_b, lead, sched, perks):
    rows = ''.join(f'<div style="display:flex;align-items:center;gap:14px;font-size:27px;font-weight:700">{E(c,44)}<span>{t}</span></div>' for c, t in perks)
    return f'''<div class="pill">ТӨГСГӨЛ</div>
<h1 style="font-size:84px">{title_a}<br><em>{title_b}</em></h1>
<div style="font-size:31px;font-weight:600;line-height:1.35">{lead}</div>
<div class="card" style="padding:0;display:grid;grid-template-columns:1fr 1fr;overflow:hidden">{sched}</div>
<div style="display:flex;gap:22px;align-items:stretch">
 <div class="card" style="padding:16px;text-align:center"><img src="{QR}" style="width:250px;height:250px;display:block"><div style="font-weight:800;font-size:23px;margin-top:6px">Скан хийж бүртгүүл</div></div>
 <div class="card" style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:16px">{rows}</div></div>
<div style="background:{AC};color:#fff;border:3px solid {INK};border-radius:24px;padding:18px;text-align:center;font-size:30px;font-weight:800;box-shadow:7px 7px 0 {INK}">WhatsApp +1 428 880 1826</div>'''

def sched_cell(label, days, AC, last=False):
    return f'<div style="padding:20px 26px;{"" if last else f"border-right:3px solid {INK};"}"><div style="font-size:21px;font-weight:800;color:{AC};letter-spacing:1px">{label}</div><div style="font-size:42px;font-weight:800;margin-top:4px">{days}</div><div style="font-size:23px;font-weight:600;opacity:.75">20:00–21:20 УБ цаг</div></div>'

def render(C, pages, out, prefix, video_first=False):
    out.mkdir(exist_ok=True)
    for f in out.glob('*'): f.unlink()
    total = len(pages)
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page(viewport={'width': 1080, 'height': 1350})
        for i, (body, extra) in enumerate(pages, 1):
            pg.set_content(page(C, i, total, body, extra)); pg.wait_for_timeout(400)
            # freeze animations at a nice moment for the PNG
            pg.evaluate("()=>document.getAnimations().forEach(a=>{a.pause();a.currentTime=1500})")
            ov = pg.evaluate("()=>{const m=document.querySelector('.mn');let t=1e9,b=0;for(const c of m.children){const r=c.getBoundingClientRect();t=Math.min(t,r.top);b=Math.max(b,r.bottom)}return [Math.round(t),Math.round(b)]}")
            fn = out / f'{prefix}-{i:02d}-of-{total:02d}.png'
            pg.screenshot(path=str(fn)); print(fn.name, ov, 'OK' if ov[0] >= 140 and ov[1] <= 1262 else 'OVERFLOW')
            if video_first is True or (video_first == 'cover' and i == 1):
                fr = out / '_frames'; fr.mkdir(exist_ok=True)
                N = 150
                for k in range(N):
                    t = k * 1000 / 30
                    pg.evaluate(f"()=>document.getAnimations().forEach(a=>{{a.pause();a.currentTime={t}}})")
                    pg.screenshot(path=str(fr / f'{k:04d}.png'))
                subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', '30', '-i', str(fr / '%04d.png'), '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '19', '-movflags', '+faststart', str(fn.with_suffix('.mp4'))], check=True)
                shutil.rmtree(fr)
        br.close()
