import subprocess, shutil
import cine, gen24, gen15 as g15
from gen18 import E, HERE
from playwright.sync_api import sync_playwright
LIME = '#c6f432'; BLK = '#0c0d0f'; CARD = '#17191d'; LINE = '#2a2d33'
QR = g15.QR; LOGO = g15.LOGO
C = cine.ff + gen24.C.split('*{{')[0] if False else ''
BB = gen24.C[gen24.C.index('.bx{'):]  # bluebook styles
CSS = cine.ff + f"""
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;font-family:M,sans-serif;color:#fff;background:{BLK}}}
.pg{{position:relative;width:1080px;height:1350px;overflow:hidden;background:radial-gradient(ellipse 70% 40% at 85% 0%,rgba(198,244,50,.13),transparent 70%),{BLK}}}
.top{{position:absolute;top:50px;left:60px;right:60px;display:flex;justify-content:space-between;align-items:center;font-weight:700;font-size:22px;letter-spacing:4px;z-index:3;opacity:.85}}
.top img{{height:58px}}
.ft{{position:absolute;bottom:44px;left:60px;right:60px;display:flex;justify-content:space-between;font-weight:700;font-size:22px;opacity:.7;z-index:3}}
.mn{{position:absolute;top:140px;bottom:100px;left:60px;right:60px;display:flex;flex-direction:column;justify-content:center;gap:28px;z-index:2}}
.mn>*{{flex-shrink:0}}
.pf{{font-family:PF,serif;font-style:italic;font-weight:900;letter-spacing:-3px;line-height:.9}}
.in{{font-family:IN,M,sans-serif;font-weight:900;letter-spacing:-2px;line-height:.95}}
.lime{{color:{LIME}}}
.chip{{display:inline-block;background:{LIME};color:#111;padding:2px 16px;border-radius:4px}}
.pill{{align-self:flex-start;border:2px solid {LIME};color:{LIME};border-radius:30px;padding:8px 20px;font-weight:800;font-size:22px;letter-spacing:2px}}
.card{{background:{CARD};border:2px solid {LINE};border-radius:24px;padding:24px 28px}}
.sent{{font-family:S,serif;font-size:42px;line-height:1.45}}
.sent b{{font-family:M;font-weight:800;color:#111;background:{LIME};padding:0 8px;border-radius:6px}}
.lead{{font-size:40px;font-weight:700;line-height:1.35}}
.bar{{background:{LIME};color:#111;border-radius:22px;padding:20px 26px;font-size:29px;font-weight:800;line-height:1.3;display:flex;gap:16px;align-items:center}}
.x{{display:flex;align-items:center;gap:18px;padding:20px 0;border-top:2px solid {LINE};font-size:31px;font-weight:600;line-height:1.3}}
.x:first-child{{border-top:0}}
.x .w{{flex:none;min-width:290px;font-weight:800;font-size:33px}}
.x .no{{color:#ff6b6b;font-weight:800}}
@keyframes up{{0%{{opacity:0;transform:translateY(34px)}}100%{{opacity:1;transform:none}}}}
@keyframes fl{{0%,100%{{transform:translateY(0) rotate(-6deg)}}50%{{transform:translateY(-20px) rotate(6deg)}}}}
@keyframes pulse{{0%,100%{{transform:scale(1)}}50%{{transform:scale(1.06)}}}}
.fl{{animation:fl 3s ease-in-out infinite}} .pulse{{animation:pulse 2s ease-in-out infinite}}
.mn>*{{animation:up .6s ease-out both}}
.mn>*:nth-child(2){{animation-delay:.15s}} .mn>*:nth-child(3){{animation-delay:.3s}} .mn>*:nth-child(4){{animation-delay:.45s}} .mn>*:nth-child(5){{animation-delay:.6s}} .mn>*:nth-child(6){{animation-delay:.75s}}
""" + BB.replace('box-shadow:7px 7px 0 #16121f', f'box-shadow:0 0 0 4px {LIME}') + """
.rwp{font-family:S,serif;font-size:34px;line-height:1.5;margin-top:18px}
.rwq{font-family:S,serif;font-size:30px;margin-top:16px;font-weight:600}
"""

def page(n, total, body, label):
    return f'''<!doctype html><html lang="mn"><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="pg">
<div class="top"><img src="{LOGO}"><span>{n:02d} / {total:02d}</span></div>
<div class="mn">{body}</div>
<div class="ft"><span>{label}</span><span>{"Гүйлгээд үз →" if n < total else "@globalmathprep"}</span></div></div></body></html>'''

def rw(qnum, passage, choices):
    ch = ''.join(f'<div><span class="l">{l}</span><span>{c}</span></div>' for l, c in zip('ABCD', choices))
    return f'''<div class="bx"><div class="bxh"><div><div class="s1">Section 1, Module 1: Reading and Writing</div><div class="s2">Directions &#8964;</div></div>
<div class="tm">24:10<br><span class="hide">Hide</span></div><div class="tl"><div>{gen24.IMORE}<br>More</div></div></div><div class="dash"></div>
<div class="bxb"><div class="qrow"><div class="n">{qnum}</div>{gen24.BOOK}<span class="mr">Mark for Review</span><span class="abc">ABC</span></div>
<div class="rwp">{passage}</div><div class="rwq">Which choice completes the text with the most logical transition?</div><div class="bxc">{ch}</div></div>
<div class="dash"></div><div class="bxf"><span>Global Math Prep</span><span class="qx">Question {qnum} of 27 &#8963;</span><div class="bt"><span>Back</span><span>Next</span></div></div></div>'''

P = []
P.append(f'''<div class="pill">SAT ENGLISH · ШИЛЖИЛТ ҮГ</div>
<div style="text-align:center;margin-top:10px"><div class="in" style="font-size:170px">However</div>
<div class="in lime pulse" style="font-size:150px;line-height:1">≠</div>
<div class="pf lime" style="font-size:190px">in contrast</div></div>
<div class="lead" style="text-align:center">SAT-д хамгийн их андуурдаг <span class="chip">2 шилжилт үг</span></div>
<div style="text-align:center;font-size:26px;font-weight:700;opacity:.8">2 дүрэм · 5 секундын тест · 2 дасгал</div>''')

P.append(f'''<div class="pill">ДҮРЭМ 1</div>
<div><div class="pf lime" style="font-size:150px">In contrast</div><div class="lead" style="margin-top:16px">= <b>2 ӨӨР</b> зүйлийг хажуу хажууд нь тавьж харьцуулна</div></div>
<div style="display:flex;align-items:stretch;gap:18px">
 <div class="card" style="flex:1;text-align:center">{E("1f981",150)}<div style="font-size:40px;font-weight:800;margin-top:8px">Lions</div><div style="font-size:30px;opacity:.8">сүргээрээ амьдарна</div></div>
 <div style="display:flex;align-items:center;font-size:60px;font-weight:900;color:{LIME}">↔</div>
 <div class="card" style="flex:1;text-align:center">{E("1f42f",150)}<div style="font-size:40px;font-weight:800;margin-top:8px">Tigers</div><div style="font-size:30px;opacity:.8">ганцаараа амьдарна</div></div></div>
<div class="card sent">Lions live in groups. Tigers, <b>in contrast</b>, live alone.</div>''')

P.append(f'''<div class="pill">ДҮРЭМ 2</div>
<div><div class="in" style="font-size:130px">However<span class="lime"> · </span>Still</div><div class="lead" style="margin-top:16px">= <b>НЭГ</b> сэдэв, гэтэл хоёр дахь санаа эхнийхээ <span class="lime">эсрэг</span> гарна</div></div>
<div style="display:flex;align-items:stretch;gap:14px">
 <div class="card" style="flex:1;text-align:center">{E("1f50d",130)}<div style="font-size:34px;font-weight:800;margin-top:8px">Нарийн судлах хэрэгтэй</div></div>
 <div style="display:flex;align-items:center">{E("1f6a7",110)}</div>
 <div class="card" style="flex:1;text-align:center">{E("1f4c9",130)}<div style="font-size:34px;font-weight:800;margin-top:8px">Гэтэл мэдээлэл хомс</div></div></div>
<div class="card sent">Scientists must study the species. Information is scarce, <b>however</b>.</div>''')

P.append(f'''<div class="pill">5 СЕКУНДЫН ТЕСТ</div>
<div class="in" style="font-size:88px">Хоёр <span class="lime">өөр</span> зүйлийг<br>нэрлэж чадах уу?</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px">
 <div class="card" style="border-color:{LIME}"><div style="font-size:30px;font-weight:800;color:{LIME}">ТИЙМ ✓</div><div style="font-size:26px;opacity:.85;margin-top:6px">арслан ба бар · хот ба хөдөө</div><div class="pf" style="font-size:72px;margin-top:14px">in contrast</div></div>
 <div class="card"><div style="font-size:30px;font-weight:800;color:#ff8f6b">ҮГҮЙ, “гэтэл…” ✗</div><div style="font-size:26px;opacity:.85;margin-top:6px">нэг сэдэв · саад · сул тал</div><div class="in" style="font-size:66px;margin-top:14px">however<br>still</div></div></div>
<div class="bar">{E("1f4a1",50)}<div>Одоо SAT маягийн 2 асуулт дээр туршаад үз 👉</div></div>'''.replace(' 👉', ''))

q1 = 'In order to save an endangered species, preservationists must study it in detail. Scientific information about some endangered animals is scarce, ______.'
P.append(f'''<div class="pill">АСУУЛТ 1 · ЭХЛЭЭД ӨӨРӨӨ БОД</div>{rw(4, q1, ["therefore", "moreover", "in contrast", "however"])}''')
P.append(f'''<div class="pill">ХАРИУ 1</div>
<div style="display:flex;align-items:center;gap:22px"><div class="chip in" style="font-size:80px;padding:6px 22px">D</div><div class="in" style="font-size:96px">however</div></div>
<div class="lead">Хоёр өөр амьтан биш. <b>Нэг</b> нөхцөл: судлах хэрэгтэй, <span class="lime">гэтэл</span> мэдээлэл хомс.</div>
<div class="card" style="padding:10px 28px"><div class="x"><span class="w">A) therefore</span><span><span class="no">✗</span> Хомс байгаа нь судлах хэрэгцээний үр дүн биш</span></div>
<div class="x"><span class="w">B) moreover</span><span><span class="no">✗</span> Ижил санаа нэмэхгүй, саад гаргаж байна</span></div>
<div class="x"><span class="w">C) in contrast</span><span><span class="no">✗</span> Хоёр өөр зүйлийг харьцуулаагүй</span></div></div>''')

q2 = 'Modern chemistry keeps insects from ravaging crops, removes stains, and saves lives. ______ constant exposure to chemicals is taking a toll on many people’s health.'
P.append(f'''<div class="pill">АСУУЛТ 2 · ЭХЛЭЭД ӨӨРӨӨ БОД</div>{rw(6, q2, ["Hence,", "In contrast,", "Still,", "Subsequently,"])}''')
P.append(f'''<div class="pill">ХАРИУ 2</div>
<div style="display:flex;align-items:center;gap:22px"><div class="chip in" style="font-size:80px;padding:6px 22px">C</div><div class="in" style="font-size:96px">Still,</div></div>
<div class="lead">Нэг сэдэв: <b>химийн</b> 2 тал. Сайн тал нь үнэн, <span class="lime">гэсэн хэдий ч</span> хор хөнөөлтэй.</div>
<div class="card" style="padding:10px 28px"><div class="x"><span class="w">A) Hence,</span><span><span class="no">✗</span> Хор хөнөөл нь ашиг тусын үр дүн биш</span></div>
<div class="x"><span class="w">B) In contrast,</span><span><span class="no">✗</span> 2 өөр зүйл биш, нэг зүйлийн 2 тал</span></div>
<div class="x"><span class="w">D) Subsequently,</span><span><span class="no">✗</span> Цаг хугацааны дараалал биш</span></div></div>''')

fam = [('Эсрэг, саад', 'however · still · nevertheless · yet', LIME), ('2 зүйл харьцуулах', 'in contrast · conversely · on the other hand', '#8fd3ff'),
       ('Үр дагавар', 'therefore · hence · thus · consequently', '#ffb86b'), ('Нэмэх', 'moreover · furthermore · in addition', '#d7a8ff'), ('Цаг хугацаа', 'subsequently · then · afterward', '#ff8fa3')]
fr = ''.join(f'<div style="display:flex;align-items:center;gap:18px;padding:16px 0;{"border-top:2px solid "+LINE+";" if i else ""}"><span style="flex:none;width:18px;height:60px;border-radius:9px;background:{c}"></span><div><div style="font-size:33px;font-weight:800;color:{c}">{a}</div><div style="font-size:30px;font-weight:600;margin-top:4px">{b}</div></div></div>' for i, (a, b, c) in enumerate(fam))
P.append(f'''<div class="pill">ХАДГАЛАХ ХУУДАС</div><div class="in" style="font-size:96px">Шилжилт үгийн<br><span class="lime">5 бүлэг</span></div>
<div class="card" style="padding:8px 28px">{fr}</div>''')

P.append(f'''<div class="pill">ТӨГСГӨЛ</div>
<div style="text-align:center"><div class="in" style="font-size:64px">Дахиад дасгал авах бол</div>
<div class="in lime pulse" style="font-size:190px;margin:10px 0">SAT</div>
<div class="in" style="font-size:58px">гэж комментод бичээрэй</div></div>
<div style="display:flex;gap:20px;align-items:stretch">
 <div style="background:#fff;border-radius:22px;padding:14px;text-align:center"><img src="{QR}" style="width:230px;height:230px;display:block"><div style="color:#111;font-weight:800;font-size:22px;margin-top:4px">Скан хийж бүртгүүл</div></div>
 <div class="card" style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:12px;font-size:27px;font-weight:700">
  <div><span class="lime">Англи</span> · Мя · Пү · Бя · 20:00–21:20</div><div><span class="lime">Math</span> · Да · Лх · Ба · 20:00–21:20</div><div style="opacity:.8">WhatsApp +1 428 880 1826</div></div></div>''')

def render(out, prefix, video=False):
    out.mkdir(exist_ok=True)
    for f in out.glob('*'): f.unlink()
    T = len(P)
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page(viewport={'width': 1080, 'height': 1350})
        for i, body in enumerate(P, 1):
            pg.set_content(page(i, T, body, 'SAT · ШИЛЖИЛТ ҮГ')); pg.wait_for_timeout(400)
            pg.evaluate("()=>document.getAnimations().forEach(a=>{a.pause();a.currentTime=2000})")
            ov = pg.evaluate("()=>{const m=document.querySelector('.mn');let t=1e9,b=0;for(const c of m.children){const r=c.getBoundingClientRect();t=Math.min(t,r.top);b=Math.max(b,r.bottom)}return [Math.round(t),Math.round(b)]}")
            fn = out / f'{prefix}-{i:02d}-of-{T:02d}.png'; pg.screenshot(path=str(fn))
            print(fn.name, ov, 'OK' if ov[0] >= 130 and ov[1] <= 1255 else 'OVERFLOW')
            if video:
                fr = out / '_f'; fr.mkdir(exist_ok=True)
                for k in range(150):
                    pg.evaluate(f"()=>document.getAnimations().forEach(a=>{{a.pause();a.currentTime={k*1000/30}}})"); pg.screenshot(path=str(fr / f'{k:04d}.png'))
                subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', '30', '-i', str(fr / '%04d.png'), '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '19', '-movflags', '+faststart', str(fn.with_suffix('.mp4'))], check=True)
                shutil.rmtree(fr)
        br.close()

if __name__ == '__main__':
    import sys
    render(HERE / 'out28', 'GMP-SAT-However-vs-InContrast', '--video' in sys.argv)
