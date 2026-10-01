import pathlib
import gen4 as g
from gen4 import ic, rgba, Y, INK, TEAL, GREEN, CORAL, BLUE, PURPLE, CHECK, XX, ARR, KEY
from playwright.sync_api import sync_playwright

def page(n, total, body):
    return g.page(n, total, body).replace('SAT English · Chapter 1', 'SAT English · Chapter 2')
def kick(label):
    return f'<div class="kick"><span class="bd">{label}</span><span class="ks">STUDENT NOTES</span></div>'
rule = g.rule
PEN = '<path d="M5 4v7a7 7 0 0 0 14 0V4"/><path d="M4 21h16"/>'
TARGET = '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.5"/>'

def notes(items, size=27, title='STUDENT NOTES'):
    lis = ''.join(f'<div style="display:flex;gap:12px;align-items:flex-start"><span style="flex:none;width:12px;height:12px;border-radius:50%;background:#134560;margin-top:{size*0.55:.0f}px"></span><span>{t}</span></div>' for t in items)
    return f'<div class="sent" style="font-size:{size}px;padding:22px 28px;display:flex;flex-direction:column;gap:6px"><div style="font-family:M,sans-serif;font-size:19px;font-weight:800;letter-spacing:3px;color:#1f6f8b;margin-bottom:4px">{title}</div>{lis}</div>'
def goal(html, size=29):
    return f'<div class="card" style="display:flex;align-items:center;gap:18px;padding:18px 24px"><div class="disc" style="width:58px;height:58px;background:{Y}">{ic(TARGET,32)}</div><div style="font-size:{size}px;font-weight:700;line-height:1.3">{html}</div></div>'
def tk(t, c, size=26):
    return f'<span class="tok" style="background:{c};color:{INK};font-size:{size}px;padding:6px 16px">{t}</span>'
def choice(t, tag, state, size=24):
    bg = {1: rgba(Y, .22), 0: 'rgba(255,255,255,.07)'}[1 if state == 1 else 0]
    bc = Y if state == 1 else 'rgba(255,255,255,.2)'
    tc = GREEN if state == 1 else CORAL
    return f'<div style="display:flex;align-items:center;gap:12px;background:{bg};border:2.5px solid {bc};border-radius:16px;padding:12px 16px"><div style="flex:1;font-family:S,serif;font-size:{size}px;line-height:1.3">{t}</div><span style="flex:none;font-size:17px;font-weight:800;letter-spacing:1px;padding:6px 12px;border-radius:20px;background:{tc if state==1 else rgba(CORAL,.22)};color:{INK if state==1 else "#fff"}">{tag}</span></div>'

CARSON = ['Rachel Carson was a marine biologist.', 'In 1962, she published <i>Silent Spring</i>.', 'The book documented harm caused by the pesticide DDT.', 'It helped inspire the modern environmental movement.']

S = []
# 1 COVER
S.append(f'''<div class="kick"><span class="bd">SAT ENGLISH · CHAPTER 2</span></div>
<h1 class="t" style="font-size:112px;line-height:.98">Student Notes</h1>
<p class="lead" style="font-size:40px;color:#c9f2ff;font-weight:700">Rhetorical synthesis, decoded</p>
<div style="display:flex;align-items:center;gap:16px">
<div class="sent" style="flex:1.2;font-size:24px;padding:20px 22px;line-height:1.5"><div style="font-family:M,sans-serif;font-size:16px;font-weight:800;letter-spacing:2px;color:#1f6f8b">NOTES</div>• fact one<br>• fact two<br>• fact three</div>
{ic(ARR,48,3,TEAL)}
<div style="flex:1;text-align:center" class="card"><div class="disc" style="width:70px;height:70px;background:{Y};margin:0 auto">{ic(TARGET,40)}</div><div style="font-size:24px;font-weight:800;margin-top:10px">the goal</div></div>
{ic(ARR,48,3,TEAL)}
<div style="flex:1;text-align:center" class="card"><div class="disc" style="width:70px;height:70px;background:{GREEN};margin:0 auto">{ic(CHECK,40,3)}</div><div style="font-size:24px;font-weight:800;margin-top:10px">one answer</div></div></div>
<p class="lead">Every choice is accurate. <b style="color:#fff">Only one does what the student actually wants.</b> Learn to read the goal, and these become free points.</p>
<div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px">{''.join(f'<div class="card" style="text-align:center;padding:22px 10px"><div style="font-size:70px;font-weight:800;color:#f6c343;line-height:1">{n}</div><div style="font-size:25px;font-weight:700;margin-top:6px">{l}</div></div>' for n,l in (('4','step method'),('4','goal types'),('2','classic traps')))}</div>''')

# 2 CORE IDEA
S.append(f'''{kick('THE CORE IDEA')}
<h1 class="t" style="font-size:68px">The goal, not the notes,<br><em>picks the answer</em></h1>
{notes(CARSON, 28)}
{goal('The student wants to <b style="color:#f6c343">emphasize the book’s impact.</b>', 30)}
<div class="card" style="padding:20px 24px"><div class="lab2" style="margin-bottom:10px">ONLY ONE NOTE SERVES THAT GOAL</div><div style="font-family:S,serif;font-size:29px;line-height:1.35">Carson’s <i>Silent Spring</i> <span class="mk">helped inspire the modern environmental movement</span>.</div></div>
{rule('All four options will be true. The question tests whether you can <b>serve one specific purpose.</b>')}''')

# 3 METHOD
steps = ((1, 'Read the goal first', 'Skip the notes for now.'), (2, 'Underline two things', 'the purpose verb + the topic'), (3, 'Predict the content', 'What must the sentence mention?'), (4, 'Eliminate off-goal options', 'True isn’t enough.'))
S.append(f'''{kick('THE METHOD')}
<h1 class="t" style="font-size:68px">Goal first,<br><em>notes second</em></h1>
{''.join(f'<div style="display:flex;align-items:center;gap:20px"><div class="num">{i}</div><div style="flex:1"><div style="font-size:32px;font-weight:800">{h}</div><div style="font-size:26px;font-weight:600;color:#cfe3ea;margin-top:2px">{p}</div></div></div>' for i,h,p in steps)}
{goal('…wants to ' + tk('emphasize', Y) + ' the book’s ' + tk('impact', TEAL) + '', 29)}
<div style="display:flex;flex-direction:column;gap:9px">
{choice('Carson, a marine biologist, published <i>Silent Spring</i> in 1962.', 'NO IMPACT', 0)}
{choice('<i>Silent Spring</i> documented harm caused by DDT.', 'CONTENT ONLY', 0)}
{choice('Carson’s <i>Silent Spring</i> helped inspire the modern environmental movement.', '✓ IMPACT', 1)}</div>''')

# 4 GOAL SIGNALS
G = [('contrast', CORAL, '≠', '<i>whereas · although · but</i>', 'Whereas Everest is 8,849 m tall, K2 is 8,611 m.'),
     ('similarity', GREEN, '=', '<i>both · similarly · like</i>', 'Both species hunt mainly at night.'),
     ('new audience', BLUE, 'i', 'background: <b>who or what</b> it is', 'Rachel Carson, <u>a marine biologist</u>, …'),
     ('A and B', PURPLE, '2', 'a sentence with <b>both</b> parts', 'Using satellite data, the team found …')]
rows = ''.join(f'''<div class="card" style="padding:16px 22px"><div style="display:flex;align-items:center;gap:14px">{tk(s+'&nbsp;&nbsp;'+g_, c, 26)}{ic(ARR,34,3,TEAL)}<div style="flex:1;font-size:25px;font-weight:700;line-height:1.25">{l}</div></div>
<div style="font-family:S,serif;font-size:25px;line-height:1.35;margin-top:10px;color:#f4f8fa;padding-left:6px;border-left:4px solid {c};padding-left:14px">{e}</div></div>''' for g_, c, s, l, e in G)
S.append(f'''{kick('GOAL TYPES')}
<h1 class="t" style="font-size:68px">Goal words are<br><em>clues in disguise</em></h1>
<div style="display:flex;flex-direction:column;gap:12px">{rows}</div>''')

# 5 TRAP 1 accurate != right
def cell(ok):
    return f'<div class="disc" style="width:64px;height:64px;margin:0 auto;background:{GREEN if ok else CORAL}">{ic(CHECK if ok else XX,36,3.4)}</div>'
trs = ''.join(f'<div style="display:grid;grid-template-columns:1.7fr 1fr 1fr;align-items:center;padding:16px 0;border-top:1.5px solid rgba(255,255,255,.15)"><div style="font-size:29px;font-weight:800;line-height:1.15">{q}</div>{cell(a)}{cell(b)}</div>' for q, a, b in (('Is it accurate?', 1, 1), ('Is it from the notes?', 1, 1), ('Does it serve the goal?', 0, 1)))
S.append(f'''{kick('TRAP 1 · TRUE BUT USELESS')}
<h1 class="t" style="font-size:68px">Accurate isn’t<br><em>the same as right</em></h1>
<div class="card" style="padding:22px 28px"><div style="display:grid;grid-template-columns:1.7fr 1fr 1fr;padding-bottom:12px;text-align:center"><div></div>
<div><div style="font-size:21px;font-weight:800;letter-spacing:2px;color:{CORAL}">CHOICE B</div><div style="font-size:17px;font-weight:700;color:#cfe3ea">“documented DDT harm”</div></div>
<div><div style="font-size:21px;font-weight:800;letter-spacing:2px;color:{GREEN}">CHOICE C</div><div style="font-size:17px;font-weight:700;color:#cfe3ea">“inspired a movement”</div></div></div>{trs}</div>
<p class="lead">Wrong answers aren’t false. They’re <b style="color:#fff">true facts aimed at the wrong target</b>, which is exactly why they feel safe.</p>
{rule('Never ask “Is this true?” Ask <b>“Does this do the job?”</b>')}''')

# 6 TRAP 2 near-miss
def bar(frac, col, label, verdict):
    return f'<div style="margin-top:18px"><div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:10px"><span style="font-size:24px;font-weight:800">{label}</span><span style="font-size:24px;font-weight:800;color:{col}">{verdict}</span></div><div style="height:36px;border-radius:18px;background:rgba(255,255,255,.12);overflow:hidden"><div style="height:36px;width:{frac}%;background:{col};border-radius:18px"></div></div></div>'
S.append(f'''{kick('TRAP 2 · NEAR-MISS')}
<h1 class="t" style="font-size:68px">Half the goal<br><em>is still a miss</em></h1>
{goal('…wants to present the study’s ' + tk('method', Y) + ' and its ' + tk('result', TEAL), 29)}
<div class="card" style="padding:22px 26px">
<div style="font-family:S,serif;font-size:27px;line-height:1.35">“The team found that wolf packs cover long distances each day.”</div>
{bar(50, CORAL, 'result only', '1 of 2 · MISS')}
<div style="height:1.5px;background:rgba(255,255,255,.15);margin:22px 0 18px"></div>
<div style="font-family:S,serif;font-size:27px;line-height:1.35">“<span class="mk">Using GPS collars</span>, the team found that wolf packs cover long distances each day.”</div>
{bar(100, GREEN, 'method + result', '2 of 2 · CORRECT')}</div>
{rule('Count the parts of the goal, then <b>check every choice against each part.</b>')}''')

# 7 PRACTICE
S.append(f'''{kick('YOUR TURN')}
<h1 class="t" style="font-size:66px">Try a real-style<br><em>question</em></h1>
{notes(['Mount Everest is 8,849 meters tall.', 'It lies on the border of Nepal and China.', 'K2 is 8,611 meters tall.', 'It lies on the border of Pakistan and China.'], 25)}
{goal('…wants to ' + tk('contrast', CORAL, 24) + ' the ' + tk('heights', Y, 24) + ' of the two mountains.', 26)}
<div style="display:flex;flex-direction:column;gap:9px">
{choice('A) Mount Everest lies on the border of Nepal and China.', 'NO HEIGHTS', 0, 23)}
{choice('B) Both Mount Everest and K2 lie on China’s border.', 'SIMILARITY', 0, 23)}
{choice('C) Whereas Mount Everest is 8,849 meters tall, K2 is 8,611 meters tall.', '✓ CONTRAST', 1, 23)}
{choice('D) K2, which is 8,611 meters tall, lies on China’s border.', 'ONE HEIGHT', 0, 23)}</div>
{rule('Answer: <b>C.</b> <i>Whereas</i> signals contrast, and both heights appear.', 'THE ANSWER')}''')

# 8 ENROLL (reuse ch1, change footer line)
S.append(g.S[7].replace('NEXT SERIES · CHAPTER 2 · STUDENT NOTES →', 'MORE CHAPTERS COMING SOON →'))

if __name__ == '__main__':
    out = g.HERE / 'out4c2'; out.mkdir(exist_ok=True)
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page(viewport={'width': 1080, 'height': 1350})
        for i, body in enumerate(S, 1):
            pg.set_content(page(i, len(S), body)); pg.wait_for_timeout(250)
            ov = pg.evaluate("()=>{const m=document.querySelector('.mn');let t=1e9,b=0;for(const c of m.children){const x=c.getBoundingClientRect();t=Math.min(t,x.top);b=Math.max(b,x.bottom)}return [Math.round(t),Math.round(b)]}")
            fn = out / f'SAT-English-v4-Ch2-{i}-of-8.png'
            pg.screenshot(path=str(fn)); print(fn.name, ov, 'OK' if ov[0] >= 120 and ov[1] <= 1246 else 'OVERFLOW')
        br.close()
