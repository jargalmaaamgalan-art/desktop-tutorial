import gen5 as b
from playwright.sync_api import sync_playwright

BG = '''<svg class="bgart" width="1080" height="1350" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">
<defs>
<filter id="b2"><feGaussianBlur stdDeviation="2"/></filter>
<filter id="b6"><feGaussianBlur stdDeviation="6"/></filter>
<filter id="b20"><feGaussianBlur stdDeviation="22"/></filter>
<linearGradient id="pg" x1="0" x2="1"><stop offset="0" stop-color="#f7f2e7"/><stop offset="1" stop-color="#dfe7f2"/></linearGradient>
</defs>
<circle cx="930" cy="420" r="140" fill="#f8c12d" opacity=".14" filter="url(#b20)"/>
<circle cx="140" cy="1040" r="160" fill="#5aa9ff" opacity=".16" filter="url(#b20)"/>
<circle cx="560" cy="760" r="220" fill="#3f86e6" opacity=".10" filter="url(#b20)"/>
<g opacity=".55" filter="url(#b2)">
 <g transform="translate(700 1010) rotate(-3)">
  <rect x="0" y="0" width="380" height="64" rx="10" fill="#1f5aa6"/><rect x="18" y="8" width="344" height="48" rx="4" fill="url(#pg)" opacity=".9"/><rect x="0" y="0" width="30" height="64" rx="8" fill="#16477f"/>
 </g>
 <g transform="translate(730 1070) rotate(2)">
  <rect x="0" y="0" width="350" height="70" rx="10" fill="#f8c12d"/><rect x="16" y="9" width="318" height="52" rx="4" fill="url(#pg)" opacity=".9"/><rect x="0" y="0" width="28" height="70" rx="8" fill="#d9a41c"/>
 </g>
 <g transform="translate(690 1136) rotate(-1)">
  <rect x="0" y="0" width="400" height="76" rx="10" fill="#2f73c9"/><rect x="18" y="10" width="364" height="56" rx="4" fill="url(#pg)" opacity=".9"/><rect x="0" y="0" width="32" height="76" rx="8" fill="#245fa9"/>
 </g>
 <g transform="translate(715 1208) rotate(1.5)">
  <rect x="0" y="0" width="380" height="80" rx="10" fill="#7fb3e8"/><rect x="18" y="10" width="344" height="60" rx="4" fill="url(#pg)" opacity=".9"/><rect x="0" y="0" width="30" height="80" rx="8" fill="#6a9fd6"/>
 </g>
</g>
<g opacity=".30" filter="url(#b2)" transform="translate(760 250)">
 <path d="M0 40 C60 10 130 10 170 40 L170 200 C130 170 60 170 0 200 Z" fill="#f7f2e7"/>
 <path d="M340 40 C280 10 210 10 170 40 L170 200 C210 170 280 170 340 200 Z" fill="#e6edf6"/>
 <path d="M30 75h110M30 105h110M30 135h90M200 75h110M200 105h110M200 135h90" stroke="#7a93b0" stroke-width="7" stroke-linecap="round"/>
</g>
<g opacity=".28" filter="url(#b2)" transform="translate(30 540) rotate(-12)">
 <path d="M0 60 L120 0 L240 60 L120 120 Z" fill="#0b1f3a" stroke="#bfe6ff" stroke-width="4"/>
 <path d="M50 85 v60 c40 30 100 30 140 0 v-60" fill="#0b1f3a" stroke="#bfe6ff" stroke-width="4"/>
 <path d="M120 60 L220 90 v70" stroke="#f8c12d" stroke-width="6" fill="none" stroke-linecap="round"/><circle cx="220" cy="168" r="11" fill="#f8c12d"/>
</g>
<g opacity=".32" filter="url(#b2)" transform="translate(-30 1260) rotate(-28)">
 <rect x="0" y="0" width="380" height="36" rx="6" fill="#f8c12d"/><rect x="0" y="0" width="56" height="36" rx="6" fill="#ff8a80"/><rect x="50" y="0" width="16" height="36" fill="#c7cfd9"/>
 <path d="M380 0 L440 18 L380 36 Z" fill="#f2d7b0"/><path d="M425 13 L440 18 L425 23 Z" fill="#0b1f3a"/>
</g>
<g opacity=".20" filter="url(#b6)" transform="translate(40 830)">
 <circle cx="130" cy="80" r="62" fill="#bfe6ff"/>
 <path d="M20 330 C20 210 70 160 130 160 C190 160 240 210 240 330 Z" fill="#bfe6ff"/>
 <path d="M40 250 C80 230 110 232 130 248 C150 232 180 230 220 250 L220 310 C180 292 150 294 130 308 C110 294 80 292 40 310 Z" fill="#f7f2e7"/>
</g>
<g opacity=".18" fill="#bfe6ff">
 <circle cx="300" cy="230" r="5"/><circle cx="990" cy="820" r="7"/><circle cx="640" cy="1160" r="5"/><circle cx="90" cy="420" r="6"/><circle cx="1010" cy="640" r="4"/>
</g>
</svg>'''

GLASS = """
.bgart{position:absolute;inset:0}
.sc,.card{background:linear-gradient(150deg,rgba(255,255,255,.16),rgba(255,255,255,.05)) !important;backdrop-filter:blur(18px) saturate(140%);-webkit-backdrop-filter:blur(18px) saturate(140%);border:1.5px solid rgba(255,255,255,.28) !important;box-shadow:inset 0 1px 0 rgba(255,255,255,.35),0 18px 40px rgba(0,0,0,.25)}
.c{backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);background-color:rgba(255,255,255,.08)}
.sent{background:rgba(250,246,238,.97);backdrop-filter:blur(10px);border:1.5px solid rgba(255,255,255,.7)}
"""

def page(n, total, body):
    html = b.page(n, total, body)
    html = html.replace('</style>', GLASS + '</style>', 1)
    html = html.replace('<div class="gr"></div><div class="sw1"></div><div class="ring"></div><div class="ring2"></div>', BG + '<div class="gr"></div>')
    return html

if __name__ == '__main__':
    out = b.g.HERE / 'out6'; out.mkdir(exist_ok=True)
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page(viewport={'width': 1080, 'height': 1350})
        for i, body in enumerate(b.S, 1):
            pg.set_content(page(i, len(b.S), body)); pg.wait_for_timeout(300)
            fn = out / f'SAT-Transitions-glass-{i}-of-8.png'
            pg.screenshot(path=str(fn)); print(fn.name)
        br.close()
