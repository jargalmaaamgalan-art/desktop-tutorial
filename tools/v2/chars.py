"""Original GMP cartoon kids. One cast member per word, 13 moods each. All SVG, drawn by hand here."""
OUT = '#2b1d2e'   # outline / pupils

def _arm(pts, col, hand, w=40):
    d = 'M' + ' L'.join(f'{x} {y}' for x, y in pts)
    x, y = pts[-1]
    return (f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<circle cx="{x}" cy="{y}" r="24" fill="{hand}"/>')

def _mirror(pts): return [(400 - x, y) for x, y in pts]

POSES = {
 'hang':   ([(124, 292), (104, 372)], [(276, 292), (296, 372)]),
 'up':     ([(124, 288), (70, 210)], [(276, 288), (330, 210)]),
 'flex':   ([(124, 292), (104, 372)], [(276, 292), (338, 290), (338, 212)]),
 'point':  ([(124, 292), (104, 372)], [(276, 292), (350, 220)]),
 'hips':   ([(124, 290), (70, 335), (128, 362)], [(276, 290), (330, 335), (272, 362)]),
 'cross':  ([(124, 296), (270, 336)], [(276, 296), (130, 336)]),
 'shrug':  ([(124, 292), (66, 326), (52, 282)], [(276, 292), (334, 326), (348, 282)]),
 'chin':   ([(124, 292), (104, 372)], [(276, 292), (262, 238), (236, 214)]),
 'pray':   ([(124, 292), (176, 346)], [(276, 292), (224, 346)]),
 'shout':  ([(124, 288), (76, 232), (96, 150)], [(276, 288), (324, 232), (304, 150)]),
}
MOOD = {  # mood -> (face, pose)
 'think': ('think', 'chin'), 'fruit': ('happy', 'hang'), 'please': ('worry', 'pray'), 'cost': ('worry', 'shrug'),
 'ears': ('shout', 'shout'), 'out': ('smug', 'point'), 'sun': ('cool', 'hips'), 'happy': ('happy', 'up'),
 'wow': ('wow', 'up'), 'flex': ('smug', 'flex'), 'point': ('smug', 'point'), 'shrug': ('worry', 'shrug'),
 'sleepy': ('sleepy', 'hang'),
}

def face(kind, skin, brow='#2b1d2e', cheek='#ff8fa3', angry=False):
    ex = (160, 240)
    eye = lambda r=1.0: ''.join(f'<ellipse cx="{x}" cy="152" rx="{19*r:.0f}" ry="{24*r:.0f}" fill="#fff" stroke="{OUT}" stroke-width="4"/>'
                                f'<circle cx="{x+(2 if x>200 else -2)}" cy="156" r="{11*r:.0f}" fill="{OUT}"/><circle cx="{x+5}" cy="150" r="4" fill="#fff"/>' for x in ex)
    brows = lambda a=0, y=120: (f'<path d="M{ex[0]-22} {y+a} Q{ex[0]} {y-8} {ex[0]+20} {y-a}" stroke="{brow}" stroke-width="8" fill="none" stroke-linecap="round"/>'
                                f'<path d="M{ex[1]-20} {y-a} Q{ex[1]} {y-8} {ex[1]+22} {y+a}" stroke="{brow}" stroke-width="8" fill="none" stroke-linecap="round"/>')
    blush = f'<ellipse cx="128" cy="196" rx="20" ry="12" fill="{cheek}" opacity=".7"/><ellipse cx="272" cy="196" rx="20" ry="12" fill="{cheek}" opacity=".7"/>'
    smile = f'<path d="M172 204 Q200 232 228 204" stroke="{OUT}" stroke-width="6" fill="none" stroke-linecap="round"/>'
    grin = f'<path d="M168 200 Q200 252 232 200 Z" fill="{OUT}" stroke="{OUT}" stroke-width="4" stroke-linejoin="round"/><path d="M180 222 Q200 236 220 222 Q200 214 180 222Z" fill="#ff7b8e"/>'
    flat = f'<path d="M180 214 L220 214" stroke="{OUT}" stroke-width="6" stroke-linecap="round"/>'
    smirk = f'<path d="M174 212 Q210 226 232 200" stroke="{OUT}" stroke-width="6" fill="none" stroke-linecap="round"/>'
    frown = f'<path d="M176 220 Q200 200 224 220" stroke="{OUT}" stroke-width="6" fill="none" stroke-linecap="round"/>'
    oh = f'<ellipse cx="200" cy="214" rx="17" ry="21" fill="{OUT}"/><ellipse cx="200" cy="222" rx="9" ry="8" fill="#ff7b8e"/>'
    if kind == 'happy':   return eye() + brows(-2, 116) + blush + grin
    if kind == 'wow':     return eye(1.2) + brows(-6, 110) + blush + oh
    if kind == 'shout':   return eye(1.1) + brows(-4, 112) + blush + oh
    if kind == 'worry':   return eye() + brows(8, 118) + blush + frown
    if kind == 'think':   return eye() + brows(-4, 114) + blush + smirk
    if kind == 'cool':    # sunglasses
        return (f'<rect x="118" y="130" width="76" height="46" rx="16" fill="{OUT}"/><rect x="206" y="130" width="76" height="46" rx="16" fill="{OUT}"/>'
                f'<path d="M194 146 L206 146" stroke="{OUT}" stroke-width="7"/><path d="M130 140 L156 140" stroke="#fff" stroke-width="6" stroke-linecap="round" opacity=".6"/>' + blush + grin)
    if kind == 'sleepy':
        z = '<text x="296" y="90" font-size="56" font-weight="900" fill="#60a5fa" font-family="Arial Black,sans-serif">Z</text><text x="338" y="52" font-size="38" font-weight="900" fill="#93c5fd" font-family="Arial Black,sans-serif">z</text>'
        return ''.join(f'<path d="M{x-20} 154 Q{x} 172 {x+20} 154" stroke="{OUT}" stroke-width="7" fill="none" stroke-linecap="round"/>' for x in ex) + blush + f'<ellipse cx="200" cy="214" rx="12" ry="9" fill="{OUT}"/>' + z
    # smug: half-lid eyes
    lid = ''.join(f'<ellipse cx="{x}" cy="152" rx="19" ry="24" fill="#fff" stroke="{OUT}" stroke-width="4"/><circle cx="{x+(3 if x>200 else -3)}" cy="160" r="11" fill="{OUT}"/>'
                  f'<path d="M{x-24} 130 L{x+24} 130 L{x+24} 150 L{x-24} 150 Z" fill="{skin}"/><path d="M{x-22} 150 L{x+22} 150" stroke="{OUT}" stroke-width="6" stroke-linecap="round"/>' for x in ex)
    return lid + brows(-4, 118) + blush + smirk


def _head(skin, hair_back='', hair_front='', hat='', ears=True, extra_face=''):
    ear = f'<circle cx="108" cy="160" r="20" fill="{skin}"/><circle cx="292" cy="160" r="20" fill="{skin}"/>' if ears else ''
    head = f'<ellipse cx="200" cy="150" rx="92" ry="90" fill="{skin}"/>'
    return hair_back, ear + head


def kid(spec, mood):
    fk, pk = MOOD[mood]
    pk = spec.get('poses', {}).get(mood, pk)
    skin, tone = spec['skin'], spec.get('cheek', '#ff8fa3')
    out, sleeve = spec['outfit'], spec.get('sleeve', spec['outfit'])
    handc = skin
    L, R = POSES[pk]
    arms = _arm(L, sleeve, handc) + _arm(R, sleeve, handc)
    if pk == 'pray': arms = _arm(L, sleeve, handc) + _arm(R, sleeve, handc)
    torso = (f'<path d="M112 410 Q104 270 158 254 L242 254 Q296 270 288 410 Z" fill="{out}"/><rect x="178" y="226" width="44" height="40" rx="14" fill="{skin}"/>'
             + spec.get('torso_extra', ''))
    back = spec.get('back', '')
    ears = f'<circle cx="108" cy="160" r="20" fill="{skin}"/><circle cx="292" cy="160" r="20" fill="{skin}"/>' if spec.get('ears', True) else ''
    head = f'<ellipse cx="200" cy="150" rx="92" ry="90" fill="{skin}"/>'
    f = face(fk, skin, spec.get('brow', OUT), tone)
    if spec.get('angry') and fk in ('smug', 'worry', 'think'):
        f += (f'<path d="M132 118 L186 138 M268 118 L214 138" stroke="{spec["brow"]}" stroke-width="12" stroke-linecap="round"/>')
    over = spec.get('front', '')
    svg = (f'<svg viewBox="-10 -10 420 420" xmlns="http://www.w3.org/2000/svg">{back}{torso}{arms}{ears}{head}{spec["mid"] if "mid" in spec else ""}{f}{over}'
           f'{spec.get("hat", "")}{spec.get("hand_extra", "")}</svg>')
    return svg


# ------------------------------------------------------------------ the cast (all original)
def curls(cx, cy, r, n, col, rad):
    import math
    return ''.join(f'<circle cx="{cx+rad*math.cos(2*math.pi*i/n):.0f}" cy="{cy+rad*math.sin(2*math.pi*i/n):.0f}" r="{r}" fill="{col}"/>' for i in range(n))

CAST = {
 # DRAW: art girl with a purple beret and a big bun
 'DRAW': dict(skin='#f2c9a0', outfit='#ff7a59', sleeve='#ff7a59', brow='#3a2415',
    back='<circle cx="200" cy="34" r="44" fill="#3a2415"/>' + '<ellipse cx="200" cy="130" rx="104" ry="96" fill="#3a2415"/>',
    front='<path d="M108 128 Q130 70 200 66 Q270 70 292 128 Q250 100 200 108 Q150 100 108 128Z" fill="#3a2415"/>',
    hat='<ellipse cx="204" cy="76" rx="92" ry="32" fill="#7c3aed"/><circle cx="216" cy="44" r="10" fill="#7c3aed"/><path d="M118 82 Q204 108 290 78" stroke="#5b21b6" stroke-width="6" fill="none"/>',
    torso_extra='<path d="M150 300 L170 330 M240 290 L226 340" stroke="#22c55e" stroke-width="12" stroke-linecap="round"/><circle cx="196" cy="340" r="12" fill="#38bdf8"/><circle cx="244" cy="318" r="10" fill="#fde047"/>'),
 # ACCOUNT: neat kid with big glasses and a bow tie
 'ACCOUNT': dict(skin='#f6d2b0', outfit='#ffffff', sleeve='#ffffff', brow='#2f3b52',
    back='', front='<path d="M110 130 Q112 62 200 60 Q290 62 290 130 Q262 92 214 96 Q170 92 110 130Z" fill="#2f3b52"/>',
    hat='<g fill="none" stroke="#1d4ed8" stroke-width="8"><circle cx="160" cy="154" r="34"/><circle cx="240" cy="154" r="34"/><path d="M194 150 L206 150"/></g>',
    torso_extra='<path d="M200 270 L172 252 L172 292Z M200 270 L228 252 L228 292Z" fill="#dc2626"/><circle cx="200" cy="270" r="8" fill="#991b1b"/><rect x="226" y="300" width="36" height="46" rx="6" fill="#e5e7eb" stroke="#475569" stroke-width="3"/>'),
 # HOLD: strong teen, headband, spiky black hair
 'HOLD': dict(skin='#e9b98a', outfit='#16a34a', sleeve='#e9b98a', brow='#1b1220',
    back='', front='<path d="M104 126 L96 62 L140 92 L160 34 L196 84 L232 30 L250 90 L304 58 L296 126 Q250 94 200 100 Q150 94 104 126Z" fill="#1b1220"/>',
    hat='<rect x="110" y="104" width="180" height="20" rx="8" fill="#ef4444"/>',
    torso_extra='<path d="M168 286 L232 286" stroke="#14532d" stroke-width="6"/><text x="170" y="350" font-size="46" font-weight="900" fill="#fff" font-family="Arial Black,sans-serif">GMP</text>'),
 # SUPPORT: caped hero girl with a mask and puffy curls
 'SUPPORT': dict(poses={'flex': 'hips', 'sun': 'hips', 'point': 'hips', 'out': 'hips'}, skin='#a8683f', outfit='#38bdf8', sleeve='#38bdf8', brow='#2a1408', cheek='#ff7a8a',
    back='<path d="M104 250 Q60 330 90 410 L310 410 Q340 330 296 250 Z" fill="#ec4899"/>' + curls(200, 96, 46, 9, '#2a1408', 96),
    front='<path d="M112 120 Q130 82 200 80 Q270 82 288 120 Q244 98 200 106 Q156 98 112 120Z" fill="#2a1408"/>',
    mid='<path d="M104 134 Q200 112 296 134 L292 184 Q250 172 218 186 Q200 192 182 186 Q150 172 108 184Z" fill="#ec4899"/>', hat='',
    torso_extra='<circle cx="200" cy="310" r="26" fill="#fde047"/><path d="M200 292 L206 306 L222 308 L210 318 L214 334 L200 326 L186 334 L190 318 L178 308 L194 306Z" fill="#ec4899"/>'),
 # ADDRESS: postal kid with a cap, braid and a mail bag
 'ADDRESS': dict(skin='#f1c9a5', outfit='#1d4ed8', sleeve='#1d4ed8', brow='#6b3a1a',
    back='<path d="M280 150 Q330 230 300 330" stroke="#6b3a1a" stroke-width="30" fill="none" stroke-linecap="round"/>',
    front='<path d="M108 132 Q112 76 200 70 Q288 76 292 132 Q250 104 200 108 Q150 104 108 132Z" fill="#6b3a1a"/>',
    hat='<path d="M106 112 Q110 36 200 34 Q290 36 294 112 Z" fill="#1e3a8a"/><path d="M96 112 Q200 130 330 106 L316 94 Q200 110 110 96Z" fill="#172554"/><circle cx="200" cy="74" r="12" fill="#fbbf24"/>',
    torso_extra='<path d="M130 270 L270 380" stroke="#92400e" stroke-width="22" stroke-linecap="round"/><rect x="214" y="332" width="64" height="48" rx="8" fill="#b45309" stroke="#78350f" stroke-width="4"/><path d="M220 340 L246 358 L272 340" stroke="#fde68a" stroke-width="4" fill="none"/>'),
 # FIGURE: cool teen with sunglasses-ready look, blue beanie and scarf
 'FIGURE': dict(skin='#f4cba3', outfit='#f97316', sleeve='#f97316', brow='#8b5a2b',
    back='', front='<path d="M108 124 Q112 70 200 66 Q288 70 292 124 Q250 108 200 112 Q150 108 108 124Z" fill="#8b5a2b"/>',
    hat='<path d="M102 116 Q100 24 200 22 Q300 24 298 116 Z" fill="#0ea5e9"/><rect x="96" y="100" width="208" height="30" rx="14" fill="#0284c7"/><circle cx="200" cy="18" r="18" fill="#fff"/>',
    torso_extra='<rect x="140" y="248" width="120" height="30" rx="15" fill="#0ea5e9"/><rect x="214" y="262" width="32" height="64" rx="14" fill="#0ea5e9"/><text x="160" y="360" font-size="60" font-weight="900" fill="#fff" font-family="Arial Black,sans-serif">%</text>'),
 # CHARGE: grumpy boss girl with a big ponytail and black outfit (angry-cute)
 'CHARGE': dict(poses={'flex': 'cross', 'sun': 'cross', 'out': 'cross', 'point': 'cross'}, skin='#f3c8a6', outfit='#1f2937', sleeve='#1f2937', brow='#120d18', angry=True, cheek='#ff6b6b',
    back='<path d="M262 70 Q380 40 372 170 Q366 250 322 300 Q340 200 300 150Z" fill="#120d18"/><ellipse cx="200" cy="132" rx="100" ry="92" fill="#120d18"/>',
    front='<path d="M106 150 Q100 66 200 60 Q300 66 294 150 Q276 110 236 104 Q200 120 150 100 Q118 116 106 150Z" fill="#120d18"/><circle cx="272" cy="62" r="18" fill="#f43f5e"/>',
    hat='', torso_extra='<path d="M168 286 L232 286" stroke="#374151" stroke-width="6"/><path d="M204 298 L184 338 L202 338 L194 372 L226 326 L208 326Z" fill="#facc15"/>'),
 # MAINTAIN: builder kid with a yellow hard hat and overalls
 'MAINTAIN': dict(skin='#e6b48a', outfit='#2563eb', sleeve='#f97316', brow='#3b2210',
    back='', front='<path d="M110 130 Q112 90 200 88 Q288 90 290 130 Q250 110 200 114 Q150 110 110 130Z" fill="#3b2210"/>',
    hat='<path d="M104 104 Q104 20 200 20 Q296 20 296 104 Z" fill="#facc15" stroke="#a16207" stroke-width="5"/><rect x="92" y="98" width="216" height="20" rx="10" fill="#eab308" stroke="#a16207" stroke-width="5"/><rect x="186" y="22" width="28" height="70" fill="#eab308"/>',
    torso_extra='<rect x="150" y="300" width="100" height="110" rx="10" fill="#1d4ed8"/><circle cx="168" cy="296" r="8" fill="#facc15"/><circle cx="232" cy="296" r="8" fill="#facc15"/><rect x="176" y="330" width="48" height="36" rx="6" fill="#1e40af"/>'),
 # TRACE: detective kid with a deerstalker cap and a trench coat
 'TRACE': dict(skin='#f0c6a0', outfit='#92713f', sleeve='#92713f', brow='#3a2a18',
    back='', front='<path d="M108 128 Q112 80 200 78 Q288 80 292 128 Q250 108 200 112 Q150 108 108 128Z" fill="#3a2a18"/>',
    hat='<path d="M104 112 Q104 24 200 22 Q296 24 296 112 Z" fill="#a78b5a" stroke="#6b5326" stroke-width="5"/><path d="M104 112 Q200 130 296 112 L296 100 Q200 118 104 100Z" fill="#6b5326"/><path d="M104 84 L100 130 M296 84 L300 130" stroke="#6b5326" stroke-width="10" stroke-linecap="round"/><path d="M200 22 L200 100" stroke="#6b5326" stroke-width="5"/>',
    torso_extra='<path d="M200 260 L200 410" stroke="#6b5326" stroke-width="5"/><path d="M200 262 L168 300 L200 322 L232 300Z" fill="#fff"/><circle cx="188" cy="350" r="6" fill="#6b5326"/><circle cx="212" cy="350" r="6" fill="#6b5326"/>'),
 # BEAR: kid in a bear hoodie (the word BEAR!)
 'BEAR': dict(skin='#f3c9a4', outfit='#8b5a2b', sleeve='#8b5a2b', brow='#3b2210',
    back='<circle cx="112" cy="70" r="40" fill="#8b5a2b"/><circle cx="288" cy="70" r="40" fill="#8b5a2b"/><circle cx="112" cy="72" r="21" fill="#ecd0a2"/><circle cx="288" cy="72" r="21" fill="#ecd0a2"/><ellipse cx="200" cy="150" rx="112" ry="108" fill="#8b5a2b"/>',
    front='<path d="M104 130 Q120 78 200 74 Q280 78 296 130 Q250 104 200 108 Q150 104 104 130Z" fill="#8b5a2b"/>',
    hat='', torso_extra='<path d="M150 290 Q200 330 250 290" stroke="#6b4423" stroke-width="8" fill="none"/><ellipse cx="200" cy="350" rx="48" ry="26" fill="#ecd0a2"/>'),
}

def draw_kid(word, mood):
    return kid(CAST[word], mood)
