import base64, pathlib
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).parent
FD = HERE.parent / 'poster/fonts/package/files'
ff = ''
for w in (500, 600, 700, 800):
    for sub in ('latin', 'latin-ext'):
        p = FD / f'montserrat-{sub}-{w}-normal.woff2'
        if p.exists():
            ff += "@font-face{font-family:M;font-weight:%d;src:url(data:font/woff2;base64,%s)}\n" % (w, base64.b64encode(p.read_bytes()).decode())
QR = 'data:image/svg+xml;base64,' + base64.b64encode((HERE / 'qr.svg').read_bytes()).decode()

Y = '#f6c343'; CY = '#c9f2ff'; INK = '#14232d'
GREEN = '#5fd6a8'; CORAL = '#ff8a80'; BLUE = '#7cc2ff'; PURPLE = '#c9a6ff'; TEAL = '#7fdcf2'

def rgba(hexc, a):
    h = hexc.lstrip('#'); return f'rgba({int(h[0:2],16)},{int(h[2:4],16)},{int(h[4:6],16)},{a})'

CSS = ff + """
*{box-sizing:border-box}
body{margin:0;width:1080px;height:1350px;font-family:M,sans-serif;color:#fff;overflow:hidden}
.pg{width:1080px;height:1350px;position:relative;overflow:hidden;background:radial-gradient(ellipse at 50% 8%,#24698a 0%,#134560 40%,#092131 100%)}
.gr{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.03) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.03) 1px,transparent 1px);background-size:54px 54px}
.o1{position:absolute;width:620px;height:620px;border-radius:50%;background:radial-gradient(circle,rgba(246,195,67,.13),transparent 65%);right:-240px;bottom:-180px}
.o2{position:absolute;width:560px;height:560px;border-radius:50%;background:radial-gradient(circle,rgba(127,220,242,.12),transparent 65%);left:-240px;top:260px}
.hd{position:absolute;top:46px;left:56px;right:56px;display:flex;justify-content:space-between;align-items:center}
.lg{display:flex;align-items:center;gap:12px;font-weight:800;font-size:20px;line-height:1.15;letter-spacing:1.5px}
.pn{border:2px solid rgba(160,215,235,.35);background:rgba(255,255,255,.07);border-radius:30px;padding:8px 20px;font-weight:800;font-size:22px}
.ft{position:absolute;left:56px;right:56px;bottom:40px}
.tr{height:6px;border-radius:6px;background:rgba(255,255,255,.14);margin-bottom:18px;overflow:hidden}
.tf{height:6px;background:linear-gradient(90deg,#f6c343,#ffd978);border-radius:6px}
.fr{display:flex;justify-content:space-between;font-size:20px;font-weight:600;color:#cfe3ea}
.mn{position:absolute;top:128px;left:56px;right:56px;bottom:108px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:28px}
.bd{background:#f6c343;color:#14232d;border-radius:40px;padding:12px 30px;font-weight:800;font-size:25px;letter-spacing:3px;box-shadow:0 10px 24px rgba(0,0,0,.3)}
.t{margin:0;text-align:center;font-weight:800;font-size:96px;line-height:1;letter-spacing:-1px;text-shadow:0 6px 24px rgba(0,0,0,.35)}
.t span{display:block;color:#c9f2ff}
.card{align-self:stretch;background:linear-gradient(145deg,rgba(255,255,255,.12),rgba(255,255,255,.04));border:1.5px solid rgba(255,255,255,.16);box-shadow:inset 0 1px 0 rgba(255,255,255,.18),0 18px 40px rgba(0,0,0,.28);border-radius:32px;padding:26px 30px}
.row{display:flex;align-items:center;gap:24px}
.num{flex:none;width:86px;height:86px;border-radius:26px;background:linear-gradient(145deg,#ffd978,#f6c343);color:#14232d;font-weight:800;font-size:48px;display:flex;align-items:center;justify-content:center;box-shadow:0 8px 18px rgba(0,0,0,.3)}
.disc{flex:none;width:86px;height:86px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#14232d;font-weight:800;font-size:40px;box-shadow:0 8px 18px rgba(0,0,0,.28)}
.h{font-size:42px;font-weight:800;line-height:1.1}
.p{font-size:30px;font-weight:600;color:#d3e8f0;line-height:1.3;margin-top:6px}
.tip{align-self:stretch;background:linear-gradient(135deg,#ffd978,#f6c343);color:#14232d;border-radius:28px;padding:22px 30px;font-weight:700;font-size:31px;line-height:1.3;display:flex;gap:20px;align-items:center;box-shadow:0 12px 26px rgba(0,0,0,.3)}
.tip b{font-weight:800}
.stats{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px;align-self:stretch}
.st{background:linear-gradient(160deg,rgba(255,255,255,.13),rgba(255,255,255,.04));border:1.5px solid rgba(255,255,255,.16);box-shadow:inset 0 1px 0 rgba(255,255,255,.18);border-radius:30px;padding:24px 10px;text-align:center}
.st .n{font-size:84px;font-weight:800;color:#f6c343;line-height:1}
.st .l{font-size:27px;font-weight:700;margin-top:8px;line-height:1.2}
.tok{display:inline-flex;align-items:center;gap:10px;padding:10px 22px;border-radius:40px;font-weight:700;font-size:29px;line-height:1.2}
.sub{text-align:center;font-size:36px;font-weight:700;line-height:1.3}
.swipe{font-size:26px;font-weight:800;color:#c9f2ff;letter-spacing:2px}
.ex{background:#f7f2e7;color:#14232d;border-radius:24px;padding:24px 28px;font-size:34px;line-height:1.4;font-weight:600}
.hl{background:#f6c343;border-radius:10px;padding:0 10px;font-weight:800}
.lab{font-size:22px;font-weight:800;letter-spacing:3px;color:#7fdcf2}
b{font-weight:800}
"""

LOGO = '<svg width="54" height="50" viewBox="0 0 60 56" fill="none" stroke="#fff" stroke-width="2.4"><circle cx="30" cy="24" r="19"/><ellipse cx="30" cy="24" rx="8" ry="19"/><path d="M11 24h38M14 14h32M14 34h32"/><path d="M6 44c9-5 17-5 24 2 7-7 15-7 24-2M6 50c9-5 17-5 24 2 7-7 15-7 24-2" stroke="#f6c343" stroke-width="3"/></svg>'

def ic(d, size=44, sw=2.6, col=INK):
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
UP = '<path d="M12 20V4M5 11l7-7 7 7"/>'
ARR = '<path d="M4 12h15M13 6l6 6-6 6"/>'

def page(n, total, body, chap):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="pg"><div class="gr"></div><div class="o1"></div><div class="o2"></div>
<div class="hd"><div class="lg">{LOGO}<div>GLOBAL<br>MATH PREP</div></div><div class="pn">{n}/{total}</div></div>
<div class="mn">{body}</div>
<div class="ft"><div class="tr"><div class="tf" style="width:{n/total*100}%"></div></div><div class="fr"><span>@globalmathprep · globalmathprep.academy</span><span>SAT English · Ch {chap}</span></div></div>
</div></body></html>'''

def tip(txt, icon=BULB):
    return f'<div class="tip">{ic(icon,50,2.4)}<div>{txt}</div></div>'

def step(num, color, icon, h, p):
    return f'<div class="card"><div class="row"><div class="num">{num}</div><div style="flex:1"><div class="h">{h}</div><div class="p">{p}</div></div><div class="disc" style="background:{color}">{ic(icon,46)}</div></div></div>'

def hero(svg):
    return f'<div style="width:620px;height:260px;border-radius:48px;background:linear-gradient(160deg,rgba(127,220,242,.28),rgba(40,110,140,.18));border:2px solid rgba(160,215,235,.3);box-shadow:0 0 0 16px rgba(255,255,255,.03),0 30px 60px rgba(0,0,0,.35);display:flex;align-items:center;justify-content:center">{svg}</div>'

def enroll(nexttxt):
    days = ''.join(f'<div style="flex:1;background:#f7f2e7;color:{INK};border-radius:18px;padding:14px 4px;text-align:center;font-weight:800;font-size:27px">{d}</div>' for d in ('Tue', 'Thu', 'Fri'))
    chk = ''.join(f'<div style="display:flex;align-items:center;gap:12px">{ic(CHECK,32,3.2,Y)}<span>{x}</span></div>' for x in ('Live on Zoom', 'Nov &amp; Dec SAT', 'Weekly parent report'))
    toks = ''.join(f'<span class="tok" style="font-size:25px;padding:9px 20px;border:2px solid rgba(160,215,235,.45);background:rgba(255,255,255,.07)">{x}</span>' for x in ('Transitions', 'Student Notes', 'Punctuation', 'Grammar'))
    stat = lambda n, l: f'<div class="st" style="padding:20px 6px"><div class="n" style="font-size:62px">{n}</div><div class="l" style="font-size:23px">{l}</div></div>'
    return f'''<div class="bd">ENROLLMENT OPEN</div>
<h1 class="t" style="font-size:100px">SAT English<span style="font-size:62px;margin-top:8px">new group starts now</span></h1>
<div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px;align-self:stretch">{stat('6','seats left')}{stat('2–5','per group')}{stat('3×','a week')}{stat('80','min / class')}</div>
<div style="display:flex;gap:18px;align-self:stretch">
<div class="card" style="flex:1.45;display:flex;flex-direction:column;gap:16px;padding:26px">
<div class="lab">MONGOLIA TIME</div><div style="display:flex;gap:10px">{days}</div>
<div style="font-size:60px;font-weight:800;line-height:1">18:30<span style="color:#9fd2e2">–</span>19:50</div>
<div style="display:flex;flex-direction:column;gap:10px;font-size:26px;font-weight:700">{chk}</div></div>
<div style="flex:1;background:#fff;border-radius:32px;padding:22px 16px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;color:{INK};text-align:center">
<img src="{QR}" style="width:230px;height:230px"><div style="font-size:30px;font-weight:800;line-height:1.1">FREE<br>level test</div></div></div>
<div style="display:flex;flex-wrap:wrap;justify-content:center;gap:10px">{toks}</div>
<div class="tip" style="justify-content:center;text-align:center;padding:20px"><div>WhatsApp <b>“SAT English”</b><br><span style="font-size:44px;font-weight:800">+1 428 880 1826</span></div></div>'''

TYPES = [('Continue', GREEN, '+', 'more of the same', ['moreover', 'in addition', 'likewise', 'similarly']),
         ('Contradict', CORAL, '≠', 'the opposite turn', ['however', 'nevertheless', 'in contrast', 'still']),
         ('Cause &amp; effect', Y, '→', 'a result', ['therefore', 'thus', 'hence', 'consequently']),
         ('Example', BLUE, 'e.g.', 'a specific case', ['for example', 'for instance']),
         ('Emphasis', PURPLE, '!', 'same idea, stronger', ['in fact', 'indeed', 'in other words', 'namely'])]

C1 = []
C1.append(f'''{hero('<svg width="540" height="200" viewBox="0 0 540 200"><rect x="10" y="60" width="190" height="130" rx="20" fill="#f7f2e7"/><text x="105" y="112" text-anchor="middle" font-family="M" font-weight="800" font-size="30" fill="#14232d">Idea A</text><path d="M44 145h122M44 168h86" stroke="#9fb4bd" stroke-width="9" stroke-linecap="round"/><rect x="340" y="60" width="190" height="130" rx="20" fill="#f7f2e7"/><text x="435" y="112" text-anchor="middle" font-family="M" font-weight="800" font-size="30" fill="#14232d">Idea B</text><path d="M374 145h122M374 168h86" stroke="#9fb4bd" stroke-width="9" stroke-linecap="round"/><path d="M208 125h118" stroke="#7fdcf2" stroke-width="8" stroke-linecap="round" stroke-dasharray="2 16"/><path d="M314 111l16 14-16 14" stroke="#7fdcf2" stroke-width="8" fill="none" stroke-linecap="round" stroke-linejoin="round"/><rect x="170" y="4" width="200" height="60" rx="30" fill="#f6c343"/><text x="270" y="45" text-anchor="middle" font-family="M" font-weight="800" font-size="31" fill="#14232d">however?</text></svg>')}
<div class="bd">SAT ENGLISH · CHAPTER 1</div>
<h1 class="t" style="font-size:118px">Transitions<span style="font-size:74px;margin-top:6px">made simple</span></h1>
<div class="sub">Link two ideas.<br><span style="color:#f6c343">Logic, not grammar.</span></div>
<div class="stats"><div class="st"><div class="n">5</div><div class="l">link<br>types</div></div><div class="st"><div class="n">3</div><div class="l">easy<br>steps</div></div><div class="st"><div class="n">2</div><div class="l">traps to<br>avoid</div></div></div>
<div class="swipe">SWIPE →</div>''')
C1.append(f'''<div class="bd">STEP 1 · METHOD</div>
<h1 class="t">One method<span>3 moves</span></h1>
{step(1, CORAL, EYEOFF, 'Cover', 'Hide the answer choices')}
{step(2, BLUE, BOOK, 'Read', 'The sentence before + after')}
{step(3, GREEN, TAG, 'Name', 'The link, then find its match')}
{tip('Sounds nice ≠ right.<br><b>Decide first, then look.</b>')}''')
rows = ''.join(f'<div class="card" style="padding:18px 26px"><div class="row"><div class="disc" style="background:{c};font-size:{30 if len(s)>1 else 46}px">{s}</div><div><div class="h" style="font-size:42px;color:{c}">{n}</div><div class="p" style="margin-top:2px">{m}</div></div></div></div>' for n, c, s, m, _ in TYPES)
C1.append(f'''<div class="bd">STEP 2 · TYPES</div>
<h1 class="t">5 link types</h1>
<div style="align-self:stretch;display:flex;flex-direction:column;gap:14px">{rows}</div>''')
def wcard(n, c, s, words, span=False):
    toks = ''.join(f'<span class="tok" style="font-size:27px;padding:8px 18px;margin:0 8px 10px 0;background:{rgba(c,.18)};border:2px solid {rgba(c,.7)}">{w}</span>' for w in words)
    return f'<div class="card" style="padding:20px 22px;{"grid-column:1 / -1;" if span else ""}"><div class="row" style="gap:14px;margin-bottom:14px"><div class="disc" style="background:{c};width:58px;height:58px;font-size:{22 if len(s)>1 else 32}px">{s}</div><div class="h" style="font-size:32px;color:{c}">{n}</div></div><div style="display:flex;flex-wrap:wrap">{toks}</div></div>'
cards = ''.join(wcard(n, c, s, w, i == 4) for i, (n, c, s, m, w) in enumerate(TYPES))
C1.append(f'''<div class="bd">STEP 3 · WORD BANK</div>
<h1 class="t">Word bank</h1>
<div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;align-self:stretch">{cards}</div>
{tip('Name the type → <b>find its word.</b>')}''')
twin = lambda w: f'<div style="text-align:center"><span class="tok" style="font-size:38px;padding:14px 30px;background:{rgba(CORAL,.2)};border:3px solid {CORAL};text-decoration:line-through;text-decoration-thickness:4px">{w}</span><div style="margin-top:12px;font-size:25px;font-weight:800;color:{CORAL};letter-spacing:2px">CONTRADICT</div></div>'
C1.append(f'''<div class="bd">TRAP 1 · TWINS</div>
<h1 class="t">Same job?<span>Both wrong</span></h1>
<div class="card" style="padding:36px 26px"><div style="display:flex;align-items:center;justify-content:center;gap:18px">{twin('however')}<div style="font-size:72px;font-weight:800;color:{CORAL}">=</div>{twin('nevertheless')}</div>
<div style="text-align:center;margin-top:28px;font-size:34px;font-weight:700">Only <b style="color:#f6c343">1</b> answer can be right.</div></div>
<div class="card"><div class="row"><div class="disc" style="background:{GREEN}">{ic(CHECK,48,3)}</div><div><div class="h" style="font-size:40px">Only one fits?</div><div class="p">It wins. Pick it.</div></div></div></div>''')
C1.append(f'''<div class="bd">TRAP 2 · LOOK BACK</div>
<h1 class="t">Look back<span>one sentence</span></h1>
<div class="card" style="padding:30px;display:flex;flex-direction:column;gap:18px">
<div class="ex" style="border:5px solid {TEAL}"><span style="color:#5a7c8a">①</span> The first trial <b>failed</b>.</div>
<div style="display:flex;align-items:center;gap:14px;padding-left:30px;color:{TEAL};font-weight:800;font-size:28px">{ic(UP,48,3,TEAL)} compare with this</div>
<div class="ex"><span style="color:#5a7c8a">②</span> The second trial <b>succeeded</b>, <span class="hl">however</span>.</div></div>
<div style="display:flex;gap:12px;align-items:center;justify-content:center;flex-wrap:wrap">{''.join(f'<span class="tok" style="background:rgba(255,255,255,.1);border:2px solid rgba(255,255,255,.25)">{x}</span>' for x in ('Start','Middle','End'))}<span style="font-size:30px;font-weight:800">→ links back</span></div>''')
chs = ''.join(f'<div style="background:{rgba(Y,.22) if ok else "rgba(255,255,255,.08)"};border:2.5px solid {Y if ok else "rgba(255,255,255,.22)"};border-radius:18px;padding:16px 20px;font-size:30px;font-weight:700">{t}</div>' for t, ok in (('A) However,',0),('B) Consequently,',1),('C) For example,',0),('D) Similarly,',0)))
sol = lambda col, icon, t: f'<div class="st" style="padding:18px 8px"><div class="disc" style="background:{col};width:66px;height:66px;margin:0 auto">{icon}</div><div style="font-size:27px;font-weight:800;margin-top:10px;line-height:1.2">{t}</div></div>'
C1.append(f'''<div class="bd">PRACTICE</div>
<h1 class="t" style="font-size:86px">Try it</h1>
<div class="card" style="padding:28px 30px"><div style="font-size:33px;line-height:1.45;font-weight:600">The bridge was built with cheap steel. <span style="display:inline-block;width:150px;border-bottom:4px solid #fff"></span> cracks appeared within five years.</div>
<div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin-top:22px">{chs}</div></div>
<div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;align-self:stretch">{sol(CORAL, ic(EYEOFF,34), 'Cover')}{sol(BLUE, ic(BOOK,34), 'steel → cracks')}{sol(Y, '<span style="font-size:34px">→</span>', 'Cause &amp; effect')}</div>
{tip('Answer: <b>B) Consequently</b>', CHECK)}''')
C1.append(enroll('NEXT: CHAPTER 2 · STUDENT NOTES →'))

C2 = []
C2.append(f'''{hero('<svg width="540" height="200" viewBox="0 0 540 200"><rect x="10" y="14" width="160" height="176" rx="20" fill="#f7f2e7"/><circle cx="40" cy="58" r="8" fill="#134560"/><circle cx="40" cy="102" r="8" fill="#134560"/><circle cx="40" cy="146" r="8" fill="#134560"/><path d="M60 58h86M60 102h74M60 146h62" stroke="#9fb4bd" stroke-width="10" stroke-linecap="round"/><path d="M182 102h44" stroke="#7fdcf2" stroke-width="8" stroke-linecap="round"/><path d="M214 88l16 14-16 14" stroke="#7fdcf2" stroke-width="8" fill="none" stroke-linecap="round" stroke-linejoin="round"/><circle cx="300" cy="102" r="60" fill="#134560" stroke="#f7f2e7" stroke-width="8"/><circle cx="300" cy="102" r="36" fill="none" stroke="#7fdcf2" stroke-width="8"/><circle cx="300" cy="102" r="14" fill="#f6c343"/><path d="M372 102h44" stroke="#7fdcf2" stroke-width="8" stroke-linecap="round"/><path d="M404 88l16 14-16 14" stroke="#7fdcf2" stroke-width="8" fill="none" stroke-linecap="round" stroke-linejoin="round"/><circle cx="480" cy="102" r="48" fill="#5fd6a8"/><path d="M458 103l15 15 30-32" stroke="#14232d" stroke-width="11" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>')}
<div class="bd">SAT ENGLISH · CHAPTER 2</div>
<h1 class="t" style="font-size:108px">Student Notes<span style="font-size:74px;margin-top:6px">made simple</span></h1>
<div class="sub">Notes → goal → answer.<br><span style="color:#f6c343">The goal decides.</span></div>
<div class="stats"><div class="st"><div class="n">3</div><div class="l">easy<br>steps</div></div><div class="st"><div class="n">4</div><div class="l">goal<br>types</div></div><div class="st"><div class="n">1</div><div class="l">big<br>trap</div></div></div>
<div class="swipe">SWIPE →</div>''')
C2.append(f'''<div class="bd">STEP 1 · METHOD</div>
<h1 class="t">Goal first<span>notes later</span></h1>
{step(1, Y, TARGET, 'Read the goal', '“The student wants to…”')}
{step(2, BLUE, PEN, 'Underline', 'contrast · similarity · emphasize')}
{step(3, GREEN, CHECK, 'Match all', 'Every part of the goal')}
{tip('Goal + choices<br><b>are usually enough.</b>')}''')
def cell(ok):
    return f'<div class="disc" style="width:78px;height:78px;margin:0 auto;background:{GREEN if ok else CORAL}">{ic(CHECK if ok else XX,44,3.4)}</div>'
trs = ''.join(f'<div style="display:grid;grid-template-columns:1.6fr 1fr 1fr;align-items:center;padding:20px 0;border-top:1.5px solid rgba(255,255,255,.15)"><div style="font-size:34px;font-weight:800;line-height:1.15">{q}</div>{cell(a)}{cell(b)}</div>' for q, a, b in (('True?', 1, 1), ('From the notes?', 1, 1), ('Does the goal?', 0, 1)))
C2.append(f'''<div class="bd">STEP 2 · REAL TEST</div>
<h1 class="t">True is<span>not enough</span></h1>
<div class="card" style="padding:28px 34px"><div style="display:grid;grid-template-columns:1.6fr 1fr 1fr;padding-bottom:16px;text-align:center;font-size:26px;font-weight:800;letter-spacing:2px"><div></div><div style="color:{CORAL}">WRONG</div><div style="color:{GREEN}">RIGHT</div></div>{trs}</div>
{tip('Ask one thing:<br><b>“Does it do the goal?”</b>')}''')
G = [('contrast', CORAL, '≠', '<i>whereas · although · but</i>'),
     ('similarity', GREEN, '=', '<i>both · similarly · like</i>'),
     ('new audience', BLUE, 'i', '<b>longest</b> choice'),
     ('A and B', PURPLE, '2', 'has <b>both</b> parts')]
grow = ''.join(f'<div class="card" style="padding:20px 24px"><div class="lab" style="display:flex;justify-content:space-between;font-size:19px;margin-bottom:10px;color:#9fd2e2"><span>GOAL SAYS</span><span>LOOK FOR</span></div><div class="row" style="gap:16px"><span class="tok" style="flex:none;background:{c};color:{INK};font-size:30px;font-weight:800;padding:12px 24px">{s}&nbsp;&nbsp;{g}</span>{ic(ARR,44,3,TEAL)}<div style="flex:1;text-align:right;font-size:31px;font-weight:700;line-height:1.2">{l}</div></div></div>' for g, c, s, l in G)
C2.append(f'''<div class="bd">STEP 3 · CLUES</div>
<h1 class="t">Goal words<span>= clues</span></h1>
<div style="align-self:stretch;display:flex;flex-direction:column;gap:14px">{grow}</div>''')
def bar(frac, col, label, verdict):
    return f'<div style="margin-top:26px"><div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:12px"><span style="font-size:30px;font-weight:800">{label}</span><span style="font-size:28px;font-weight:800;color:{col}">{verdict}</span></div><div style="height:44px;border-radius:22px;background:rgba(255,255,255,.12);overflow:hidden"><div style="height:44px;width:{frac}%;background:{col};border-radius:22px"></div></div></div>'
C2.append(f'''<div class="bd">TRAP · NEAR-MISS</div>
<h1 class="t">Half right<span>= wrong</span></h1>
<div class="card" style="padding:30px 32px"><div class="lab">GOAL · 2 PARTS</div>
<div style="display:flex;gap:14px;margin-top:14px;align-items:center"><span class="tok" style="background:{Y};color:{INK};font-size:34px;font-weight:800">method</span><span style="font-size:40px;font-weight:800">+</span><span class="tok" style="background:{TEAL};color:{INK};font-size:34px;font-weight:800">result</span></div>
{bar(50, CORAL, 'Result only', '1/2 ✗')}
{bar(100, GREEN, 'Method + result', '2/2 ✓')}</div>
{tip('<b>Count the parts.</b><br>Check every one.', LIST)}''')
chs2 = [('A) Everest lies on the Nepal–China border.', 'no heights', 0),
        ('B) Both mountains lie on China’s border.', 'similarity', 0),
        ('C) Whereas Everest is 8,849 m tall, K2 is 8,611 m tall.', 'contrast ✓', 1),
        ('D) K2, which is 8,611 m tall, lies on China’s border.', 'one height', 0)]
chrows = ''.join(f'<div style="display:flex;align-items:center;gap:12px;background:{rgba(Y,.22) if ok else "rgba(255,255,255,.08)"};border:2.5px solid {Y if ok else "rgba(255,255,255,.2)"};border-radius:18px;padding:12px 16px"><div style="flex:1;font-size:25px;font-weight:700;line-height:1.3">{t}</div><span class="tok" style="flex:none;font-size:19px;padding:6px 12px;font-weight:800;background:{GREEN if ok else rgba(CORAL,.25)};color:{INK if ok else "#fff"}">{tg}</span></div>' for t, tg, ok in chs2)
note = lambda n, a: f'<div style="flex:1;background:#f7f2e7;color:{INK};border-radius:20px;padding:16px 20px"><div style="font-weight:800;font-size:30px">{n}</div><div style="font-size:27px;font-weight:700;color:#3b5663">{a}</div></div>'
C2.append(f'''<div class="bd">PRACTICE</div>
<h1 class="t" style="font-size:86px">Try it</h1>
<div class="card" style="padding:24px 26px;display:flex;flex-direction:column;gap:14px">
<div style="display:flex;gap:12px">{note('Everest','8,849 m')}{note('K2','8,611 m')}</div>
<div style="font-size:30px;font-weight:700">Goal: <span class="tok" style="background:{CORAL};color:{INK};font-size:27px;padding:6px 16px">contrast</span> their <span class="tok" style="background:{Y};color:{INK};font-size:27px;padding:6px 16px">heights</span></div>
<div style="display:flex;flex-direction:column;gap:10px">{chrows}</div></div>
{tip('Answer: <b>C</b> · whereas + both heights', CHECK)}''')
C2.append(f'''<div class="bd">STEP 4 · CHECKLIST</div>
<h1 class="t">3-step<span>checklist</span></h1>
{step(1, Y, PEN, 'Underline', 'Key words + count parts')}
{step(2, CORAL, SCISS, 'Cut', 'Off-topic choices')}
{step(3, GREEN, CHECK, 'Pick', 'The one with every part')}
{tip('Two left?<br><b>Take the most direct one.</b>')}''')
C2.append(enroll('NEXT SERIES COMING SOON →'))

out = HERE / 'out3'; out.mkdir(exist_ok=True)
with sync_playwright() as p:
    br = p.chromium.launch(); pg = br.new_page(viewport={'width': 1080, 'height': 1350})
    for chap, slides in ((1, C1), (2, C2)):
        for i, body in enumerate(slides, 1):
            pg.set_content(page(i, len(slides), body, chap)); pg.wait_for_timeout(250)
            ov = pg.evaluate("()=>{const m=document.querySelector('.mn');const r=m.getBoundingClientRect();let t=1e9,b=0;for(const c of m.children){const x=c.getBoundingClientRect();t=Math.min(t,x.top);b=Math.max(b,x.bottom)}return [Math.round(t),Math.round(b)]}")
            fn = out / f'SAT-English-v3-Ch{chap}-{i}-of-8.png'
            pg.screenshot(path=str(fn)); print(fn.name, ov, 'OK' if ov[0] >= 128 and ov[1] <= 1242 else 'OVERFLOW')
    br.close()
