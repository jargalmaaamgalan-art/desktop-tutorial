import random, math
import gen5 as b
from playwright.sync_api import sync_playwright

def scene(seed=7):
    R = random.Random(seed)
    s = ['<svg class="bgart" width="1080" height="1350" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg"><defs>',
         '<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0a2f6b"/><stop offset=".45" stop-color="#2d6fc0"/><stop offset=".8" stop-color="#8ab8e6"/><stop offset="1" stop-color="#c9ddf2"/></linearGradient>',
         '<radialGradient id="sun" cx=".12" cy=".58" r=".55"><stop offset="0" stop-color="#fff4c8" stop-opacity=".95"/><stop offset=".18" stop-color="#ffd878" stop-opacity=".55"/><stop offset=".5" stop-color="#ffcf6b" stop-opacity=".12"/><stop offset="1" stop-color="#ffcf6b" stop-opacity="0"/></radialGradient>',
         '<filter id="cl"><feGaussianBlur stdDeviation="18"/></filter><filter id="bl1"><feGaussianBlur stdDeviation="1.2"/></filter><filter id="bl3"><feGaussianBlur stdDeviation="3.5"/></filter>',
         '<linearGradient id="gown" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#101a2c"/><stop offset="1" stop-color="#05080f"/></linearGradient>',
         '<linearGradient id="shade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#061634" stop-opacity=".72"/><stop offset=".35" stop-color="#061634" stop-opacity=".42"/><stop offset=".62" stop-color="#061634" stop-opacity=".4"/><stop offset="1" stop-color="#040c1e" stop-opacity=".78"/></linearGradient>',
         '</defs><rect width="1080" height="1350" fill="url(#sky)"/>']
    for _ in range(9):
        x, y = R.uniform(-100, 1100), R.uniform(250, 780)
        s.append(f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="{R.uniform(140,300):.0f}" ry="{R.uniform(35,70):.0f}" fill="#ffffff" opacity="{R.uniform(.18,.4):.2f}" filter="url(#cl)"/>')
    s.append('<rect width="1080" height="1350" fill="url(#sun)"/>')

    def cap(x, y, sc, rot, tilt, blur):
        w = 70 * sc; h = w * tilt
        f = ' filter="url(#bl3)"' if blur == 2 else (' filter="url(#bl1)"' if blur == 1 else '')
        tx = R.choice([-1, 1])
        return (f'<g transform="translate({x:.0f} {y:.0f}) rotate({rot:.0f})"{f}>'
                f'<path d="M{-w*.42:.1f} {h*.25:.1f} Q0 {h*1.3:.1f} {w*.42:.1f} {h*.25:.1f} L{w*.38:.1f} {h*.9:.1f} Q0 {h*1.9:.1f} {-w*.38:.1f} {h*.9:.1f} Z" fill="#0a0f1a"/>'
                f'<path d="M0 {-h:.1f} L{w:.1f} 0 L0 {h:.1f} L{-w:.1f} 0 Z" fill="#111827" stroke="#3a4a66" stroke-width="{1.2*sc:.1f}"/>'
                f'<path d="M0 {-h:.1f} L{w:.1f} 0 L0 {h*.15:.1f} Z" fill="#1c2a44" opacity=".8"/>'
                f'<circle cx="0" cy="0" r="{3*sc:.1f}" fill="#0a0f1a"/>'
                f'<path d="M0 0 Q{tx*w*.5:.1f} {h*.3:.1f} {tx*w*.72:.1f} {h*1.6+12*sc:.1f}" stroke="#d9a52a" stroke-width="{2.4*sc:.1f}" fill="none" stroke-linecap="round"/>'
                f'<path d="M{tx*w*.72:.1f} {h*1.6+12*sc:.1f} l{-3*sc:.1f} {14*sc:.1f} l{6*sc:.1f} 0 Z" fill="#d9a52a"/></g>')

    caps = []
    for i in range(22):
        depth = R.random()
        sc = 0.3 + depth * 0.95
        x = R.uniform(-30, 1110); y = R.uniform(20, 700 - depth * 120)
        blur = 2 if depth < .25 else (1 if depth > .92 else 0)
        caps.append((sc, cap(x, y, sc, R.uniform(-45, 45), R.uniform(.28, .6), blur)))
    for sc, c in sorted(caps):
        s.append(c)

    def person(x, base, sc, arms):
        c = '#070c16'
        p = [f'<g transform="translate({x:.0f} {base:.0f}) scale({sc:.2f})">']
        p.append(f'<path d="M-70 400 L-62 120 Q-55 70 0 62 Q55 70 62 120 L70 400 Z" fill="url(#gown)"/>')
        for side in (-1, 1):
            if arms == 'up' or (arms == 'one' and side == 1):
                ang = R.uniform(-20, 20)
                ex = side * R.uniform(40, 80) + ang; ey = R.uniform(-120, -95)
                p.append(f'<path d="M{side*48} 100 Q{side*60 + ang*.5:.0f} 10 {ex:.0f} {ey:.0f}" stroke="{c}" stroke-width="28" fill="none" stroke-linecap="round"/>')
                p.append(f'<ellipse cx="{ex:.0f}" cy="{ey-18:.0f}" rx="13" ry="20" fill="#1a2233"/>')
        p.append(f'<ellipse cx="0" cy="22" rx="42" ry="48" fill="#0b1220"/>')
        p.append(f'<path d="M-40 -2 Q0 -40 40 -2 Q0 10 -40 -2 Z" fill="#0b1220"/>')
        p.append('</g>')
        return ''.join(p)
    s.append('<g opacity=".97">')
    for row, (y0, sc0, n) in enumerate(((1030, .8, 8), (1110, 1.0, 7), (1200, 1.2, 6))):
        for k in range(n):
            x = (k + R.uniform(.1, .9)) * 1080 / n
            s.append(person(x, y0 + R.uniform(-25, 25), sc0 * R.uniform(.9, 1.1), R.choice(['up', 'up', 'one'])))
    s.append('</g>')
    s.append('<rect width="1080" height="1350" fill="url(#shade)"/>')
    s.append('</svg>')
    return ''.join(s)

BG = scene()
GLASS = """
.bgart{position:absolute;inset:0}
.sc,.card{background:linear-gradient(150deg,rgba(10,32,78,.62),rgba(6,20,52,.55)) !important;backdrop-filter:blur(22px) saturate(150%);-webkit-backdrop-filter:blur(22px) saturate(150%);border:1.5px solid rgba(255,255,255,.3) !important;box-shadow:inset 0 1px 0 rgba(255,255,255,.4),0 22px 50px rgba(0,0,0,.4)}
.c{backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);background-color:rgba(8,26,64,.6) !important}
.sent{background:rgba(250,246,238,.97);border:1.5px solid rgba(255,255,255,.8)}
.t,.st2,.pno,.lgt,.satw{text-shadow:0 4px 18px rgba(0,0,0,.55)}
.fr{text-shadow:0 2px 8px rgba(0,0,0,.7)}
"""

def page(n, total, body):
    html = b.page(n, total, body)
    html = html.replace('</style>', GLASS + '</style>', 1)
    html = html.replace('<div class="gr"></div><div class="sw1"></div><div class="ring"></div><div class="ring2"></div>', BG)
    return html

if __name__ == '__main__':
    out = b.g.HERE / 'out7'; out.mkdir(exist_ok=True)
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page(viewport={'width': 1080, 'height': 1350})
        pg.set_content(f'<html><body style="margin:0">{BG}</body></html>'); pg.screenshot(path=str(out / 'bg-only.png'))
        for i, body in enumerate(b.S, 1):
            pg.set_content(page(i, len(b.S), body)); pg.wait_for_timeout(300)
            pg.screenshot(path=str(out / f'SAT-Transitions-grad-{i}-of-8.png'))
        br.close()
