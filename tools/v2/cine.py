import math, random, base64, pathlib
import gen15 as g15
from gen18 import E, render, HERE, LOGO_D
F2 = HERE.parent / 'fonts2'
b64 = lambda p: base64.b64encode(p.read_bytes()).decode()
R = g15.RNG
def face(fam, path, w, st, rng):
    return "@font-face{font-family:%s;font-weight:%d;font-style:%s;unicode-range:%s;src:url(data:font/woff2;base64,%s)}\n" % (fam, w, st, rng, b64(path))
PF = next(F2.glob('fontsource-playfair-display-*/package/files'))
IN = next(F2.glob('fontsource-inter-*/package/files'))
GV = next(F2.glob('fontsource-great-vibes-*/package/files'))
ff = g15.ff
for sub in ('latin', 'latin-ext', 'cyrillic'):
    ff += face('PF', PF / f'playfair-display-{sub}-900-italic.woff2', 900, 'italic', R[sub])
for sub in ('latin', 'latin-ext', 'cyrillic', 'cyrillic-ext'):
    for w in (800, 900):
        ff += face('IN', IN / f'inter-{sub}-{w}-normal.woff2', w, 'normal', R[sub])
for sub in ('latin', 'latin-ext', 'cyrillic', 'cyrillic-ext'):
    ff += face('GV', GV / f'great-vibes-{sub}-400-normal.woff2', 400, 'normal', R[sub])

def ridge(seed, y0, amp, rough, W=1080, step=12):
    rnd = random.Random(seed); pts = []; y = y0
    ph = [rnd.random() * 6 for _ in range(4)]
    for x in range(0, W + step, step):
        t = x / W
        yy = y0 - amp * (0.55 * math.sin(t * 5.1 + ph[0]) + 0.3 * math.sin(t * 11.7 + ph[1]) + 0.15 * math.sin(t * 23 + ph[2])) - rough * rnd.random()
        pts.append(f'{x},{yy:.1f}')
    return 'M0,1350 L' + ' L'.join(pts) + ' L1080,1350 Z'

THEMES = {
 'steppe': dict(sky=('#7fb6e6', '#cfe6f7', '#f4f1e6'), sun=(820, 520, '#fff6d8'), m=[('#9fb3c8', 700, 60, 18), ('#7f99b3', 760, 50, 14)], lake=('#3f7fb5', 800), hills=[('#8cbf5a', 880, 40, 4), ('#6fa83f', 980, 50, 4), ('#5a9433', 1110, 60, 3)], ink='#111'),
 'sunset': dict(sky=('#2b3a67', '#e07a5f', '#f6c28b'), sun=(540, 760, '#ffd9a0'), m=[('#6b4e71', 740, 70, 16), ('#4a3a5a', 820, 60, 12)], lake=('#3a3150', 880), hills=[('#2d2440', 960, 40, 4), ('#1e1830', 1100, 50, 3)], ink='#fff'),
 'night': dict(sky=('#070b1a', '#16213e', '#2a3a5e'), sun=(800, 360, '#e8edf7'), m=[('#1c2640', 760, 70, 18), ('#121a2e', 840, 60, 12)], lake=('#0f1a33', 900), hills=[('#0b1122', 980, 40, 4), ('#070b16', 1120, 50, 3)], ink='#fff'),
 'sea': dict(sky=('#2f6fd6', '#6aa8ec', '#cfe3f8'), sun=(200, 460, '#ffffff'), m=[('#8fb0d6', 800, 25, 6)], lake=('#1f5fae', 820), hills=[('#6d8f3a', 1060, 70, 5), ('#557a2b', 1180, 60, 4)], ink='#fff'),
 'dawn': dict(sky=('#f3b8a8', '#f9dcc4', '#fdf2e3'), sun=(540, 700, '#fff3df'), m=[('#c9a3a8', 720, 60, 14), ('#a98590', 800, 55, 12)], lake=('#d7b3b0', 860), hills=[('#8a6b73', 960, 40, 4), ('#6c525c', 1100, 50, 3)], ink='#1d1320'),
}

def scene(name, seed=1):
    t = THEMES[name]; s1, s2, s3 = t['sky']; sx, sy, sc = t['sun']
    s = f'''<svg width="1080" height="1350" viewBox="0 0 1080 1350" style="position:absolute;inset:0"><defs>
<linearGradient id="sk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{s1}"/><stop offset=".55" stop-color="{s2}"/><stop offset="1" stop-color="{s3}"/></linearGradient>
<radialGradient id="sn"><stop offset="0" stop-color="{sc}" stop-opacity="1"/><stop offset=".18" stop-color="{sc}" stop-opacity=".9"/><stop offset="1" stop-color="{sc}" stop-opacity="0"/></radialGradient>
<linearGradient id="lk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{t['lake'][0]}" stop-opacity=".85"/><stop offset="1" stop-color="{t['lake'][0]}"/></linearGradient>
<filter id="bl"><feGaussianBlur stdDeviation="2"/></filter></defs>
<rect width="1080" height="1350" fill="url(#sk)"/><circle cx="{sx}" cy="{sy}" r="330" fill="url(#sn)"/>'''
    if name == 'night':
        rnd = random.Random(seed)
        for _ in range(140):
            s += f'<circle cx="{rnd.random()*1080:.0f}" cy="{rnd.random()*700:.0f}" r="{rnd.random()*1.8+.4:.1f}" fill="#fff" opacity="{rnd.random()*.7+.2:.2f}"/>'
        s += f'<circle cx="{sx}" cy="{sy}" r="34" fill="#f4f6fb"/>'
    else:
        rnd = random.Random(seed + 7)
        for _ in range(5):
            cx, cy, w = rnd.random() * 1080, 180 + rnd.random() * 380, 140 + rnd.random() * 200
            s += f'<g opacity=".38" filter="url(#bl)">' + ''.join(f'<ellipse cx="{cx + dx:.0f}" cy="{cy + dy:.0f}" rx="{w*r:.0f}" ry="{w*r*.42:.0f}" fill="#ffffff" opacity=".8"/>' for dx, dy, r in [(-w*.4, 8, .5), (0, -10, .62), (w*.45, 6, .48), (w*.1, 14, .7)]) + '</g>'
    for i, (col, y0, amp, rough) in enumerate(t['m']):
        s += f'<path d="{ridge(seed * 10 + i, y0, amp, rough)}" fill="{col}"/>'
    ly = t['lake'][1]
    s += f'<rect x="0" y="{ly}" width="1080" height="{1350-ly}" fill="url(#lk)"/>'
    rnd = random.Random(seed + 3)
    for _ in range(46):
        x, y, w = sx - 180 + rnd.random() * 360, ly + 10 + rnd.random() * 140, 20 + rnd.random() * 70
        s += f'<rect x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="3" rx="1.5" fill="{sc}" opacity="{rnd.random()*.5+.3:.2f}"/>'
    for i, (col, y0, amp, rough) in enumerate(t['hills']):
        s += f'<path d="{ridge(seed * 20 + i, y0, amp, rough)}" fill="{col}"/>'
    s += '<rect width="1080" height="1350" fill="url(#vg)" opacity="0"/></svg>'
    return s

LOGO_W = g15.LOGO
def cine(theme, label, n, total, body, seed=1):
    t = THEMES[theme]; ink = t['ink']
    return f'''<!doctype html><html lang="mn"><head><meta charset="utf-8"><style>{ff}
*{{margin:0;padding:0;box-sizing:border-box}} body{{width:1080px;height:1350px;font-family:IN,M,sans-serif;color:{ink}}}
.pg{{position:relative;width:1080px;height:1350px;overflow:hidden}}
.top{{position:absolute;top:56px;left:60px;right:60px;display:flex;justify-content:space-between;font-family:M;font-weight:700;font-size:24px;letter-spacing:4px;z-index:3}}
.handle{{position:absolute;bottom:56px;left:0;right:0;text-align:center;font-family:M;font-weight:700;font-size:26px;letter-spacing:1px;z-index:3}}
.logo{{position:absolute;bottom:40px;left:56px;height:62px;z-index:3}}
.c{{position:absolute;left:60px;right:60px;top:210px;text-align:center;z-index:3}}
.pf{{font-family:PF,serif;font-style:italic;font-weight:900;letter-spacing:-4px;line-height:.85}}
.in{{font-family:IN,M,sans-serif;font-weight:900;letter-spacing:-2px;line-height:.95}}
.gv{{font-family:GV,cursive;font-weight:400}}
.chip{{display:inline-block;background:#d9f99d;color:#111;padding:0 18px}}
.sm{{font-family:M;font-weight:700}}
@keyframes up{{0%{{opacity:0;transform:translateY(30px)}}100%{{opacity:1;transform:none}}}}
@keyframes drift{{0%,100%{{transform:translateX(0)}}50%{{transform:translateX(-24px)}}}}
@keyframes shim{{0%,100%{{opacity:.55}}50%{{opacity:1}}}}
.c>*{{animation:up .8s ease-out both}} .c>*:nth-child(2){{animation-delay:.2s}} .c>*:nth-child(3){{animation-delay:.4s}} .c>*:nth-child(4){{animation-delay:.6s}} .c>*:nth-child(5){{animation-delay:.8s}}
svg g{{animation:drift 9s ease-in-out infinite}}
.mn{{display:none}}
</style></head><body><div class="pg">{scene(theme, seed)}
<div class="top"><span>{label}</span><span>{n:02d} / {total:02d}</span></div>
<div class="c">{body}</div>
<div class="handle">@globalmathprep</div></div></body></html>'''
