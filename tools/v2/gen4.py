import base64, pathlib
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).parent
FD = HERE.parent / 'poster/fonts/package/files'
SD = HERE.parent / 'poster/fonts/serif/package/files'
b64 = lambda p: base64.b64encode(p.read_bytes()).decode()
ff = ''
for w in (500, 600, 700, 800):
    for sub in ('latin', 'latin-ext'):
        p = FD / f'montserrat-{sub}-{w}-normal.woff2'
        if p.exists(): ff += "@font-face{font-family:M;font-weight:%d;src:url(data:font/woff2;base64,%s)}\n" % (w, b64(p))
for w in (400, 600, 700):
    for st in ('normal', 'italic'):
        ff += "@font-face{font-family:S;font-weight:%d;font-style:%s;src:url(data:font/woff2;base64,%s)}\n" % (w, st, b64(SD / f'source-serif-4-latin-{w}-{st}.woff2'))
QR = 'data:image/svg+xml;base64,' + b64(HERE / 'qr_join.svg')

Y = '#f6c343'; INK = '#14232d'; TEAL = '#7fdcf2'
GREEN = '#5fd6a8'; CORAL = '#ff8a80'; BLUE = '#7cc2ff'; PURPLE = '#c9a6ff'
def rgba(h, a):
    h = h.lstrip('#'); return f'rgba({int(h[0:2],16)},{int(h[2:4],16)},{int(h[4:6],16)},{a})'

CSS = ff + """
*{box-sizing:border-box}
body{margin:0;width:1080px;height:1350px;font-family:M,sans-serif;color:#fff;overflow:hidden}
.pg{width:1080px;height:1350px;position:relative;overflow:hidden;background:radial-gradient(ellipse at 20% 0%,#24698a 0%,#134560 42%,#092131 100%)}
.gr{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.028) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.028) 1px,transparent 1px);background-size:54px 54px}
.o1{position:absolute;width:640px;height:640px;border-radius:50%;background:radial-gradient(circle,rgba(246,195,67,.12),transparent 65%);right:-260px;bottom:-200px}
.hd{position:absolute;top:44px;left:60px;right:60px;display:flex;justify-content:space-between;align-items:center}
.lg{display:flex;align-items:center;gap:12px;font-weight:800;font-size:20px;line-height:1.15;letter-spacing:1.5px}
.pn{font-weight:800;font-size:22px;letter-spacing:2px;color:#cfe3ea}
.pn b{color:#f6c343;font-size:30px}
.ft{position:absolute;left:60px;right:60px;bottom:40px}
.tr{height:6px;border-radius:6px;background:rgba(255,255,255,.14);margin-bottom:16px;overflow:hidden}
.tf{height:6px;background:linear-gradient(90deg,#f6c343,#ffd978)}
.fr{display:flex;justify-content:space-between;font-size:20px;font-weight:600;color:#cfe3ea}
.mn{position:absolute;top:128px;left:60px;right:60px;bottom:104px;display:flex;flex-direction:column;justify-content:center;gap:26px}
.kick{display:flex;align-items:center;gap:14px}
.bd{background:#f6c343;color:#14232d;border-radius:40px;padding:10px 24px;font-weight:800;font-size:22px;letter-spacing:2.5px}
.ks{font-weight:800;font-size:22px;letter-spacing:2.5px;color:#9fd2e2}
.t{margin:0;font-weight:800;font-size:74px;line-height:1.04;letter-spacing:-1px}
.t em{font-style:normal;color:#c9f2ff}
.lead{font-size:31px;font-weight:600;color:#d3e8f0;line-height:1.35;margin:0}
.sent{background:#f7f2e7;color:#14232d;border-radius:26px;padding:28px 32px;font-family:S,serif;font-size:37px;line-height:1.45;box-shadow:0 18px 40px rgba(0,0,0,.3)}
.mk{background:#f6c343;border-radius:8px;padding:0 8px;font-weight:700}
.blank{display:inline-block;width:150px;border-bottom:4px solid #14232d;transform:translateY(-8px)}
.card{background:linear-gradient(145deg,rgba(255,255,255,.12),rgba(255,255,255,.04));border:1.5px solid rgba(255,255,255,.16);box-shadow:inset 0 1px 0 rgba(255,255,255,.18),0 18px 40px rgba(0,0,0,.25);border-radius:28px;padding:24px 28px}
.rule{display:flex;gap:22px;align-items:center;background:linear-gradient(135deg,#ffd978,#f6c343);color:#14232d;border-radius:26px;padding:24px 30px;box-shadow:0 12px 26px rgba(0,0,0,.3)}
.rule .lab{font-size:19px;font-weight:800;letter-spacing:3px;color:#6b5210;margin-bottom:4px}
.rule .tx{font-size:30px;font-weight:700;line-height:1.3}
.tok{display:inline-flex;align-items:center;gap:10px;padding:10px 20px;border-radius:40px;font-weight:800;font-size:26px;line-height:1.1}
.lab2{font-size:20px;font-weight:800;letter-spacing:3px;color:#7fdcf2}
.num{flex:none;width:64px;height:64px;border-radius:20px;background:linear-gradient(145deg,#ffd978,#f6c343);color:#14232d;font-weight:800;font-size:34px;display:flex;align-items:center;justify-content:center}
.disc{flex:none;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#14232d;font-weight:800}
.ch{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
.c{position:relative;border-radius:18px;padding:16px 20px;font-size:29px;font-weight:700;background:rgba(255,255,255,.08);border:2.5px solid rgba(255,255,255,.2)}
.c small{display:block;font-size:19px;font-weight:800;letter-spacing:1.5px;margin-top:4px}
b{font-weight:800}
"""

LOGO = '<svg width="52" height="48" viewBox="0 0 60 56" fill="none" stroke="#fff" stroke-width="2.4"><circle cx="30" cy="24" r="19"/><ellipse cx="30" cy="24" rx="8" ry="19"/><path d="M11 24h38M14 14h32M14 34h32"/><path d="M6 44c9-5 17-5 24 2 7-7 15-7 24-2M6 50c9-5 17-5 24 2 7-7 15-7 24-2" stroke="#f6c343" stroke-width="3"/></svg>'
def ic(d, size=40, sw=2.6, col=INK):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{col}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{d}</svg>'
CHECK = '<path d="M5 12.5l4.5 4.5L19 7.5"/>'; XX = '<path d="M6 6l12 12M18 6L6 18"/>'
KEY = '<circle cx="8" cy="15" r="4"/><path d="M11 12l9-9M17 6l3 3M14 9l2 2"/>'
ARR = '<path d="M4 12h15M13 6l6 6-6 6"/>'

def page(n, total, body):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="pg"><div class="gr"></div><div class="o1"></div>
<div class="hd"><div class="lg">{LOGO}<div>GLOBAL<br>MATH PREP</div></div><div class="pn"><b>{n:02d}</b> / {total:02d}</div></div>
<div class="mn">{body}</div>
<div class="ft"><div class="tr"><div class="tf" style="width:{n/total*100}%"></div></div><div class="fr"><span>@globalmathprep · globalmathprep.academy</span><span>SAT English · Chapter 1</span></div></div>
</div></body></html>'''

def kick(label):
    return f'<div class="kick"><span class="bd">{label}</span><span class="ks">TRANSITIONS</span></div>'
def rule(txt, label='THE RULE'):
    return f'<div class="rule"><div class="disc" style="width:70px;height:70px;background:#14232d">{ic(KEY,38,2.4,Y)}</div><div><div class="lab">{label}</div><div class="tx">{txt}</div></div></div>'

S = []
# 1 COVER
S.append(f'''<div class="kick"><span class="bd">SAT ENGLISH · CHAPTER 1</span></div>
<h1 class="t" style="font-size:124px;line-height:.98">Transitions</h1>
<p class="lead" style="font-size:40px;color:#c9f2ff;font-weight:700">The logic that links your sentences</p>
<div class="sent" style="font-size:40px">The first draft was rejected. <span class="mk">&nbsp;&nbsp;?&nbsp;&nbsp;</span>, the second one won the prize.</div>
<div style="display:flex;gap:12px;flex-wrap:wrap">{''.join(f'<span class="tok" style="background:{rgba(c,.2)};border:2px solid {c}">{w}</span>' for w,c in (('However',CORAL),('Therefore',Y),('Moreover',GREEN),('For instance',BLUE),('In fact',PURPLE)))}</div>
<p class="lead">Five small words, one big question: <b style="color:#fff">how do these two ideas relate?</b> Answer it, and the right choice becomes obvious.</p>
<div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px">{''.join(f'<div class="card" style="text-align:center;padding:22px 10px"><div style="font-size:70px;font-weight:800;color:#f6c343;line-height:1">{n}</div><div style="font-size:25px;font-weight:700;margin-top:6px">{l}</div></div>' for n,l in (('5','relationships'),('4','step method'),('2','classic traps')))}</div>''')

# 2 WHAT IT DOES
S.append(f'''{kick('THE CORE IDEA')}
<h1 class="t">What does a<br>transition <em>actually do?</em></h1>
<div class="sent">Solar panels are expensive to install. <span class="mk">However</span>, they pay for themselves within a decade.</div>
<div style="display:flex;align-items:center;gap:14px">
<div class="card" style="flex:1;text-align:center;padding:20px 12px"><div class="lab2">IDEA A</div><div style="font-size:32px;font-weight:800;margin-top:6px">high cost</div></div>
<div style="text-align:center"><div style="font-size:48px;font-weight:800;color:{CORAL};line-height:1">⇄</div><div style="font-size:18px;font-weight:800;letter-spacing:2px;color:{CORAL}">OPPOSITE</div></div>
<div class="card" style="flex:1;text-align:center;padding:20px 12px"><div class="lab2">IDEA B</div><div style="font-size:32px;font-weight:800;margin-top:6px">long-term saving</div></div></div>
<div class="card" style="display:flex;align-items:center;gap:18px;padding:20px 26px"><span class="tok" style="background:{CORAL};color:{INK}">≠ Contrast</span><span style="font-size:29px;font-weight:600;line-height:1.3">so <i>however</i> is the natural signal</span></div>
{rule('A transition adds no new facts. It only signals <b>how the second idea relates to the first.</b>')}''')

# 3 FIVE RELATIONSHIPS
T = [('Continue', GREEN, '+', 'moreover · in addition · likewise', 'The city added bus routes. <span class="mk" style="background:%s">Moreover</span>, it cut fares.'),
     ('Contrast', CORAL, '≠', 'however · nevertheless · yet', 'The plan was bold. <span class="mk" style="background:%s">However</span>, it lacked funding.'),
     ('Cause &amp; effect', Y, '→', 'therefore · consequently · thus', 'The river flooded. <span class="mk" style="background:%s">Consequently</span>, the road closed.'),
     ('Example', BLUE, 'e.g.', 'for example · for instance', 'Some birds travel far. <span class="mk" style="background:%s">For instance</span>, the Arctic tern flies pole to pole.'),
     ('Emphasis', PURPLE, '!', 'in fact · indeed · that is', 'The exam was hard. <span class="mk" style="background:%s">In fact</span>, no one finished it.')]
rows = ''.join(f'''<div class="card" style="padding:16px 22px"><div style="display:flex;align-items:center;gap:14px"><div class="disc" style="width:50px;height:50px;background:{c};font-size:{19 if len(s)>1 else 28}px">{s}</div><div style="font-size:30px;font-weight:800;color:{c};flex:none">{n}</div><div style="flex:1;text-align:right;font-size:20px;font-weight:700;color:#cfe3ea">{w}</div></div>
<div style="font-family:S,serif;font-size:27px;line-height:1.35;margin-top:8px;color:#f4f8fa">{e % c}</div></div>''' for n, c, s, w, e in T)
S.append(f'''{kick('THE FIVE TYPES')}
<h1 class="t" style="font-size:66px">Five ways ideas <em>connect</em></h1>
<div style="display:flex;flex-direction:column;gap:12px">{rows}</div>''')

# 4 METHOD
S.append(f'''{kick('THE METHOD')}
<h1 class="t" style="font-size:68px">Predict first,<br><em>then match</em></h1>
<div class="sent" style="font-size:33px;padding:22px 28px">Solar panels are expensive to install. <span class="blank"></span>, they pay for themselves within a decade.</div>
{''.join(f'<div style="display:flex;align-items:center;gap:20px"><div class="num">{i}</div><div style="flex:1"><div style="font-size:32px;font-weight:800">{h}</div><div style="font-size:26px;font-weight:600;color:#cfe3ea;margin-top:2px">{p}</div></div></div>' for i,h,p in ((1,'Cover the choices','Don’t let a polished word lead you.'),(2,'Paraphrase both ideas','“It costs a lot … but it pays off.”'),(3,'Predict your own word','You’d say “but”, so the family is Contrast.'),(4,'Match the family','Scan for the only Contrast option.')))}
<div class="ch">{''.join(f'<div class="c" style="{st}">{t}</div>' for t,st in (('A) Therefore','opacity:.55'),('B) However',f'background:{rgba(Y,.22)};border-color:{Y}'),('C) For example','opacity:.55'),('D) Similarly','opacity:.55')))}</div>''')

# 5 TRAP 1
S.append(f'''{kick('TRAP 1 · TWINS')}
<h1 class="t" style="font-size:68px">Two answers that match<br><em>cancel each other out</em></h1>
<div class="sent" style="font-size:33px;padding:22px 28px">The factory switched to solar power. <span class="blank"></span>, its energy bills fell sharply.</div>
<div class="ch">
<div class="c" style="border-color:{CORAL};"><span style="text-decoration:line-through;text-decoration-thickness:3px">A) However</span><small style="color:{CORAL};text-decoration:none">TWIN · CONTRAST</small></div>
<div class="c" style="border-color:{CORAL};"><span style="text-decoration:line-through;text-decoration-thickness:3px">B) Nevertheless</span><small style="color:{CORAL}">TWIN · CONTRAST</small></div>
<div class="c" style="background:{rgba(Y,.22)};border-color:{Y}">C) As a result<small style="color:{Y}">✓ CAUSE &amp; EFFECT</small></div>
<div class="c" style="opacity:.6">D) For instance<small style="color:#cfe3ea">✗ NO EXAMPLE HERE</small></div></div>
<p class="lead">A and B do the same job. The test has one right answer, so <b style="color:#fff">neither twin can be it</b>, and you’re down to two options in seconds.</p>
{rule('When two choices share a function, <b>eliminate both at once.</b>')}''')

# 6 TRAP 2
S.append(f'''{kick('TRAP 2 · POSITION')}
<h1 class="t" style="font-size:68px">Mid-sentence, it still<br><em>looks backward</em></h1>
<div class="sent" style="position:relative;padding:30px 32px">
<div><span style="color:#8a9aa2;font-weight:700">①</span> Critics dismissed the novel as trivial.</div>
<div style="display:flex;align-items:center;gap:12px;margin:10px 0 10px 40px;font-family:M,sans-serif;font-size:22px;font-weight:800;color:#1f6f8b;letter-spacing:1px">{ic('<path d="M12 20V4M5 11l7-7 7 7"/>',36,3,'#1f6f8b')} CONTRAST WITH THIS IDEA</div>
<div><span style="color:#8a9aa2;font-weight:700">②</span> Readers, <span class="mk">however</span>, embraced it.</div></div>
<div class="card" style="display:flex;align-items:center;justify-content:space-between;gap:12px;padding:20px 24px">
{''.join(f'<span class="tok" style="background:rgba(255,255,255,.1);border:2px solid rgba(255,255,255,.3)">{x}</span>' for x in ('Start','Middle','End'))}
{ic(ARR,40,3,TEAL)}<span style="font-size:28px;font-weight:800">same job</span></div>
<p class="lead">Don’t be fooled by where the word sits. Read the sentence <b style="color:#fff">before</b> to find the relationship.</p>
{rule('A transition always links its idea to <b>the one that came before.</b>')}''')

# 7 PRACTICE
S.append(f'''{kick('YOUR TURN')}
<h1 class="t" style="font-size:68px">Try a real-style<br><em>question</em></h1>
<div class="sent" style="font-size:33px;padding:24px 28px">Octopuses have no bones; only their beak is hard. <span class="blank"></span>, they can squeeze through openings barely larger than that beak.<div style="font-family:M,sans-serif;font-size:22px;font-weight:600;color:#4a6470;margin-top:12px;font-style:italic">Which choice completes the text with the most logical transition?</div></div>
<div class="ch">{''.join(f'<div class="c" style="{st}">{t}</div>' for t,st in (('A) Nevertheless',''),('B) Consequently',f'background:{rgba(Y,.22)};border-color:{Y}'),('C) Similarly',''),('D) For example','')))}</div>
<div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px">{''.join(f'<div class="card" style="padding:16px 14px"><div class="lab2" style="font-size:17px">{a}</div><div style="font-size:24px;font-weight:800;margin-top:6px;line-height:1.2">{b}</div></div>' for a,b in (('PARAPHRASE','no bones → fits through'),('PREDICT','“so”'),('FAMILY','Cause &amp; effect')))}</div>
{rule('Answer: <b>B) Consequently.</b> The lack of bones <i>causes</i> the flexibility.', 'THE ANSWER')}''')

# 8 ENROLL
days = ''.join(f'<div style="flex:1;background:#f7f2e7;color:{INK};border-radius:16px;padding:12px 4px;text-align:center;font-weight:800;font-size:26px">{d}</div>' for d in ('Tue', 'Thu', 'Fri'))
chk = ''.join(f'<div style="display:flex;align-items:center;gap:12px">{ic(CHECK,30,3.2,Y)}<span>{x}</span></div>' for x in ('Live on Zoom from Canada', 'Nov &amp; Dec SAT sittings', 'Weekly report for parents'))
S.append(f'''<div class="kick"><span class="bd">ENROLLMENT OPEN</span><span class="ks">SAT ENGLISH</span></div>
<h1 class="t" style="font-size:88px">A new cohort<br><em>is forming now</em></h1>
<div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px">{''.join(f'<div class="card" style="text-align:center;padding:18px 6px"><div style="font-size:56px;font-weight:800;color:#f6c343;line-height:1">{n}</div><div style="font-size:21px;font-weight:700;margin-top:6px">{l}</div></div>' for n,l in (('6','seats left'),('2–5','per group'),('3×','a week'),('80','min per class')))}</div>
<div style="display:flex;gap:16px">
<div class="card" style="flex:1.45;display:flex;flex-direction:column;gap:14px"><div class="lab2">MONGOLIA TIME</div><div style="display:flex;gap:10px">{days}</div>
<div style="font-size:56px;font-weight:800;line-height:1">18:30–19:50</div><div style="display:flex;flex-direction:column;gap:8px;font-size:23px;font-weight:700">{chk}</div></div>
<div style="flex:1;background:#fff;border-radius:28px;padding:20px 14px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;color:{INK};text-align:center"><img src="{QR}" style="width:220px;height:220px"><div style="font-size:26px;font-weight:800;line-height:1.1">Free placement<br>test</div></div></div>
<div class="rule" style="justify-content:center;text-align:center"><div><div class="tx">Message <b>“SAT English”</b> on WhatsApp</div><div style="font-size:44px;font-weight:800;margin-top:4px">+1 428 880 1826</div></div></div>
<div class="ks" style="text-align:center">NEXT SERIES · CHAPTER 2 · STUDENT NOTES →</div>''')

if __name__ == '__main__':
  out = HERE / 'out4'; out.mkdir(exist_ok=True)
  with sync_playwright() as p:
      br = p.chromium.launch(); pg = br.new_page(viewport={'width': 1080, 'height': 1350})
      for i, body in enumerate(S, 1):
          pg.set_content(page(i, len(S), body)); pg.wait_for_timeout(250)
          ov = pg.evaluate("()=>{const m=document.querySelector('.mn');let t=1e9,b=0;for(const c of m.children){const x=c.getBoundingClientRect();t=Math.min(t,x.top);b=Math.max(b,x.bottom)}return [Math.round(t),Math.round(b)]}")
          fn = out / f'SAT-English-v4-Ch1-{i}-of-8.png'
          pg.screenshot(path=str(fn)); print(fn.name, ov, 'OK' if ov[0] >= 120 and ov[1] <= 1246 else 'OVERFLOW')
      br.close()
