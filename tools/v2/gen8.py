import gen5 as b, gen7
from gen4 import ic, rgba, CHECK, XX
from playwright.sync_api import sync_playwright
Y, GREEN, CORAL, BLUE, PURPLE = b.Y, b.GREEN, b.CORAL, b.BLUE, b.PURPLE
kick = lambda a: b.kick(a, 'SAT STRATEGY')
stats = b.stats

S = []
S.append(f'''{b.kick('READING &amp; WRITING', 'SAT STRATEGY')}
<h1 class="t" style="font-size:110px;line-height:.98">Start with<br><em>grammar.</em></h1>
<p class="st2" style="font-size:42px">Not because it’s easy.<br><span>Because it’s finite.</span></p>
{stats([('∞','reading','endless texts, slow gains'),('~12','grammar rules','learn once, keep forever'),('46%','of the section','runs on rules &amp; patterns')])}
<p class="st2" style="font-size:30px;font-weight:700">The smartest first move most students skip. <span>Swipe →</span></p>''')

S.append(f'''{kick('KNOW THE TEST')}
<h1 class="t" style="font-size:86px">The test in<br><em>10 seconds</em></h1>
{stats([('54','questions','two modules of 27'),('64','minutes','32 per module'),('~71s','per question','64 × 60 ÷ 54')])}
<div class="card" style="display:flex;align-items:center;gap:22px"><div class="disc" style="width:74px;height:74px;background:{BLUE};font-size:36px">↗</div><div><div style="font-size:34px;font-weight:800">Every question is a solo</div><div style="font-size:27px;font-weight:500;color:#e6f0fb;margin-top:4px">One short passage each. No giant texts.</div></div></div>
<div class="card" style="display:flex;align-items:center;gap:22px"><div class="disc" style="width:74px;height:74px;background:{PURPLE};font-size:34px">⚖</div><div><div style="font-size:34px;font-weight:800">It’s adaptive</div><div style="font-size:27px;font-weight:500;color:#e6f0fb;margin-top:4px">Module 1 decides how hard Module 2 gets.</div></div></div>''')

col = lambda title, c, rows, icon: f'''<div class="card" style="flex:1;padding:22px 20px;border-color:{rgba(c,.8)} !important"><div style="display:flex;align-items:center;gap:12px;margin-bottom:10px"><div class="disc" style="width:54px;height:54px;background:{c}">{ic(icon,30,3.2)}</div><div style="font-size:32px;font-weight:800;color:{c}">{title}</div></div>{''.join(f'<div style="font-size:26px;font-weight:600;line-height:1.3;padding:13px 0;border-top:1.5px solid rgba(255,255,255,.16)">{r}</div>' for r in rows)}</div>'''
S.append(f'''{kick('TWO DIFFERENT GAMES')}
<h1 class="t" style="font-size:80px">Reading is a vibe.<br><em>Grammar is a rulebook.</em></h1>
<div style="display:flex;gap:16px">{col('Reading', CORAL, ['Guess from clues and shades of meaning', 'Two answers can both look right', 'Gets better slowly', 'No limit on what they can ask'], XX)}{col('Grammar', GREEN, ['One answer, set by a rule', 'Wrong answers break a nameable rule', 'Gets better fast, and stays', 'A closed list you can finish'], CHECK)}</div>''')

D = [('Craft &amp; Structure', 28, BLUE), ('Information &amp; Ideas', 26, PURPLE), ('Standard English Conventions', 26, Y), ('Expression of Ideas', 20, GREEN)]
bars = ''.join(f'<div style="margin-top:16px"><div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:8px"><span style="font-size:27px;font-weight:800">{n}</span><span style="font-size:32px;font-weight:800;color:{c}">~{p}%</span></div><div style="height:30px;border-radius:15px;background:rgba(255,255,255,.12);overflow:hidden"><div style="height:30px;width:{p/28*100:.0f}%;background:{c};border-radius:15px"></div></div></div>' for n, p, c in D)
S.append(f'''{kick('THE NUMBERS')}
<h1 class="t" style="font-size:80px">Almost half the points<br><em>follow rules</em></h1>
<div class="card" style="padding:24px 28px"><div style="font-size:21px;font-weight:800;letter-spacing:3px;color:#7fc4ff">SHARE OF READING &amp; WRITING</div>{bars}</div>
<div class="card" style="display:flex;align-items:center;gap:24px;border-color:{Y} !important"><div style="font-size:92px;font-weight:800;color:{Y};line-height:1">46%</div><div style="font-size:29px;font-weight:700;line-height:1.3">Conventions 26% + Expression of Ideas 20%. <span style="color:{Y}">Learnable. Predictable.</span></div></div>''')

topics = ['Sentence boundaries', 'Joining clauses', 'Non-essential clauses', 'Comma rules', 'Colons &amp; dashes', 'Subject–verb agreement', 'Verb tense', 'Pronouns', 'Apostrophes', 'Modifiers', 'Parallel structure', 'Word pairs']
toks = ''.join(f'<div class="card" style="display:flex;align-items:center;gap:12px;padding:14px 16px;border-radius:20px"><div class="disc" style="width:44px;height:44px;background:{Y};font-size:22px">{i}</div><span style="font-size:26px;font-weight:700;line-height:1.15">{t}</span></div>' for i, t in enumerate(topics, 1))
S.append(f'''{kick('THE WHOLE LIST')}
<h1 class="t" style="font-size:80px">~12 rules.<br><em>That’s the boss level.</em></h1>
<div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px">{toks}</div>
<p class="st2" style="font-size:31px">Spot the rule, <span>and the answer takes seconds.</span></p>''')

S.append(f'''{kick('WHY IT PAYS TWICE')}
<h1 class="t" style="font-size:80px">Module 1 is the<br><em>main character.</em></h1>
<div style="display:flex;flex-direction:column;gap:16px">
<div class="card" style="display:flex;align-items:center;gap:22px;border-color:{GREEN} !important"><div class="disc" style="width:78px;height:78px;background:{GREEN}">{ic(CHECK,44,3.2)}</div><div><div style="font-size:34px;font-weight:800;color:{GREEN}">Nail Module 1</div><div style="font-size:27px;font-weight:500;color:#e6f0fb;margin-top:4px">You unlock the harder Module 2, where the top scores live.</div></div></div>
<div class="card" style="display:flex;align-items:center;gap:22px;opacity:.9"><div class="disc" style="width:78px;height:78px;background:{CORAL}">{ic(XX,44,3.2)}</div><div><div style="font-size:34px;font-weight:800;color:{CORAL}">Slip in Module 1</div><div style="font-size:27px;font-weight:500;color:#e6f0fb;margin-top:4px">You get the easier Module 2, and your ceiling drops.</div></div></div></div>
{stats([('fast','points','grammar takes seconds'),('sure','points','rules don’t change'),('+time','for reading','the bonus round')])}''')

plan = [(1, Y, 'Grammar → near-perfect', 'Lose zero points on conventions.'), (2, GREEN, 'Expression of Ideas', 'Transitions + Student Notes. Patterns too.'), (3, BLUE, 'Reading, every day', 'Build it steadily while grammar pays off.')]
S.append(f'''{kick('THE GAME PLAN')}
<h1 class="t" style="font-size:84px">Your order<br><em>of attack</em></h1>
{''.join(f'<div class="card" style="display:flex;align-items:center;gap:22px;padding:22px 26px"><div class="num" style="width:80px;height:80px;font-size:44px;background:{c}">{i}</div><div><div style="font-size:36px;font-weight:800">{h}</div><div style="font-size:27px;font-weight:500;color:#e6f0fb;margin-top:4px">{p}</div></div></div>' for i,c,h,p in plan)}
<div class="card" style="display:flex;align-items:center;gap:18px;border-color:{CORAL} !important"><div class="disc" style="width:66px;height:66px;background:{CORAL}">{ic(XX,36,3.2)}</div><div style="font-size:29px;font-weight:700;line-height:1.3">Classic mistake: <span style="color:{CORAL}">only grinding more reading.</span> Relatable, but the wrong first move.</div></div>''')

S.append(b.S[7])

if __name__ == '__main__':
    out = b.g.HERE / 'out8'; out.mkdir(exist_ok=True)
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page(viewport={'width': 1080, 'height': 1350})
        for i, body in enumerate(S, 1):
            pg.set_content(gen7.page(i, len(S), body)); pg.wait_for_timeout(300)
            ov = pg.evaluate("()=>{const m=document.querySelector('.mn');let t=1e9,b=0;for(const c of m.children){const x=c.getBoundingClientRect();t=Math.min(t,x.top);b=Math.max(b,x.bottom)}return [Math.round(t),Math.round(b)]}")
            fn = out / f'SAT-Strategy-grad-{i}-of-8.png'
            pg.screenshot(path=str(fn)); print(fn.name, ov, 'OK' if ov[0] >= 242 and ov[1] <= 1215 else 'OVERFLOW')
        br.close()
