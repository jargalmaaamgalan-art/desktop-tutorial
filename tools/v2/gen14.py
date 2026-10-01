import base64, pathlib
import gen4 as g
from playwright.sync_api import sync_playwright

HERE = g.HERE
HDR = 'data:image/png;base64,' + base64.b64encode((HERE / 'hdr_logo_dark.png').read_bytes()).decode()
QR = 'data:image/svg+xml;base64,' + base64.b64encode((HERE / 'qr_join.svg').read_bytes()).decode()
INK = '#0f172a'

def css(acc, tint, soft):
    return g.ff + f"""
*{{box-sizing:border-box}}
body{{margin:0;width:1080px;height:1350px;font-family:M,sans-serif;color:{INK};overflow:hidden}}
.pg{{width:1080px;height:1350px;position:relative;overflow:hidden;background:{tint};
background-image:linear-gradient(rgba(15,23,42,.045) 1px,transparent 1px),linear-gradient(90deg,rgba(15,23,42,.045) 1px,transparent 1px);background-size:54px 54px}}
.hd{{position:absolute;top:40px;left:48px;right:48px}} .hd img{{width:984px;display:block}}
.mn{{position:absolute;top:140px;left:44px;right:44px;bottom:100px;display:flex;flex-direction:column;justify-content:center;gap:22px}}
.tt{{text-align:center;display:flex;flex-direction:column;align-items:center;gap:14px}}
.t{{margin:0;font-weight:800;font-size:96px;line-height:.98;letter-spacing:-2.5px}}
.t em{{font-style:normal;color:{acc}}}
.pp{{border:3px solid {INK};border-radius:40px;padding:8px 30px;font-weight:800;font-size:32px;background:#fff}}
.g2{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px}}
.g3{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}}
.cd{{background:#fff;border:2.5px solid {INK};border-radius:18px;padding:16px 20px 18px}}
.cd.dk{{background:{acc};border-color:{acc};color:#fff}}
.ch{{display:flex;justify-content:space-between;align-items:center;margin-bottom:10px}}
.pl{{background:{acc};color:#fff;border-radius:30px;padding:7px 18px;font-weight:700;font-size:25px}}
.dk .pl{{background:#fff;color:{acc}}}
.cb{{font-size:28px;line-height:1.3;font-weight:500}}
.h{{color:{acc};font-weight:800}} .dk .h{{color:#fff;text-decoration:underline}}
.sv{{font-family:S,serif;font-size:26px;line-height:1.35;background:{soft};border-radius:10px;padding:8px 12px;margin-top:8px;color:{INK}}}
.dk .sv{{background:rgba(255,255,255,.18);color:#fff}}
.mk{{background:{acc};color:#fff;border-radius:6px;padding:0 6px;font-weight:700}}
.bl{{display:inline-block;width:110px;border-bottom:3px solid {INK};transform:translateY(-6px)}}
.big{{font-family:S,serif;font-size:36px;line-height:1.42;background:#fff;border:2.5px solid {INK};border-radius:20px;padding:24px 30px}}
.ft{{position:absolute;left:48px;right:48px;bottom:42px;display:flex;justify-content:space-between;align-items:center;font-size:22px;font-weight:600;color:#475569}}
.ft b{{color:{acc}}}
.dots{{display:flex;gap:8px}} .dots i{{width:12px;height:12px;border-radius:50%;background:#cbd5e1}} .dots i.on{{background:{acc};width:34px;border-radius:7px}}
.sw{{display:inline-flex;align-items:center;gap:18px;border:3px solid {INK};border-radius:50px;padding:12px 16px 12px 34px;font-size:30px;font-weight:700;background:#fff}}
.sw span{{width:52px;height:52px;border-radius:50%;background:{acc};display:flex;align-items:center;justify-content:center}}
.lab{{display:inline-block;background:{INK};color:#fff;border-radius:30px;padding:8px 24px;font-weight:800;font-size:24px;letter-spacing:3px}}
b{{font-weight:800}}
"""

ARROW = f'<svg width="30" height="22" viewBox="0 0 30 22" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M2 11h25M18 3l9 8-9 8"/></svg>'
ARW = '<svg width="28" height="22" viewBox="0 0 30 22" fill="none" stroke="#fff" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"><path d="M2 11h25M18 3l9 8-9 8"/></svg>'

def card(pill, body, dark=False, span=False, arrow=True):
    a = ARROW.replace(INK, '#fff') if dark else ARROW
    return f'<div class="cd{" dk" if dark else ""}" style="{"grid-column:1 / -1;" if span else ""}"><div class="ch"><span class="pl">{pill}</span>{a if arrow else ""}</div><div class="cb">{body}</div></div>'
def head(a, b, pill=None, size=100):
    return f'<div class="tt"><h1 class="t" style="font-size:{size}px">{a}<br><em>{b}</em></h1>{f"<div class=pp>{pill}</div>" if pill else ""}</div>'

def page(n, total, body, c):
    dots = ''.join(f'<i class="{"on" if k == n else ""}"></i>' for k in range(1, total + 1))
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><style>{c}</style></head><body><div class="pg">
<div class="hd"><img src="{HDR}"></div><div class="mn">{body}</div>
<div class="ft"><span>@globalmathprep · globalmathprep.academy</span><div class="dots">{dots}</div><span><b>{n:02d}</b> / {total:02d}</span></div></div></body></html>'''

def cover(label, icon, a, b, sub, acc):
    return f'''<div class="tt" style="gap:26px"><span class="lab">{label}</span>{icon}
<h1 class="t" style="font-size:132px;line-height:.92;letter-spacing:-4px">{a}<br><em>{b}</em></h1>
<div style="font-size:44px;font-weight:700;line-height:1.2;max-width:880px">{sub}</div>
<div style="width:120px;height:5px;background:{acc};border-radius:4px"></div>
<div style="font-size:26px;font-weight:600;color:#475569;letter-spacing:1px">by <b style="color:{INK}">Jargalmaa Amgalan</b> · Global Math Prep</div>
<div class="sw">Swipe to start<span>{ARW}</span></div></div>'''

def back(chapter, recap, nxt, acc, soft):
    rec = ''.join(f'<div style="display:flex;gap:14px;align-items:flex-start"><span style="flex:none;width:34px;height:34px;border-radius:50%;background:{acc};color:#fff;font-weight:800;font-size:20px;display:flex;align-items:center;justify-content:center;margin-top:2px">{i}</span><span>{t}</span></div>' for i, t in enumerate(recap, 1))
    days = ''.join(f'<div style="flex:1;background:{soft};border:2.5px solid {INK};border-radius:14px;padding:10px 0;text-align:center;font-weight:800;font-size:32px">{d}</div>' for d in ('Tue', 'Thu', 'Sat'))
    return f'''<div class="tt" style="gap:12px"><span class="lab">THE END · {chapter}</span>
<h1 class="t" style="font-size:84px">That’s a wrap.<br><em>Ready for more?</em></h1></div>
<div class="cd" style="padding:20px 26px"><div class="ch"><span class="pl">Quick recap</span></div><div class="cb" style="display:flex;flex-direction:column;gap:10px;font-size:26px">{rec}</div></div>
<div style="display:flex;gap:16px">
<div class="cd" style="flex:1.55;display:flex;flex-direction:column;gap:12px;padding:20px 24px"><div class="ch" style="margin:0"><span class="pl">SAT English · enrollment open</span></div>
<div style="display:flex;gap:10px">{days}</div>
<div style="font-size:70px;font-weight:800;line-height:1;letter-spacing:-1px">18:30–19:50</div>
<div style="font-size:24px;font-weight:600;color:#475569">Mongolia time · live on Zoom · groups of 2–5 · <b style="color:{acc}">6 seats left</b></div></div>
<div class="cd" style="flex:1;padding:12px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px"><img src="{QR}" style="width:100%;display:block"><div style="font-size:26px;font-weight:800">Scan to register</div></div></div>
<div style="background:{INK};color:#fff;border-radius:20px;padding:16px 26px;display:flex;justify-content:space-between;align-items:center"><div style="font-size:24px;font-weight:600">WhatsApp “SAT English”<br><b style="font-size:38px">+1 428 880 1826</b></div><div style="text-align:right;font-size:22px;font-weight:600;color:#cbd5e1">Save it · Share it<br><b style="color:#fff">Next: {nxt}</b></div></div>'''


def cover2(label, icon, num, word, line2, hook, chips, acc):
    ch = ''.join(f'<span style="border:2.5px solid {INK};border-radius:30px;padding:8px 20px;font-size:25px;font-weight:700;background:#fff">{c}</span>' for c in chips)
    return f'''<div class="tt" style="gap:24px"><span class="lab">{label}</span>{icon}
<h1 class="t" style="font-size:{150 if len(word)<11 else 118}px;line-height:.9;letter-spacing:-5px;white-space:nowrap"><em>{num}</em> {word}</h1>
<div style="font-size:62px;font-weight:800;line-height:1.05;letter-spacing:-1.5px;max-width:960px">{line2}</div>
<div style="font-size:32px;font-weight:600;color:#334155;max-width:900px;line-height:1.3">{hook}</div>
<div style="display:flex;gap:10px;flex-wrap:wrap;justify-content:center">{ch}</div>
<div style="font-size:24px;font-weight:600;color:#475569">by <b style="color:{INK}">Jargalmaa Amgalan</b> · Global Math Prep</div>
<div class="sw">Swipe to find out<span>{ARW}</span></div></div>'''

# ---------- line-art icons ----------
def ic_link(acc):
    return f'''<svg width="360" height="235" viewBox="0 0 260 170" fill="none" stroke="{INK}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"><rect x="6" y="20" width="96" height="70" rx="16" fill="#fff"/><path d="M30 44h48M30 64h32"/><rect x="158" y="80" width="96" height="70" rx="16" fill="#fff"/><path d="M182 104h48M182 124h32"/><path d="M102 56 C140 56 120 115 158 115" stroke="{acc}" stroke-width="8"/><circle cx="130" cy="86" r="18" fill="{acc}" stroke="{INK}"/></svg>'''
def ic_book(acc):
    return f'''<svg width="360" height="235" viewBox="0 0 260 170" fill="none" stroke="{INK}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"><path d="M130 40 C100 18 50 16 14 26 V150 C50 140 100 142 130 164 C160 142 210 140 246 150 V26 C210 16 160 18 130 40 Z" fill="#fff"/><path d="M130 40 V164"/><path d="M42 58h60M42 82h60M42 106h44" stroke="{acc}"/><path d="M158 58h60M158 82h60M158 106h44"/></svg>'''
def ic_notes(acc):
    return f'''<svg width="360" height="235" viewBox="0 0 260 170" fill="none" stroke="{INK}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"><rect x="20" y="18" width="120" height="148" rx="14" fill="#fff"/><rect x="52" y="6" width="56" height="24" rx="8" fill="{acc}"/><path d="M44 62h70M44 90h70M44 118h50"/><circle cx="196" cy="96" r="54" fill="#fff"/><circle cx="196" cy="96" r="32"/><circle cx="196" cy="96" r="11" fill="{acc}"/></svg>'''

SETS = {}

# ================= SET A: TRANSITIONS (blue) =================
A = dict(acc='#1d4ed8', tint='#eef4ff', soft='#e0ebff', name='SAT-Transitions-book')
acc = A['acc']
SA = []
SA.append(cover2('SAT ENGLISH · CHAPTER 1', ic_link(acc), '5', 'Tiny Words', 'Worth <span style="color:%s">Big SAT Points</span>' % acc, 'However? Therefore? In fact? Pick the wrong one and the point is gone.', ['5 link types', '4-step method', '6 traps'], acc))
SA.append(head('5 Ways Ideas', 'Link Up', size=86) + '<div class="g2" style="gap:14px">' +
  card('Type 1 · Continue', '“and there’s more” · <span class="h">moreover, in addition, likewise</span><div class="sv">The museum extended its hours. <span class="mk">Moreover</span>, entry became free on Sundays.</div>') +
  card('Type 2 · Contrast', '“plot twist” · <span class="h">however, nevertheless, yet</span><div class="sv">The plan was bold. <span class="mk">However</span>, it lacked funding.</div>') +
  card('Type 3 · Cause & effect', '“so this happened” · <span class="h">therefore, consequently, thus</span><div class="sv">The river flooded. <span class="mk">Consequently</span>, the road closed.</div>') +
  card('Type 4 · Example', '“receipts, please” · <span class="h">for example, for instance</span><div class="sv">Some fruits are rich in vitamin C. <span class="mk">For example</span>, oranges.</div>') +
  card('Type 5 · Emphasis', '“no, seriously” · <span class="h">in fact, indeed</span><div class="sv">The test was long. <span class="mk">In fact</span>, it lasted four hours.</div>') +
  card('Pro tip', 'Name the type <b>before</b> you look. Then pick the only word from that family.', dark=True) + '</div>')
SA.append(head('Predict First,', 'Then Match', 'The 4-step method') + '<div class="g2">' +
  card('Step 1 · Cover', 'Hide the answer choices. Fancy words can <span class="h">catfish</span> you.') +
  card('Step 2 · Paraphrase', 'Say both ideas in your own words: <span class="h">“costs a lot… but pays off.”</span>') +
  card('Step 3 · Predict', 'Pick your own linking word first. <span class="h">But? So? And?</span>') +
  card('Step 4 · Match', 'Find the only choice from that <span class="h">same family</span>.') +
  card('Try it', '<div class="sv" style="font-size:27px">Solar panels are expensive to install. <span class="bl"></span>, they pay for themselves within a decade.</div><div style="display:flex;gap:10px;margin-top:12px;flex-wrap:wrap;font-weight:700"><span style="opacity:.45">A) Therefore</span>·<span class="mk" style="padding:2px 10px">B) However ✓</span>·<span style="opacity:.45">C) For example</span>·<span style="opacity:.45">D) Similarly</span></div><div style="margin-top:8px">“But” = contrast → <b>However</b>.</div>', span=True) + '</div>')
SA.append(head('4 Questions,', 'Fully Solved', 'Worked examples') + '<div class="g2">' +
  card('Q1 · Example', '<div class="sv" style="margin-top:0">Some birds travel huge distances. <span class="bl"></span>, the Arctic tern flies from pole to pole.</div><div style="margin-top:8px"><span class="h">For instance</span>: one bird illustrates the claim.</div>') +
  card('Q2 · Cause & effect', '<div class="sv" style="margin-top:0">Octopuses have no bones. <span class="bl"></span>, they can squeeze through tiny gaps.</div><div style="margin-top:8px"><span class="h">Consequently</span>: no bones → squeezing is the result.</div>') +
  card('Q3 · Emphasis', '<div class="sv" style="margin-top:0">The exam was hard. <span class="bl"></span>, no one finished it.</div><div style="margin-top:8px"><span class="h">In fact</span>: same idea, pushed further.</div>') +
  card('Q4 · Twins trap', '<div class="sv" style="margin-top:0">The factory switched to solar power. <span class="bl"></span>, its energy bills fell sharply.</div><div style="margin-top:8px"><span class="h">As a result</span>. However &amp; Nevertheless are twins, so both go.</div>') + '</div>')
SA.append(head('Don’t Get', 'Played', '6 classic traps') + '<div class="g2">' +
  card('Trap 1 · Twins', 'Two choices do the <span class="h">same job</span>? Neither can be right. Cross out both.') +
  card('Trap 2 · Position', 'Start, middle or end, a transition always links to the <span class="h">sentence before</span>. <i>Readers, however, loved it.</i>') +
  card('Trap 3 · Fancy ≠ right', '“Nevertheless” sounds smart. Doesn’t matter. Only the <span class="h">logic</span> counts.') +
  card('Trap 4 · Half-reading', 'Read <span class="h">both</span> sentences in full. The link lives in the second one.') +
  card('Trap 5 · Example vs reason', 'An example shows <span class="h">one case</span>. A reason explains <span class="h">why</span>. Don’t mix them up.') +
  card('The rule', 'Only one choice fits the family? It <b>wins by default</b>, even if it sounds boring.', dark=True) + '</div>')
SA.append(head('Your Turn.', 'Can You Crack It?') +
  '<div class="big">The city added more bus routes. <span class="bl" style="width:170px"></span>, it lowered fares for students.</div><div class="g2">' +
  ''.join(f'<div class="cd" style="font-size:34px;font-weight:800;padding:18px 24px">{t}</div>' for t in ('A) However', 'B) Moreover', 'C) Consequently', 'D) For example')) + '</div>' +
  card('Hint', 'Is idea 2 a <span class="h">plot twist</span>, a <span class="h">result</span>, or just <span class="h">more good news</span>?') +
  f'<div style="text-align:center;font-size:32px;font-weight:800">Drop <span style="color:{acc}">A, B, C or D</span> in the comments. Answer tomorrow!</div>')
SA.append(back('CHAPTER 1', ['Transitions show how idea B links to idea A.', 'Predict your own word first, then match its family.', 'Twins cancel out. The only fit wins.'], 'Chapter 2 · Student Notes', acc, A['soft']))
SETS['A'] = (A, SA)

# ================= SET B: START WITH GRAMMAR (green) =================
B = dict(acc='#15803d', tint='#effaf2', soft='#dcf5e4', name='SAT-Grammar-First-book')
acc = B['acc']
SB = []
SB.append(cover2('SAT READING &amp; WRITING', ic_book(acc), '12', 'Rules', 'That Unlock <span style="color:%s">Half</span><br>of SAT English' % acc, 'Most students start with reading. Top scorers start here. The cheat code nobody tells you.', ['no cap', 'learn once', 'score forever'], acc))
SB.append(head('Why Grammar', 'Comes First', '5 reasons, no cap') + '<div class="g2">' +
  card('Reason 1 · It ends', 'About <span class="h">12 rules</span> cover the whole grammar part. Learn once, use forever.') +
  card('Reason 2 · One answer', 'Every question is decided by a <span class="h">rule</span>, not a vibe.') +
  card('Reason 3 · Big share', 'Grammar ≈26% + Expression of Ideas ≈20% = <span class="h">almost half</span> the section.') +
  card('Reason 4 · Speed', 'A rule you know = answer in <span class="h">seconds</span>. More time for reading.') +
  card('Reason 5 · Module 1', 'A strong Module 1 unlocks the <span class="h">harder Module 2</span>, where top scores live.') +
  card('Real talk', 'Reading still matters. Just start with the part you can <b>master fastest</b>.', dark=True) + '</div>')
colr = lambda t, c, rows, ok: f'<div class="cd" style="padding:18px 22px"><div class="ch"><span class="pl" style="background:{c}">{t}</span></div>' + ''.join(f'<div style="display:flex;gap:12px;align-items:flex-start;padding:10px 0;border-top:2px dashed #cbd5e1;font-size:29px;font-weight:600;line-height:1.3"><b style="color:{c};font-size:26px">{"✓" if ok else "✗"}</b><span>{r}</span></div>' for r in rows) + '</div>'
SB.append(head('Vibes vs', 'Rules', 'Reading vs grammar') + '<div class="g2">' +
  colr('Reading', '#dc2626', ['Guessing from clues', 'Two answers can look right', 'Slow, bumpy progress', 'Endless possible texts'], False) +
  colr('Grammar', acc, ['One answer, set by a rule', 'Wrong answers break a rule', 'Fast progress that sticks', 'A list you can finish'], True) + '</div>' +
  card('The takeaway', 'Build the <b>sure points</b> first, then stretch into reading.', dark=True, arrow=False))
D = [('Craft &amp; Structure', 28, '#64748b'), ('Information &amp; Ideas', 26, '#94a3b8'), ('Grammar (Conventions)', 26, acc), ('Expression of Ideas', 20, '#22c55e')]
bars = ''.join(f'<div style="margin-top:12px"><div style="display:flex;justify-content:space-between;font-size:25px;font-weight:700;margin-bottom:6px"><span>{n}</span><span>~{p}%</span></div><div style="height:30px;border-radius:16px;background:#e2e8f0;border:2px solid {INK};overflow:hidden"><div style="height:100%;width:{p/28*100:.0f}%;background:{c};border-right:2px solid {INK}"></div></div></div>' for n, p, c in D)
st = lambda n, l: f'<div class="cd" style="text-align:center;padding:16px 8px"><div style="font-size:62px;font-weight:800;color:{acc};line-height:1">{n}</div><div style="font-size:23px;font-weight:700;margin-top:6px">{l}</div></div>'
SB.append(head('The Receipts:', '46%', 'Real numbers') + card('Share of Reading &amp; Writing', bars, arrow=False) +
  f'<div class="g3">{st("54","questions")}{st("64","minutes")}{st("~71s","per question")}</div>' +
  '<div style="text-align:center;font-size:21px;color:#475569;font-weight:600">Approximate published weightings · 26 + 20 = 46 · 64 × 60 ÷ 54 ≈ 71 s</div>')
R = [('Sentence boundaries', 'no comma splices'), ('Joining clauses', '; : and FANBOYS'), ('Extra-info commas', 'always in pairs'), ('Comma rules', 'lists and intros'), ('Colons &amp; dashes', 'explain or stress'), ('Subject–verb', '“the list … is”'), ('Verb tense', 'stay consistent'), ('Pronouns', 'it vs they'), ('Apostrophes', 'its vs it’s'), ('Modifiers', 'who is doing it?'), ('Parallelism', 'same form in lists'), ('Word pairs', 'neither … nor')]
cells = ''.join(f'<div class="cd" style="padding:14px 16px"><span class="pl" style="font-size:20px;padding:4px 12px">{i}</span><div style="font-size:24px;font-weight:800;line-height:1.15;margin-top:10px">{a}</div><div style="font-size:21px;color:#475569;font-weight:600;margin-top:4px">{b}</div></div>' for i, (a, b) in enumerate(R, 1))
SB.append(head('~12 Rules.', 'That’s The List.', 'Boss level, unlocked') + f'<div class="g3">{cells}</div>' +
  f'<div style="text-align:center;font-size:30px;font-weight:800">Spot the rule → <span style="color:{acc}">answer in seconds.</span></div>')
SB.append(head('Your Glow-Up', 'Plan', 'The order that works') +
  card('Step 1 · Grammar first', 'Aim to lose <span class="h">zero points</span> on the rules. Understood the assignment.') +
  card('Step 2 · Expression of Ideas', 'Transitions and Student Notes. <span class="h">Pattern-based</span>, so they level up fast too.') +
  card('Step 3 · Reading, daily', 'Small reps <span class="h">every day</span> while grammar carries your score.') +
  card('Don’t be that student', 'The one who only grinds reading practice. Relatable, but <b>not the move</b>.', dark=True))
SB.append(back('STRATEGY', ['Grammar has an ending: about 12 rules.', 'Almost half the section runs on rules and patterns.', 'Grammar first, then reading every day.'], 'Chapter 1 · Transitions', acc, B['soft']))
SETS['B'] = (B, SB)

# ================= SET C: STUDENT NOTES (purple) =================
C = dict(acc='#7c3aed', tint='#f5f1ff', soft='#ede5ff', name='SAT-Student-Notes-book')
acc = C['acc']
SC = []
SC.append(cover2('SAT ENGLISH · CHAPTER 2', ic_notes(acc), '4', 'True Answers.', 'Only <span style="color:%s">1</span> Is Right.' % acc, 'The Student Notes question tricks almost everyone. Here’s the move that cracks it.', ['4 steps', 'goal words', '4 traps'], acc))
notes = ['Rachel Carson was a marine biologist.', 'In 1962, she published <i>Silent Spring</i>.', 'The book documented harm caused by the pesticide DDT.', 'It helped inspire the modern environmental movement.']
SC.append(head('What Even Is', 'This Question?', 'How it looks on the SAT') +
  card('Student notes', ''.join(f'<div style="font-family:S,serif;font-size:29px;line-height:1.35;padding:3px 0">• {t}</div>' for t in notes), arrow=False) +
  card('The goal', 'The student wants to <span class="h">emphasize the book’s impact</span>. Which choice does that?', arrow=False) +
  card('The twist', 'All four choices are <b>true</b>. Only one does the <b>goal</b>. That’s the whole game.', dark=True, arrow=False))
SC.append(head('Goal First,', 'Notes Later', 'The 4-step method') + '<div class="g2">' +
  card('Step 1 · Read the goal', 'Start with <span class="h">“The student wants to…”</span>, not the notes.') +
  card('Step 2 · Underline', 'Mark the <span class="h">purpose verb</span> and the <span class="h">topic</span>.') +
  card('Step 3 · Predict', 'What <span class="h">must</span> the right sentence mention?') +
  card('Step 4 · Eliminate', 'Cross out choices that are true but <span class="h">off-goal</span>.') +
  card('Try it · goal: emphasize the impact', '<div style="display:flex;flex-direction:column;gap:8px;font-family:S,serif;font-size:27px"><span style="opacity:.45">A) Carson, a marine biologist, published <i>Silent Spring</i> in 1962.</span><span style="opacity:.45">B) <i>Silent Spring</i> documented harm caused by DDT.</span><span><span class="mk">C)</span> <i>Silent Spring</i> helped inspire the modern environmental movement. ✓</span></div>', span=True) + '</div>')
SC.append(head('Goal Words', 'Are Clues', 'Decode the goal') + '<div class="g2">' +
  card('Contrast', 'Look for <span class="h">whereas, although, but</span> plus <b>both</b> items.') +
  card('Similarity', 'Look for <span class="h">both, similarly, like</span>.') +
  card('New audience', 'Pick the choice that explains <span class="h">who or what</span> it is (background).') +
  card('Two-part goal', '“Method <b>and</b> result”? The answer needs <span class="h">both parts</span>.') +
  card('Specific detail', 'Goal names a number or fact? The answer must <span class="h">include it</span>.') +
  card('Pro tip', 'You rarely need every note. <b>Goal + choices</b> are usually enough.', dark=True) + '</div>')
cell = lambda ok: f'<b style="color:{acc if ok else "#dc2626"};font-size:30px">{"✓" if ok else "✗"}</b>'
tbl = '<div style="display:grid;grid-template-columns:1.6fr 1fr 1fr;gap:6px 0;align-items:center;font-size:28px;font-weight:700;text-align:center"><span></span><span style="color:#dc2626">Wrong</span><span style="color:' + acc + '">Right</span>' + ''.join(f'<span style="text-align:left">{q}</span>{cell(a)}{cell(b)}' for q, a, b in (('True?', 1, 1), ('From the notes?', 1, 1), ('Does the goal?', 0, 1))) + '</div>'
SC.append(head('Don’t Get', 'Played', '4 classic traps') + '<div class="g2">' +
  card('Trap 1 · True but useless', tbl) +
  card('Trap 2 · Near-miss', 'Goal: method <b>and</b> result. <i>“The team found wolves travel far.”</i> = result only, <span class="h">1 of 2</span>. Miss.') +
  card('Trap 3 · Wrong relationship', 'Goal says contrast, choice shows a <span class="h">similarity</span>. Out.') +
  card('Trap 4 · Extra facts', 'More details ≠ better. Anything <span class="h">off-goal</span> is noise.') + '</div>' +
  card('The rule', 'Don’t ask “Is it true?” Ask <b>“Does it do the goal?”</b>', dark=True, arrow=False))
en = ['Mount Everest is 8,849 meters tall.', 'It lies on the border of Nepal and China.', 'K2 is 8,611 meters tall.', 'It lies on the border of Pakistan and China.']
SC.append(head('Your Turn.', 'Can You Crack It?', size=84) +
  card('Notes', ''.join(f'<div style="font-family:S,serif;font-size:27px;line-height:1.32">• {t}</div>' for t in en), arrow=False) +
  card('Goal', 'The student wants to <span class="h">contrast the heights</span> of the two mountains.', arrow=False) +
  '<div style="display:flex;flex-direction:column;gap:10px">' + ''.join(f'<div class="cd" style="padding:13px 20px;font-family:S,serif;font-size:27px">{t}</div>' for t in ('A) Mount Everest lies on the border of Nepal and China.', 'B) Both Mount Everest and K2 lie on China’s border.', 'C) Whereas Mount Everest is 8,849 meters tall, K2 is 8,611 meters tall.', 'D) K2, which is 8,611 meters tall, lies on the border of Pakistan and China.')) + '</div>' +
  f'<div style="text-align:center;font-size:30px;font-weight:800">Comment <span style="color:{acc}">A, B, C or D</span>. Answer tomorrow!</div>')
SC.append(back('CHAPTER 2', ['Every choice is true. Only one does the goal.', 'Read the goal first and underline its key words.', 'Count the parts of the goal; check each one.'], 'Chapter 3 · coming soon', acc, C['soft']))
SETS['C'] = (C, SC)

if __name__ == '__main__':
    out = HERE / 'out14'; out.mkdir(exist_ok=True)
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page(viewport={'width': 1080, 'height': 1350})
        for k, (M, S) in SETS.items():
            c = css(M['acc'], M['tint'], M['soft'])
            for i, body in enumerate(S, 1):
                pg.set_content(page(i, len(S), body, c)); pg.wait_for_timeout(250)
                ov = pg.evaluate("()=>{const m=document.querySelector('.mn');let t=1e9,b=0;for(const c of m.children){const x=c.getBoundingClientRect();t=Math.min(t,x.top);b=Math.max(b,x.bottom)}return [Math.round(t),Math.round(b)]}")
                fn = out / f"{M['name']}-{i:02d}-of-{len(S):02d}.png"
                pg.screenshot(path=str(fn)); print(fn.name, ov, 'OK' if ov[0] >= 140 and ov[1] <= 1245 else 'OVERFLOW')
        br.close()
