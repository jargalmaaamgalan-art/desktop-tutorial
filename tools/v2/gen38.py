"""SAT multi-meaning word carousel: BEAR (8 slides, own original bear mascot).
Run: python3 gen38.py [--video]"""
import sys
import gen30, gen29, gen37
from gen37 import CUR
from gen18 import E, HERE

AC, SOFT, TINT = '#dc2626', '#fde0dd', '#fff6f4'
FUR, LIGHT, DARK = '#8b5a2b', '#ecd0a2', '#3b2210'

def extra2():
    return f"""
.bw{{font-family:IN,M,sans-serif;font-weight:900;letter-spacing:-2px;line-height:1;color:{AC}}}
.mg{{align-self:flex-start;background:#fff;border:3px solid {AC};color:#222;border-radius:40px;padding:10px 26px;font-size:34px;font-weight:800}}
.en{{font-size:30px;font-weight:700;color:#445;line-height:1.3}}
.ex{{font-family:S,serif;font-size:37px;line-height:1.4}}
.ex .k{{background:#fde68a;border-radius:8px;padding:0 6px;font-weight:700}}
.scene{{position:relative;display:flex;align-items:flex-end;justify-content:center;height:430px}}
.scene svg{{height:420px;width:420px;flex:none;animation:bob 1.6s ease-in-out infinite;transform-origin:50% 100%}}
@keyframes bob{{0%,100%{{transform:translateY(0) rotate(-1.5deg)}}50%{{transform:translateY(-14px) rotate(1.5deg)}}}}
.bub{{position:relative;background:#fff;border:3.5px solid {DARK};border-radius:30px;padding:16px 24px;font-size:31px;font-weight:800;line-height:1.3;max-width:400px;margin-bottom:200px;margin-right:6px;animation:pop .6s 1s both}}
.bub:after{{content:"";position:absolute;right:-15px;bottom:26px;width:26px;height:26px;background:#fff;border-right:3.5px solid {DARK};border-top:3.5px solid {DARK};transform:rotate(45deg)}}
.gr{{display:grid;grid-template-columns:1fr 1fr;gap:16px}}
.gr .c{{background:#fff;border:3px solid {AC};border-radius:22px;padding:14px 20px}}
.gr .c b{{display:block;font-family:IN,M,sans-serif;font-size:42px;color:{AC};letter-spacing:-1px}}
.gr .c i{{font-family:S,serif;font-size:27px;color:#445;display:block;margin-top:2px}}
.gr .c u{{text-decoration:none;font-size:27px;font-weight:800;color:#222;display:block;margin-top:4px}}

.pg{{background-color:{TINT};background-image:radial-gradient({SOFT} 3px,transparent 3.5px);background-size:44px 44px}}
.bb{{position:relative;flex:none;width:380px;height:380px}}
.bb:before{{content:"";position:absolute;left:-6px;bottom:-6px;width:calc(100% + 12px);height:calc(100% + 12px);border-radius:50%;background:{SOFT}}}
.bb svg{{position:relative;z-index:1;width:100%;height:100%}}
.rx{{display:flex;align-items:center;gap:14px;background:#fff;border:3px dashed {AC};border-radius:44px;padding:10px 26px;font-size:28px;font-weight:800;align-self:center;color:#222}}
.rx b{{color:{AC}}}
.opt{{display:flex;align-items:center;gap:20px;background:#fff;border:3px solid {AC};border-radius:26px;padding:10px 24px;font-size:36px;font-weight:800}}
.opt i{{flex:none;width:64px;height:64px;border-radius:50%;background:{AC};color:#fff;font-style:normal;font-family:IN,M,sans-serif;font-size:40px;display:flex;align-items:center;justify-content:center}}
"""
_c = gen30.css
gen30.css = lambda a, s, t: _c(a, s, t) + extra2()


def bear(mood):
    ear = f'<circle cx="112" cy="70" r="40" fill="{FUR}"/><circle cx="288" cy="70" r="40" fill="{FUR}"/><circle cx="112" cy="72" r="21" fill="{LIGHT}"/><circle cx="288" cy="72" r="21" fill="{LIGHT}"/>'
    body = f'<ellipse cx="200" cy="318" rx="108" ry="88" fill="{FUR}"/><ellipse cx="200" cy="332" rx="62" ry="62" fill="{LIGHT}"/><ellipse cx="130" cy="396" rx="42" ry="17" fill="{DARK}"/><ellipse cx="270" cy="396" rx="42" ry="17" fill="{DARK}"/>'
    head = f'<circle cx="200" cy="165" r="108" fill="{FUR}"/><ellipse cx="200" cy="200" rx="56" ry="42" fill="{LIGHT}"/><ellipse cx="200" cy="178" rx="19" ry="13" fill="{DARK}"/>'
    def eyes(kind='open'):
        if kind == 'open':
            return ''.join(f'<circle cx="{x}" cy="145" r="12" fill="{DARK}"/><circle cx="{x+4}" cy="141" r="4" fill="#fff"/>' for x in (158, 242))
        if kind == 'smug':
            return ''.join(f'<path d="M{x-16} 150 Q{x} 134 {x+16} 150 Z" fill="{DARK}"/><path d="M{x-18} 140 L{x+18} 140" stroke="{DARK}" stroke-width="5" stroke-linecap="round"/>' for x in (158, 242))
        if kind == 'shut':
            return f'<path d="M142 140 L170 150 L142 160 M258 140 L230 150 L258 160" stroke="{DARK}" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
        if kind == 'worry':
            return eyes('open') + f'<path d="M138 120 L176 130 M262 120 L224 130" stroke="{DARK}" stroke-width="6" stroke-linecap="round"/>'
        if kind == 'glasses':
            return ''.join(f'<circle cx="{x}" cy="146" r="25" fill="#fff" stroke="{DARK}" stroke-width="6"/><circle cx="{x+3}" cy="146" r="10" fill="{DARK}"/>' for x in (158, 242)) + f'<path d="M183 146 L217 146" stroke="{DARK}" stroke-width="6"/>'
        if kind == 'shades':
            return f'<rect x="126" y="126" width="68" height="40" rx="14" fill="{DARK}"/><rect x="206" y="126" width="68" height="40" rx="14" fill="{DARK}"/><path d="M194 138 L206 138" stroke="{DARK}" stroke-width="6"/><path d="M138 134 L156 134" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".6"/>'
    smile = f'<path d="M168 214 Q200 242 232 214" stroke="{DARK}" stroke-width="6" fill="none" stroke-linecap="round"/>'
    grin = f'<path d="M165 212 Q200 262 235 212 Z" fill="{DARK}"/><path d="M180 230 Q200 246 220 230 Q200 224 180 230" fill="#f26b6b"/>'
    flat = f'<path d="M172 226 Q186 216 200 226 Q214 236 228 226" stroke="{DARK}" stroke-width="6" fill="none" stroke-linecap="round"/>'
    oh = f'<ellipse cx="200" cy="228" rx="26" ry="22" fill="{DARK}"/><ellipse cx="200" cy="236" rx="14" ry="9" fill="#f26b6b"/>'
    arm = lambda x, y, r=0: f'<ellipse cx="{x}" cy="{y}" rx="30" ry="62" fill="{FUR}" transform="rotate({r} {x} {y})"/>'
    paw = lambda x, y: f'<circle cx="{x}" cy="{y}" r="32" fill="{FUR}"/><circle cx="{x}" cy="{y}" r="15" fill="{LIGHT}"/>'
    sweat = '<path d="M300 90 Q312 118 300 128 Q288 118 300 90 Z" fill="#7dd3fc" stroke="#0284c7" stroke-width="3"/>'
    P = {
     'think': (body + arm(100, 300, 12) + head + ear + eyes('smug') + smile
               + f'<ellipse cx="300" cy="215" rx="30" ry="64" fill="{FUR}" transform="rotate(-35 300 215)"/>{paw(268,128)}'
               + '<circle cx="335" cy="38" r="26" fill="#fde047" stroke="#ca8a04" stroke-width="4"/><path d="M325 62 h20 M328 70 h14" stroke="#ca8a04" stroke-width="5" stroke-linecap="round"/><path d="M335 2 v-4 M366 14 l6 -6 M368 38 h6 M302 14 l-6 -6" stroke="#ca8a04" stroke-width="5" stroke-linecap="round"/>'),
     'fruit': (body + arm(100, 300, 12) + arm(300, 300, -12) + head + ear + eyes('open') + grin
               + '<circle cx="200" cy="318" r="46" fill="#ef4444"/><path d="M200 272 q0 -22 18 -30" stroke="#5b3a1a" stroke-width="7" fill="none" stroke-linecap="round"/><path d="M204 268 q26 -30 46 -8 q-24 22 -46 8Z" fill="#22c55e"/><circle cx="185" cy="305" r="9" fill="#fff" opacity=".5"/>'
               + paw(150, 340) + paw(250, 340)),
     'please': (body + arm(100, 300, 12) + head + ear + eyes('worry') + f'<path d="M172 226 Q200 214 228 226" stroke="{DARK}" stroke-width="6" fill="none" stroke-linecap="round"/>' + sweat
               + f'<ellipse cx="270" cy="300" rx="30" ry="62" fill="{FUR}" transform="rotate(35 270 300)"/>' + paw(214, 292) + paw(186, 292)
               + '<circle cx="330" cy="330" r="42" fill="#fff" stroke="#3b2210" stroke-width="6"/><path d="M330 330 V302 M330 330 L350 340" stroke="#3b2210" stroke-width="6" stroke-linecap="round"/>'),
     'cost': (f'<path d="M60 300 Q40 230 120 230 L170 240 L190 330 L90 380Z" fill="#c9a36a" stroke="{DARK}" stroke-width="5"/><text x="116" y="332" font-family="Arial Black,sans-serif" font-size="70" fill="#166534" stroke="#fff" stroke-width="2">$</text>'
              + body + arm(300, 300, -12) + head + ear + eyes('worry') + flat + sweat + paw(98, 270) + paw(112, 320)),
     'ears': (body + arm(100, 300, 12) + arm(300, 300, -12) + head + ear + eyes('shut') + oh + paw(88, 150) + paw(312, 150)
              + '<path d="M345 70 q16 14 0 28 M368 56 q28 28 0 56" stroke="#dc2626" stroke-width="6" fill="none" stroke-linecap="round"/><path d="M20 60 q-16 14 0 28 M-4 46 q-28 28 0 56" stroke="#dc2626" stroke-width="6" fill="none" stroke-linecap="round" transform="translate(30 0)"/>'),
     'out': (body + arm(100, 300, 12) + head + ear + eyes('glasses') + smile
             + f'<rect x="225" y="236" width="140" height="150" rx="10" fill="#fff" stroke="{DARK}" stroke-width="5" transform="rotate(8 295 310)"/><path d="M250 340 l26 -30 l24 18 l36 -50" stroke="#16a34a" stroke-width="8" fill="none" stroke-linecap="round" stroke-linejoin="round" transform="rotate(8 295 310)"/><path d="M252 360 h80" stroke="#aab" stroke-width="6" stroke-linecap="round" transform="rotate(8 295 310)"/>'
             + arm(300, 320, -30) + paw(262, 262)),
     'sun': (body + arm(100, 300, 12) + arm(300, 300, -12) + head + ear + eyes('shades') + grin + paw(88, 330) + paw(312, 330)),
    }[mood]
    return f'<svg viewBox="-10 -10 420 420" xmlns="http://www.w3.org/2000/svg">{P}</svg>'


def hi(s, k): return s.replace(k, f'<span class="k">{k}</span>')

def rx(q, em='1f4ac'):
    return f'<div class="rx">{E(em,44)}<span>{q}</span></div>'

def exp(n, title, en, mg, example, key, quip, mood, stick, q):
    return f"""<div style="display:flex;justify-content:space-between;align-items:center"><div class="pill">EXPRESSION {n} OF 6</div>{E(stick,96,'fl')}</div>
<div class="bw" style="font-size:{104 if len(title) < 12 else 88}px">{title}</div>
<div class="en">{en}</div><div class="mg">{mg}</div>
<div class="card" style="padding:18px 26px"><div class="ex">{hi(example, key)}</div></div>
<div class="scene" style="height:400px"><div class="bub" style="margin-bottom:170px">{quip}</div><div class="bb">{bear(mood)}</div></div>
{rx(q)}"""

def cover():
    sun = bear('sun').replace('<svg ', '<svg ')
    return f"""<div style="display:flex;justify-content:space-between;align-items:center"><div class="pill">DOMAIN · CRAFT AND STRUCTURE</div>{E('1f92f',100,'fl')}</div>
<div style="font-family:IN,M,sans-serif;font-weight:900;font-size:58px;letter-spacing:-1px;color:#1e1e1e"><span style="color:{AC}">SAT</span>&reg; Reading &amp; Writing</div>
<div class="bw" style="font-size:240px;margin-top:-6px">BEAR</div>
<div class="lead" style="font-size:40px;font-weight:800;line-height:1.25">A big brown animal?<br><span class="hl">Not on the SAT.</span></div>
<div class="mg" style="font-size:31px">Баавгай биш! Нэг үг, 6 өөр утга</div>
<div class="scene" style="height:330px;margin-top:-6px"><div class="bub" style="margin-bottom:120px;font-size:30px">Do you know all 6?<br>Be honest. 😏</div><div class="bb" style="width:320px;height:320px"><div style="position:absolute;left:-8px;bottom:-4px;width:340px;height:340px;border-radius:50%;background:{SOFT}"></div>{sun.replace('<svg ','<svg style="position:relative;z-index:1" ',1) if False else sun}</div></div>
<div class="chips"><span>SKILL · Words in Context</span><span>6 meanings</span></div>"""

def quiz():
    o = ''.join(f'<div class="opt"><i>{a}</i><span>{b}</span></div>' for a, b in [('A', 'carry something heavy'), ('B', 'show that it is true'), ('C', 'stand a bad thing')])
    return f"""<div style="display:flex;justify-content:space-between;align-items:center"><div class="pill">QUIZ · YOUR TURN</div>{E('1f914',96,'fl')}</div>
<div class="h" style="font-size:66px">What does <span class="blue">“bear out”</span> mean here?</div>
<div class="card" style="padding:20px 26px"><div class="ex" style="font-size:38px">The latest experiments <span class="k">bear out</span> the scientist’s hypothesis.</div></div>
{o}
<div class="scene" style="height:215px"><div class="bub" style="margin-bottom:60px;font-size:30px">Careful! It is not about honey. 🍯</div><div class="bb" style="width:215px;height:215px">{bear("think")}</div></div>
{rx('Comment <b>A</b>, <b>B</b> or <b>C</b> below!','1f447')}"""

def tip():
    cells = [('CARRY', 'bear the cost', 'The school bears the cost.', 'хариуцах'),
             ('ENDURE', 'can’t bear', 'I can’t bear the noise.', 'тэвчих'),
             ('PRODUCE', 'bear fruit', 'Her work bore fruit.', 'үр дүнгээ өгөх'),
             ('CONFIRM', 'bear out', 'The data bear out his idea.', 'баталж өгөх')]
    g = ''.join(f'<div class="c"><b>{a}</b><u>{b}</u><i>{c}</i><i style="color:#222;font-weight:700;font-family:IN,M,sans-serif">{d}</i></div>' for a, b, c, d in cells)
    return f"""<div style="display:flex;justify-content:space-between;align-items:center"><div class="pill">QUIZ ANSWER + SAT TRICK</div>{E('1f389',86,'fl')}</div>
<div class="rule" style="font-size:30px">Answer: <b>B</b>. “Bear out” = show that it is true. 🎯 Did you get it right?</div>
<div class="h" style="font-size:62px">BEAR does <span class="blue">4 hidden jobs</span></div>
<div class="gr">{g}</div>
<div style="display:flex;gap:20px;align-items:stretch">
 <div class="card" style="text-align:center;padding:12px"><img src="{gen29.QR}" style="width:190px;height:190px;display:block"><div style="font-weight:800;font-size:21px;margin-top:4px">Scan to sign up</div></div>
 <div class="card" style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:8px;font-size:26px;font-weight:700">
  <div class="in" style="font-size:36px">Comment “SAT” below</div>
  <div><span class="blue">English</span> · Tue · Thu · Sat · 20:00–21:20</div><div><span class="blue">Math</span> · Mon · Wed · Fri · 20:00–21:20</div><div style="color:#556">Ulaanbaatar, Mongolia time</div><div style="color:#556;white-space:nowrap">WhatsApp +1 428 880 1826</div></div></div>"""

def build():
    CUR.update(AC=AC, SOFT=SOFT, foot='WORDS IN CONTEXT · BEAR')
    P = [cover(),
      exp(1, 'BEAR IN MIND', 'Remember it and think about it.', 'Санаж явах, анхаарах', 'Bear in mind that the shop closes at six.', 'Bear in mind', 'Bear in mind: the honey is MINE.', 'think', '1f4a1', 'Did you know this one? Comment <b>YES</b> or <b>NO</b>'),
      exp(2, 'BEAR FRUIT', 'To give good results after hard work.', 'Үр дүнгээ өгөх', 'Years of study finally bore fruit.', 'bore fruit', 'My tree bore fruit! Apples. Not honey.', 'fruit', '1f4aa', 'Tell us a goal that will <b>bear fruit</b> 👇'),
      exp(3, 'BEAR WITH ME', 'Be patient with me for a short time.', 'Жаахан хүлээгээрэй', 'Please bear with me while I find the file.', 'bear with me', 'Bear with me… I am still thinking.', 'please', '1f605', 'Who says this the most? <b>Tag a friend</b>'),
      exp(4, 'BEAR THE COST', 'To pay for something or take the responsibility.', 'Зардлыг хариуцах', 'The school will bear the cost of the trip.', 'bear the cost', 'Who bears the cost of my honey? You.', 'cost', '1f631', 'Your honest answer: who <b>bears the cost</b> at home?'),
      exp(5, 'CAN’T BEAR', 'To not be able to stand something.', 'Тэвчиж чадахгүй', 'I can’t bear the noise in this room.', 'can’t bear', 'I can’t bear it! Too loud!', 'ears', '1f62e', 'What can you <b>not bear</b>? Comment it 👇'),
      exp(6, 'BEAR OUT', 'To show that something is true.', 'Баталж өгөх, зөв гэдгийг нотлох', 'The new data bear out her theory.', 'bear out', 'The data bear out my theory: honey wins.', 'out', '1f913', '<b>Save</b> this post for your SAT revision'),
      quiz(), tip()]
    return dict(key='Bear', prefix='GMP-SATWords', AC=AC, SOFT=SOFT, TINT=TINT, nxt='New', pages=P, foot='WORDS IN CONTEXT · BEAR')

if __name__ == '__main__':
    post = build()
    gen30.render(post, '--video' in sys.argv)
    out = HERE / 'out30-Bear'
    for f in sorted(out.glob('GMP-Transitions-*')):
        f.rename(out / f.name.replace('GMP-Transitions-', 'GMP-SATWords-'))
