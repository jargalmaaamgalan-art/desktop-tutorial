import gen10 as a
import gen4 as g
from playwright.sync_api import sync_playwright
GOLD, CREAM, TEAL = a.GOLD, a.CREAM, a.TEAL
MINT = '#5fd6a8'; CORAL = '#ff8a80'

CSS = a.CSS + f"""
.mn{{top:150px;bottom:120px;gap:24px}}
.ring{{width:210px;height:210px;border-radius:50%;background:radial-gradient(circle,rgba(127,214,232,.22),rgba(127,214,232,0) 70%);display:flex;align-items:center;justify-content:center}}
.ring svg{{width:180px;height:180px}}
.t{{font-size:84px}}
.b1{{font-size:38px}} .b2{{font-size:30px}}
.box{{padding:28px 36px}}
.vis{{align-self:stretch}}
.pl{{display:inline-block;background:rgba(255,255,255,.08);border:2px solid rgba(255,255,255,.22);border-radius:30px;padding:9px 18px;font-size:24px;font-weight:700;margin:5px}}
.tip{{align-self:stretch;display:flex;align-items:center;gap:16px;text-align:left;background:rgba(246,195,67,.12);border-left:8px solid {GOLD};border-radius:10px;padding:18px 24px;font-size:28px;font-weight:700}}
.tip b{{color:{GOLD}}}
.stp{{flex:1;background:rgba(8,28,64,.45);border:2px solid rgba(255,255,255,.2);border-radius:22px;padding:18px 12px}}
.stp .n{{width:52px;height:52px;border-radius:50%;background:{GOLD};color:#14232d;font-weight:800;font-size:28px;display:flex;align-items:center;justify-content:center;margin:0 auto 10px}}
.stp .l{{font-size:26px;font-weight:800;line-height:1.2}}
"""
import base64 as _b
HDR = 'data:image/png;base64,' + _b.b64encode((g.HERE/'hdr_logo.png').read_bytes()).decode()
LOGO = g.LOGO.replace('width="52" height="48"', 'width="60" height="56"')

def page(n, total, body):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="pg"><div class="gr"></div>
<div class="hd"><img src="{HDR}" style="width:952px;height:auto;display:block"></div>
<div class="mn">{body}</div>
<div class="ft"><span>@globalmathprep · globalmathprep.academy</span><span>{n}/{total}</span></div></div></body></html>'''

def sl(ic_, lab, title, b1, b2, vis, tip):
    return f'<div class="ring">{a.icon(ic_)}</div><div class="lab">{lab}</div><h1 class="t">{title}</h1><div class="box"><div class="b1">{b1}</div><div class="b2">{b2}</div></div><div class="vis">{vis}</div><div class="tip"><div>{tip}</div></div>'

def steps(items):
    return '<div style="display:flex;gap:14px">' + ''.join(f'<div class="stp"><div class="n">{i}</div><div class="l">{t}</div></div>' for i, t in enumerate(items, 1)) + '</div>'

rules = ['Boundaries', 'Commas', 'Colons', 'Dashes', 'Agreement', 'Tense', 'Pronouns', 'Apostrophes', 'Modifiers', 'Parallelism', 'Clauses', 'Word pairs']
bar = f'''<div style="display:flex;height:64px;border-radius:32px;overflow:hidden;border:2px solid rgba(255,255,255,.3)">
<div style="width:26%;background:{GOLD};color:#14232d;font-weight:800;font-size:24px;display:flex;align-items:center;justify-content:center">26%</div>
<div style="width:20%;background:{TEAL};color:#14232d;font-weight:800;font-size:24px;display:flex;align-items:center;justify-content:center">20%</div>
<div style="width:54%;background:rgba(255,255,255,.12);font-weight:700;font-size:23px;display:flex;align-items:center;justify-content:center">Reading · 54%</div></div>
<div style="display:flex;gap:26px;justify-content:center;margin-top:12px;font-size:22px;font-weight:700;color:#cfe0f3"><span><span style="color:{GOLD}">■</span> Grammar</span><span><span style="color:{TEAL}">■</span> Expression of Ideas</span></div>'''
ex = f'''<div style="display:flex;gap:14px;align-items:stretch">
<div style="flex:1.5;background:{CREAM};color:#14232d;border-radius:20px;padding:18px 22px;font-family:S,serif;font-size:30px;text-align:left;line-height:1.35">The list of rules <u>&nbsp;&nbsp;?&nbsp;&nbsp;</u> short.</div>
<div style="flex:1;display:flex;flex-direction:column;gap:8px;font-size:26px;font-weight:800">
<div style="background:rgba(255,138,128,.2);border:2px solid {CORAL};border-radius:14px;padding:8px">A) are ✗</div>
<div style="background:rgba(95,214,168,.2);border:2px solid {MINT};border-radius:14px;padding:8px">B) is ✓</div></div></div>'''
mod = f'''<div style="display:flex;align-items:center;gap:14px;font-size:26px;font-weight:800">
<div class="stp" style="flex:1"><div class="l">Module 1<br><span style="color:{GOLD}">strong</span></div></div><div style="font-size:40px;color:{TEAL}">→</div>
<div class="stp" style="flex:1.3;border-color:{MINT}"><div class="l" style="color:{MINT}">Harder Module 2</div><div style="font-size:22px;font-weight:600;color:#cfe0f3;margin-top:4px">top scores in reach</div></div></div>'''
tm = f'''<div style="display:flex;gap:14px">
<div class="stp"><div style="font-size:52px;font-weight:800;color:{GOLD}">~71s</div><div class="l" style="font-size:22px;font-weight:600;color:#cfe0f3">average time<br>per question</div></div>
<div class="stp"><div style="font-size:52px;font-weight:800;color:{MINT}">fast</div><div class="l" style="font-size:22px;font-weight:600;color:#cfe0f3">grammar you know<br>= quick answer</div></div>
<div class="stp"><div style="font-size:52px;font-weight:800;color:{TEAL}">+time</div><div class="l" style="font-size:22px;font-weight:600;color:#cfe0f3">saved for hard<br>reading questions</div></div></div>'''

S = [
 sl('book', 'SAT READING &amp; WRITING', 'Start with grammar.<br><em>Here’s why.</em>', '5 reasons, 1 simple plan.', 'Swipe through and save it for later.',
    steps(['Finite', 'Rule-based', '~46%', 'Fast', 'Module 1']), '<b>Save</b> this post so you can come back to the plan.'),
 sl('target', 'REASON 1', 'Grammar has an <em>ending</em>.', 'About a dozen rules cover the whole grammar section.', 'Learn them once. They work on every test.',
    ''.join(f'<span class="pl">{r}</span>' for r in rules), '<b>Reading</b> never ends. <b>Grammar</b> does.'),
 sl('scale', 'REASON 2', 'One right answer. <em>Every time.</em>', 'Each question is decided by a rule, not a feeling.', 'Wrong choices break a rule you can name.',
    ex, 'Singular subject “list” → singular verb “<b>is</b>”.'),
 sl('pie', 'REASON 3', 'Almost <em>half</em> the section.', 'Grammar 26% + Expression of Ideas 20%', 'About 46% of Reading &amp; Writing runs on rules and patterns.',
    bar, 'Percentages are the published domain weightings (approx.).'),
 sl('bolt', 'REASON 4', 'Fast points, <em>more time</em>.', 'A grammar question you know takes seconds.', 'Bank that time for the tougher reading questions.',
    tm, '64 min × 60 ÷ 54 questions ≈ <b>71 seconds</b> each.'),
 sl('stairs', 'REASON 5', 'Module 1 <em>opens the door</em>.', 'A strong Module 1 unlocks the harder Module 2.', 'That’s where the highest scores are possible.',
    mod, 'Grammar = <b>reliable points</b> right where they count.'),
 sl('map', 'YOUR GAME PLAN', 'The order <em>that works</em>.', 'Grammar first. Reading every day.', 'Build the sure points, then stretch.',
    steps(['Grammar', 'Transitions &amp; Notes', 'Reading']), 'Common mistake: <b>only</b> doing more reading practice.'),
]
S.append(a.S[7])

if __name__ == '__main__':
    out = g.HERE / 'out11'; out.mkdir(exist_ok=True)
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page(viewport={'width': 1080, 'height': 1350})
        for i, body in enumerate(S, 1):
            pg.set_content(page(i, len(S), body)); pg.wait_for_timeout(250)
            ov = pg.evaluate("()=>{const m=document.querySelector('.mn');let t=1e9,b=0;for(const c of m.children){const x=c.getBoundingClientRect();t=Math.min(t,x.top);b=Math.max(b,x.bottom)}return [Math.round(t),Math.round(b)]}")
            fn = out / f'SAT-Advice-plus-{i}-of-8.png'
            pg.screenshot(path=str(fn)); print(fn.name, ov, 'OK' if ov[0] >= 140 and ov[1] <= 1235 else 'OVERFLOW')
        br.close()
