"""BEAR post, teen design: dark neon, chat bubbles, stickers, poll. 9 slides.
Run: python3 gen39.py [--video]"""
import sys
import gen30, gen29
import gen38
import chars
bear = lambda m: chars.draw_kid('BEAR', m)
from gen18 import E, HERE

PINK, LIME, CYAN, YEL, INK, LIL = '#ff5a4e', '#9be564', '#35b6ff', '#ffd43b', '#1c2a6b', '#5b6490'
OUT = ('drop-shadow(5px 0 0 #fff) drop-shadow(-5px 0 0 #fff) drop-shadow(0 5px 0 #fff) drop-shadow(0 -5px 0 #fff) '
       'drop-shadow(4px 4px 0 #fff) drop-shadow(-4px -4px 0 #fff) drop-shadow(0 14px 16px rgba(0,0,0,.45))')

def css(a, s, t):
    FONTS = open(__import__("os").path.join(__import__("os").path.dirname(__file__), "fonts_lr.css")).read()
    return gen29.CSS + FONTS + f"""
body,.pg{{font-family:RB,sans-serif}}
.pg{{background:linear-gradient(rgba(28,42,107,.09) 2px,transparent 2px) 0 0/44px 44px,linear-gradient(90deg,rgba(28,42,107,.09) 2px,transparent 2px) 0 0/44px 44px,#fff8ea}}
.pg:before{{background:linear-gradient(90deg,{PINK},{YEL},{LIME},{CYAN})}}
.top{{top:34px}} .top img{{height:70px;background:#fff;border-radius:40px;padding:6px 22px}}
.top span{{color:{INK};font-size:26px;font-weight:900}}
.ft{{color:{LIL};border-top:2px dashed rgba(28,42,107,.3)}}
.mn{{gap:22px}}
.row{{display:flex;justify-content:space-between;align-items:center;gap:14px}}
.num{{flex:none;width:92px;height:92px;border-radius:50%;background:{YEL};color:{INK};font-family:LL,RB,sans-serif;font-weight:900;font-size:58px;display:flex;align-items:center;justify-content:center;transform:rotate(-8deg);box-shadow:5px 5px 0 {PINK}}}
.chip2{{background:#fff;border:2.5px solid {INK};color:{INK};border-radius:30px;padding:9px 22px;font-weight:800;font-size:23px;letter-spacing:1.5px}}
.chip3{{background:{PINK};color:#fff;border-radius:30px;padding:9px 22px;font-weight:800;font-size:23px;letter-spacing:1.5px;box-shadow:4px 4px 0 {INK}}}
.ttl{{font-family:LL,RB,sans-serif;font-weight:900;color:{INK};line-height:1;letter-spacing:-1px;text-shadow:4px 4px 0 {YEL},8px 8px 0 {PINK}}}
.eng{{color:{INK};font-size:30px;font-weight:700;line-height:1.3}}
.mgl{{align-self:flex-start;background:{YEL};color:{INK};border-radius:44px;padding:10px 32px;font-size:46px;font-weight:900;box-shadow:5px 5px 0 {PINK}}}
.chat{{background:rgba(255,255,255,.75);border:3px solid {INK};border-radius:40px;padding:16px 22px 22px;display:flex;flex-direction:column;gap:14px}}
.chh{{display:flex;align-items:center;gap:12px;color:{LIL};font-weight:800;font-size:22px}}
.chh i{{width:14px;height:14px;border-radius:50%;background:#4ade80;display:block}}
.m{{display:flex;align-items:flex-end;gap:12px}} .m.r{{justify-content:flex-end}}
.av{{flex:none;width:76px;height:76px;border-radius:50%;background:#ffe9b8;overflow:hidden;display:flex;align-items:center;justify-content:center;border:3px solid #fff}}
.av svg{{width:100%;height:100%}}
.b1{{background:#fff;border:3px solid {INK};color:{INK};border-radius:30px 30px 30px 8px;padding:14px 26px;font-size:37px;font-weight:700;line-height:1.3;max-width:800px}}
.b2{{background:linear-gradient(135deg,{PINK},#a24dff);color:#fff;border-radius:30px 30px 8px 30px;padding:14px 26px;font-size:34px;font-weight:800;line-height:1.25;max-width:760px}}
.mk{{background:{YEL};color:{INK};border-radius:10px;padding:0 8px;font-weight:900;font-size:1.12em;box-shadow:3px 3px 0 {PINK}}}
.stk{{flex:none}} .stk svg{{width:100%;height:100%;filter:{OUT};animation:bob 1.6s ease-in-out infinite;transform-origin:50% 100%}}
@keyframes bob{{0%,100%{{transform:translateY(0) rotate(-1.5deg)}}50%{{transform:translateY(-12px) rotate(1.5deg)}}}}
.qc{{flex:1;background:#fff;border:3px solid {INK};color:{INK};border-radius:30px;padding:18px 24px;box-shadow:6px 6px 0 {CYAN}}}
.qc small{{display:block;font-size:20px;font-weight:900;letter-spacing:2px;color:{PINK};margin-bottom:6px}}
.qc div{{font-size:37px;font-weight:900;line-height:1.25}} .qc b{{color:{PINK}}}
.sk{{display:inline-block;border-radius:16px;padding:8px 20px;font-weight:900;color:{INK}}}
.opt{{display:flex;align-items:center;gap:20px;background:#fff;border:3px solid {INK};color:{INK};border-radius:60px;padding:10px 26px 10px 12px;font-size:37px;font-weight:900;box-shadow:6px 6px 0 {PINK}}}
.opt i{{flex:none;width:68px;height:68px;border-radius:50%;background:linear-gradient(135deg,{PINK},#a24dff);color:#fff;font-style:normal;font-family:LL,RB,sans-serif;font-size:40px;display:flex;align-items:center;justify-content:center}}
.rx2{{display:flex;align-items:center;gap:14px;background:{YEL};color:{INK};border-radius:44px;padding:12px 28px;font-weight:900;font-size:30px;box-shadow:5px 5px 0 {PINK};align-self:center}}
.ban{{background:{YEL};color:{INK};border-radius:26px;padding:16px 26px;font-size:32px;font-weight:900;box-shadow:6px 6px 0 {PINK};line-height:1.3}}
.g4{{display:grid;grid-template-columns:1fr 1fr;gap:16px}}
.g4 .c{{border-radius:24px;padding:14px 20px;color:{INK};box-shadow:5px 5px 0 rgba(0,0,0,.35)}}
.g4 .c b{{display:block;font-family:LL,RB,sans-serif;font-size:42px;letter-spacing:-1px}}
.g4 .c u{{text-decoration:none;display:block;font-size:27px;font-weight:900}}
.g4 .c i{{display:block;font-family:RB,sans-serif;font-size:26px;margin-top:2px}}
.g4 .c em{{display:block;font-style:normal;font-size:27px;font-weight:900;margin-top:2px}}
.su{{background:#fff;border:3px solid {INK};color:{INK};border-radius:28px;padding:14px 22px;box-shadow:6px 6px 0 {CYAN}}}
.ttl span{{text-shadow:none}}
.note{{color:{LIL};font-size:21px;font-weight:700;text-align:center}}
"""

def page(C, n, T, body, tag):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><style>{C}</style></head><body><div class="pg">
<div class="top"><img src="{gen29.LOGO}"><span>{n:02d} / {T:02d}</span></div>
<div class="mn">{body}</div>
<div class="ft"><span>SAT R&amp;W · WORDS IN CONTEXT · BEAR</span><span>{"Swipe →" if n < T else "@globalmathprep"}</span></div></div></body></html>'''

gen30.css = css
gen30.page = page

def head(mood):
    return bear(mood).replace('viewBox="-10 -10 420 420"', 'viewBox="60 10 280 280"')

import base64, io, os
from PIL import Image
PHOTO_DIR = '/home/claude/student-photos'
PHOTOS = {}
def photo(mood):
    p = PHOTOS.get(mood)
    if not p or not os.path.exists(p): return None
    im = Image.open(p).convert('RGB'); im.thumbnail((700, 700)); b = io.BytesIO(); im.save(b, 'JPEG', quality=88)
    return 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()

def stk(mood, size):
    d = photo(mood)
    if d:
        return f'<div class="stk" style="width:{size}px;height:{size}px"><div style="width:100%;height:100%;border:8px solid #fff;border-radius:34px;background:url({d}) center/cover;box-shadow:6px 6px 0 {PINK},0 12px 24px rgba(0,0,0,.25);transform:rotate(-4deg)"></div></div>'
    return f'<div class="stk" style="width:{size}px;height:{size}px">{bear(mood)}</div>'

def hi(s, k): return s.replace(k, f'<span class="mk">{k}</span>')

def exp(n, title, en, mg, example, key, quip, mood, stick, q, em):
    fs = 128 if len(title) < 12 else 108
    return f"""<div class="row"><div style="display:flex;align-items:center;gap:16px"><div class="num">{n}</div><div class="chip2">OF 6 MEANINGS</div></div>{E(stick,92,'fl')}</div>
<div class="ttl" style="font-size:{fs}px">{title}</div>
<div class="eng">{en}</div><div class="mgl">{mg}</div>
<div class="chat"><div class="chh"><i></i>bear_buddy · online</div>
<div class="m"><div class="av">{E('1f60e',60)}</div><div class="b1">{hi(example, key)}</div></div>
<div class="m r"><div class="b2">{quip}</div><div class="av">{head(mood)}</div></div></div>
<div class="row" style="align-items:flex-end;gap:20px">{stk(mood, 250)}<div class="qc"><small>YOUR TURN</small><div>{q}</div><div style="margin-top:8px;display:flex;gap:10px">{E(em[0],46)}{E(em[1],46)}{E(em[2],46)}</div></div></div>"""

def cover():
    return f"""<div class="row"><div class="chip3">DOMAIN · CRAFT AND STRUCTURE</div>{E('1f92f',92,'fl')}</div>
<div style="font-family:LL,RB,sans-serif;font-weight:900;font-size:54px;letter-spacing:-1px;color:{INK}"><span style="color:{PINK}">SAT</span>&reg; Reading &amp; Writing</div>
<div style="font-size:38px;font-weight:900;color:{PINK};font-style:italic;line-height:1.25">POV: you think BEAR is just an animal 🐻</div>
<div class="ttl" style="font-size:270px;transform:rotate(-2deg);text-shadow:8px 8px 0 {YEL},16px 16px 0 {PINK};margin:4px 0 14px">BEAR</div>
<div class="row" style="align-items:center;gap:20px">{stk('sun', 350)}
 <div style="flex:1;display:flex;flex-direction:column;gap:18px;align-items:flex-start">
  <div class="sk" style="background:{YEL};font-size:50px;transform:rotate(4deg);box-shadow:5px 5px 0 {PINK}">6 MEANINGS 🤯</div>
  <div class="sk" style="background:{CYAN};font-size:30px;transform:rotate(-3deg);box-shadow:5px 5px 0 {PINK}">SKILL · Words in Context</div>
  <div class="mgl" style="font-size:29px;transform:rotate(2deg)">Баавгай биш! Нэг үг, 6 өөр утга</div></div></div>
<div class="rx2" style="align-self:flex-start">Swipe to level up →</div>"""

def quiz():
    o = ''.join(f'<div class="opt"><i>{a}</i><span>{b}</span></div>' for a, b in [('A', 'carry something heavy'), ('B', 'show that it is true'), ('C', 'put up with something bad')])
    return f"""<div class="row"><div class="chip3">QUIZ · POLL TIME</div>{E('1f914',92,'fl')}</div>
<div class="ttl" style="font-size:66px">What does <span style="color:{PINK}">“bear out”</span> mean here?</div>
<div class="chat" style="padding:16px 22px"><div class="m"><div class="av">{E('1f60e',60)}</div><div class="b1" style="font-size:32px">The latest experiments {hi('bear out','bear out')} the scientist’s hypothesis.</div></div></div>
{o}
<div class="row" style="align-items:flex-end;gap:14px">{stk('think', 160)}<div class="b2" style="margin-bottom:20px;font-size:29px">Careful! It is not about honey. 🍯</div></div>
<div class="rx2">{E('1f447',44)}<span>Comment A, B or C below!</span></div>
<div class="note">Original Global Math Prep practice question. Not from the College Board.</div>"""

def tip():
    cells = [('CARRY', 'bear the cost', 'The school bears the cost.', 'хариуцах', PINK),
             ('ENDURE', 'can’t bear', 'I can’t bear the noise.', 'тэвчих', CYAN),
             ('PRODUCE', 'bear fruit', 'Her work bore fruit.', 'үр дүнгээ өгөх', LIME),
             ('CONFIRM', 'bear out', 'The data bear out his idea.', 'баталж өгөх', YEL)]
    g = ''.join(f'<div class="c" style="background:{c}"><b>{a}</b><u>{b}</u><i>{x}</i><em>{d}</em></div>' for a, b, x, d, c in cells)
    return f"""<div class="row"><div class="chip3">QUIZ ANSWER + SAT TRICK</div>{E('1f389',86,'fl')}</div>
<div class="ban">Answer: B 🎯 “Bear out” means show that it is true. Did you get it?</div>
<div class="ttl" style="font-size:60px">BEAR has <span style="color:{PINK}">4 hidden jobs</span></div>
<div class="g4">{g}</div>
<div style="display:flex;gap:20px;align-items:stretch">
 <div class="su" style="text-align:center;padding:12px"><img src="{gen29.QR}" style="width:190px;height:190px;display:block"><div style="font-weight:800;font-size:21px;margin-top:4px">Scan to sign up</div></div>
 <div class="su" style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:8px;font-size:26px;font-weight:700">
  <div class="in" style="font-size:36px">Comment “SAT” below</div>
  <div><span style="color:{PINK};font-weight:900">English</span> · Tue · Thu · Sat · 20:00 to 21:20</div><div><span style="color:{PINK};font-weight:900">Math</span> · Mon · Wed · Fri · 20:00 to 21:20</div><div style="color:#556">Ulaanbaatar, Mongolia time</div><div style="color:#556;white-space:nowrap">WhatsApp +1 428 880 1826</div></div></div>"""

def build():
    P = [cover(),
      exp(1, 'BEAR IN MIND', 'To remember something and think about it.', 'Санаж явах, анхаарах', 'Bear in mind that the shop closes at six.', 'Bear in mind', 'Bear in mind: the honey is MINE.', 'think', '1f4a1', 'Did you know this one? Comment <b>YES</b> or <b>NO</b>', ('1f525', '1f92f', '1f4af')),
      exp(2, 'BEAR FRUIT', 'To give good results after hard work.', 'Үр дүнгээ өгөх', 'Years of study finally bore fruit.', 'bore fruit', 'My tree bore fruit! Apples. Not honey.', 'fruit', '1f4aa', 'Name a goal that will <b>bear fruit</b> for you 👇', ('1f4aa', '1f525', '1f3af')),
      exp(3, 'BEAR WITH ME', 'Be patient with me for a short time.', 'Жаахан хүлээгээрэй', 'Please bear with me while I find the file.', 'bear with me', 'Bear with me… I am still thinking.', 'please', '1f605', 'Who says this the most? <b>Tag a friend</b>', ('1f605', '1f64c', '1f525')),
      exp(4, 'BEAR THE COST', 'To pay for something or take the responsibility.', 'Зардлыг хариуцах', 'The school will bear the cost of the trip.', 'bear the cost', 'Who bears the cost of my honey? You.', 'cost', '1f631', 'Who <b>bears the cost</b> at your home?', ('1f631', '1f4af', '1f525')),
      exp(5, 'CAN’T BEAR', 'To be unable to stand something.', 'Тэвчиж чадахгүй', 'I can’t bear the noise in this room.', 'can’t bear', 'I can’t bear it! Too loud!', 'ears', '1f62e', 'What can you <b>not bear</b>? Comment it 👇', ('1f62e', '1f92f', '1f525')),
      exp(6, 'BEAR OUT', 'To show that something is true.', 'Зөв гэдгийг нотлох', 'The new data bear out her theory.', 'bear out', 'The data bear out my theory: honey wins.', 'out', '1f913', '<b>Save</b> this post for your SAT revision', ('1f913', '1f4af', '1f3c6')),
      quiz(), tip()]
    return dict(key='BearLight', prefix='GMP-SATWords-Light', AC=PINK, SOFT='#fff1cf', TINT='#fff8ea', nxt='New', pages=P, foot='WORDS IN CONTEXT · BEAR')

if __name__ == '__main__':
    post = build()
    gen30.render(post, '--video' in sys.argv)
    out = HERE / 'out30-BearLight'
    for f in sorted(out.glob('GMP-Transitions-*')):
        f.rename(out / f.name.replace('GMP-Transitions-BearLight', 'GMP-SATWords-Light'))
