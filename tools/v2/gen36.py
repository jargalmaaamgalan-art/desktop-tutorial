"""Words-in-Context post: Cacao and Maize (answer D, confirm). Content from the owner's own explainer (Cacao_and_Maize_Explainer.html).
Model: gen30/gen34. Run: python3 gen35.py [--video]"""
import sys, shutil
import gen30, gen29
from gen30 import frame
from gen18 import E, HERE

AC, SOFT, TINT = '#c2410c', '#fde6d8', '#fff8f3'   # orange: not used by any scheduled post

EXTRA = """
.hk{background:#fde68a;color:#1e1e1e;padding:0 6px;border-radius:8px;font-weight:700}
.cl{display:flex;gap:16px;align-items:center;padding:12px 0;border-top:2px dashed #f3d3c0}
.cl:first-child{border-top:0}
.cl .no{flex:none;width:50px;height:50px;border-radius:50%;background:@AC@;color:#fff;font-size:28px;font-weight:900;display:flex;align-items:center;justify-content:center}
.cl .ph{flex:none;width:330px;font-family:S,serif;font-size:29px;font-weight:700;background:#fde68a;border-radius:10px;padding:4px 10px;line-height:1.3}
.cl .ms{font-size:27px;font-weight:700;color:#334;line-height:1.3}
.vc{background:#fff;border-radius:22px;padding:14px 24px 16px;border:2.5px solid @SOFT@}
.vc.tp{border:3px solid #c62828}
.vc .top2{display:flex;align-items:baseline;gap:14px;flex-wrap:wrap}
.vc .wd{font-family:S,serif;font-size:40px;font-weight:700;color:#c62828}
.vc .pr{font-size:24px;font-weight:700;color:#667}
.vc .tg{font-size:20px;font-weight:800;letter-spacing:1px;background:#c62828;color:#fff;border-radius:20px;padding:3px 14px}
.vc .why{font-size:31px;font-weight:600;color:#223;line-height:1.35;margin-top:4px}
.vc .ex{font-family:S,serif;font-style:italic;font-size:29px;color:#556;margin-top:4px}
.trio{display:flex;gap:12px}
.trio span{flex:1;text-align:center;background:#fff;border:2.5px solid @AC@;border-radius:18px;padding:12px 6px;font-family:S,serif;font-size:34px;font-weight:700;color:@AC@}
.trio span.on{background:@AC@;color:#fff}
""".replace('@AC@', AC).replace('@SOFT@', SOFT)
_css = gen30.css
gen30.css = lambda a, s, t: _css(a, s, t) + EXTRA

def page(C, n, T, body, tag):
    return f'''<!doctype html><html lang="mn"><head><meta charset="utf-8"><style>{C}</style></head><body><div class="pg">
<div class="top"><img src="{gen29.LOGO}"><span>{n:02d} / {T:02d}</span></div>
<div class="mn">{body}</div>
<div class="ft"><span>SAT R&amp;W · WORDS IN CONTEXT</span><span>{"Swipe →" if n < T else "@globalmathprep"}</span></div></div></body></html>'''
gen30.page = page

S1 = 'Domesticated thousands of years ago by Indigenous people in South America, cacao, the plant from which chocolate is made, deviates structurally from the wild plant it is descended from.'
S2 = 'Maize (corn), another crop domesticated by Indigenous Americans, shows so little resemblance to any wild plant that genetic research was necessary to ______ teosinte grass as its ancestor.'
CH = ['acquire', 'develop', 'attract', 'confirm']
PR = 'Which choice completes the text with the most logical and precise word or phrase?'
PASS = f'<span style="font-size:27px;line-height:1.5;display:block">{S1} {S2}</span>'

# 1 cover
cov = gen30.cover('SAT R&amp;W · WORDS IN CONTEXT', '<span class="blue">Corn</span><br>looks nothing like<br>its ancestor',
                  'So how did scientists find out who its ancestor was? One SAT word answers it.',
                  ['Words in Context', '4 choices', '3 clues'], '1f331').replace('Гүйлгээд үз →', 'Swipe →')

p2 = f"""<div class="pill">YOUR TURN · TRY IT FIRST</div>{frame(1, PASS, CH, prompt=PR)}
<div class="card big" style="padding:16px 24px">Which word fits the blank? Decide, then swipe for the answer.</div>"""

S2h = ('Maize (corn), another crop domesticated by Indigenous Americans, shows <span class="hk">so little resemblance</span> to any wild plant that '
       '<span class="hk">genetic research was necessary</span> to ______ <span class="hk">teosinte grass as its ancestor</span>.')
cl = [('so little resemblance', 'You cannot tell by looking. Almost no similarity.'),
      ('genetic research was necessary', 'Scientists needed proof.'),
      ('teosinte grass as its ancestor', 'This is the fact being proved.')]
rows = ''.join(f'<div class="cl"><div class="no">{i}</div><div class="ph">{a}</div><div class="ms">{b}</div></div>' for i, (a, b) in enumerate(cl, 1))
p3 = f"""<div class="pill">KEY CLUES</div>
<div class="h" style="font-size:72px"><span class="blue">3 clues</span> point<br>to the answer</div>
<div class="card" style="padding:16px 24px"><div class="sen" style="font-size:31px;line-height:1.55">{S2h}</div></div>
<div class="card" style="padding:6px 24px">{rows}</div>
<div class="rule" style="font-size:27px">Looks cannot tell us, so research was needed. Research gave proof.</div>"""

p4 = f"""<div class="pill">ANSWER</div>
<div class="okrow"><div class="ok">D) confirm</div><div class="h" style="font-size:56px">= prove</div></div>
<div class="lead" style="font-size:32px">Say it: <b>kun-FURM</b>. It means to show that something is true.</div>
<div class="card" style="padding:14px 24px"><div class="lab">ASK: “WHAT DOES RESEARCH DO?”</div>
<div class="trio"><span>finds</span><span>proves</span><span class="on">confirms</span></div></div>
<div class="card" style="padding:14px 24px"><div class="lab">TEST IT</div><div class="sen" style="font-size:36px">…genetic research was necessary to <b>confirm</b> teosinte grass as its ancestor.</div></div>
<div class="rule" style="font-size:26px">Pattern: <u>to ___ X as Y</u> → confirm, identify, establish<br>so … that research was necessary → proof was needed</div>"""

def vc(w, pr, mean, why, ex, trap=False):
    tag = '<span class="tg">MOST TEMPTING</span>' if trap else ''
    return f'<div class="vc{" tp" if trap else ""}"><div class="top2"><span class="wd">{w}</span><span class="pr">{pr} · {mean}</span>{tag}</div><div class="why">{why}</div><div class="ex">{ex}</div></div>'
p5 = f"""<div class="pill">WHY THE OTHERS ARE WRONG</div>
<div class="h" style="font-size:66px">Why is <span class="blue">develop</span><br>the trap?</div>
{vc('B) develop', 'di-VEL-up', 'create, build', 'Research cannot create an ancestor. Teosinte already existed. It sounds scientific, so many students pick it.', 'Scientists developed a vaccine.', True)}
{vc('A) acquire', 'uh-KWY-er', 'get, obtain', 'Research does not get grass.', 'The museum acquired a painting.')}
{vc('C) attract', 'uh-TRAKT', 'pull toward', 'Research does not pull grass toward it.', 'Flowers attract bees.')}"""

p6 = f"""<div class="pill">THE END</div>
<div style="text-align:center"><div class="in" style="font-size:58px">Want more practice like this?</div>
<div class="in blue" style="font-size:190px;margin:8px 0">SAT</div><div class="in" style="font-size:54px">Comment “SAT” below</div></div>
<div class="card" style="font-size:27px;font-weight:700;text-align:center">Next: <span class="hl">a new SAT practice question</span></div>
<div style="display:flex;gap:20px;align-items:stretch">
 <div class="card" style="text-align:center;padding:14px"><img src="{gen29.QR}" style="width:220px;height:220px;display:block"><div style="font-weight:800;font-size:22px;margin-top:4px">Scan to sign up</div></div>
 <div class="card" style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:12px;font-size:27px;font-weight:700">
  <div><span class="blue">English</span> · Tue · Thu · Sat · 20:00–21:20</div><div><span class="blue">Math</span> · Mon · Wed · Fri · 20:00–21:20</div><div style="color:#556">Ulaanbaatar time · WhatsApp +1 428 880 1826</div></div></div>"""

POST = dict(key='Cacao-Maize-EN', AC=AC, SOFT=SOFT, TINT=TINT, nxt='New',
            pages=[cov, p2, p3, p4, p5, p6])

if __name__ == '__main__':
    gen30.render(POST, '--video' in sys.argv)
    out = HERE / ('out30-' + POST['key'])
    for f in sorted(out.glob('GMP-Transitions-*')):
        f.rename(out / f.name.replace('GMP-Transitions-Cacao-Maize-EN', 'GMP-WordsInContext-Cacao-Maize-EN'))
