import gen4 as g
from gen4 import ic, rgba, INK, CHECK, XX, ARR
from playwright.sync_api import sync_playwright

Y = '#f8c12d'; SKY = '#bfe6ff'; BLUE = '#7cc2ff'; GREEN = '#5fd6a8'; CORAL = '#ff8a80'; PURPLE = '#c9a6ff'; TEAL = '#8fd3ff'
CSS = g.ff + """
*{box-sizing:border-box}
body{margin:0;width:1080px;height:1350px;font-family:M,sans-serif;color:#fff;overflow:hidden}
.pg{width:1080px;height:1350px;position:relative;overflow:hidden;background:linear-gradient(160deg,#0f3a73 0%,#0b2d5e 45%,#07214a 100%)}
.gr{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.025) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.025) 1px,transparent 1px);background-size:60px 60px}
.sw1{position:absolute;left:-120px;top:150px;width:900px;height:120px;background:linear-gradient(90deg,rgba(120,180,255,.10),transparent);transform:rotate(-4deg);border-radius:60px}
.ring{position:absolute;right:-180px;top:260px;width:420px;height:420px;border-radius:50%;border:60px solid rgba(120,180,255,.06)}
.ring2{position:absolute;left:-200px;bottom:120px;width:380px;height:380px;border-radius:50%;border:50px solid rgba(120,180,255,.05)}
.hd{position:absolute;top:58px;left:62px;right:62px;display:flex;align-items:center;justify-content:space-between}
.lg{display:flex;align-items:center;gap:18px}
.lgt{font-family:S,serif;font-weight:700;font-size:27px;letter-spacing:2.5px;line-height:1.25}
.lgt span{display:block;color:#f8c12d;font-size:19px;letter-spacing:2.5px;font-weight:600}
.sat{display:flex;align-items:center;gap:26px}
.vl{width:2px;height:70px;background:rgba(255,255,255,.3)}
.satw{font-weight:800;font-size:58px;letter-spacing:-1px}
.satw sup{font-size:14px;vertical-align:top;position:relative;top:6px}
.pno{position:absolute;top:200px;right:62px;font-weight:800;font-size:30px;color:#cfe0f5}
.pno b{color:#f8c12d;font-size:36px}
.mn{position:absolute;top:250px;left:62px;right:62px;bottom:140px;display:flex;flex-direction:column;justify-content:center;gap:22px}
.kick{display:flex;align-items:center;gap:20px}
.bd{background:#f8c12d;color:#0b1f3a;border-radius:40px;padding:12px 30px;font-weight:800;font-size:27px;letter-spacing:3px}
.ks{font-weight:800;font-size:27px;letter-spacing:2.5px;color:#7fc4ff}
.t{margin:0;font-weight:800;font-size:92px;line-height:1.02;letter-spacing:-1.5px;text-shadow:0 6px 24px rgba(0,0,0,.3)}
.t em{font-style:normal;color:#bfe6ff}
.st2{font-size:36px;font-weight:800;line-height:1.3;margin:0}
.st2 span{color:#f8c12d}
.sent{background:#f7f2e7;color:#12203a;border-radius:26px;padding:30px 36px;font-family:S,serif;font-size:40px;line-height:1.45;box-shadow:0 18px 40px rgba(0,0,0,.35)}
.mk{background:#f8c12d;border-radius:8px;padding:0 8px;font-weight:700}
.blank{display:inline-block;width:150px;border-bottom:4px solid #12203a;transform:translateY(-8px)}
.stats{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:22px}
.sc{border:2px solid rgba(143,200,255,.35);background:linear-gradient(160deg,rgba(40,90,160,.35),rgba(10,40,90,.35));border-radius:28px;padding:20px 14px 18px;text-align:center}
.sc .n{font-size:88px;font-weight:800;color:#f8c12d;line-height:.95}
.sc .l{font-size:31px;font-weight:800;margin-top:6px}
.sc .d{height:2px;background:rgba(143,200,255,.35);margin:12px 20px}
.sc .s{font-size:27px;font-weight:500;line-height:1.3;color:#e6f0fb}
.card{border:2px solid rgba(143,200,255,.3);background:linear-gradient(160deg,rgba(40,90,160,.3),rgba(10,40,90,.3));border-radius:26px;padding:22px 26px}
.num{flex:none;width:70px;height:70px;border-radius:22px;background:#f8c12d;color:#0b1f3a;font-weight:800;font-size:38px;display:flex;align-items:center;justify-content:center}
.disc{flex:none;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#0b1f3a;font-weight:800}
.ch{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}
.c{border-radius:20px;padding:18px 22px;font-size:31px;font-weight:700;background:rgba(255,255,255,.07);border:2.5px solid rgba(143,200,255,.3)}
.c small{display:block;font-size:20px;font-weight:800;letter-spacing:1.5px;margin-top:4px}
.ft{position:absolute;left:62px;right:62px;bottom:48px}
.tr{height:8px;border-radius:8px;background:rgba(255,255,255,.18);margin-bottom:20px;overflow:hidden}
.tf{height:8px;background:#f8c12d;border-radius:8px}
.fr{display:flex;justify-content:space-between;font-size:24px;font-weight:500;color:#e6f0fb}
b{font-weight:800}
"""
LOGO = '<svg width="74" height="68" viewBox="0 0 60 56" fill="none" stroke="#fff" stroke-width="2.2"><circle cx="30" cy="24" r="19"></circle><ellipse cx="30" cy="24" rx="8" ry="19"></ellipse><path d="M11 24h38M14 14h32M14 34h32"></path><path d="M6 44c9-5 17-5 24 2 7-7 15-7 24-2M6 50c9-5 17-5 24 2 7-7 15-7 24-2" stroke="#f8c12d" stroke-width="3"></path></svg>'

def page(n, total, body):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="pg"><div class="gr"></div><div class="sw1"></div><div class="ring"></div><div class="ring2"></div>
<div class="hd"><div class="lg">{LOGO}<div class="lgt">GLOBAL MATH PREP<span>JARGALMAA AMGALAN</span></div></div><div class="sat"><div class="vl"></div><div class="satw">SAT<sup>®</sup></div></div></div>
<div class="pno"><b>{n:02d}</b> / {total:02d}</div>
<div class="mn">{body}</div>
<div class="ft"><div class="tr"><div class="tf" style="width:{n/total*100}%"></div></div><div class="fr"><span>@globalmathprep · globalmathprep.academy</span><span>SAT English</span></div></div>
</div></body></html>'''

def kick(a, b='TRANSITIONS'):
    return f'<div class="kick"><span class="bd">{a}</span><span class="ks">{b}</span></div>'
def stats(items):
    return '<div class="stats">' + ''.join(f'<div class="sc"><div class="n">{n}</div><div class="l">{l}</div><div class="d"></div><div class="s">{s}</div></div>' for n, l, s in items) + '</div>'

S = []
S.append(f'''{kick('SAT ENGLISH · CH 1')}
<h1 class="t" style="font-size:112px">Transitions</h1>
<p class="st2" style="font-size:40px">The tiny words that <span>carry your score.</span></p>
<div class="sent">The first draft flopped. <span class="mk">&nbsp;&nbsp;?&nbsp;&nbsp;</span>, the second one won the prize.</div>
<p class="st2">One question unlocks them all: <span>how do these two ideas vibe?</span></p>
{stats([('5','link types','that’s the whole map'),('4','moves','predict, then match'),('2','traps','we’ll dodge both')])}''')
S.append(f'''{kick('THE CORE IDEA')}
<h1 class="t">What does a<br>transition <em>really do?</em></h1>
<div class="sent">Solar panels are expensive to install. <span class="mk">However</span>, they pay for themselves within a decade.</div>
<p class="st2">It doesn’t spill new tea. <span>It just shows how idea B connects to idea A.</span></p>
{stats([('2','ideas','cost now vs. save later'),('1','relationship','plot twist: contrast'),('0','new facts','it only signals the link')])}''')
T = [('Continue', GREEN, '+', '“and there’s more”', 'The city added bus routes. <span class="mk" style="background:%s">Moreover</span>, it cut fares.'),
     ('Contrast', CORAL, '≠', '“plot twist”', 'The plan was bold. <span class="mk" style="background:%s">However</span>, it lacked funding.'),
     ('Cause &amp; effect', Y, '→', '“so this happened”', 'The river flooded. <span class="mk" style="background:%s">Consequently</span>, the road closed.'),
     ('Example', BLUE, 'e.g.', '“receipts, please”', 'Some birds travel far. <span class="mk" style="background:%s">For instance</span>, the Arctic tern flies pole to pole.'),
     ('Emphasis', PURPLE, '!', '“no, seriously”', 'The exam was hard. <span class="mk" style="background:%s">In fact</span>, no one finished it.')]
rows = ''.join(f'<div class="card" style="padding:16px 22px"><div style="display:flex;align-items:center;gap:14px"><div class="disc" style="width:52px;height:52px;background:{c};font-size:{19 if len(s)>1 else 28}px">{s}</div><div style="font-size:31px;font-weight:800;color:{c}">{n}</div><div style="flex:1;text-align:right;font-size:25px;font-weight:700;font-style:italic;color:#e6f0fb">{v}</div></div><div style="font-family:S,serif;font-size:27px;line-height:1.35;margin-top:8px">{e % c}</div></div>' for n, c, s, v, e in T)
S.append(f'''{kick('THE FIVE TYPES')}
<h1 class="t" style="font-size:80px">Five ways ideas <em>link up</em></h1>
<div style="display:flex;flex-direction:column;gap:12px">{rows}</div>''')
steps = ((1, 'Cover', 'Hide the choices. Fancy words can catfish you.'), (2, 'Vibe-check', 'Paraphrase both ideas in your own words.'), (3, 'Predict', 'Say the word you’d use. “But”? “So”?'), (4, 'Match', 'Find the choice in that same family.'))
S.append(f'''{kick('THE METHOD')}
<h1 class="t" style="font-size:84px">Predict first,<br><em>then match</em></h1>
{''.join(f'<div style="display:flex;align-items:center;gap:22px"><div class="num">{i}</div><div><div style="font-size:36px;font-weight:800">{h}</div><div style="font-size:28px;font-weight:500;color:#e6f0fb;margin-top:2px">{p}</div></div></div>' for i,h,p in steps)}
<div class="sent" style="font-size:32px;padding:22px 28px">Solar panels are expensive. <span class="blank"></span>, they pay for themselves. <span style="font-family:M,sans-serif;font-size:24px;font-weight:800;color:#1f5fa8">→ “but” → <span class="mk">However</span></span></div>''')
S.append(f'''{kick('TRAP 1 · TWINS')}
<h1 class="t" style="font-size:86px">Twins?<br><em>Both go home.</em></h1>
<div class="sent" style="font-size:34px;padding:24px 30px">The factory switched to solar power. <span class="blank"></span>, its energy bills fell sharply.</div>
<div class="ch">
<div class="c" style="border-color:{CORAL}"><span style="text-decoration:line-through;text-decoration-thickness:3px">A) However</span><small style="color:{CORAL}">TWIN · CONTRAST</small></div>
<div class="c" style="border-color:{CORAL}"><span style="text-decoration:line-through;text-decoration-thickness:3px">B) Nevertheless</span><small style="color:{CORAL}">TWIN · CONTRAST</small></div>
<div class="c" style="background:{rgba(Y,.2)};border-color:{Y}">C) As a result<small style="color:{Y}">✓ CAUSE &amp; EFFECT</small></div>
<div class="c" style="opacity:.6">D) For instance<small>✗ NO EXAMPLE HERE</small></div></div>
<p class="st2">Same job, same fate. <span>One question only has room for one right answer.</span></p>''')
S.append(f'''{kick('TRAP 2 · POSITION')}
<h1 class="t" style="font-size:84px">Mid-sentence?<br><em>Still looks back.</em></h1>
<div class="sent" style="padding:30px 34px">
<div><span style="color:#8a9aa2">①</span> Critics called the novel trivial.</div>
<div style="display:flex;align-items:center;gap:12px;margin:12px 0 12px 44px;font-family:M,sans-serif;font-size:24px;font-weight:800;color:#1f5fa8;letter-spacing:1px">{ic('<path d="M12 20V4M5 11l7-7 7 7"/>',38,3,'#1f5fa8')} COMPARE WITH THIS ONE</div>
<div><span style="color:#8a9aa2">②</span> Readers, <span class="mk">however</span>, loved it.</div></div>
<p class="st2">Start, middle or end, a transition <span>always checks the sentence before it.</span></p>
{stats([('①','idea A','critics: trivial'),('②','idea B','readers: loved it'),('≠','result','plot twist: contrast')])}''')
S.append(f'''{kick('YOUR TURN')}
<h1 class="t" style="font-size:80px">Octopus edition.<br><em>Can you get it?</em></h1>
<div class="sent" style="font-size:32px;padding:24px 30px">Octopuses have no bones; only their beak is hard. <span class="blank"></span>, they can squeeze through gaps barely bigger than that beak.</div>
<div class="ch">{''.join(f'<div class="c" style="{st}">{t}</div>' for t,st in (('A) Nevertheless',''),('B) Consequently',f'background:{rgba(Y,.2)};border-color:{Y}'),('C) Similarly',''),('D) For example','')))}</div>
{stats([('✓','B wins','no bones → squeezes'),('→','family','cause &amp; effect'),('“so”','your word','predicted it first')])}''')
days = ''.join(f'<div style="flex:1;background:#f7f2e7;color:{INK};border-radius:16px;padding:12px 4px;text-align:center;font-weight:800;font-size:27px">{d}</div>' for d in ('Tue', 'Thu', 'Fri'))
S.append(f'''{kick('ENROLLMENT OPEN','SAT ENGLISH')}
<h1 class="t" style="font-size:80px">Squad up<br><em>for the SAT.</em></h1>
{stats([('6','seats left','then we’re full'),('2–5','per group','small &amp; focused'),('3×','a week','80 min each')])}
<div style="display:flex;gap:18px">
<div class="card" style="flex:1.4;display:flex;flex-direction:column;gap:14px"><div style="font-size:21px;font-weight:800;letter-spacing:3px;color:#7fc4ff">MONGOLIA TIME</div><div style="display:flex;gap:10px">{days}</div><div style="font-size:56px;font-weight:800;line-height:1">18:30–19:50</div><div style="font-size:24px;font-weight:600;color:#e6f0fb">Live on Zoom · Nov &amp; Dec SAT · weekly parent report</div></div>
<div style="flex:1;background:#fff;border-radius:26px;padding:18px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;color:{INK};text-align:center"><img src="{g.QR}" style="width:180px;height:180px"><div style="font-size:24px;font-weight:800;line-height:1.1">Free level test</div></div></div>
<div style="background:#f8c12d;color:#0b1f3a;border-radius:24px;padding:20px;text-align:center"><div style="font-size:28px;font-weight:700">DM <b>“SAT English”</b> on WhatsApp</div><div style="font-size:44px;font-weight:800">+1 428 880 1826</div></div>''')

if __name__ == '__main__':
    out = g.HERE / 'out5'; out.mkdir(exist_ok=True)
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page(viewport={'width': 1080, 'height': 1350})
        for i, body in enumerate(S, 1):
            pg.set_content(page(i, len(S), body)); pg.wait_for_timeout(250)
            ov = pg.evaluate("()=>{const m=document.querySelector('.mn');let t=1e9,b=0;for(const c of m.children){const x=c.getBoundingClientRect();t=Math.min(t,x.top);b=Math.max(b,x.bottom)}return [Math.round(t),Math.round(b)]}")
            fn = out / f'SAT-Transitions-playful-{i}-of-8.png'
            pg.screenshot(path=str(fn)); print(fn.name, ov, 'OK' if ov[0] >= 242 and ov[1] <= 1215 else 'OVERFLOW')
        br.close()
