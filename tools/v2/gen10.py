import gen4 as g
from playwright.sync_api import sync_playwright

GOLD = '#f6c343'; CREAM = '#f7f1e3'; NAVY = '#0d2a55'; TEAL = '#7fd6e8'
CSS = g.ff + f"""
*{{box-sizing:border-box}}
body{{margin:0;width:1080px;height:1350px;font-family:M,sans-serif;color:#fff;overflow:hidden}}
.pg{{width:1080px;height:1350px;position:relative;overflow:hidden;background:radial-gradient(ellipse at 50% 30%,#1b4a86 0%,#12366b 45%,#0a2248 100%)}}
.gr{{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.045) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.045) 1px,transparent 1px);background-size:64px 64px}}
.hd{{position:absolute;top:56px;left:64px;right:64px;display:flex;justify-content:space-between;align-items:center}}
.br{{font-weight:800;font-size:25px;letter-spacing:2px;line-height:1.2}}
.br span{{display:block;font-weight:600;font-size:17px;letter-spacing:3px;color:{GOLD}}}
.pn{{background:rgba(0,0,0,.28);border-radius:30px;padding:10px 22px;font-weight:700;font-size:25px}}
.mn{{position:absolute;top:170px;left:80px;right:80px;bottom:150px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:34px;text-align:center}}
.lab{{font-weight:800;font-size:30px;letter-spacing:6px;color:{GOLD}}}
.t{{margin:0;font-weight:800;font-size:88px;line-height:1.08;letter-spacing:-1px;text-shadow:0 6px 20px rgba(0,0,0,.3)}}
.t em{{font-style:normal;color:{GOLD}}}
.box{{align-self:stretch;border:3px solid rgba(127,214,232,.75);border-radius:32px;padding:34px 40px;background:rgba(8,28,64,.35)}}
.b1{{font-size:36px;font-weight:800;line-height:1.35}}
.b2{{font-size:29px;font-weight:500;line-height:1.4;color:#cfe0f3;margin-top:12px}}
.ft{{position:absolute;left:64px;right:64px;bottom:56px;display:flex;justify-content:space-between;font-size:23px;font-weight:600;color:#cfe0f3}}
b{{font-weight:800}}
"""

def icon(kind):
    sh = '<ellipse cx="110" cy="206" rx="80" ry="10" fill="#000" opacity=".22"/>'
    I = {
    'book': f'''<svg width="220" height="220" viewBox="0 0 220 220">{sh}<rect x="40" y="130" width="140" height="30" rx="6" fill="{TEAL}"/><rect x="48" y="136" width="124" height="18" rx="3" fill="{CREAM}"/><rect x="30" y="98" width="150" height="32" rx="6" fill="{GOLD}"/><rect x="38" y="104" width="134" height="20" rx="3" fill="{CREAM}"/><rect x="45" y="160" width="140" height="36" rx="6" fill="#2f73c9"/><rect x="53" y="166" width="124" height="22" rx="3" fill="{CREAM}"/><g transform="translate(150 20) rotate(35)"><rect x="0" y="0" width="22" height="110" rx="4" fill="{GOLD}"/><rect x="0" y="0" width="22" height="18" rx="4" fill="#ff8a80"/><path d="M0 110 L11 136 L22 110 Z" fill="#f2d7b0"/><path d="M7 126 L11 136 L15 126 Z" fill="#14232d"/></g></svg>''',
    'target': f'''<svg width="220" height="220" viewBox="0 0 220 220">{sh}<circle cx="110" cy="110" r="84" fill="{CREAM}"/><circle cx="110" cy="110" r="62" fill="#2f73c9"/><circle cx="110" cy="110" r="42" fill="{CREAM}"/><circle cx="110" cy="110" r="20" fill="#2f73c9"/><path d="M112 108 L176 44" stroke="#14232d" stroke-width="8" stroke-linecap="round"/><path d="M168 30 L190 30 L180 52 Z M180 30 L196 20 L200 40 Z" fill="{GOLD}"/></svg>''',
    'check': f'''<svg width="220" height="220" viewBox="0 0 220 220">{sh}<rect x="50" y="24" width="130" height="170" rx="16" fill="{CREAM}"/><rect x="82" y="12" width="66" height="28" rx="10" fill="{GOLD}"/><circle cx="82" cy="80" r="15" fill="#2f73c9"/><path d="M75 80l5 5 10-11" stroke="#fff" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M106 80h52" stroke="#9fb4c8" stroke-width="10" stroke-linecap="round"/><circle cx="82" cy="122" r="15" fill="#2f73c9"/><path d="M75 122l5 5 10-11" stroke="#fff" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M106 122h52" stroke="#9fb4c8" stroke-width="10" stroke-linecap="round"/><circle cx="82" cy="164" r="15" fill="#2f73c9"/><path d="M75 164l5 5 10-11" stroke="#fff" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M106 164h40" stroke="#9fb4c8" stroke-width="10" stroke-linecap="round"/></svg>''',
    'scale': f'''<svg width="220" height="220" viewBox="0 0 220 220">{sh}<rect x="104" y="40" width="12" height="140" rx="4" fill="{CREAM}"/><rect x="70" y="176" width="80" height="18" rx="8" fill="{GOLD}"/><path d="M40 70 H180" stroke="{CREAM}" stroke-width="10" stroke-linecap="round"/><circle cx="110" cy="44" r="14" fill="{GOLD}"/><path d="M40 70 L18 128 H62 Z M180 70 L158 128 H202 Z" fill="none" stroke="{CREAM}" stroke-width="4"/><path d="M14 128 Q40 156 66 128 Z" fill="{TEAL}"/><path d="M154 128 Q180 156 206 128 Z" fill="{TEAL}"/></svg>''',
    'pie': f'''<svg width="220" height="220" viewBox="0 0 220 220">{sh}<circle cx="110" cy="108" r="86" fill="{CREAM}"/><path d="M110 108 L110 22 A86 86 0 0 1 194 126 Z" fill="{GOLD}"/><path d="M110 108 L194 126 A86 86 0 0 1 138 190 Z" fill="{TEAL}"/><circle cx="110" cy="108" r="36" fill="#12366b"/><text x="110" y="120" text-anchor="middle" font-family="M" font-weight="800" font-size="32" fill="#fff">46%</text></svg>''',
    'bolt': f'''<svg width="220" height="220" viewBox="0 0 220 220">{sh}<circle cx="110" cy="110" r="84" fill="{CREAM}"/><circle cx="110" cy="110" r="84" fill="none" stroke="#2f73c9" stroke-width="10" stroke-dasharray="330 200" transform="rotate(-90 110 110)"/><path d="M122 38 L72 120 H106 L94 184 L150 96 H114 Z" fill="{GOLD}" stroke="#14232d" stroke-width="4" stroke-linejoin="round"/></svg>''',
    'stairs': f'''<svg width="220" height="220" viewBox="0 0 220 220">{sh}<rect x="24" y="150" width="56" height="46" rx="6" fill="{CREAM}"/><rect x="82" y="112" width="56" height="84" rx="6" fill="{TEAL}"/><rect x="140" y="70" width="56" height="126" rx="6" fill="{GOLD}"/><path d="M44 118 L108 80 L168 40" stroke="{CREAM}" stroke-width="7" fill="none" stroke-linecap="round" stroke-dasharray="4 14"/><path d="M152 30 L176 34 L166 56 Z" fill="{CREAM}"/><text x="52" y="182" text-anchor="middle" font-family="M" font-weight="800" font-size="24" fill="#14232d">1</text><text x="168" y="100" text-anchor="middle" font-family="M" font-weight="800" font-size="24" fill="#14232d">2</text></svg>''',
    'map': f'''<svg width="220" height="220" viewBox="0 0 220 220">{sh}<path d="M24 50 L78 30 L142 50 L196 30 V170 L142 190 L78 170 L24 190 Z" fill="{CREAM}"/><path d="M78 30 V170 M142 50 V190" stroke="#d6cdb8" stroke-width="4"/><path d="M50 150 C80 140 90 100 120 104 S160 80 170 64" stroke="#2f73c9" stroke-width="7" fill="none" stroke-dasharray="10 10" stroke-linecap="round"/><circle cx="50" cy="150" r="12" fill="{TEAL}"/><path d="M170 34 c-16 0 -24 12 -24 22 c0 16 24 36 24 36 s24 -20 24 -36 c0 -10 -8 -22 -24 -22 z" fill="{GOLD}" stroke="#14232d" stroke-width="3"/><circle cx="170" cy="56" r="8" fill="#14232d"/></svg>''',
    'cap': f'''<svg width="220" height="220" viewBox="0 0 220 220">{sh}<path d="M20 90 L110 48 L200 90 L110 132 Z" fill="#14232d" stroke="{CREAM}" stroke-width="4"/><path d="M58 108 v46 c30 26 74 26 104 0 v-46 L110 132 Z" fill="#1f3350" stroke="{CREAM}" stroke-width="4"/><path d="M110 90 L184 106 v52" stroke="{GOLD}" stroke-width="6" fill="none" stroke-linecap="round"/><path d="M176 158 h16 l-4 26 h-8 Z" fill="{GOLD}"/></svg>''',
    }
    return I[kind]

def slide(ic_, lab, title, b1, b2):
    return f'{icon(ic_)}<div class="lab">{lab}</div><h1 class="t">{title}</h1><div class="box"><div class="b1">{b1}</div><div class="b2">{b2}</div></div>'

S = [
 slide('book', 'SAT READING &amp; WRITING', 'Start with grammar.<br><em>Here’s why.</em>', '5 reasons, 1 simple plan.', 'Swipe through → and save it for later.'),
 slide('target', 'REASON 1', 'Grammar has an <em>ending</em>.', 'About a dozen rules cover the whole grammar section.', 'Learn them once, and they work on every test.'),
 slide('scale', 'REASON 2', 'One right answer. <em>Every time.</em>', 'Each question is decided by a rule, not a feeling.', 'Wrong choices break a rule you can actually name.'),
 slide('pie', 'REASON 3', 'Almost <em>half</em> the section.', 'Grammar ≈ 26% + Expression of Ideas ≈ 20%.', 'That’s about 46% of Reading &amp; Writing, all rule- and pattern-based.'),
 slide('bolt', 'REASON 4', 'Fast points, <em>more time</em>.', 'A grammar question you know takes seconds.', 'Bank that time and spend it on the tougher reading questions.'),
 slide('stairs', 'REASON 5', 'Module 1 <em>opens the door</em>.', 'A strong Module 1 unlocks the harder Module 2.', 'That’s where the highest scores are possible.'),
 slide('map', 'YOUR GAME PLAN', 'The order <em>that works</em>.', '<span style="color:#f6c343">1</span> Grammar &nbsp;→&nbsp; <span style="color:#f6c343">2</span> Transitions &amp; Notes<br>→&nbsp; <span style="color:#f6c343">3</span> Reading', 'Grammar first, but keep a little reading every day.'),
]
days = 'Tue · Thu · Sat'
S.append(f'''{icon('cap')}<div class="lab">ENROLLMENT OPEN</div><h1 class="t" style="font-size:74px">Want this plan <em>built for you?</em></h1>
<div class="box" style="display:flex;gap:24px;align-items:center;text-align:left;padding:28px 28px">
<div style="flex:1"><div class="b1">SAT English<br><span style="white-space:nowrap">Small groups of 2–5</span></div><div style="margin-top:16px;background:rgba(255,255,255,.08);border:2px solid rgba(246,195,67,.7);border-radius:20px;padding:18px 22px"><div style="font-size:22px;font-weight:800;letter-spacing:3px;color:#f6c343">SCHEDULE · MONGOLIA TIME</div><div style="font-size:44px;font-weight:800;margin-top:8px">{days}</div><div style="font-size:62px;font-weight:800;line-height:1.05">18:30–19:50</div><div class="b2" style="margin-top:6px">Live on Zoom · 6 seats left</div></div><div class="b1" style="margin-top:18px;color:{GOLD}">WhatsApp +1 428 880 1826</div><div class="b2" style="margin-top:10px;font-size:23px">globalmathprep.academy/portal#join</div></div>
<div style="flex:none;background:#fff;border-radius:22px;padding:12px;text-align:center;color:#14232d"><img src="{g.QR}" style="width:250px;height:250px;display:block"><div style="font-size:24px;font-weight:800;margin-top:6px">Scan to register</div></div></div>''')

def page(n, total, body):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="pg"><div class="gr"></div>
<div class="hd"><div class="br">GLOBAL MATH PREP<span>JARGALMAA AMGALAN</span></div><div class="pn">{n}/{total}</div></div>
<div class="mn">{body}</div>
<div class="ft"><span>@globalmathprep</span><span>{n}/{total}</span></div></div></body></html>'''

if __name__ == '__main__':
    out = g.HERE / 'out10'; out.mkdir(exist_ok=True)
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page(viewport={'width': 1080, 'height': 1350})
        for i, body in enumerate(S, 1):
            pg.set_content(page(i, len(S), body)); pg.wait_for_timeout(250)
            ov = pg.evaluate("()=>{const m=document.querySelector('.mn');let t=1e9,b=0;for(const c of m.children){const x=c.getBoundingClientRect();t=Math.min(t,x.top);b=Math.max(b,x.bottom)}return [Math.round(t),Math.round(b)]}")
            fn = out / f'SAT-Advice-clean-{i}-of-8.png'
            pg.screenshot(path=str(fn)); print(fn.name, ov, 'OK' if ov[0] >= 160 and ov[1] <= 1200 else 'OVERFLOW')
        br.close()
