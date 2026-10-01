import random
import gen4 as g
from gen4 import ic, CHECK, XX
from playwright.sync_api import sync_playwright

INK = '#120d2e'; LEMON = '#ffe14d'; MINT = '#7cf0c5'; PINK = '#ff8fc7'; LILAC = '#b9a4ff'; SKY = '#8fd8ff'; CORAL = '#ff8a7a'; CREAM = '#fff8ea'

def scene():
    R = random.Random(3)
    s = ['<svg class="bgart" width="1080" height="1350" viewBox="0 0 1080 1350"><defs>',
         '<linearGradient id="nt" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#140f3d"/><stop offset=".55" stop-color="#2c1a6b"/><stop offset="1" stop-color="#4a2584"/></linearGradient>',
         '<radialGradient id="lamp" cx=".2" cy=".78" r=".5"><stop offset="0" stop-color="#ffd27a" stop-opacity=".55"/><stop offset=".5" stop-color="#ff9ecb" stop-opacity=".12"/><stop offset="1" stop-color="#ff9ecb" stop-opacity="0"/></radialGradient>',
         '<radialGradient id="scr" cx=".72" cy=".86" r=".35"><stop offset="0" stop-color="#8fd8ff" stop-opacity=".45"/><stop offset="1" stop-color="#8fd8ff" stop-opacity="0"/></radialGradient>',
         '<filter id="bb"><feGaussianBlur stdDeviation="2.5"/></filter></defs>',
         '<rect width="1080" height="1350" fill="url(#nt)"/>']
    for _ in range(70):
        x, y, r = R.uniform(0, 1080), R.uniform(0, 900), R.uniform(1, 2.8)
        s.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r:.1f}" fill="#fff" opacity="{R.uniform(.25,.8):.2f}"/>')
    for x, y in ((150, 260), (930, 700), (80, 820)):
        s.append(f'<path d="M{x} {y-18} L{x+5} {y-5} L{x+18} {y} L{x+5} {y+5} L{x} {y+18} L{x-5} {y+5} L{x-18} {y} L{x-5} {y-5} Z" fill="{LEMON}" opacity=".8"/>')
    s.append(f'<g filter="url(#bb)" opacity=".9"><circle cx="905" cy="300" r="70" fill="#fff4d6"/><circle cx="935" cy="285" r="62" fill="#2a1a66"/></g>')
    s.append('<rect width="1080" height="1350" fill="url(#lamp)"/><rect width="1080" height="1350" fill="url(#scr)"/>')
    s.append('<g opacity=".95">')
    s.append(f'<rect x="-20" y="1240" width="1120" height="130" fill="#23164f"/><rect x="-20" y="1236" width="1120" height="10" fill="#3a2a7a"/>')
    s.append(f'<g transform="translate(60 1040)"><rect x="-6" y="190" width="120" height="14" rx="4" fill="{INK}"/><path d="M50 190 L50 70 L130 20" stroke="{INK}" stroke-width="12" fill="none" stroke-linecap="round"/><path d="M110 -10 L200 30 L170 70 L90 25 Z" fill="{PINK}" stroke="{INK}" stroke-width="6"/></g>')
    s.append(f'<g transform="translate(260 1150)"><rect x="0" y="0" width="190" height="34" rx="6" fill="{LILAC}" stroke="{INK}" stroke-width="5"/><rect x="12" y="-34" width="170" height="34" rx="6" fill="{MINT}" stroke="{INK}" stroke-width="5"/><rect x="-8" y="-66" width="180" height="32" rx="6" fill="{LEMON}" stroke="{INK}" stroke-width="5"/><rect x="-8" y="34" width="210" height="52" rx="6" fill="{SKY}" stroke="{INK}" stroke-width="5"/></g>')
    s.append(f'<g transform="translate(640 1040)"><rect x="0" y="0" width="300" height="190" rx="14" fill="#2b2f55" stroke="{INK}" stroke-width="7"/><rect x="16" y="16" width="268" height="158" rx="6" fill="#9fe2ff"/><path d="M40 60h150M40 90h200M40 120h120" stroke="#5a8fd0" stroke-width="10" stroke-linecap="round"/><path d="M-30 196 L330 196 L350 214 L-50 214 Z" fill="#c9cde6" stroke="{INK}" stroke-width="6"/></g>')
    s.append(f'<g transform="translate(500 1160)"><rect x="0" y="0" width="80" height="84" rx="10" fill="{CORAL}" stroke="{INK}" stroke-width="6"/><path d="M80 20 q34 0 34 26 q0 26 -34 26" stroke="{INK}" stroke-width="7" fill="none"/><path d="M22 -14 q10 -16 0 -30 M50 -14 q10 -16 0 -30" stroke="#fff" stroke-width="5" fill="none" opacity=".7" stroke-linecap="round"/></g>')
    s.append(f'<g transform="translate(960 1110)"><rect x="0" y="60" width="70" height="72" rx="8" fill="{LEMON}" stroke="{INK}" stroke-width="6"/><path d="M35 60 C10 20 0 0 20 -20 M35 60 C50 20 70 10 60 -30 M35 60 C30 30 40 10 35 -10" stroke="#3cc48f" stroke-width="9" fill="none" stroke-linecap="round"/></g>')
    s.append('</g></svg>')
    return ''.join(s)
BG = scene()

CSS = g.ff + f"""
*{{box-sizing:border-box}}
body{{margin:0;width:1080px;height:1350px;font-family:M,sans-serif;color:#fff;overflow:hidden}}
.pg{{width:1080px;height:1350px;position:relative;overflow:hidden}}
.bgart{{position:absolute;inset:0}}
.hd{{position:absolute;top:50px;left:60px;right:60px;display:flex;align-items:center;justify-content:space-between}}
.lg{{display:flex;align-items:center;gap:16px}}
.lgt{{font-family:S,serif;font-weight:700;font-size:25px;letter-spacing:2.5px;line-height:1.25}}
.lgt span{{display:block;color:{LEMON};font-size:18px;letter-spacing:2.5px;font-weight:600}}
.pill{{background:{LEMON};color:{INK};border:4px solid {INK};box-shadow:5px 5px 0 {INK};border-radius:40px;padding:8px 22px;font-weight:800;font-size:26px}}
.mn{{position:absolute;top:160px;left:60px;right:60px;bottom:150px;display:flex;flex-direction:column;justify-content:center;gap:26px}}
.tag{{align-self:flex-start;background:{PINK};color:{INK};border:4px solid {INK};box-shadow:6px 6px 0 {INK};border-radius:14px;padding:10px 20px;font-weight:800;font-size:25px;letter-spacing:2px;transform:rotate(-2deg)}}
.t{{margin:0;font-weight:800;font-size:92px;line-height:1.02;letter-spacing:-1.5px;text-shadow:0 5px 0 {INK}}}
.hl{{background:{LEMON};color:{INK};padding:0 14px;border-radius:12px;text-shadow:none;display:inline-block;transform:rotate(-1.5deg);box-shadow:6px 6px 0 {INK};border:4px solid {INK}}}
.sub{{font-size:36px;font-weight:700;line-height:1.3;margin:0}}
.stk{{background:{CREAM};color:{INK};border:4px solid {INK};box-shadow:8px 8px 0 {INK};border-radius:26px;padding:22px 24px}}
.grid3{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:22px}}
.big{{font-size:84px;font-weight:800;line-height:.95}}
.lab{{font-size:28px;font-weight:800;margin-top:6px}}
.sm{{font-size:25px;font-weight:600;line-height:1.3;margin-top:6px;color:#3a3160}}
.row{{display:flex;align-items:center;gap:20px}}
.dot{{flex:none;width:72px;height:72px;border-radius:50%;border:4px solid {INK};display:flex;align-items:center;justify-content:center;font-weight:800;font-size:36px;color:{INK}}}
.ft{{position:absolute;left:60px;right:60px;bottom:46px;display:flex;justify-content:space-between;align-items:center}}
.fch{{background:{INK};border:3px solid rgba(255,255,255,.35);border-radius:30px;padding:10px 20px;font-size:22px;font-weight:700}}
.dots{{display:flex;gap:8px}}
.dots i{{width:14px;height:14px;border-radius:50%;background:rgba(255,255,255,.35);border:2px solid {INK}}}
.dots i.on{{background:{LEMON};width:40px;border-radius:8px}}
b{{font-weight:800}}
"""
LOGO = g.LOGO.replace('width="52" height="48"', 'width="68" height="62"').replace('#f6c343', LEMON)

def page(n, total, body):
    dots = ''.join(f'<i class="{"on" if k == n else ""}"></i>' for k in range(1, total + 1))
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="pg">{BG}
<div class="hd"><div class="lg">{LOGO}<div class="lgt">GLOBAL MATH PREP<span>JARGALMAA AMGALAN</span></div></div><div class="pill">{n}/{total}</div></div>
<div class="mn">{body}</div>
<div class="ft"><span class="fch">@globalmathprep · globalmathprep.academy</span><div class="dots">{dots}</div></div>
</div></body></html>'''

def stk(inner, bg=CREAM, rot=0, st=''):
    return f'<div class="stk" style="background:{bg};transform:rotate({rot}deg);{st}">{inner}</div>'
def stat(n, l, s, bg, rot):
    return stk(f'<div class="big">{n}</div><div class="lab">{l}</div><div class="sm">{s}</div>', bg, rot, 'text-align:center;padding:24px 14px')

S = []
S.append(f'''<div class="tag">SAT READING &amp; WRITING</div>
<h1 class="t" style="font-size:104px">Start with grammar.<br><span class="hl">No cap.</span></h1>
<p class="sub">Reading = a side quest that never ends.<br><span style="color:{LEMON}">Grammar = the cheat code.</span></p>
<div class="grid3">{stat('∞','reading','endless texts, slow gains',LILAC,-2)}{stat('~12','rules','that’s the whole list',LEMON,1.5)}{stat('46%','of the section','runs on rules',MINT,-1)}</div>
<p class="sub" style="font-size:30px;align-self:flex-start;background:#120d2e;border:3px solid rgba(255,255,255,.35);border-radius:40px;padding:10px 26px">Swipe if you want your score to glow up →</p>''')

S.append(f'''<div class="tag" style="background:{SKY}">THE TEST · SPEEDRUN EDITION</div>
<h1 class="t">Know the map<br><span class="hl">before you play.</span></h1>
<div class="grid3">{stat('54','questions','2 modules of 27',LEMON,-1.5)}{stat('64','minutes','32 per module',PINK,1)}{stat('~71s','per question','64 × 60 ÷ 54',MINT,-1)}</div>
{stk(f'<div class="row"><div class="dot" style="background:{SKY}">1</div><div><div style="font-size:33px;font-weight:800">Every question is a solo</div><div class="sm" style="font-size:27px">One short text each. No giant passages.</div></div></div>', CREAM, .8)}
{stk(f'<div class="row"><div class="dot" style="background:{LILAC}">2</div><div><div style="font-size:33px;font-weight:800">It’s adaptive (it reads the room)</div><div class="sm" style="font-size:27px">How you do in Module 1 sets Module 2.</div></div></div>', CREAM, -.8)}''')

def col(title, bg, rows, good):
    items = ''.join(f'<div style="display:flex;gap:12px;align-items:flex-start;padding:12px 0;border-top:3px dashed rgba(18,13,46,.25)"><div class="dot" style="width:40px;height:40px;font-size:20px;border-width:3px;background:{MINT if good else CORAL}">{"✓" if good else "✗"}</div><span style="font-size:25px;font-weight:700;line-height:1.3">{r}</span></div>' for r in rows)
    return stk(f'<div style="font-size:34px;font-weight:800;margin-bottom:6px">{title}</div>{items}', bg, -1 if good else 1, 'flex:1;padding:22px 20px')
S.append(f'''<div class="tag" style="background:{MINT}">READING VS GRAMMAR</div>
<h1 class="t" style="font-size:86px">Vibes-based<br><span class="hl">vs rules-based.</span></h1>
<div style="display:flex;gap:20px">{col('Reading 😵', PINK, ['Guessing from clues', 'Two answers look right (lowkey stressful)', 'Slow, bumpy progress', 'Infinite possible questions'], False).replace('😵','')}{col('Grammar', LEMON, ['One answer, set by a rule', 'Wrong answers break a rule you can name', 'Fast progress that sticks', 'A list you can actually finish'], True)}</div>''')

D = [('Craft &amp; Structure', 28, SKY), ('Information &amp; Ideas', 26, LILAC), ('Grammar (Conventions)', 26, LEMON), ('Expression of Ideas', 20, MINT)]
bars = ''.join(f'<div style="margin-top:14px"><div style="display:flex;justify-content:space-between;font-size:27px;font-weight:800;margin-bottom:8px"><span>{n}</span><span>~{p}%</span></div><div style="height:34px;border-radius:18px;background:#e9e2d2;border:3px solid {INK};overflow:hidden"><div style="height:100%;width:{p/28*100:.0f}%;background:{c};border-right:3px solid {INK}"></div></div></div>' for n, p, c in D)
S.append(f'''<div class="tag" style="background:{LEMON}">THE RECEIPTS</div>
<h1 class="t" style="font-size:86px">Almost half the points?<br><span class="hl">Literally rules.</span></h1>
{stk(f'<div style="font-size:22px;font-weight:800;letter-spacing:3px;color:#5b4fa0">SHARE OF READING &amp; WRITING</div>{bars}', CREAM, -.6)}
{stk(f'<div class="row"><div class="big" style="font-size:96px">46%</div><div style="font-size:29px;font-weight:800;line-height:1.3">Grammar 26% + Expression of Ideas 20% = points you can <u>actually</u> learn.</div></div>', MINT, .8)}''')

topics = ['Sentence boundaries', 'Joining clauses', 'Extra-info clauses', 'Comma rules', 'Colons &amp; dashes', 'Subject–verb agreement', 'Verb tense', 'Pronouns', 'Apostrophes', 'Modifiers', 'Parallel structure', 'Word pairs']
cols = [LEMON, MINT, PINK, SKY, LILAC, CORAL]
chips = ''.join(f'<div style="background:{cols[i%6]};color:{INK};border:4px solid {INK};box-shadow:5px 5px 0 {INK};border-radius:18px;padding:14px 16px;font-size:26px;font-weight:800;transform:rotate({[-1.5,1,-.5,1.5,-1,.5][i%6]}deg)">{i+1}. {t}</div>' for i, t in enumerate(topics))
S.append(f'''<div class="tag" style="background:{LILAC}">THE WHOLE LIST</div>
<h1 class="t" style="font-size:76px">~12 rules.<br><span class="hl">That’s it. That’s the list.</span></h1>
<div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px">{chips}</div>
<p class="sub" style="font-size:30px;align-self:flex-start;background:#120d2e;border:3px solid rgba(255,255,255,.35);border-radius:40px;padding:10px 26px">Spot the rule → <span style="color:{LEMON}">answer in seconds.</span> Hits different.</p>''')

S.append(f'''<div class="tag" style="background:{CORAL}">WHY IT PAYS TWICE</div>
<h1 class="t" style="font-size:88px">Module 1 is the<br><span class="hl">main character.</span></h1>
{stk(f'<div class="row"><div class="dot" style="background:{MINT};font-size:30px">W</div><div><div style="font-size:34px;font-weight:800">Nail Module 1</div><div class="sm" style="font-size:27px">Harder Module 2 unlocked. Top scores = in play.</div></div></div>', CREAM, -1)}
{stk(f'<div class="row"><div class="dot" style="background:{CORAL};font-size:30px">L</div><div><div style="font-size:34px;font-weight:800">Fumble Module 1</div><div class="sm" style="font-size:27px">Easier Module 2. Your ceiling drops. Oof.</div></div></div>', CREAM, 1)}
<div class="grid3">{stat('fast','points','grammar = seconds',LEMON,-1)}{stat('safe','points','rules don’t change',MINT,1)}{stat('+time','bonus','more time for reading',PINK,-1)}</div>''')

plan = [(1, LEMON, 'Grammar first', 'Aim for zero lost points. Understood the assignment.'), (2, MINT, 'Expression of Ideas', 'Transitions + Student Notes. Also pattern-based.'), (3, SKY, 'Reading, daily', 'Small reps every day while grammar carries.')]
S.append(f'''<div class="tag" style="background:{MINT}">THE GLOW-UP PLAN</div>
<h1 class="t" style="font-size:90px">Your order<br><span class="hl">of attack.</span></h1>
{''.join(stk(f'<div class="row"><div class="dot" style="background:{c};width:80px;height:80px;font-size:42px">{i}</div><div><div style="font-size:35px;font-weight:800">{h}</div><div class="sm" style="font-size:27px">{p}</div></div></div>', CREAM, [-1,.8,-.6][i-1]) for i,c,h,p in plan)}
{stk(f'<div class="row"><div class="dot" style="background:{CORAL}">{ic(XX,36,3.4)}</div><div style="font-size:29px;font-weight:800;line-height:1.3">Don’t be the NPC who only grinds reading. Relatable, but not the move.</div></div>', PINK, .6)}''')

days = ''.join(f'<div style="flex:1;background:{LEMON};border:3px solid {INK};border-radius:14px;padding:10px 4px;text-align:center;font-weight:800;font-size:26px">{d}</div>' for d in ('Tue', 'Thu', 'Fri'))
S.append(f'''<div class="tag" style="background:{LEMON}">ENROLLMENT OPEN</div>
<h1 class="t" style="font-size:90px">Join the squad.<br><span class="hl">6 seats left.</span></h1>
<div class="grid3">{stat('2–5','per group','small &amp; chill',MINT,-1.5)}{stat('3×','a week','80 min each',PINK,1)}{stat('1','mock test','every week',SKY,-1)}</div>
<div style="display:flex;gap:22px">
{stk(f'<div style="font-size:22px;font-weight:800;letter-spacing:3px;color:#5b4fa0">MONGOLIA TIME</div><div style="display:flex;gap:10px;margin:12px 0">{days}</div><div style="font-size:54px;font-weight:800">18:30–19:50</div><div class="sm">Live on Zoom · Nov &amp; Dec SAT · weekly parent report</div>', CREAM, -.8, 'flex:1.4')}
{stk(f'<img src="{g.QR}" style="width:190px;height:190px;display:block;margin:0 auto"><div style="font-size:25px;font-weight:800;text-align:center;margin-top:8px">Free level test</div>', '#ffffff', 1.2, 'flex:1')}</div>
{stk(f'<div style="text-align:center;font-size:29px;font-weight:700">Slide into our WhatsApp with <b>“SAT English”</b></div><div style="text-align:center;font-size:48px;font-weight:800">+1 428 880 1826</div>', LEMON, -.5)}''')

if __name__ == '__main__':
    out = g.HERE / 'out9'; out.mkdir(exist_ok=True)
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page(viewport={'width': 1080, 'height': 1350})
        for i, body in enumerate(S, 1):
            pg.set_content(page(i, len(S), body)); pg.wait_for_timeout(300)
            ov = pg.evaluate("()=>{const m=document.querySelector('.mn');let t=1e9,b=0;for(const c of m.children){const x=c.getBoundingClientRect();t=Math.min(t,x.top);b=Math.max(b,x.bottom)}return [Math.round(t),Math.round(b)]}")
            fn = out / f'SAT-Advice-night-{i}-of-8.png'
            pg.screenshot(path=str(fn)); print(fn.name, ov, 'OK' if ov[0] >= 150 and ov[1] <= 1210 else 'OVERFLOW')
        br.close()
