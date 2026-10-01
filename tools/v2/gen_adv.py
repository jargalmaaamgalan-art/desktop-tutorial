import gen4 as g
from gen4 import ic, rgba, Y, INK, TEAL, GREEN, CORAL, BLUE, PURPLE, CHECK, XX, ARR, KEY
from playwright.sync_api import sync_playwright

def page(n, total, body):
    return g.page(n, total, body).replace('SAT English · Chapter 1', 'SAT English · Study strategy')
def kick(label):
    return f'<div class="kick"><span class="bd">{label}</span><span class="ks">SAT STRATEGY</span></div>'
rule = g.rule
card = lambda inner, st='': f'<div class="card" style="{st}">{inner}</div>'

S = []
# 1 COVER
S.append(f'''<div class="kick"><span class="bd">SAT READING &amp; WRITING</span></div>
<h1 class="t" style="font-size:108px;line-height:.98">Start with<br><em>grammar.</em></h1>
<p class="lead" style="font-size:40px;color:#fff;font-weight:700">Not because it’s easy.<br><span style="color:#f6c343">Because it’s finite.</span></p>
<div style="display:flex;gap:16px;align-items:stretch">
<div class="card" style="flex:1;text-align:center;padding:26px 14px"><div class="lab2" style="color:{CORAL}">READING</div><div style="font-size:84px;font-weight:800;line-height:1;margin-top:10px;color:{CORAL}">∞</div><div style="font-size:24px;font-weight:700;margin-top:8px">endless texts,<br>slow progress</div></div>
<div style="display:flex;align-items:center;font-size:40px;font-weight:800;color:#9fd2e2">vs</div>
<div class="card" style="flex:1;text-align:center;padding:26px 14px;border-color:{Y}"><div class="lab2" style="color:{Y}">GRAMMAR</div><div style="font-size:84px;font-weight:800;line-height:1;margin-top:10px;color:{Y}">~12</div><div style="font-size:24px;font-weight:700;margin-top:8px">rules to learn,<br>fast progress</div></div></div>
<p class="lead">The smartest first move in SAT English, and the one most students skip. <b style="color:#fff">Swipe to see why →</b></p>''')

# 2 THE SECTION
stat = lambda n, l: f'<div class="card" style="text-align:center;padding:22px 8px"><div style="font-size:66px;font-weight:800;color:#f6c343;line-height:1">{n}</div><div style="font-size:23px;font-weight:700;margin-top:8px">{l}</div></div>'
S.append(f'''{kick('KNOW THE TEST')}
<h1 class="t" style="font-size:70px">The section<br><em>at a glance</em></h1>
<div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px">{stat('54','questions')}{stat('64','minutes')}{stat('2×27','two modules')}{stat('~71s','per question')}</div>
{card(f'<div style="display:flex;align-items:center;gap:20px"><div class="disc" style="width:70px;height:70px;background:{BLUE};font-size:34px">↗</div><div><div style="font-size:32px;font-weight:800">Every question stands alone</div><div style="font-size:26px;font-weight:600;color:#cfe3ea;margin-top:4px">A short passage each, no long shared texts.</div></div></div>')}
{card(f'<div style="display:flex;align-items:center;gap:20px"><div class="disc" style="width:70px;height:70px;background:{PURPLE};font-size:34px">⚖</div><div><div style="font-size:32px;font-weight:800">The section is adaptive</div><div style="font-size:26px;font-weight:600;color:#cfe3ea;margin-top:4px">Module 1 decides how hard Module 2 is.</div></div></div>')}
<div class="ks" style="font-size:18px">64 min × 60 ÷ 54 = 71.1 s · Check current specs on collegeboard.org</div>''')

# 3 TWO KINDS
rowsR = ['Depends on inference and shades of meaning', 'Two choices can both look defensible', 'Improves slowly and unevenly', 'No finite list of what can be asked']
rowsG = ['One answer, fixed by a rule', 'Wrong choices are wrong for nameable reasons', 'Improves fast, and it holds', 'A closed list of rules you can finish']
col = lambda title, c, rows, icon: f'''<div class="card" style="flex:1;padding:22px 20px;border-color:{rgba(c,.7)}"><div style="display:flex;align-items:center;gap:12px;margin-bottom:12px"><div class="disc" style="width:48px;height:48px;background:{c}">{ic(icon,28,3.2)}</div><div style="font-size:27px;font-weight:800;color:{c}">{title}</div></div>{''.join(f'<div style="font-size:24px;font-weight:600;line-height:1.3;padding:12px 0;border-top:1.5px solid rgba(255,255,255,.14)">{r}</div>' for r in rows)}</div>'''
S.append(f'''{kick('TWO KINDS OF QUESTION')}
<h1 class="t" style="font-size:68px">Reading vs grammar:<br><em>a different game</em></h1>
<div style="display:flex;gap:14px">{col('Reading', CORAL, rowsR, XX)}{col('Grammar', GREEN, rowsG, CHECK)}</div>
{rule('Grammar rewards study <b>more directly than anything else</b> in the section.')}''')

# 4 THE NUMBERS
D = [('Craft &amp; Structure', 28, BLUE, 'reading'), ('Information &amp; Ideas', 26, PURPLE, 'reading'), ('Standard English Conventions', 26, Y, 'rules'), ('Expression of Ideas', 20, GREEN, 'patterns')]
bars = ''.join(f'<div style="margin-top:16px"><div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:8px"><span style="font-size:25px;font-weight:800">{n}</span><span style="font-size:30px;font-weight:800;color:{c}">~{p}%</span></div><div style="height:30px;border-radius:15px;background:rgba(255,255,255,.1);overflow:hidden"><div style="height:30px;width:{p/28*100:.0f}%;background:{c};border-radius:15px"></div></div></div>' for n, p, c, t in D)
S.append(f'''{kick('THE NUMBERS')}
<h1 class="t" style="font-size:68px">Almost half the section<br><em>runs on rules</em></h1>
{card(f'<div class="lab2">SHARE OF READING &amp; WRITING</div>{bars}', 'padding:24px 28px')}
<div class="card" style="display:flex;align-items:center;gap:22px;padding:22px 26px;border-color:{Y}"><div style="font-size:78px;font-weight:800;color:#f6c343;line-height:1">~46%</div><div style="font-size:27px;font-weight:700;line-height:1.3">Conventions <b>(26%)</b> + Expression of Ideas <b>(20%)</b>: rule- and pattern-based points</div></div>
<div class="ks" style="font-size:18px">Published domain weightings, approximate · 26 + 20 = 46</div>''')

# 5 FINITE LIST
topics = ['Sentence boundaries', 'Joining clauses', 'Non-essential clauses', 'Comma rules', 'Colons &amp; dashes', 'Subject–verb agreement', 'Verb tense', 'Pronouns', 'Apostrophes', 'Modifiers', 'Parallel structure', 'Word pairs &amp; comparisons']
toks = ''.join(f'<div style="display:flex;align-items:center;gap:12px;background:rgba(255,255,255,.08);border:2px solid rgba(255,255,255,.2);border-radius:18px;padding:14px 16px"><div class="disc" style="width:40px;height:40px;background:{Y};font-size:20px">{i}</div><span style="font-size:24px;font-weight:700;line-height:1.15">{t}</span></div>' for i, t in enumerate(topics, 1))
S.append(f'''{kick('A CLOSED LIST')}
<h1 class="t" style="font-size:68px">About a dozen rules.<br><em>Learn them once.</em></h1>
<div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px">{toks}</div>
{rule('Spot which rule a question tests, and <b>the answer follows in seconds.</b>')}''')

# 6 ADAPTIVE
S.append(f'''{kick('WHY IT PAYS TWICE')}
<h1 class="t" style="font-size:68px">Sure points early<br><em>raise your ceiling</em></h1>
<div class="card" style="padding:26px 24px">
<div style="display:flex;align-items:center;gap:16px">
<div style="flex:none;width:200px;text-align:center"><div style="background:#f7f2e7;color:{INK};border-radius:22px;padding:22px 10px"><div style="font-size:22px;font-weight:800;letter-spacing:2px;color:#1f6f8b">MODULE 1</div><div style="font-size:26px;font-weight:800;margin-top:6px;line-height:1.2">grammar<br>done right</div></div></div>
<svg width="120" height="220" viewBox="0 0 120 220"><path d="M6 110 C60 110 60 40 112 40" stroke="{GREEN}" stroke-width="7" fill="none" stroke-linecap="round"></path><path d="M6 110 C60 110 60 180 112 180" stroke="rgba(255,255,255,.35)" stroke-width="7" fill="none" stroke-linecap="round" stroke-dasharray="4 12"></path></svg>
<div style="flex:1;display:flex;flex-direction:column;gap:28px">
<div style="background:{rgba(GREEN,.2)};border:2.5px solid {GREEN};border-radius:20px;padding:18px 20px"><div style="font-size:27px;font-weight:800;color:{GREEN}">Harder Module 2</div><div style="font-size:23px;font-weight:700;margin-top:4px">full score range open</div></div>
<div style="background:rgba(255,255,255,.06);border:2px dashed rgba(255,255,255,.3);border-radius:20px;padding:18px 20px;opacity:.75"><div style="font-size:27px;font-weight:800">Easier Module 2</div><div style="font-size:23px;font-weight:700;margin-top:4px">top scores out of reach</div></div></div></div></div>
<p class="lead">Early questions carry more weight than their number suggests. Grammar you’ve mastered is <b style="color:#fff">fast, reliable points exactly where they count most.</b></p>
{rule('Bonus: seconds saved on grammar become <b>extra time for reading.</b>')}''')

# 7 THE PLAN
plan = [(1, Y, 'Grammar to near-perfect', 'Aim to lose zero points on conventions.'),
        (2, GREEN, 'Expression of Ideas', 'Transitions and Student Notes: pattern-based too.'),
        (3, BLUE, 'Reading, every day', 'Build it steadily while grammar pays off.')]
S.append(f'''{kick('THE GAME PLAN')}
<h1 class="t" style="font-size:70px">Your order<br><em>of attack</em></h1>
{''.join(f'<div class="card" style="display:flex;align-items:center;gap:22px;padding:24px 26px"><div class="num" style="width:78px;height:78px;font-size:42px;background:{c}">{i}</div><div><div style="font-size:35px;font-weight:800">{h}</div><div style="font-size:26px;font-weight:600;color:#cfe3ea;margin-top:4px">{p}</div></div></div>' for i,c,h,p in plan)}
<div class="card" style="display:flex;align-items:center;gap:18px;padding:20px 26px"><div class="disc" style="width:62px;height:62px;background:{CORAL}">{ic(XX,34,3.2)}</div><div style="font-size:27px;font-weight:700;line-height:1.3">The common mistake: <b>only doing more reading practice.</b> Understandable, but usually the wrong first move.</div></div>''')

# 8 CTA
S.append(g.S[7].replace('NEXT SERIES · CHAPTER 2 · STUDENT NOTES →', 'OUR COURSE STARTS WITH GRAMMAR, FOR EXACTLY THESE REASONS'))

if __name__ == '__main__':
    out = g.HERE / 'out_adv'; out.mkdir(exist_ok=True)
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page(viewport={'width': 1080, 'height': 1350})
        for i, body in enumerate(S, 1):
            pg.set_content(page(i, len(S), body)); pg.wait_for_timeout(250)
            ov = pg.evaluate("()=>{const m=document.querySelector('.mn');let t=1e9,b=0;for(const c of m.children){const x=c.getBoundingClientRect();t=Math.min(t,x.top);b=Math.max(b,x.bottom)}return [Math.round(t),Math.round(b)]}")
            fn = out / f'SAT-Strategy-Grammar-First-{i}-of-8.png'
            pg.screenshot(path=str(fn)); print(fn.name, ov, 'OK' if ov[0] >= 120 and ov[1] <= 1246 else 'OVERFLOW')
        br.close()
