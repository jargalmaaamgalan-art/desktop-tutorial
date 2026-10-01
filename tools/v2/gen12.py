import gen4 as g
from playwright.sync_api import sync_playwright

GOLD = '#f8c12d'; SKY = '#bfe6ff'; CORAL = '#ff8a80'; BLUE = '#8fd3ff'; MINT = '#5fd6a8'
TOTAL = 9
CSS = g.ff + f"""
*{{box-sizing:border-box}}
body{{margin:0;width:1080px;height:1350px;font-family:M,sans-serif;color:#fff;overflow:hidden}}
.pg{{width:1080px;height:1350px;position:relative;overflow:hidden;background:linear-gradient(160deg,#123f73 0%,#0c2f5c 50%,#08244a 100%)}}
.gr{{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.028) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.028) 1px,transparent 1px);background-size:60px 60px}}
.arc{{position:absolute;right:-230px;top:230px;width:520px;height:520px;border-radius:50%;border:70px solid rgba(143,211,255,.05)}}
.arc2{{position:absolute;left:-260px;bottom:40px;width:480px;height:480px;border-radius:50%;border:60px solid rgba(143,211,255,.04)}}
.hd{{position:absolute;top:54px;left:64px;right:64px;display:flex;align-items:center;justify-content:space-between}}
.lg{{display:flex;align-items:center;gap:16px}}
.lgt{{font-weight:800;font-size:25px;letter-spacing:3px;line-height:1.3}}
.lgt span{{display:block;color:{GOLD};font-size:17px;letter-spacing:3.5px;font-weight:600}}
.rt{{display:flex;align-items:center;gap:22px}}
.sat{{font-weight:800;font-size:46px;letter-spacing:-1px}} .sat sup{{font-size:12px;vertical-align:top;position:relative;top:6px}}
.vl{{width:2px;height:54px;background:rgba(255,255,255,.28)}}
.pn{{font-weight:800;font-size:28px;color:#d6e4f5}} .pn b{{color:{GOLD};font-size:34px}}
.mn{{position:absolute;top:160px;left:64px;right:64px;bottom:128px;display:flex;flex-direction:column;justify-content:center;gap:20px}}
.kick{{display:flex;align-items:center;gap:18px}}
.bd{{background:{GOLD};color:#0b1f3a;border-radius:40px;padding:11px 28px;font-weight:800;font-size:25px;letter-spacing:3px}}
.ks{{font-weight:800;font-size:25px;letter-spacing:3px;color:#8fd3ff}}
.t{{margin:0;font-weight:800;font-size:78px;line-height:1.03;letter-spacing:-1.5px}}
.t em{{font-style:normal;color:{SKY}}}
.sent{{background:#f7f2e7;color:#12203a;border-radius:26px;padding:24px 32px;font-family:S,serif;font-size:37px;line-height:1.42;box-shadow:0 16px 36px rgba(0,0,0,.3)}}
.blank{{display:inline-block;width:170px;border-bottom:4px solid #12203a;transform:translateY(-9px)}}
.mk{{background:{GOLD};border-radius:8px;padding:0 10px;font-weight:700}}
.ch{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}}
.c{{border:2px solid rgba(143,211,255,.35);background:rgba(8,28,60,.45);border-radius:18px;padding:16px 24px;font-size:32px;font-weight:700}}
.c.ok{{border:3px solid {GOLD};color:{GOLD};background:rgba(248,193,45,.08)}}
.c.x{{opacity:.55;text-decoration:line-through;text-decoration-thickness:3px}}
.steps{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}}
.st{{border:2px solid rgba(143,211,255,.3);background:rgba(8,28,60,.45);border-radius:22px;padding:18px 18px}}
.st .n{{width:52px;height:52px;border-radius:50%;color:#0b1f3a;font-weight:800;font-size:28px;display:flex;align-items:center;justify-content:center;margin-bottom:12px}}
.st .h{{font-size:28px;font-weight:800;line-height:1.15;margin-bottom:8px}}
.st .p{{font-size:24px;font-weight:500;line-height:1.35;color:#e3edf8}}
.rule{{background:{GOLD};color:#0b1f3a;border-radius:24px;padding:22px 30px}}
.rule .l{{font-size:19px;font-weight:800;letter-spacing:3px;color:#6b5210}}
.rule .x{{font-size:30px;font-weight:800;line-height:1.3;margin-top:4px}}
.stats{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px}}
.sc{{border:2px solid rgba(143,211,255,.3);background:rgba(8,28,60,.45);border-radius:24px;padding:22px 14px;text-align:center}}
.sc .n{{font-size:84px;font-weight:800;color:{GOLD};line-height:1}}
.sc .l{{font-size:30px;font-weight:800;margin-top:6px;line-height:1.15}}
.sc .d{{height:2px;background:rgba(143,211,255,.3);margin:14px 20px}}
.sc .s{{font-size:24px;line-height:1.3;color:#e3edf8}}
.lead{{margin:0;font-size:34px;font-weight:700;line-height:1.3}} .lead span{{color:{GOLD}}}
.ft{{position:absolute;left:64px;right:64px;bottom:48px}}
.tr{{height:7px;border-radius:7px;background:rgba(255,255,255,.16);margin-bottom:18px;overflow:hidden}} .tf{{height:7px;background:{GOLD}}}
.fr{{display:flex;justify-content:space-between;font-size:23px;font-weight:500;color:#e3edf8}}
"""
import base64 as _b
HDR = 'data:image/png;base64,' + _b.b64encode((g.HERE/'hdr_logo.png').read_bytes()).decode()
LOGO = g.LOGO.replace('width="52" height="48"', 'width="66" height="62"').replace('#f6c343', GOLD)

def page(n, body):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="pg"><div class="gr"></div><div class="arc"></div><div class="arc2"></div>
<div class="hd"><img src="{HDR}" style="width:952px;height:auto;display:block"></div>
<div class="mn">{body}</div>
<div class="ft"><div class="tr"><div class="tf" style="width:{n/TOTAL*100:.1f}%"></div></div><div class="fr"><span>@globalmathprep · globalmathprep.academy</span><span>SAT English · <b style="color:#f8c12d">{n:02d}</b> / {TOTAL:02d}</span></div></div></div></body></html>'''

kick = lambda a, b='TRANSITIONS': f'<div class="kick"><span class="bd">{a}</span><span class="ks">{b}</span></div>'
def choices(items):
    return '<div class="ch">' + ''.join(f'<div class="c {cl}">{t}</div>' for t, cl in items) + '</div>'
def steps(items):
    cols = (CORAL, BLUE, MINT)
    return '<div class="steps">' + ''.join(f'<div class="st"><div class="n" style="background:{cols[i]}">{i+1}</div><div class="h" style="color:{cols[i]}">{h}</div><div class="p">{p}</div></div>' for i, (h, p) in enumerate(items)) + '</div>'
rule = lambda x, l='THE RULE': f'<div class="rule"><div class="l">{l}</div><div class="x">{x}</div></div>'
def stats(items):
    return '<div class="stats">' + ''.join(f'<div class="sc"><div class="n">{n}</div><div class="l">{l}</div><div class="d"></div><div class="s">{s}</div></div>' for n, l, s in items) + '</div>'

S = []
S.append(f'''<div style="text-align:center"><h1 class="t" style="font-size:124px">Transitions<br><em style="font-size:88px">made simple</em></h1></div>
<p class="lead" style="text-align:center">Pick the word that links two ideas.<br><span>It’s logic, not grammar.</span></p>
<div class="sent">The first draft was rejected. <span class="mk">&nbsp;&nbsp;?&nbsp;&nbsp;</span>, the second one won the prize.</div>
<div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap">{''.join(f'<span style="border:2px solid rgba(255,255,255,.4);border-radius:14px;padding:9px 16px;font-size:24px;font-weight:700;{"background:"+SKY+";color:#0b1f3a;border-color:"+SKY if i==0 else ""}">{w}</span>' for i,w in enumerate(['However','Therefore','Moreover','For instance','In fact']))}</div>
{stats([('5','relationship types','contrast · cause · example · emphasis · continue'),('4','step method','predict first, then match'),('6','worked questions','with the answer explained')])}''')

S.append(f'''{kick('THE CORE IDEA')}
<h1 class="t">What does a<br>transition <em>really do?</em></h1>
<div class="sent">Solar panels are expensive to install. <span class="mk">However</span>, they pay for themselves within a decade.</div>
<p class="lead">A transition doesn’t add a new fact. <span>It shows how idea B connects to idea A.</span></p>
{stats([('2','ideas','cost now vs. savings later'),('1','relationship','these ideas contrast'),('0','new facts','the transition only signals the link')])}''')

S.append(f'''{kick('THE METHOD')}
<h1 class="t">Predict first,<br><em>then match</em></h1>
<div class="sent" style="font-size:35px">Solar panels are expensive to install. <span style="white-space:nowrap"><span class="blank"></span>,</span> they pay for themselves within a decade.</div>
{''.join(f'<div style="display:flex;align-items:center;gap:22px"><div style="flex:none;width:66px;height:66px;border-radius:18px;background:{GOLD};color:#0b1f3a;font-weight:800;font-size:34px;display:flex;align-items:center;justify-content:center">{i}</div><div><div style="font-size:33px;font-weight:800">{h}</div><div style="font-size:26px;color:{SKY};margin-top:2px">{p}</div></div></div>' for i,h,p in ((1,'Cover the choices','Don’t let a polished word lead you.'),(2,'Paraphrase both ideas','“It costs a lot … but it pays off.”'),(3,'Predict your own word','You’d say “but”, so the family is Contrast.'),(4,'Match the family','Pick the only Contrast option.')))}
{choices([('A) Therefore',''),('B) However','ok'),('C) For example',''),('D) Similarly','')])}''')

S.append(f'''{kick('EXAMPLE')}
<h1 class="t">Give a <em>specific case</em></h1>
<div class="sent">Some birds travel remarkable distances. <span style="white-space:nowrap"><span class="blank"></span>,</span> the Arctic tern flies from pole to pole every year.</div>
{choices([('A) However',''),('B) Therefore',''),('C) For instance','ok'),('D) Similarly','')])}
{steps([('Read the meaning','Sentence 2 names one bird that illustrates sentence 1.'),('Name the type','General claim, then one specific case = Example.'),('Check the fit','“For instance” introduces that case.')])}
{rule('Use <i>for example</i> or <i>for instance</i> when the second idea is a specific case of the first.')}''')

S.append(f'''{kick('CAUSE &amp; EFFECT')}
<h1 class="t">Find the cause<br><em>and the result</em></h1>
<div class="sent" style="font-size:33px">Octopuses have no bones; only their beak is hard. <span style="white-space:nowrap"><span class="blank"></span>,</span> they can squeeze through openings barely larger than that beak.</div>
{choices([('A) Nevertheless',''),('B) Consequently','ok'),('C) Similarly',''),('D) For instance','')])}
{steps([('Find the link','Sentence 1 gives the reason: no bones.'),('Name the type','Sentence 2 is what happens because of it.'),('Check the fit','“Consequently” signals a result.')])}
{rule('Use <i>consequently, therefore, thus</i> when the second idea is the result of the first.')}''')

S.append(f'''{kick('EMPHASIS')}
<h1 class="t">Make the point<br><em>even stronger</em></h1>
<div class="sent">The exam was hard. <span style="white-space:nowrap"><span class="blank"></span>,</span> no one finished it.</div>
{choices([('A) However',''),('B) Nevertheless',''),('C) In fact','ok'),('D) Similarly','')])}
{steps([('Read the meaning','“Very hard” becomes “no one finished”.'),('Name the type','Same idea, pushed further = Emphasis.'),('Check the fit','“In fact” intensifies the first idea.')])}
{rule('Use <i>in fact</i> or <i>indeed</i> when the second idea makes the first one stronger.')}''')

S.append(f'''{kick('TRAP · TWINS')}
<h1 class="t">Two answers that<br><em>cancel each other out</em></h1>
<div class="sent" style="font-size:37px">The factory switched to solar power. <span style="white-space:nowrap"><span class="blank"></span>,</span> its energy bills fell sharply.</div>
{choices([('A) However','x'),('B) Nevertheless','x'),('C) As a result','ok'),('D) For instance','')])}
{steps([('Spot the twins','A and B both show contrast, so both go.'),('Find the link','Solar power → lower bills: a result.'),('Choose','“As a result” shows the effect.')])}
{rule('When two choices do the same job, eliminate both at once.')}''')

S.append(f'''{kick('YOUR TURN')}
<h1 class="t">Can you<br><em>crack this one?</em></h1>
<div class="sent">The city added more bus routes. <span style="white-space:nowrap"><span class="blank"></span>,</span> it lowered fares for students.</div>
{choices([('A) However',''),('B) Moreover',''),('C) Consequently',''),('D) For example','')])}
{steps([('Paraphrase','Put both ideas in your own words.'),('Predict','Would you say “but”, “so” or “and also”?'),('Match','Find the choice in that family.')])}
{rule('Comment <b>A, B, C or D</b> below. We’ll reply with the answer and why.', 'CHALLENGE')}''')

days = ''.join(f'<div style="flex:1;background:#f7f2e7;color:#0b1f3a;border-radius:14px;padding:16px 4px;text-align:center;font-weight:800;font-size:36px">{d}</div>' for d in ('Tue', 'Thu', 'Sat'))
chk = ''.join(f'<div style="display:flex;gap:12px;align-items:center"><span style="color:{GOLD};font-weight:800">✓</span>{x}</div>' for x in ('Live on Zoom from Canada', 'Nov &amp; Dec SAT sittings', 'Weekly report for parents'))
S.append(f'''{kick('ENROLLMENT OPEN','SAT ENGLISH')}
<h1 class="t" style="font-size:76px">A new cohort<br><em>is forming now</em></h1>
<div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px">{''.join(f'<div class="sc" style="padding:14px 6px"><div class="n" style="font-size:52px">{n}</div><div class="l" style="font-size:22px;font-weight:600">{l}</div></div>' for n,l in (('6','seats left'),('2–5','per group'),('3×','a week'),('80','min per class')))}</div>
<div style="display:flex;gap:18px">
<div class="st" style="flex:1.7;padding:28px 30px;display:flex;flex-direction:column;gap:18px;border:3px solid rgba(248,193,45,.7)"><div class="ks" style="font-size:25px">SCHEDULE · MONGOLIA TIME</div><div style="display:flex;gap:12px">{days}</div><div style="font-size:80px;font-weight:800;line-height:1">18:30–19:50</div><div style="display:flex;flex-direction:column;gap:10px;font-size:29px;font-weight:600">{chk}</div></div>
<div style="flex:1;background:#fff;border-radius:24px;padding:14px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;color:#0b1f3a;text-align:center"><img src="{g.QR}" style="width:100%;height:auto;display:block"><div style="font-size:28px;font-weight:800;line-height:1.1">Scan to register</div></div></div>
<div class="rule" style="text-align:center"><div class="x" style="font-weight:700">Message <b>“SAT English”</b> on WhatsApp</div><div style="font-size:48px;font-weight:800">+1 428 880 1826</div></div>
<div class="ks" style="text-align:center;font-size:23px;letter-spacing:1px">Register: globalmathprep.academy/portal#join · Free test: globalmathprep.academy/test</div>''')

if __name__ == '__main__':
    out = g.HERE / 'out12'; out.mkdir(exist_ok=True)
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page(viewport={'width': 1080, 'height': 1350})
        for i, body in enumerate(S, 1):
            pg.set_content(page(i, body)); pg.wait_for_timeout(250)
            ov = pg.evaluate("()=>{const m=document.querySelector('.mn');let t=1e9,b=0;for(const c of m.children){const x=c.getBoundingClientRect();t=Math.min(t,x.top);b=Math.max(b,x.bottom)}return [Math.round(t),Math.round(b)]}")
            fn = out / f'SAT-Transitions-final-{i:02d}-of-09.png'
            pg.screenshot(path=str(fn)); print(fn.name, ov, 'OK' if ov[0] >= 150 and ov[1] <= 1230 else 'OVERFLOW')
        br.close()
