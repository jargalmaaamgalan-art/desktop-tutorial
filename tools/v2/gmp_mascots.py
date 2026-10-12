"""Three original GMP mascot candidates. Same 400x420 canvas as chars.py."""
import chars
OUT = chars.OUT
NAVY, GOLD = '#14216b', '#f2b632'

def emblem(cx, cy, r):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{NAVY}"/><circle cx="{cx}" cy="{cy-r*0.18:.0f}" r="{r*0.46:.0f}" fill="none" stroke="#fff" stroke-width="{max(2,r*0.07):.0f}"/>'
            f'<path d="M{cx-r*0.46:.0f} {cy-r*0.18:.0f} H{cx+r*0.46:.0f} M{cx} {cy-r*0.64:.0f} V{cy+r*0.28:.0f}" stroke="#fff" stroke-width="{max(2,r*0.06):.0f}"/>'
            f'<path d="M{cx-r*0.7:.0f} {cy+r*0.28:.0f} Q{cx-r*0.35:.0f} {cy+r*0.08:.0f} {cx:.0f} {cy+r*0.34:.0f} Q{cx+r*0.35:.0f} {cy+r*0.08:.0f} {cx+r*0.7:.0f} {cy+r*0.28:.0f} L{cx+r*0.6:.0f} {cy+r*0.58:.0f} Q{cx+r*0.3:.0f} {cy+r*0.4:.0f} {cx} {cy+r*0.62:.0f} Q{cx-r*0.3:.0f} {cy+r*0.4:.0f} {cx-r*0.6:.0f} {cy+r*0.58:.0f}Z" fill="{GOLD}"/>')

# A: "Gee", a student with a navy graduation cap and the GMP badge on her hoodie
KID = dict(skin='#f2c9a0', outfit=NAVY, sleeve=NAVY, brow='#3a2415', cheek='#ff8fa3',
  back='<ellipse cx="200" cy="140" rx="104" ry="96" fill="#2a1a10"/><path d="M96 150 Q80 250 112 300 L150 270Z M304 150 Q320 250 288 300 L250 270Z" fill="#2a1a10"/>',
  front='<path d="M108 128 Q130 74 200 70 Q270 74 292 128 Q250 102 200 108 Q150 102 108 128Z" fill="#2a1a10"/>',
  hat=f'<g transform="translate(0,-34)"><path d="M90 92 L200 44 L310 92 L200 134Z" fill="{NAVY}"/><path d="M130 112 V150 Q200 176 270 150 V112 L200 134Z" fill="#0f1850"/><path d="M300 96 V150" stroke="{GOLD}" stroke-width="7"/><circle cx="300" cy="156" r="10" fill="{GOLD}"/></g>',
  torso_extra=emblem(200, 330, 44))

def globe(mood):
    fk = {'happy': 'happy', 'wow': 'wow', 'flex': 'smug', 'sleepy': 'sleepy', 'think': 'think', 'sun': 'cool'}.get(mood, 'happy')
    body = ('<defs><radialGradient id="g" cx="40%" cy="35%"><stop offset="0" stop-color="#6fb8ff"/><stop offset="1" stop-color="#2563eb"/></radialGradient></defs>'
            '<ellipse cx="130" cy="400" rx="46" ry="16" fill="#14216b"/><ellipse cx="270" cy="400" rx="46" ry="16" fill="#14216b"/>'
            '<path d="M120 330 L120 392 M280 330 L280 392" stroke="#14216b" stroke-width="30" stroke-linecap="round"/>')
    arms = {'happy': ((70, 250, 40, 170), (330, 250, 360, 170)), 'wow': ((70, 250, 40, 170), (330, 250, 360, 170)),
            'flex': ((70, 290, 50, 300), (330, 250, 360, 160)), 'sleepy': ((70, 290, 60, 360), (330, 290, 340, 360)),
            'think': ((70, 290, 60, 360), (330, 270, 280, 230)), 'sun': ((70, 290, 40, 340), (330, 290, 360, 340))}[mood if mood in ('happy','wow','flex','sleepy','think','sun') else 'happy']
    a = ''.join(f'<path d="M{x1} {y1} L{x2} {y2}" stroke="#fff" stroke-width="30" stroke-linecap="round"/><circle cx="{x2}" cy="{y2}" r="22" fill="#fff" stroke="#14216b" stroke-width="5"/>' for x1, y1, x2, y2 in arms)
    ball = ('<circle cx="200" cy="215" r="150" fill="url(#g)" stroke="#14216b" stroke-width="6"/>'
            '<path d="M70 150 Q110 120 150 150 Q160 190 120 210 Q80 200 70 150Z M250 100 Q300 90 330 130 Q320 170 280 160 Q250 140 250 100Z M270 250 Q320 250 330 300 Q300 330 270 300Z" fill="#4ade80" opacity=".9"/>'
            '<ellipse cx="200" cy="215" rx="150" ry="52" fill="none" stroke="#fff" stroke-width="3" opacity=".5"/><path d="M200 65 V365" stroke="#fff" stroke-width="3" opacity=".4"/>')
    f = chars.face(fk, '#fff', OUT, '#ff8fa3')
    f = f.replace('y="130"', 'y="160"')
    cap = f'<path d="M110 90 L200 48 L290 90 L200 128Z" fill="{NAVY}"/><path d="M148 108 V140 Q200 164 252 140 V108 L200 128Z" fill="#0f1850"/><path d="M280 94 V140" stroke="{GOLD}" stroke-width="6"/><circle cx="280" cy="146" r="9" fill="{GOLD}"/>'
    return f'<svg viewBox="-10 -10 420 420" xmlns="http://www.w3.org/2000/svg">{body}{a}{ball}<g transform="translate(0,40)">{f}</g><g transform="translate(0,-26)">{cap}</g></svg>'

def owl(mood):
    fk = {'happy': 'happy', 'wow': 'wow', 'flex': 'smug', 'sleepy': 'sleepy', 'think': 'think', 'sun': 'cool'}.get(mood, 'happy')
    body = ('<ellipse cx="200" cy="320" rx="120" ry="95" fill="#8b6b4a"/><ellipse cx="200" cy="335" rx="74" ry="70" fill="#f3e2c0"/>'
            '<path d="M150 318 q12 12 24 0 M188 318 q12 12 24 0 M226 318 q12 12 24 0 M166 346 q12 12 24 0 M204 346 q12 12 24 0" stroke="#c9a678" stroke-width="5" fill="none" stroke-linecap="round"/>'
            '<path d="M120 400 l-6 10 h30 M280 400 l6 10 h-30" stroke="#f59e0b" stroke-width="8" stroke-linecap="round"/>')
    wing = {'happy': (-1, 'up'), 'wow': (-1, 'up'), 'flex': (-1, 'flex')}.get(mood, (-1, 'down'))
    if wing[1] == 'up':
        wings = '<path d="M96 290 Q40 230 56 170 Q110 200 120 270Z M304 290 Q360 230 344 170 Q290 200 280 270Z" fill="#6f5238"/>'
    elif wing[1] == 'flex':
        wings = '<path d="M96 300 Q60 340 70 380 Q110 360 120 300Z" fill="#6f5238"/><path d="M304 290 Q360 240 340 170 Q290 200 280 270Z" fill="#6f5238"/>'
    else:
        wings = '<path d="M96 290 Q56 340 70 392 Q116 360 122 290Z M304 290 Q344 340 330 392 Q284 360 278 290Z" fill="#6f5238"/>'
    head = ('<path d="M96 120 L84 40 L152 84Z M304 120 L316 40 L248 84Z" fill="#8b6b4a"/><ellipse cx="200" cy="170" rx="112" ry="100" fill="#8b6b4a"/>'
            '<ellipse cx="200" cy="165" rx="92" ry="66" fill="#fff7e0"/>')
    beak = f'<path d="M184 196 L216 196 L200 232Z" fill="#f59e0b" stroke="{OUT}" stroke-width="4" stroke-linejoin="round"/>'
    f = chars.face(fk, '#fff7e0', OUT, '#ff8fa3')
    import re
    f = re.sub(r'<path d="M(1[67]\d) 2\d\d.*?/>', '', f) if False else f
    f = f.replace('cy="152"', 'cy="150"')
    cap = f'<path d="M96 96 L200 50 L304 96 L200 138Z" fill="{NAVY}"/><path d="M144 116 V146 Q200 172 256 146 V116 L200 138Z" fill="#0f1850"/><path d="M292 100 V146" stroke="{GOLD}" stroke-width="6"/><circle cx="292" cy="152" r="9" fill="{GOLD}"/>'
    badge = emblem(200, 330, 34)
    return f'<svg viewBox="-10 -10 420 420" xmlns="http://www.w3.org/2000/svg">{body}{wings}{head}{f}{beak}<g transform="translate(0,-22)">{cap}</g>{badge}</svg>'

def candidate(name, mood):
    if name == 'A': return chars.kid(KID, mood)
    if name == 'B': return globe(mood)
    return owl(mood)
