import subprocess, shutil
import cine, gen24, gen15 as g15
from gen18 import E, HERE
from playwright.sync_api import sync_playwright
BLUE = '#324dc7'; INK = '#1e1e1e'; SOFT = '#e8ecfb'; GREEN = '#15803d'; RED = '#c62828'
LOGO = 'data:image/png;base64,' + g15.b64(HERE / 'hdr_logo_dark.png')
QR = g15.QR
BB = gen24.C[gen24.C.index('.bx{'):].replace('box-shadow:7px 7px 0 #16121f', 'box-shadow:0 10px 30px rgba(30,40,90,.18)').replace('border:3px solid #16121f', 'border:2px solid #1e1e1e')
CSS = cine.ff + f"""
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;font-family:M,sans-serif;color:{INK};background:#fff}}
.pg{{position:relative;width:1080px;height:1350px;overflow:hidden;background:#fff}}
.pg:before{{content:'';position:absolute;left:0;right:0;top:0;height:10px;background:{BLUE}}}
.top{{position:absolute;top:44px;left:56px;right:56px;display:flex;justify-content:space-between;align-items:center;z-index:3}}
.top img{{height:58px}} .top span{{font-weight:800;font-size:22px;color:{BLUE};letter-spacing:2px}}
.ft{{position:absolute;bottom:40px;left:56px;right:56px;display:flex;justify-content:space-between;font-weight:700;font-size:22px;color:#667;z-index:3;border-top:2px dashed #c9cde0;padding-top:16px}}
.mn{{position:absolute;top:140px;bottom:104px;left:56px;right:56px;display:flex;flex-direction:column;justify-content:center;gap:26px;z-index:2}}
.mn>*{{flex-shrink:0}}
.pill{{display:inline-block;align-self:flex-start;background:{BLUE};color:#fff;border-radius:30px;padding:9px 22px;font-weight:800;font-size:23px;letter-spacing:1.5px}}
.in{{font-family:IN,M,sans-serif;font-weight:900;letter-spacing:-2px;line-height:1}}
.blue{{color:{BLUE}}}
.card{{background:#fff;border:2px solid #d6daea;border-radius:22px;padding:22px 26px;box-shadow:0 6px 18px rgba(30,40,90,.08)}}
.lead{{font-size:34px;font-weight:700;line-height:1.35}}
.map{{display:flex;align-items:stretch;gap:12px}}
.map .n{{flex:1;background:{SOFT};border-radius:18px;padding:16px 16px;font-size:25px;font-weight:700;line-height:1.3}}
.map .n small{{display:block;font-size:19px;font-weight:800;color:{BLUE};letter-spacing:1px;margin-bottom:4px}}
.map .n.hot{{background:{BLUE};color:#fff}} .map .n.hot small{{color:#c9d3ff}}
.map .ar{{display:flex;align-items:center;font-size:40px;font-weight:900;color:{BLUE}}}
.okrow{{display:flex;align-items:center;gap:20px}}
.ok{{flex:none;background:{GREEN};color:#fff;border-radius:18px;padding:12px 22px;font-family:S,serif;font-size:40px;font-weight:700}}
.test{{font-size:29px;font-weight:700;line-height:1.35}} .test i{{font-family:S,serif;font-weight:600}} .test b{{color:{GREEN}}}
.wr{{display:flex;gap:16px;align-items:flex-start;padding:12px 0;border-top:2px dashed #e0e3ef;font-size:26px;font-weight:600;line-height:1.3}}
.wr:first-child{{border-top:0}}
.wr .w{{flex:none;width:250px;font-family:S,serif;font-size:29px;color:{RED};text-decoration:line-through;text-decoration-thickness:2px}}
.tip{{background:#fff7e0;border:2px solid #f2c94c;border-radius:20px;padding:16px 22px;font-size:26px;font-weight:700;line-height:1.35;display:flex;gap:14px;align-items:center}}
@keyframes up{{0%{{opacity:0;transform:translateY(30px)}}100%{{opacity:1;transform:none}}}}
@keyframes fl{{0%,100%{{transform:translateY(0) rotate(-6deg)}}50%{{transform:translateY(-18px) rotate(6deg)}}}}
@keyframes pop{{0%{{transform:scale(.6);opacity:0}}70%{{transform:scale(1.1);opacity:1}}100%{{transform:scale(1)}}}}
.fl{{animation:fl 3s ease-in-out infinite}}
.mn>*{{animation:up .55s ease-out both}}
.mn>*:nth-child(2){{animation-delay:.15s}} .mn>*:nth-child(3){{animation-delay:.3s}} .mn>*:nth-child(4){{animation-delay:.45s}} .mn>*:nth-child(5){{animation-delay:.6s}} .mn>*:nth-child(6){{animation-delay:.75s}}
.ok{{animation:pop .6s .9s both}}
""" + BB + """
.rwp{font-family:S,serif;font-size:28px;line-height:1.45;margin-top:12px}
.rwq{font-family:S,serif;font-size:29px;margin-top:14px;font-weight:600}
.bxc{gap:9px!important;margin-top:14px!important}
.bxc div{padding:7px 16px!important;font-size:27px!important}
.qrow{padding:6px 34px!important}
"""

def page(n, T, body):
    return f'''<!doctype html><html lang="mn"><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="pg">
<div class="top"><img src="{LOGO}"><span>{n:02d} / {T:02d}</span></div>
<div class="mn">{body}</div>
<div class="ft"><span>SAT R&amp;W · ШИЛЖИЛТ ҮГ</span><span>{"Гүйлгээд үз →" if n < T else "@globalmathprep"}</span></div></div></body></html>'''

def rw(qnum, passage, choices):
    ch = ''.join(f'<div><span class="l">{l}</span><span>{c}</span></div>' for l, c in zip('ABCD', choices))
    return f'''<div class="bx"><div class="bxh"><div><div class="s1">Section 1, Module 1: Reading and Writing</div><div class="s2">Directions &#8964;</div></div>
<div class="tm">24:10<br><span class="hide">Hide</span></div><div class="tl"><div>{gen24.IMORE}<br>More</div></div></div><div class="dash"></div>
<div class="bxb"><div class="qrow"><div class="n">{qnum}</div>{gen24.BOOK}<span class="mr">Mark for Review</span><span class="abc">ABC</span></div>
<div class="rwp">{passage}</div><div class="rwq">Which choice completes the text with the most logical transition?</div><div class="bxc">{ch}</div></div>
<div class="dash"></div><div class="bxf"><span>Global Math Prep</span><span class="qx">Question {qnum} of 27 &#8963;</span><div class="bt"><span>Back</span><span>Next</span></div></div></div>'''

def qslide(k, typ_hint, qnum, passage, choices, emo):
    return f'''<div style="display:flex;justify-content:space-between;align-items:center"><div class="pill">АСУУЛТ {k}/4 · ЭХЛЭЭД ӨӨРӨӨ БОД</div>{E(emo,90,"fl")}</div>
{rw(qnum, passage, choices)}
<div class="tip">{E("1f4a1",44)}<div>Сонголтоо харахаас өмнө: 2 өгүүлбэр хоорондоо ямар холбоотой вэ?</div></div>'''

def aslide(k, rel, rel_sub, mapn, ok, test, wrong, tip, emo):
    m = ''.join((f'<div class="ar">→</div>' if i else '') + f'<div class="n{" hot" if i == len(mapn) - 1 else ""}"><small>{a}</small>{b}</div>' for i, (a, b) in enumerate(mapn))
    w = ''.join(f'<div class="wr"><span class="w">{a}</span><span>{b}</span></div>' for a, b in wrong)
    return f'''<div style="display:flex;justify-content:space-between;align-items:center"><div><div class="pill">ХАРИУ {k}/4</div>
<div class="in" style="font-size:84px;margin-top:16px">{rel}</div><div class="lead" style="margin-top:8px">{rel_sub}</div></div>{E(emo,120,"fl")}</div>
<div class="map">{m}</div>
<div class="card okrow"><div class="ok">{ok}</div><div class="test">{test}</div></div>
<div class="card" style="padding:8px 26px">{w}</div>
<div class="tip">{E("1f914",44)}<div>{tip}</div></div>'''

P = []
P.append(f'''<div class="pill">SAT READING &amp; WRITING</div>
<div class="in" style="font-size:118px;margin-top:6px">Сонголтоо<br>харахаасаа<br><span class="blue">өмнө</span> тааж сур</div>
<div class="lead">SAT-ын шилжилт үгийн асуултыг <b>3 алхмаар</b> бод.</div>
<div style="display:flex;gap:12px;flex-wrap:wrap">{''.join(f'<span class="card" style="padding:10px 18px;font-size:24px;font-weight:800">{E(e,34)} {t}</span>' for e, t in [('2795','Нэмэх'),('1f50d','Тодорхойлох'),('23f3','Цаг хугацаа'),('27a1','Үр дагавар')])}</div>
<div class="tip">{E("1f447",44)}<div>4 дасгал асуулт · эхлээд өөрөө бодоод, дараа нь хариугаа шалга</div></div>''')

steps = [('1', 'Шилжилт үгийг хаа', 'Хоосон зайг алгасаад 2 өгүүлбэрийг уншина'), ('2', 'Холбоог нэрлэ', 'Нэмэх үү? Жишээ юу? Дараа нь уу? Тиймээс үү? Гэхдээ юу?'), ('3', 'Дараа нь л сонголтоо хар', 'Тэр төрлийн цорын ганц үгийг сонго')]
sh = ''.join(f'<div class="card" style="display:flex;gap:20px;align-items:center;padding:18px 24px"><div style="flex:none;width:60px;height:60px;border-radius:50%;background:{BLUE};color:#fff;display:flex;align-items:center;justify-content:center;font-size:30px;font-weight:900">{a}</div><div><div style="font-size:33px;font-weight:800">{b}</div><div style="font-size:25px;font-weight:600;color:#556;margin-top:4px">{c}</div></div></div>' for a, b, c in steps)
tbl = ''.join(f'<div style="display:flex;justify-content:space-between;padding:10px 0;border-top:2px dashed #e0e3ef;font-size:27px;font-weight:700"><span>{E(e,34)} {a}</span><span style="font-family:S,serif;font-style:italic;color:{BLUE}">“…{b}…”</span></div>' for e, a, b in [('2795', 'Нэмэх', 'and also'), ('1f50d', 'Тодорхойлох', 'for example'), ('23f3', 'Цаг хугацаа', 'later'), ('27a1', 'Үр дагавар', 'so'), ('274c', 'Эсрэг', 'but')])
P.append(f'''<div class="pill">АРГА</div><div class="in" style="font-size:80px">3 алхам</div>{sh}
<div class="card" style="padding:14px 26px"><div style="font-size:23px;font-weight:800;color:{BLUE};letter-spacing:1px">ТЕСТ: ХООСОН ЗАЙД ЭНГИЙН ҮГ ХЭЛЖ ҮЗ</div>{tbl}</div>''')

q = [
 dict(qnum=9, emo='1f3a8', choices=['Moreover,', 'Thus,', 'Meanwhile,', 'Nevertheless,'],
  passage='Although the abstract painter Joan Mitchell disliked being compared to Monet, the parallels between them were undeniable. Her terrace overlooked a house that Monet occupied from 1878 to 1881, as well as a landscape that he painted. ______ some of her own late works unmistakably hark back to the paintings that Monet produced in his twilight years at Giverny.',
  rel='Нэмэх', sub='2 дахь нотолгоо нэмж байна', mapn=[('S1', 'Monet-той адил байсан'), ('S2', 'Нотолгоо 1: ижил газар'), ('S3', 'Нотолгоо 2: ижил зураг')],
  ok='A) Moreover,', test='Тест: “Monet-ийн байшин харагддаг байсан, <i>and also</i> зураг нь ч адил” → <b>✓ таарч байна</b>',
  wrong=[('B) Thus,', 'Байшин харагддаг байсан нь зургийн хэв маягийн шалтгаан биш'), ('C) Meanwhile,', 'Эсрэгцэл, зэрэгцэл алга'), ('D) Nevertheless,', 'Эсрэг санаа алга')],
  tip='<b>Урхи:</b> “Although… disliked” нь эсрэг мэт харагдана. Гэхдээ тэр эсрэгцэл 1-р өгүүлбэр дотроо дууссан.', aemo='2795'),
 dict(qnum=1, emo='1f58c', choices=['Moreover,', 'Specifically,', 'Nevertheless,', 'Besides,'],
  passage='Rather than embrace the type of abstract work that many artists of her generation preferred, Gwendolyn Knight preferred to depict figures in a spontaneous and personal manner. ______ she painted oil portraits of friends as well as studies of dancers in motion.',
  rel='Тодорхойлох', sub='Ерөнхий санааг жишээгээр батлах', mapn=[('S1', 'Хүмүүсийг өөрийнхөөрөө зурдаг'), ('S2', 'Жишээ нь: найзуудын хөрөг, бүжигчид')],
  ok='B) Specifically,', test='Тест: “хүмүүсийг зурдаг, <i>for example</i> найзуудаа, бүжигчдийг” → <b>✓ таарч байна</b>',
  wrong=[('A) Moreover,', '“Нэмэх” үг. D-тэй ижил үүрэгтэй тул хоёулаа хасагдана'), ('D) Besides,', 'A-тай ижил үүрэгтэй'), ('C) Nevertheless,', 'Эсрэг биш, жишээ')],
  tip='<b>Товчлол:</b> 2 сонголт ижил үүрэгтэй бол хоёулаа буруу. Зөв хариу ганцхан байдаг!', aemo='1f50d'),
 dict(qnum=3, emo='2604', choices=['Therefore,', 'Meanwhile,', 'Subsequently,', 'Additionally,'],
  passage='While doing fieldwork on Gorgonilla Island in Colombia in 2014, Hermann Bermúdez found spherule deposits—layers of sediment filled with tiny glass beads. These beads formed when the heat and pressure from an asteroid impact melted and scattered the crust of the Earth, ejecting tiny liquid blobs into the atmosphere. ______ they fell back to earth in solid form under the influence of gravity.',
  rel='Цаг хугацаа', sub='Үйл явцын дараагийн алхам', mapn=[('①', 'Астероид мөргөв'), ('②', 'Шингэн дусал агаарт цацагдав'), ('③', 'Дараа нь хатуураад унав')],
  ok='C) Subsequently,', test='Тест: “агаарт цацагдсан, <i>later</i> газарт унасан” → <b>✓ таарч байна</b>',
  wrong=[('A) Therefore,', 'Логик дүгнэлт биш, дараагийн алхам'), ('B) Meanwhile,', '“Тэр үед зэрэг” гэсэн утгатай. Унасан нь дараа нь болсон'), ('D) Additionally,', 'Шинэ баримт нэмээгүй, үйл явц үргэлжилж байна')],
  tip='<b>Сонирхолтой нь:</b> эдгээр шилэн сувс үлэг гүрвэлийг устгасан астероидоос үүссэн!', aemo='23f3'),
 dict(qnum=4, emo='1f40b', choices=['Consequently,', 'For instance,', 'Furthermore,', 'Alternatively,'],
  passage='Blue whales recognize when the wind is changing their habitat and identify places where ocean currents produce large aggregations of krill. The tiny shrimp are the primary food sources for the massive animals, which can weigh 165 tons or more. ______ their ability to locate these dense concentrations of nutrients is a matter of survival.',
  rel='Үр дагавар', sub='Өмнөх баримтаас гарах дүгнэлт', mapn=[('S2', '165 тонн жинтэй мөртлөө жижигхэн криль иддэг'), ('S3', 'Тиймээс криль олох = амьд үлдэх')],
  ok='A) Consequently,', test='Тест: “165 тонн, криль иддэг, <i>so</i> криль олох нь амьдралын асуудал” → <b>✓ таарч байна</b>',
  wrong=[('B) For instance,', 'Жишээ биш, дүгнэлт'), ('C) Furthermore,', 'Тусдаа баримт биш, өмнөхөөсөө гарч байна'), ('D) Alternatively,', 'Өөр сонголт санал болгоогүй')],
  tip='<b>Нэг зүйл, 3 нэр:</b> krill → the tiny shrimp → these dense concentrations of nutrients. SAT нэрийг сольж шалгадаг!', aemo='27a1'),
]
for k, d in enumerate(q, 1):
    P.append(qslide(k, d['rel'], d['qnum'], d['passage'], d['choices'], d['emo']))
    P.append(aslide(k, d['rel'], d['sub'], d['mapn'], d['ok'], d['test'], d['wrong'], d['tip'], d['aemo']))

fam = [('2795', 'Нэмэх', 'moreover · furthermore · in addition · likewise', '“and also”'), ('1f50d', 'Тодорхойлох', 'specifically · for example · for instance · in particular', '“for example”'),
       ('23f3', 'Цаг хугацаа', 'subsequently · then · afterward · meanwhile*', '“later”'), ('27a1', 'Үр дагавар', 'consequently · therefore · thus · hence', '“so”'), ('274c', 'Эсрэг', 'however · still · nevertheless · in contrast', '“but”')]
fr = ''.join(f'<div style="display:flex;gap:16px;align-items:center;padding:14px 0;{"border-top:2px dashed #e0e3ef;" if i else ""}">{E(e,46)}<div style="flex:1"><div style="display:flex;justify-content:space-between;font-size:30px;font-weight:800"><span>{a}</span><span style="font-family:S,serif;font-style:italic;color:{BLUE};font-weight:600">{t}</span></div><div style="font-size:25px;font-weight:600;color:#445;margin-top:4px">{b}</div></div></div>' for i, (e, a, b, t) in enumerate(fam))
P.append(f'''<div class="pill">ХАДГАЛАХ ХУУДАС</div><div class="in" style="font-size:84px">4 төрөл + Эсрэг,<br><span class="blue">5 тест үг</span></div>
<div class="card" style="padding:8px 26px">{fr}</div><div style="font-size:21px;font-weight:600;color:#667">*meanwhile нь “тэр үед” эсвэл эсрэгцэл илэрхийлж болно</div>''')

P.append(f'''<div class="pill">ТӨГСГӨЛ</div>
<div style="text-align:center"><div class="in" style="font-size:60px">Ийм дасгал дахиад авах бол</div>
<div class="in blue" style="font-size:200px;margin:10px 0">SAT</div><div class="in" style="font-size:56px">гэж комментод бичээрэй</div></div>
<div style="display:flex;gap:20px;align-items:stretch">
 <div class="card" style="text-align:center;padding:14px"><img src="{QR}" style="width:230px;height:230px;display:block"><div style="font-weight:800;font-size:22px;margin-top:4px">Скан хийж бүртгүүл</div></div>
 <div class="card" style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:12px;font-size:27px;font-weight:700">
  <div><span class="blue">Англи</span> · Мя · Пү · Бя · 20:00–21:20</div><div><span class="blue">Math</span> · Да · Лх · Ба · 20:00–21:20</div><div style="color:#556">WhatsApp +1 428 880 1826</div></div></div>''')

def render(out, prefix, video=False):
    out.mkdir(exist_ok=True)
    for f in out.glob('*'): f.unlink()
    T = len(P)
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page(viewport={'width': 1080, 'height': 1350})
        for i, body in enumerate(P, 1):
            pg.set_content(page(i, T, body)); pg.wait_for_timeout(400)
            pg.evaluate("()=>document.getAnimations().forEach(a=>{a.pause();a.currentTime=2500})")
            ov = pg.evaluate("()=>{const m=document.querySelector('.mn');let t=1e9,b=0;for(const c of m.children){const r=c.getBoundingClientRect();t=Math.min(t,r.top);b=Math.max(b,r.bottom)}return [Math.round(t),Math.round(b)]}")
            fn = out / f'{prefix}-{i:02d}-of-{T:02d}.png'; pg.screenshot(path=str(fn))
            print(fn.name, ov, 'OK' if ov[0] >= 130 and ov[1] <= 1240 else 'OVERFLOW')
            if video:
                fr = out / '_f'; fr.mkdir(exist_ok=True)
                for k in range(150):
                    pg.evaluate(f"()=>document.getAnimations().forEach(a=>{{a.pause();a.currentTime={k*1000/30}}})"); pg.screenshot(path=str(fr / f'{k:04d}.png'))
                subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', '30', '-i', str(fr / '%04d.png'), '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '19', '-movflags', '+faststart', str(fn.with_suffix('.mp4'))], check=True)
                shutil.rmtree(fr)
        br.close()

if __name__ == '__main__':
    import sys
    render(HERE / 'out29', 'GMP-SAT-Transitions-4-Types', '--video' in sys.argv)
