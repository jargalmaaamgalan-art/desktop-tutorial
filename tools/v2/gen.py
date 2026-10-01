import base64, pathlib
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).parent
FD = HERE.parent / 'poster/fonts/package/files'
ff = ''
for w in (500, 600, 700, 800):
    for sub in ('latin', 'latin-ext', 'cyrillic', 'cyrillic-ext'):
        p = FD / f'montserrat-{sub}-{w}-normal.woff2'
        if p.exists():
            ff += "@font-face{font-family:M;font-weight:%d;src:url(data:font/woff2;base64,%s)}\n" % (w, base64.b64encode(p.read_bytes()).decode())
QR = 'data:image/svg+xml;base64,' + base64.b64encode((HERE / 'qr.svg').read_bytes()).decode()

Y = '#f6c343'; CY = '#c9f2ff'
GREEN = '#5fd6a8'; CORAL = '#ff8a80'; BLUE = '#7cc2ff'; PURPLE = '#c9a6ff'

CSS = ff + """
*{box-sizing:border-box}
body{margin:0;width:1080px;height:1350px;font-family:M,sans-serif;color:#fff;overflow:hidden}
.pg{width:1080px;height:1350px;position:relative;overflow:hidden;background:radial-gradient(ellipse at 50% 12%,#22647f 0%,#134560 42%,#0a2636 100%)}
.gr{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.035) 1px,transparent 1px);background-size:46px 46px}
.glow{position:absolute;width:700px;height:700px;border-radius:50%;background:radial-gradient(circle,rgba(246,195,67,.10),transparent 65%);right:-260px;bottom:-200px}
.hd{position:absolute;top:50px;left:60px;right:60px;display:flex;justify-content:space-between;align-items:center}
.lg{display:flex;align-items:center;gap:14px;font-weight:800;font-size:21px;line-height:1.15;letter-spacing:1.5px}
.pn{border:2px solid rgba(160,215,235,.35);background:rgba(255,255,255,.06);border-radius:30px;padding:9px 22px;font-weight:700;font-size:22px}
.ft{position:absolute;left:60px;right:60px;bottom:42px}
.tr{height:4px;border-radius:4px;background:rgba(255,255,255,.15);margin-bottom:22px;overflow:hidden}
.tf{height:4px;background:#f6c343;border-radius:4px}
.fr{display:flex;justify-content:space-between;font-size:21px;font-weight:600;color:#dcebf1}
.mn{position:absolute;top:140px;left:60px;right:60px;bottom:120px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:30px}
.bd{background:#f6c343;color:#14232d;border-radius:40px;padding:11px 28px;font-weight:800;font-size:22px;letter-spacing:3px;box-shadow:0 10px 24px rgba(0,0,0,.3)}
.t{margin:0;text-align:center;font-weight:800;font-size:78px;line-height:1.02;text-shadow:0 6px 20px rgba(0,0,0,.35)}
.t span{display:block;color:#c9f2ff}
.sub{text-align:center;font-size:28px;font-weight:600;color:#d7ebf2;line-height:1.4;max-width:900px}
.card{align-self:stretch;background:linear-gradient(135deg,rgba(52,128,160,.45),rgba(16,52,72,.65));border:1.5px solid rgba(160,215,235,.3);border-radius:28px;padding:24px 30px;box-shadow:0 18px 40px rgba(0,0,0,.25)}
.row{display:flex;align-items:center;gap:24px}
.num{flex:none;width:66px;height:66px;border-radius:20px;background:#f6c343;color:#14232d;font-weight:800;font-size:34px;display:flex;align-items:center;justify-content:center;box-shadow:0 6px 14px rgba(0,0,0,.25)}
.disc{flex:none;width:74px;height:74px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#14232d;font-weight:800;font-size:32px;box-shadow:0 6px 14px rgba(0,0,0,.25)}
.h{font-size:33px;font-weight:800;line-height:1.15}
.p{font-size:24px;font-weight:500;color:#cfe6ee;line-height:1.35;margin-top:4px}
.tip{align-self:stretch;background:#f6c343;color:#14232d;border-radius:24px;padding:20px 28px;font-weight:700;font-size:25px;line-height:1.35;display:flex;gap:18px;align-items:center}
.tip b{font-weight:800}
.stats{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px;align-self:stretch}
.st{background:linear-gradient(160deg,rgba(52,128,160,.5),rgba(16,52,72,.7));border:1.5px solid rgba(160,215,235,.3);border-radius:26px;padding:22px 12px;text-align:center}
.st .n{font-size:62px;font-weight:800;color:#f6c343;line-height:1}
.st .l{font-size:22px;font-weight:700;margin-top:10px;line-height:1.25}
.pill{display:inline-block;padding:8px 18px;border-radius:30px;font-weight:700;font-size:22px;margin:5px 6px 5px 0}
.swipe{font-size:24px;font-weight:700;color:#c9f2ff;letter-spacing:1px}
.ex{background:#f4efe3;color:#14232d;border-radius:20px;padding:20px 26px;font-size:28px;line-height:1.45;font-weight:600}
.hl{background:#f6c343;border-radius:8px;padding:0 8px;font-weight:800}
.lab{font-size:19px;font-weight:800;letter-spacing:3px;color:#7fdcf2}
.ch{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin-top:16px}
.ch div{background:rgba(255,255,255,.07);border:2px solid rgba(255,255,255,.2);border-radius:16px;padding:14px 20px;font-size:25px;font-weight:600}
.ch .ok{background:rgba(246,195,67,.2);border-color:#f6c343}
b{font-weight:800}
"""

LOGO = '<svg width="58" height="54" viewBox="0 0 60 56" fill="none" stroke="#fff" stroke-width="2.4"><circle cx="30" cy="24" r="19"/><ellipse cx="30" cy="24" rx="8" ry="19"/><path d="M11 24h38M14 14h32M14 34h32"/><path d="M6 44c9-5 17-5 24 2 7-7 15-7 24-2M6 50c9-5 17-5 24 2 7-7 15-7 24-2" stroke="#f6c343" stroke-width="3"/></svg>'

def ic(d, size=38, sw=2.6, col='#14232d'):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{col}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{d}</svg>'
EYEOFF = '<path d="M3 3l18 18"/><path d="M10.6 5.1A10 10 0 0 1 12 5c5 0 9 5 9 7a11 11 0 0 1-2.6 3.4"/><path d="M6.6 6.6C4.3 8 3 10.3 3 12c0 2 4 7 9 7a9.6 9.6 0 0 0 5.4-1.6"/><path d="M9.9 9.9a3 3 0 0 0 4.2 4.2"/>'
BOOK = '<path d="M2 5c3-1.5 7-1.5 10 1 3-2.5 7-2.5 10-1v14c-3-1.5-7-1.5-10 1-3-2.5-7-2.5-10-1z"/><path d="M12 6v14"/>'
TAG = '<path d="M3 12V4h8l10 10-8 8z"/><circle cx="7.5" cy="8.5" r="1.5"/>'
TARGET = '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.5"/>'
PEN = '<path d="M5 4v7a7 7 0 0 0 14 0V4"/><path d="M4 21h16"/>'
CHECK = '<path d="M5 12.5l4.5 4.5L19 7.5"/>'
XX = '<path d="M6 6l12 12M18 6L6 18"/>'
BULB = '<path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2.1h5c0-.9.4-1.6 1-2.1A6 6 0 0 0 12 3z"/>'
SCISS = '<circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M8.1 8.1L20 20M8.1 15.9L20 4"/>'
LIST = '<path d="M9 6h11M9 12h11M9 18h11"/><path d="M4 6l1 1 2-2M4 12l1 1 2-2M4 18l1 1 2-2"/>'

def page(n, total, body, chap):
    w = n / total * 100
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="pg"><div class="gr"></div><div class="glow"></div>
<div class="hd"><div class="lg">{LOGO}<div>GLOBAL<br>MATH PREP</div></div><div class="pn">{n}/{total}</div></div>
<div class="mn">{body}</div>
<div class="ft"><div class="tr"><div class="tf" style="width:{w}%"></div></div><div class="fr"><span>@globalmathprep · globalmathprep.academy</span><span>SAT English · Ch {chap}</span></div></div>
</div></body></html>'''

def step(num, color, icon, h, p):
    return f'<div class="card"><div class="row"><div class="num">{num}</div><div style="flex:1"><div class="h">{h}</div><div class="p">{p}</div></div><div class="disc" style="background:{color}">{ic(icon)}</div></div></div>'

def enroll(nexttxt):
    return f'''<div class="bd">SAT ENGLISH · ENROLLMENT OPEN</div>
<h1 class="t" style="font-size:84px">SAT English<span style="font-size:60px">join our new group</span></h1>
<div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px;align-self:stretch">
<div class="st"><div class="n" style="font-size:50px">6</div><div class="l" style="font-size:19px">seats left</div></div>
<div class="st"><div class="n" style="font-size:50px">2–5</div><div class="l" style="font-size:19px">students per group</div></div>
<div class="st"><div class="n" style="font-size:50px">3×80</div><div class="l" style="font-size:19px">minutes a week</div></div>
<div class="st"><div class="n" style="font-size:50px">1</div><div class="l" style="font-size:19px">practice test every week</div></div></div>
<div style="display:flex;gap:20px;align-self:stretch">
<div class="card" style="flex:1.5;display:flex;flex-direction:column;gap:14px">
<div class="lab">SCHEDULE · MONGOLIA TIME</div>
<div style="display:flex;gap:10px">{''.join(f'<div style="flex:1;background:#f4efe3;color:#14232d;border-radius:14px;padding:12px 4px;text-align:center;font-weight:800;font-size:21px">{d}</div>' for d in ('Tuesday','Thursday','Friday'))}</div>
<div style="font-size:44px;font-weight:800">18:30–19:50</div>
<div style="display:flex;flex-direction:column;gap:8px;font-size:21px;font-weight:600;color:#e2f0f5">
<div>{ic(CHECK,24,3,Y)} Live on Zoom from Canada</div><div>{ic(CHECK,24,3,Y)} For the Nov &amp; Dec SAT</div><div>{ic(CHECK,24,3,Y)} Weekly report to parents</div></div></div>
<div style="flex:1;background:#fff;border-radius:28px;padding:22px 18px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;color:#14232d;text-align:center">
<img src="{QR}" style="width:210px;height:210px"><div style="font-size:25px;font-weight:800;line-height:1.15">Free placement test</div><div style="font-size:15px;font-weight:600;color:#3b5663">globalmathprep.academy/schedule</div></div></div>
<div style="align-self:stretch;display:flex;flex-wrap:wrap;justify-content:center;gap:8px">{''.join(f'<span class="pill" style="border:2px solid rgba(160,215,235,.45);background:rgba(255,255,255,.06);margin:0">{x}</span>' for x in ('Transitions','Student Notes','Punctuation','Grammar','Reading'))}</div>
<div class="tip" style="justify-content:center;text-align:center"><div>Message <b>“SAT English”</b> on WhatsApp<br><span style="font-size:32px;font-weight:800">+1 428 880 1826</span></div></div>
<div class="swipe" style="font-size:21px">{nexttxt}</div>'''

TYPES = [('Continue', GREEN, '+', 'adds more of the same idea', ['moreover', 'furthermore', 'in addition', 'likewise', 'similarly']),
         ('Contradict', CORAL, '≠', 'goes against the idea before', ['however', 'nevertheless', 'nonetheless', 'in contrast', 'still']),
         ('Cause & effect', Y, '→', 'shows a result', ['therefore', 'thus', 'hence', 'consequently', 'accordingly']),
         ('Example', BLUE, 'e.g.', 'gives a specific case', ['for example', 'for instance']),
         ('Emphasis', PURPLE, '!', 'says it again, more strongly', ['in fact', 'indeed', 'that is', 'in other words', 'namely'])]

def rgba(hexc, a):
    h = hexc.lstrip('#'); r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return f'rgba({r},{g},{b},{a})'

C1 = []
# 1 cover
C1.append(f'''<div style="width:560px;height:250px;border-radius:44px;background:linear-gradient(160deg,rgba(110,190,215,.3),rgba(40,110,140,.25));border:2px solid rgba(160,215,235,.28);box-shadow:0 0 0 14px rgba(255,255,255,.03),0 30px 60px rgba(0,0,0,.35);display:flex;align-items:center;justify-content:center">
<svg width="480" height="190" viewBox="0 0 480 190"><rect x="10" y="50" width="170" height="120" rx="16" fill="#f4efe3"/><text x="95" y="96" text-anchor="middle" font-family="M" font-weight="800" font-size="22" fill="#14232d">Idea A</text><path d="M40 125h110M40 147h80" stroke="#9fb4bd" stroke-width="8" stroke-linecap="round"/>
<rect x="300" y="50" width="170" height="120" rx="16" fill="#f4efe3"/><text x="385" y="96" text-anchor="middle" font-family="M" font-weight="800" font-size="22" fill="#14232d">Idea B</text><path d="M330 125h110M330 147h80" stroke="#9fb4bd" stroke-width="8" stroke-linecap="round"/>
<path d="M185 110h108" stroke="#7fdcf2" stroke-width="7" stroke-linecap="round" stroke-dasharray="2 14"/><path d="M280 98l14 12-14 12" stroke="#7fdcf2" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<rect x="160" y="8" width="160" height="50" rx="25" fill="#f6c343"/><text x="240" y="42" text-anchor="middle" font-family="M" font-weight="800" font-size="25" fill="#14232d">however?</text></svg></div>
<div class="bd">SAT ENGLISH · CHAPTER 1</div>
<h1 class="t" style="font-size:96px">Transitions<span style="font-size:66px">made simple</span></h1>
<div class="sub">Pick the word that links two ideas.<br><b style="color:#f6c343">It is logic, not grammar.</b></div>
<div class="stats"><div class="st"><div class="n">5</div><div class="l">relationship<br>types</div></div><div class="st"><div class="n">3</div><div class="l">steps to<br>the answer</div></div><div class="st"><div class="n">2</div><div class="l">traps to<br>avoid</div></div></div>
<div class="swipe">SWIPE TO LEARN →</div>''')
# 2 method
C1.append(f'''<div class="bd">STEP 1 · THE METHOD</div>
<h1 class="t">One method<span>three moves</span></h1>
{step(1, CORAL, EYEOFF, 'Cover the blank', 'Hide the transition and the answer choices.')}
{step(2, BLUE, BOOK, 'Read both sides', 'Read the sentence before and the sentence after.')}
{step(3, GREEN, TAG, 'Name the link', 'Say the relationship yourself, then find the matching choice.')}
<div class="tip">{ic(BULB,44,2.4)}<div>Choices that <b>sound nice</b> are the trap. Decide first, then look.</div></div>''')
# 3 five types
rows = ''.join(f'<div class="card" style="padding:16px 26px"><div class="row"><div class="disc" style="background:{c};width:66px;height:66px;font-size:{26 if len(s)>1 else 36}px">{s}</div><div style="flex:1"><div class="h" style="font-size:30px;color:{c}">{n.replace("&","&amp;")}</div><div class="p" style="margin-top:2px">{m}</div></div></div></div>' for n, c, s, m, _ in TYPES)
C1.append(f'''<div class="bd">STEP 2 · KNOW THE TYPES</div>
<h1 class="t">5 ways ideas<span>connect</span></h1>
<div style="align-self:stretch;display:flex;flex-direction:column;gap:14px">{rows}</div>''')
# 4 word bank
def wcard(n, c, s, m, words, span=False):
    pills = ''.join(f'<span class="pill" style="background:{rgba(c,.16)};border:2px solid {rgba(c,.6)};color:#fff">{w}</span>' for w in words)
    return f'<div class="card" style="padding:18px 22px;{"grid-column:1 / -1;" if span else ""}"><div class="row" style="gap:14px;margin-bottom:8px"><div class="disc" style="background:{c};width:48px;height:48px;font-size:{18 if len(s)>1 else 26}px">{s}</div><div class="h" style="font-size:27px;color:{c}">{n.replace("&","&amp;")}</div></div><div>{pills}</div></div>'
cards = ''.join(wcard(*t, span=(i == 4)) for i, t in enumerate(TYPES))
C1.append(f'''<div class="bd">STEP 3 · WORD BANK</div>
<h1 class="t">The words<span>for each type</span></h1>
<div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;align-self:stretch">{cards}</div>
<div class="tip">{ic(BULB,44,2.4)}<div>Name the type, then find <b>one of its words</b> in the choices.</div></div>''')
# 5 trap 1
C1.append(f'''<div class="bd">TRAP 1 · TWINS</div>
<h1 class="t">Same job?<span>Both are wrong</span></h1>
<div class="card" style="padding:30px"><div style="display:flex;align-items:center;justify-content:center;gap:22px">
<div style="text-align:center"><div class="pill" style="background:{rgba(CORAL,.2)};border:2px solid {CORAL};font-size:30px;padding:12px 26px;margin:0;text-decoration:line-through;text-decoration-thickness:3px">however</div><div style="margin-top:10px;font-size:20px;font-weight:700;color:{CORAL}">contradict</div></div>
<div style="font-size:60px;font-weight:800;color:{CORAL}">=</div>
<div style="text-align:center"><div class="pill" style="background:{rgba(CORAL,.2)};border:2px solid {CORAL};font-size:30px;padding:12px 26px;margin:0;text-decoration:line-through;text-decoration-thickness:3px">nevertheless</div><div style="margin-top:10px;font-size:20px;font-weight:700;color:{CORAL}">contradict</div></div></div>
<div class="p" style="text-align:center;margin-top:22px;font-size:26px;color:#fff">A question has only <b>one</b> right answer, so twins cancel out.</div></div>
<div class="card"><div class="row"><div class="disc" style="background:{GREEN}">{ic(CHECK,40,3)}</div><div><div class="h" style="font-size:30px">Only one fits the type?</div><div class="p">It wins by default, even if you don’t love it.</div></div></div></div>''')
# 6 trap 2
C1.append(f'''<div class="bd">TRAP 2 · LOOK BACK</div>
<h1 class="t">A transition<span>points backward</span></h1>
<div class="card" style="padding:30px;display:flex;flex-direction:column;gap:14px">
<div class="ex" style="border:4px solid #7fdcf2">① The first trial <b>failed</b>.</div>
<div style="display:flex;align-items:center;gap:14px;padding-left:40px;color:#7fdcf2;font-weight:800;font-size:23px">{ic('<path d="M12 20V4M5 11l7-7 7 7"/>',40,3,'#7fdcf2')} compare with the sentence BEFORE</div>
<div class="ex">② The second trial <b>succeeded</b>, <span class="hl">however</span>.</div></div>
<div class="card"><div class="row"><div class="disc" style="background:{Y}">{ic(TARGET,40,2.6)}</div><div><div class="h" style="font-size:30px">Start, middle or end</div><div class="p">Wherever it sits, the transition links to the <b style="color:#fff">previous</b> idea.</div></div></div></div>''')
# 7 example
C1.append(f'''<div class="bd">PRACTICE · TRY IT</div>
<h1 class="t" style="font-size:70px">Worked example</h1>
<div class="card" style="padding:28px 30px"><div class="lab" style="margin-bottom:12px">GMP PRACTICE QUESTION</div>
<div style="font-size:28px;line-height:1.5;font-weight:500">The bridge was built with low-grade steel to cut costs. <span style="border-bottom:3px solid #fff">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span> cracks appeared in its supports within five years.</div>
<div class="ch"><div>A) However,</div><div class="ok">B) Consequently,</div><div>C) For example,</div><div>D) Similarly,</div></div></div>
<div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;align-self:stretch">
<div class="st" style="padding:18px 14px"><div class="disc" style="background:{CORAL};width:54px;height:54px;margin:0 auto">{ic(EYEOFF,28)}</div><div class="l" style="margin-top:10px">Cover</div><div class="p" style="font-size:20px">hide the blank</div></div>
<div class="st" style="padding:18px 14px"><div class="disc" style="background:{BLUE};width:54px;height:54px;margin:0 auto">{ic(BOOK,28)}</div><div class="l" style="margin-top:10px">Read</div><div class="p" style="font-size:20px">cheap steel → cracks</div></div>
<div class="st" style="padding:18px 14px"><div class="disc" style="background:{Y};width:54px;height:54px;margin:0 auto;font-size:28px">→</div><div class="l" style="margin-top:10px">Name</div><div class="p" style="font-size:20px">cause &amp; effect</div></div></div>
<div class="tip" style="justify-content:center"><div>Answer: <b>B) Consequently</b> · A, C, D are the wrong type</div></div>''')
C1.append(enroll('NEXT SERIES: CHAPTER 2 · STUDENT NOTES →'))

C2 = []
C2.append(f'''<div style="width:560px;height:250px;border-radius:44px;background:linear-gradient(160deg,rgba(110,190,215,.3),rgba(40,110,140,.25));border:2px solid rgba(160,215,235,.28);box-shadow:0 0 0 14px rgba(255,255,255,.03),0 30px 60px rgba(0,0,0,.35);display:flex;align-items:center;justify-content:center">
<svg width="480" height="190" viewBox="0 0 480 190"><rect x="10" y="20" width="150" height="160" rx="16" fill="#f4efe3"/><circle cx="36" cy="60" r="6" fill="#134560"/><circle cx="36" cy="100" r="6" fill="#134560"/><circle cx="36" cy="140" r="6" fill="#134560"/><path d="M52 60h82M52 100h70M52 140h60" stroke="#9fb4bd" stroke-width="8" stroke-linecap="round"/>
<path d="M170 100h40" stroke="#7fdcf2" stroke-width="7" stroke-linecap="round"/><path d="M198 88l14 12-14 12" stroke="#7fdcf2" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="275" cy="100" r="52" fill="#134560" stroke="#f4efe3" stroke-width="7"/><circle cx="275" cy="100" r="32" fill="none" stroke="#7fdcf2" stroke-width="7"/><circle cx="275" cy="100" r="12" fill="#f6c343"/>
<path d="M335 100h40" stroke="#7fdcf2" stroke-width="7" stroke-linecap="round"/><path d="M363 88l14 12-14 12" stroke="#7fdcf2" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="430" cy="100" r="40" fill="#5fd6a8"/><path d="M412 101l12 12 24-26" stroke="#14232d" stroke-width="9" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<text x="85" y="15" text-anchor="middle" font-family="M" font-weight="800" font-size="0" fill="#fff">.</text></svg></div>
<div class="bd">SAT ENGLISH · CHAPTER 2</div>
<h1 class="t" style="font-size:92px">Student Notes<span style="font-size:66px">made simple</span></h1>
<div class="sub">Notes → goal → answer.<br><b style="color:#f6c343">The goal decides everything.</b></div>
<div class="stats"><div class="st"><div class="n">3</div><div class="l">steps to<br>the answer</div></div><div class="st"><div class="n">4</div><div class="l">goal types<br>to spot</div></div><div class="st"><div class="n">1</div><div class="l">big trap:<br>the near-miss</div></div></div>
<div class="swipe">SWIPE TO LEARN →</div>''')
C2.append(f'''<div class="bd">STEP 1 · THE METHOD</div>
<h1 class="t">Goal first<span>notes later</span></h1>
{step(1, Y, TARGET, 'Read the goal', 'Start with “The student wants to…”, not the notes.')}
{step(2, BLUE, PEN, 'Underline key words', '<i>contrast, similarity, emphasize, introduce…</i>')}
{step(3, GREEN, CHECK, 'Match every part', 'Pick the choice that does the whole goal.')}
<div class="tip">{ic(BULB,44,2.4)}<div>You rarely need every note. <b>Goal + choices</b> are usually enough.</div></div>''')
def cell(ok):
    return f'<div class="disc" style="width:58px;height:58px;margin:0 auto;background:{GREEN if ok else CORAL}">{ic(CHECK if ok else XX,32,3.2)}</div>'
trs = ''.join(f'<div style="display:grid;grid-template-columns:1.5fr 1fr 1fr;align-items:center;padding:18px 0;border-top:1px solid rgba(255,255,255,.15)"><div style="font-size:27px;font-weight:700">{q}</div>{cell(a)}{cell(b)}</div>' for q, a, b in (('Is it true?', 1, 1), ('Is it from the notes?', 1, 1), ('Does it meet the goal?', 0, 1)))
C2.append(f'''<div class="bd">STEP 2 · THE REAL TEST</div>
<h1 class="t">True is not<span>enough</span></h1>
<div class="card" style="padding:26px 34px"><div style="display:grid;grid-template-columns:1.5fr 1fr 1fr;padding-bottom:14px;text-align:center;font-size:22px;font-weight:800;letter-spacing:2px"><div></div><div style="color:{CORAL}">WRONG<br>ANSWER</div><div style="color:{GREEN}">RIGHT<br>ANSWER</div></div>{trs}</div>
<div class="tip">{ic(BULB,44,2.4)}<div>Don’t ask “Is it true?” Ask <b>“Does it do the goal?”</b></div></div>''')
ARR = ic('<path d="M5 12h14M13 6l6 6-6 6"/>',36,3,'#7fdcf2')
G = [('contrast', CORAL, '≠', '<i>whereas · although · while · but</i>'),
     ('similarity', GREEN, '=', '<i>both · similarly · like · also</i>'),
     ('new audience', BLUE, 'i', 'the <b>longest</b> choice, with background'),
     ('A and B', PURPLE, '2', 'a choice with <b>both</b> parts')]
grow = ''.join(f'<div class="card" style="padding:18px 24px"><div class="row" style="gap:18px"><div class="disc" style="background:{c};width:62px;height:62px;font-size:30px">{s}</div><div style="width:230px;flex:none"><div style="font-size:17px;font-weight:800;letter-spacing:2px;color:#9fd2e2">GOAL SAYS</div><div class="h" style="font-size:29px;color:{c}">{g}</div></div>{ARR}<div style="flex:1"><div style="font-size:17px;font-weight:800;letter-spacing:2px;color:#9fd2e2">LOOK FOR</div><div style="font-size:25px;font-weight:600;line-height:1.3">{l}</div></div></div></div>' for g, c, s, l in G)
C2.append(f'''<div class="bd">STEP 3 · SIGNAL WORDS</div>
<h1 class="t">Goal words<span>point to answers</span></h1>
<div style="align-self:stretch;display:flex;flex-direction:column;gap:14px">{grow}</div>''')
def bar(frac, col, label, verdict, vcol, ok):
    return f'<div style="margin-top:18px"><div style="display:flex;justify-content:space-between;font-size:24px;font-weight:700;margin-bottom:10px"><span>{label}</span><span style="color:{vcol}">{verdict}</span></div><div style="height:30px;border-radius:16px;background:rgba(255,255,255,.12);overflow:hidden"><div style="height:30px;width:{frac}%;background:{col};border-radius:16px"></div></div></div>'
C2.append(f'''<div class="bd">TRAP · THE NEAR-MISS</div>
<h1 class="t">Half right<span>is still wrong</span></h1>
<div class="card" style="padding:28px 32px"><div class="lab">THE GOAL HAS 2 PARTS</div>
<div style="font-size:28px;font-weight:600;margin-top:10px;line-height:1.4">The student wants to present the study’s <span class="pill" style="background:{Y};color:#14232d;margin:0 4px">method</span> and its <span class="pill" style="background:#7fdcf2;color:#14232d;margin:0 4px">result</span>.</div>
{bar(50, CORAL, 'Choice gives only the result', '1 of 2 · near-miss', CORAL, 0)}
{bar(100, GREEN, 'Choice gives method + result', '2 of 2 · correct', GREEN, 1)}</div>
<div class="tip">{ic(LIST,44,2.4)}<div><b>Count the parts</b> of the goal. Check each choice against every part.</div></div>''')
C2.append(f'''<div class="bd">PRACTICE · TRY IT</div>
<h1 class="t" style="font-size:66px">Worked example</h1>
<div class="card" style="padding:22px 28px"><div class="lab" style="margin-bottom:8px">STUDENT NOTES</div>
<div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px">
<div style="background:#f4efe3;color:#14232d;border-radius:16px;padding:14px 18px"><div style="font-weight:800;font-size:24px">Mount Everest</div><div style="font-size:21px;font-weight:600;line-height:1.4">8,849 meters tall<br>Nepal–China border</div></div>
<div style="background:#f4efe3;color:#14232d;border-radius:16px;padding:14px 18px"><div style="font-weight:800;font-size:24px">K2</div><div style="font-size:21px;font-weight:600;line-height:1.4">8,611 meters tall<br>Pakistan–China border</div></div></div>
<div style="margin-top:14px;font-size:24px;font-weight:600">Goal: <span class="pill" style="background:{CORAL};color:#14232d;margin:0 4px;font-size:21px">contrast</span> the <span class="pill" style="background:{Y};color:#14232d;margin:0 4px;font-size:21px">heights</span> of the two mountains.</div>
<div style="display:flex;flex-direction:column;gap:9px;margin-top:14px;font-size:21px;font-weight:600">
<div style="background:rgba(255,255,255,.07);border:2px solid rgba(255,255,255,.2);border-radius:14px;padding:10px 16px">A) Mount Everest lies on the border of Nepal and China.</div>
<div style="background:rgba(255,255,255,.07);border:2px solid rgba(255,255,255,.2);border-radius:14px;padding:10px 16px">B) Both Mount Everest and K2 lie on China’s border.</div>
<div style="background:rgba(246,195,67,.2);border:2px solid #f6c343;border-radius:14px;padding:10px 16px">C) Whereas Mount Everest is 8,849 meters tall, K2 is 8,611 meters tall.</div>
<div style="background:rgba(255,255,255,.07);border:2px solid rgba(255,255,255,.2);border-radius:14px;padding:10px 16px">D) K2, which is 8,611 meters tall, lies on the border of Pakistan and China.</div></div></div>
<div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;align-self:stretch;font-size:19px;font-weight:700;text-align:center">
<div class="st" style="padding:14px 10px"><span style="color:{CORAL}">A ✗</span><br>no heights</div><div class="st" style="padding:14px 10px"><span style="color:{CORAL}">B ✗</span><br>similarity, not contrast</div><div class="st" style="padding:14px 10px"><span style="color:{CORAL}">D ✗</span><br>only one height</div></div>
<div class="tip" style="justify-content:center;padding:16px 24px"><div>Answer: <b>C</b> · <i>whereas</i> = contrast + both heights</div></div>''')
C2.append(f'''<div class="bd">STEP 4 · CHECKLIST</div>
<h1 class="t">Your 3-step<span>checklist</span></h1>
{step(1, Y, PEN, 'Underline the goal', 'Mark its key words and count its parts.')}
{step(2, CORAL, SCISS, 'Cut the off-topic', 'Cross out choices that miss the goal’s topic.')}
{step(3, GREEN, CHECK, 'Pick the full match', 'Keep the one that covers every part.')}
<div class="tip">{ic(BULB,44,2.4)}<div>Two left? Take the one that meets the goal <b>most directly</b>.</div></div>''')
C2.append(enroll('NEXT SERIES COMING SOON →'))

out = HERE / 'out'; out.mkdir(exist_ok=True)
with sync_playwright() as p:
    br = p.chromium.launch(); pg = br.new_page(viewport={'width': 1080, 'height': 1350})
    for chap, slides in ((1, C1), (2, C2)):
        for i, body in enumerate(slides, 1):
            html = page(i, len(slides), body, chap)
            pg.set_content(html); pg.wait_for_timeout(250)
            ov = pg.evaluate("()=>{const m=document.querySelector('.mn');const r=m.getBoundingClientRect();let top=1e9,bot=0;for(const c of m.children){const b=c.getBoundingClientRect();top=Math.min(top,b.top);bot=Math.max(bot,b.bottom)}return [Math.round(top),Math.round(bot),Math.round(r.top),Math.round(r.bottom)]}")
            fn = out / f'SAT-English-v2-Ch{chap}-{i}-of-8.png'
            pg.screenshot(path=str(fn))
            print(fn.name, ov)
    br.close()
