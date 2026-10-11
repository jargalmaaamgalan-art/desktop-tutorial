"""Four SAT R&W explainer carousels from the owner's own explainer pages (Chiquihuite, John Redding v3, Neanderthal, State Taxes).
Model: gen36.py. Run: python3 gen37.py [--video] [key ...]"""
import sys
import gen30, gen29
from gen30 import frame
from gen18 import E, HERE

CUR = dict(AC='#000', SOFT='#eee', foot='')
PR_WIC = 'Which choice completes the text with the most logical and precise word or phrase?'

def extra(AC, SOFT):
    return """
.hk{background:#fde68a;color:#1e1e1e;padding:0 6px;border-radius:8px;font-weight:700}
.ul{text-decoration:underline;text-decoration-thickness:3px;text-underline-offset:5px}
.cl{display:flex;gap:16px;align-items:center;padding:12px 0;border-top:2px dashed @SOFT@}
.cl:first-child{border-top:0}
.cl .no{flex:none;width:50px;height:50px;border-radius:50%;background:@AC@;color:#fff;font-size:28px;font-weight:900;display:flex;align-items:center;justify-content:center}
.cl .ph{flex:none;width:330px;font-family:S,serif;font-size:28px;font-weight:700;background:#fde68a;border-radius:10px;padding:4px 10px;line-height:1.3}
.cl .ms{font-size:27px;font-weight:700;color:#334;line-height:1.3}
.vc{background:#fff;border-radius:22px;padding:14px 24px 16px;border:2.5px solid @SOFT@}
.vc.tp{border:3px solid #c62828}
.vc .top2{display:flex;align-items:baseline;gap:14px;flex-wrap:wrap}
.vc .wd{font-family:S,serif;font-size:38px;font-weight:700;color:#c62828}
.vc .pr{font-size:27px;font-weight:700;color:#667}
.vc .tg{font-size:20px;font-weight:800;letter-spacing:1px;background:#c62828;color:#fff;border-radius:20px;padding:3px 14px}
.vc .why{font-size:30px;font-weight:600;color:#223;line-height:1.35;margin-top:4px}
.vc .ex{font-family:S,serif;font-style:italic;font-size:29px;color:#556;margin-top:4px}
.tx{background:#fff;border-radius:22px;padding:14px 24px 16px;border:2.5px solid @SOFT@}
.tx .tl{display:inline-block;font-size:20px;font-weight:800;letter-spacing:1.5px;background:@AC@;color:#fff;border-radius:8px;padding:3px 14px;margin-bottom:6px}
.tx .sen{font-size:27px;line-height:1.5}
""".replace('@AC@', AC).replace('@SOFT@', SOFT)

_css = gen30.css
gen30.css = lambda a, s, t: _css(a, s, t) + extra(CUR['AC'], CUR['SOFT'])

def page(C, n, T, body, tag):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><style>{C}</style></head><body><div class="pg">
<div class="top"><img src="{gen29.LOGO}"><span>{n:02d} / {T:02d}</span></div>
<div class="mn">{body}</div>
<div class="ft"><span>SAT R&amp;W · {CUR['foot']}</span><span>{"Swipe →" if n < T else "@globalmathprep"}</span></div></div></body></html>'''
gen30.page = page

def cover(h, teaser, skill, chips, emo):
    AC = CUR['AC']
    ch = ''.join(f'<span>{c}</span>' for c in [f'SKILL · {skill}'] + chips)
    return f'''<div style="display:flex;justify-content:space-between;align-items:center"><div class="pill">DOMAIN · CRAFT AND STRUCTURE</div>{E(emo,110,'fl')}</div>
<div style="font-family:IN,M,sans-serif;font-weight:900;font-size:58px;letter-spacing:-1px;color:#1e1e1e"><span style="color:{AC}">SAT</span>&reg; Reading &amp; Writing</div>
<div class="h" style="font-size:96px">{h}</div>
<div class="lead">{teaser}</div><div class="chips">{ch}</div><div class="swipe">Swipe →</div>'''

def fix(fr): return fr.replace('Section 1, Module 1: Reading and Writing', 'Reading and Writing · GMP practice').replace('Question 1 of 27', 'Practice question 1')
def qslide(fr, note='Decide first, then swipe for the answer.'):
    return f'''<div class="pill">YOUR TURN · TRY IT FIRST</div>{fix(fr)}
<div class="card big" style="padding:16px 24px">{note}<div style="font-size:22px;font-weight:600;color:#667;margin-top:6px">Original Global Math Prep practice question. Not from the College Board.</div></div>'''

def cluerows(cl):
    return ''.join(f'<div class="cl"><div class="no">{i}</div><div class="ph">{a}</div><div class="ms">{b}</div></div>' for i, (a, b) in enumerate(cl, 1))

def vc(w, pr, mean, why, ex, trap=False):
    tag = '<span class="tg">MOST TEMPTING</span>' if trap else ''
    sub = f'<span class="pr">{pr} · {mean}</span>' if pr else ''
    exs = f'<div class="ex">{ex}</div>' if ex else ''
    return f'<div class="vc{" tp" if trap else ""}"><div class="top2"><span class="wd">{w}</span>{sub}{tag}</div><div class="why">{why}</div>{exs}</div>'

def endp():
    return f'''<div class="pill">THE END</div>
<div style="text-align:center"><div class="in" style="font-size:58px">Want more practice like this?</div>
<div class="in blue" style="font-size:190px;margin:8px 0">SAT</div><div class="in" style="font-size:54px">Comment “SAT” below</div></div>
<div class="card" style="font-size:27px;font-weight:700;text-align:center">Next: <span class="hl">a new SAT practice question</span></div>
<div style="display:flex;gap:20px;align-items:stretch">
 <div class="card" style="text-align:center;padding:14px"><img src="{gen29.QR}" style="width:220px;height:220px;display:block"><div style="font-weight:800;font-size:22px;margin-top:4px">Scan to sign up</div></div>
 <div class="card" style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:12px;font-size:27px;font-weight:700">
  <div><span class="blue">English</span> · Tue · Thu · Sat · 20:00–21:20</div><div><span class="blue">Math</span> · Mon · Wed · Fri · 20:00–21:20</div><div style="color:#556">Ulaanbaatar, Mongolia time</div><div style="color:#556;white-space:nowrap">WhatsApp +1 428 880 1826</div></div></div>'''

def wic(key, prefix, AC, SOFT, TINT, skill, h, teaser, emo, passage, choices, clue_sent, clues, rule, ok, eq, say, test, wordcard, wrong, rule2):
    CUR.update(AC=AC, SOFT=SOFT, foot=skill.upper())
    p1 = cover(h, teaser, skill, ['4 choices', '3 clues'], emo)
    p2 = qslide(frame(1, f'<span style="font-size:27px;line-height:1.5;display:block">{passage}</span>', choices, prompt=PR_WIC), 'Which word or phrase fits the blank? Decide, then swipe.')
    p3 = f'''<div class="pill">KEY CLUES</div><div class="h" style="font-size:72px"><span class="blue">3 clues</span> point<br>to the answer</div>
<div class="card" style="padding:16px 24px"><div class="sen" style="font-size:30px;line-height:1.55">{clue_sent}</div></div>
<div class="card" style="padding:6px 24px">{cluerows(clues)}</div>
<div class="rule" style="font-size:27px">{rule}</div>'''
    wc = ''.join(f'<div style="font-size:27px;font-weight:700;color:#334;line-height:1.4">{x}</div>' for x in wordcard)
    p4 = f'''<div class="pill">ANSWER</div>
<div class="okrow"><div class="ok">{ok}</div><div class="h" style="font-size:54px">{eq}</div></div>
<div class="lead" style="font-size:31px">{say}</div>
<div class="card" style="padding:14px 24px"><div class="lab">TEST IT</div><div class="sen" style="font-size:33px">{test}</div></div>
<div class="card" style="padding:14px 24px"><div class="lab">WORD CARD</div>{wc}</div>
<div class="rule" style="font-size:26px">{rule2}</div>'''
    ws = ''.join(vc(*w) for w in wrong)
    p5 = f'''<div class="pill">WHY THE OTHERS ARE WRONG</div><div class="h" style="font-size:64px">Why not the<br><span class="blue">other three?</span></div>{ws}
<div style="font-size:27px;font-weight:800;color:#445;text-align:center">{ok.split(')')[0]}) is explained on the previous slide.</div>'''
    return dict(key=key, prefix=prefix, AC=AC, SOFT=SOFT, TINT=TINT, nxt='New', pages=[p1, p2, p3, p4, p5, endp()], foot=skill.upper())

POSTS = {}

def mk_neander():
    return wic('Neanderthal', 'GMP-WordsInContext', '#7e22ce', '#f0e4fb', '#fbf7ff', 'Words in Context',
      '<span class="blue">One claim.</span><br>Strong<br>or weak?', 'One word decides it. Look at what the author ignores.', '1f9d0',
      'The author’s claim about the relationship between Neanderthals and Homo sapiens is ______, as it fails to account for several recent archaeological discoveries. To be convincing, his argument would need to address recent finds of additional hominid fossils, such as the latest Denisovan specimens and Homo longi.',
      ['disorienting', 'tenuous', 'nuanced', 'unoriginal'],
      'The author’s claim about the relationship between Neanderthals and Homo sapiens is ______, as <span class="hk">it fails to account for</span> several recent archaeological discoveries. <span class="hk">To be convincing</span>, his argument <span class="hk">would need to address</span> recent finds of additional hominid fossils, such as the latest Denisovan specimens and Homo longi.',
      [('fails to account for', 'The claim leaves out evidence.'), ('To be convincing, ... would need to', 'Right now it is not convincing.'), ('recent finds of additional hominid fossils', 'New evidence the claim ignores.')],
      'Negative clues, so the blank must be negative: the claim is weak.',
      'B) tenuous', '= weak', 'Say it: <b>TEN-yoo-us</b>. It means weak, not well supported by evidence.',
      'The author’s claim … is <b>tenuous</b> (weak), as it fails to account for several recent discoveries.',
      ['Similar: weak · shaky · flimsy · unconvincing', 'Opposite: strong · solid · well-supported', 'Also: very thin, easy to break (a tenuous thread)'],
      [('C) nuanced', 'NOO-ahnst', 'careful, showing small differences', 'It is a positive word. The text criticizes the claim. It sounds academic, so students pick it.', 'She gave a nuanced answer about the war.', True),
       ('A) disorienting', 'dis-OR-ee-en-ting', 'confusing', 'The text says the claim is incomplete, not confusing.', 'The dark maze was disorienting.'),
       ('D) unoriginal', 'un-uh-RIJ-i-nul', 'not new, copied', 'The problem is missing evidence, not a lack of new ideas.', 'The film’s story felt unoriginal.')],
      'Tip: “fails to” and “would need to” are negative clues. Cross out positive words.')

def mk_state():
    return wic('State-Taxes', 'GMP-WordsInContext', '#be185d', '#fbe4ee', '#fff7fa', 'Words in Context',
      '<span class="blue">Do taxes</span><br>decide where<br>you move?', 'One phrase shows what really matters. Spot the 3 clues.', '1f4cd',
      'According to a US tax policy expert, state taxes are ______ other factors when considering an interstate move. Even significant differences in state taxation have almost no effect on most people’s decisions, while differences in employment opportunities, housing availability, and climate are strong influences.',
      ['consistent with', 'representative of', 'overshadowed by', 'irrelevant to'],
      'Even significant differences in state taxation have <span class="hk">almost no effect</span> on most people’s decisions, <span class="hk">while</span> differences in employment opportunities, housing availability, and climate are <span class="hk">strong influences</span>.',
      [('almost no effect', 'Taxes matter very little.'), ('while', 'A contrast with the other factors.'), ('strong influences', 'The other factors matter a lot.')],
      'Taxes are weak, other factors are strong, so taxes seem less important than them.',
      'C) overshadowed by', '= less important than', 'Say it: <b>OH-ver-shad-ohd</b>. Made to seem less important than something bigger.',
      'State taxes are <b>overshadowed by</b> other factors when considering an interstate move.',
      ['Think of a small tree in the shadow of a big one.', 'Similar: outweighed by · less important than', 'Opposite: more important than'],
      [('D) irrelevant to', 'i-REL-uh-vunt', 'not connected to', '“Almost no effect” is not zero, so taxes are less important, not unimportant. Taxes are unimportant to people’s decisions, not to the other factors.', 'His age is irrelevant to the job.', True),
       ('A) consistent with', 'kun-SIS-tunt', 'in agreement with', 'Taxes and the other factors are contrasted, not in agreement.', 'His story is consistent with the facts.'),
       ('B) representative of', 'rep-ri-ZEN-tuh-tiv', 'a typical example of', 'Taxes are not an example of jobs, housing or climate.', 'This painting is representative of her style.')],
      '“almost no” is not “no”. Avoid choices that are too extreme.')

def mk_john():
    AC, SOFT, TINT = '#0e7490', '#d8f0f5', '#f3fbfd'
    CUR.update(AC=AC, SOFT=SOFT, foot='TEXT STRUCTURE AND PURPOSE')
    p1 = cover('<span class="blue">What is this</span><br>sentence doing?', 'A boy throws twigs into a river. Function questions ask what a sentence does, not what it says.', 'Text Structure and Purpose', ['5 sentences', '3 clues'], '1f4da')
    s1 = 'Perhaps ten-year-old John was puzzling to the folk there in the Florida woods for he was an imaginative child and fond of day-dreams.'
    s24 = 'The St. John River flowed a scarce three hundred feet from his back door. On its banks at this point grow numerous palms, luxuriant magnolias and bay trees. On the bosom of the stream float millions of delicately colored hyacinths.'
    s5 = '[John Redding] loved to wander down to the water’s edge, and, casting in dry twigs, watch them sail away down stream to Jacksonville, the sea, the wide world and [he] wanted to follow them.'
    def tx(l, t): return f'<div class="tx"><span class="tl">{l}</span><div class="sen" style="font-size:28px">{t}</div></div>'
    p2 = f"""<div class="pill">READ FIRST · 3 JOBS</div>
<div class="lead" style="font-size:26px;font-style:italic">The following text is adapted from Zora Neale Hurston’s 1921 short story “John Redding Goes to Sea.” John is a child who lives in a town in the woods.</div>
{tx('JOB 1 · THE DREAMER', s1)}{tx('JOB 2 · THE PLACE', s24)}{tx('JOB 3 · THE WISH (UNDERLINED)', '<span class="ul">' + s5 + '</span>')}"""
    ch = ['It provides an extended description of a location that John likes to visit.', 'It reveals that some residents of John’s town are confused by his behavior.', 'It illustrates the uniqueness of John’s imagination compared to the imaginations of other children.', 'It suggests that John longs to experience a larger life outside the Florida woods.']
    fr = frame(1, '<span style="font-size:27px;line-height:1.5;display:block"><i>Underlined sentence:</i><br><u style="text-decoration-thickness:3px;text-underline-offset:4px">' + s5 + '</u></span>', ch, prompt='Which choice best describes the function of the underlined sentence in the text as a whole?')
    p3 = qslide(fr, 'What job does the underlined sentence do? Decide, then swipe.')
    p3 = p3.replace('class="bxc"', 'class="bxc" style="font-size:25px"')
    cl = [('watch them sail away … to Jacksonville, the sea, the wide world', 'The places get bigger and farther away.'), ('wanted to follow them', 'He wishes to go too.'), ('fond of day-dreams (Sentence 1)', 'He already dreams about other places.')]
    p4 = f'''<div class="pill">ANSWER</div><div class="okrow"><div class="ok">D)</div><div class="h" style="font-size:52px">= longs for a larger life</div></div>
<div class="lead" style="font-size:29px">It suggests that John longs to experience a larger life outside the Florida woods.</div>
<div class="card" style="padding:6px 24px">{cluerows(cl).replace('width:330px','width:330px')}</div>
<div class="card" style="padding:14px 24px"><div class="lab">WORD CARD · LONGS</div><div style="font-size:27px;font-weight:700;color:#334;line-height:1.4">Say it: LONGZ. Wishes very much for something.<br>Similar: yearns · wishes · dreams of</div></div>'''
    p5 = f'''<div class="pill">WHY THE OTHERS ARE WRONG</div><div class="h" style="font-size:64px">Why not <span class="blue">A, B, C?</span></div>
{vc('A) extended description', '', '', 'The place is described in Sentences 2 to 4. Sentence 5 says what John does there and what he wants. It mentions the water’s edge, so many students pick it.', '', True)}
{vc('B) residents are confused', '', '', 'This idea appears only in Sentence 1 (“puzzling to the folk”).', '')}
{vc('C) imagination is unique', '', '', 'No other children appear in the text, so nothing is compared.', '')}'''
    return dict(key='John-Redding', prefix='GMP-TextStructure', AC=AC, SOFT=SOFT, TINT=TINT, nxt='New', pages=[p1, p2, p3, p4, p5, endp()], foot='TEXT STRUCTURE AND PURPOSE')

def mk_chiq():
    AC, SOFT, TINT = '#a16207', '#f8ecc9', '#fffbee'
    CUR.update(AC=AC, SOFT=SOFT, foot='CROSS-TEXT CONNECTIONS')
    p1 = cover('<span class="blue">200 stones.</span><br>Were they really<br>tools?', 'Two texts disagree. Find the one idea the whole claim depends on.', 'Cross-Text Connections', ['2 texts', '3 doubts'], '1f50d')
    t1 = 'An excavation in Chiquihuite Cave in central Mexico has upended the belief that approximately 13,000 years ago, a group known as the Clovis people were the first human inhabitants of North America. More than 200 crude stone tools were found embedded in a layer of earth that is up to 33,150 years old, revealing that <span class="ul">humans occupied the cave thousands of years before the Clovis people reached the continent</span>.'
    t2 = 'The objects uncovered in Chiquihuite Cave are intriguing, but it is premature to characterize them as tools. The stone pieces are so roughly shaped that they may have simply fractured from rocks during natural geological activity in the cave. Moreover, their unearthing has thus far not been accompanied by discoveries of other signs of human activity or even traces of human DNA from surfaces.'
    p2 = f'''<div class="pill">YOUR TURN · READ BOTH TEXTS</div>
<div class="tx"><span class="tl">TEXT 1</span><div class="sen">{t1}</div></div>
<div class="tx"><span class="tl">TEXT 2</span><div class="sen">{t2}</div></div>
<div class="card big" style="padding:14px 24px;font-size:28px">What does Text 2 think of the underlined claim? Decide, then swipe.<div style="font-size:22px;font-weight:600;color:#667;margin-top:4px">Original Global Math Prep practice passage. Not from the College Board.</div></div>'''
    p3 = f'''<div class="pill">STEP 1 · TEXT 1</div><div class="h" style="font-size:72px">The claim rests on<br><span class="blue">one hidden idea</span></div>
<div class="card" style="padding:16px 24px"><div class="lab">THE UNDERLINED CLAIM</div><div class="sen" style="font-size:32px"><span class="ul">humans occupied the cave thousands of years before the Clovis people reached the continent</span></div></div>
<div class="card" style="padding:6px 24px">{cluerows([('More than 200 crude stone tools', 'The proof is these stones.'), ('up to 33,150 years old', 'The soil layer is very old.')])}</div>
<div class="card" style="padding:14px 24px"><div class="lab">EASY MEANING</div><div style="font-size:28px;font-weight:700;line-height:1.4">Over 200 stone tools in 33,000-year-old soil show that people lived there long before the Clovis people.</div></div>
<div class="rule" style="font-size:27px">The claim only works if the stones really are tools made by humans.</div>'''
    cl = [('so roughly shaped', 'They may not be carefully made.'), ('may have simply fractured … natural geological activity', 'Nature, not people, may have broken the rocks.'), ('other signs of human activity … traces of human DNA', 'No other proof of people was found.')]
    p4 = f'''<div class="pill">STEP 2 · TEXT 2</div><div class="h" style="font-size:72px">Text 2 gives<br><span class="blue">3 reasons to doubt</span></div>
<div class="lead" style="font-size:30px">Text 2: “it is <span class="hk">premature</span> to characterize them as tools.” Premature means too early, before there is enough proof.</div>
<div class="card" style="padding:6px 24px">{cluerows(cl)}</div>
<div class="rule" style="font-size:27px">Text 2 attacks the base: are the stones tools at all?</div>'''
    wr = ''.join(f'<div class="wr"><span class="w">{a}</span><span>{b}</span></div>' for a, b in [('A) needs more study', 'Most tempting. Text 2 never calls the claim plausible. “Further study” only sounds like its caution.'), ('C) proved right', 'Opposite. Text 2 doubts the claim.'), ('D) ignores Clovis dates', 'Text 2 says nothing about the Clovis people. It only talks about the stones.')])
    p5 = f'''<div class="pill">ANSWER</div><div class="okrow"><div class="ok">B)</div><div class="h" style="font-size:50px">assumption not supported</div></div>
<div class="card" style="padding:14px 24px"><div class="lab">TEST IT</div><div class="sen" style="font-size:31px">The claim rests on <b>an assumption about the stone pieces</b> that is <b>not sufficiently supported by evidence</b>.</div></div>
<div class="lead" style="font-size:27px">assumption = an idea believed without proof (uh&#8209;SUMP&#8209;shun)</div>
<div class="card" style="padding:8px 26px">{wr}</div>
<div class="rule" style="font-size:26px">If Text 2 attacks what the claim depends on, choose “assumption not supported”.</div>'''
    return dict(key='Chiquihuite', prefix='GMP-CrossText', AC=AC, SOFT=SOFT, TINT=TINT, nxt='New', pages=[p1, p2, p3, p4, p5, endp()], foot='CROSS-TEXT CONNECTIONS')

BUILD = {'Chiquihuite': mk_chiq, 'John-Redding': mk_john, 'Neanderthal': mk_neander, 'State-Taxes': mk_state}

if __name__ == '__main__':
    sel = [a for a in sys.argv[1:] if not a.startswith('--')] or list(BUILD)
    for k in sel:
        post = BUILD[k]()
        CUR.update(AC=post['AC'], SOFT=post['SOFT'], foot=post['foot'])
        gen30.render(post, '--video' in sys.argv)
        out = HERE / ('out30-' + post['key'])
        for f in sorted(out.glob('GMP-Transitions-*')):
            f.rename(out / f.name.replace('GMP-Transitions-', post['prefix'] + '-'))
