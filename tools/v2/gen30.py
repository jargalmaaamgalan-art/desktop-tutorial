"""Transitions mini-series: 6 short posts, one idea each. Content verbatim from sat-writing-transitions.html (GMP module)."""
import subprocess, shutil, sys
import gen29, gen24
from gen18 import E, HERE
from playwright.sync_api import sync_playwright

GREEN = '#15803d'; RED = '#c62828'; INK = '#1e1e1e'

def css(AC, SOFT, TINT):
    c = gen29.CSS.replace('#324dc7', AC).replace('#e8ecfb', SOFT)
    return c + f"""
.bxf .bt span{{background:#324dc7!important}}
.pg{{background:{TINT}}}
.hl{{color:{AC};font-weight:800}}
.h{{font-family:IN,M,sans-serif;font-weight:900;letter-spacing:-2px;line-height:1.02}}
.chips{{display:flex;gap:12px;flex-wrap:wrap}}
.chips span{{background:#fff;border:2.5px solid {AC};color:{AC};border-radius:30px;padding:9px 20px;font-size:26px;font-weight:800}}
.swipe{{align-self:flex-start;background:{INK};color:#fff;border-radius:30px;padding:12px 26px;font-size:25px;font-weight:800}}
.fam{{display:flex;gap:22px;align-items:center}}
.disc{{flex:none;width:92px;height:92px;border-radius:50%;background:{AC};color:#fff;display:flex;align-items:center;justify-content:center;font-size:50px;font-weight:900}}
.fam .t{{font-size:36px;font-weight:800}} .fam .d{{font-size:26px;font-weight:600;color:#445;margin-top:4px;line-height:1.3}}
.fam .w{{font-family:S,serif;font-style:italic;font-size:27px;color:{AC};margin-top:6px}}
.sen{{font-family:S,serif;font-size:36px;line-height:1.45}}
.sen b{{color:{AC}}}
.lab{{font-size:21px;font-weight:800;letter-spacing:1.5px;color:{AC};margin-bottom:8px}}
.rule{{background:{AC};color:#fff;border-radius:22px;padding:20px 26px;font-size:29px;font-weight:800;line-height:1.3}}
.big{{font-size:30px;font-weight:600;line-height:1.4}}
.x{{color:{RED};text-decoration:line-through;text-decoration-thickness:3px}}
.bxc div.cut{{opacity:.45;text-decoration:line-through;text-decoration-color:{RED};text-decoration-thickness:3px}}
.bxc div.win{{border:3px solid {GREEN}!important;background:#effaf2}}
.skel div{{height:20px;border-radius:10px;background:#e3e5ec;margin-top:14px}}
.rwp{{font-size:34px!important;line-height:1.5!important}}
.map .n{{font-size:30px!important;padding:20px!important}} .map .n small{{font-size:20px!important}}
.wr{{font-size:28px!important;padding:16px 0!important}} .wr .w{{font-size:31px!important;width:270px!important}}
.ok{{font-size:44px!important}} .lead{{font-size:36px!important}}
.eq{{display:flex;align-items:center;gap:18px;justify-content:center}}
.eq .card{{font-family:S,serif;font-size:38px;font-weight:600}}
"""

def cover(pill, h, teaser, chips, emo):
    ch = ''.join(f'<span>{c}</span>' for c in chips)
    return f'''<div style="display:flex;justify-content:space-between;align-items:flex-start"><div class="pill">{pill}</div>{E(emo,150,"fl")}</div>
<div class="h" style="font-size:104px">{h}</div>
<div class="lead">{teaser}</div><div class="chips">{ch}</div><div class="swipe">Гүйлгээд үз →</div>'''

def frame(qnum, passage, choices, prompt='Which choice completes the text with the most logical transition?', cut=(), win=None):
    ch = ''.join(f'<div class="{"cut" if i in cut else ""}{" win" if i == win else ""}"><span class="l">{l}</span><span>{c}</span></div>' for i, (l, c) in enumerate(zip('ABCD', choices)))
    return f'''<div class="bx"><div class="bxh"><div><div class="s1">Section 1, Module 1: Reading and Writing</div><div class="s2">Directions &#8964;</div></div>
<div class="tm">24:10<br><span class="hide">Hide</span></div><div class="tl"><div>{gen24.IMORE}<br>More</div></div></div><div class="dash"></div>
<div class="bxb"><div class="qrow"><div class="n">{qnum}</div>{gen24.BOOK}<span class="mr">Mark for Review</span><span class="abc">ABC</span></div>
<div class="rwp">{passage}</div><div class="rwq">{prompt}</div><div class="bxc">{ch}</div></div>
<div class="dash"></div><div class="bxf"><span>Global Math Prep</span><span class="qx">Question {qnum} of 27 &#8963;</span><div class="bt"><span>Back</span><span>Next</span></div></div></div>'''

def qslide(fr, tip):
    return f'''<div class="pill">ДАСГАЛ · ЭХЛЭЭД ӨӨРӨӨ БОД</div>{fr}
<div class="card big" style="padding:16px 24px">{tip}</div>'''

def aslide(ok, rel, mapn, wrong, rule, sep='→'):
    m = ''.join((f'<div class="ar">{sep}</div>' if i else '') + f'<div class="n{" hot" if i == len(mapn) - 1 else ""}"><small>{a}</small>{b}</div>' for i, (a, b) in enumerate(mapn))
    w = ''.join(f'<div class="wr"><span class="w">{a}</span><span>{b}</span></div>' for a, b in wrong)
    return f'''<div class="pill">ХАРИУ</div>
<div class="okrow"><div class="ok">{ok}</div><div class="h" style="font-size:60px">{rel}</div></div>
<div class="map">{m}</div>
<div class="card" style="padding:8px 26px">{w}</div>
<div class="rule">{rule}</div>'''

def endp(nxt):
    return f'''<div class="pill">ТӨГСГӨЛ</div>
<div style="text-align:center"><div class="in" style="font-size:58px">Дахиад ийм дасгал хүсвэл</div>
<div class="in blue" style="font-size:190px;margin:8px 0">SAT</div><div class="in" style="font-size:54px">гэж комментод бичээрэй</div></div>
<div class="card" style="font-size:27px;font-weight:700;text-align:center">Дараагийн хичээл: <span class="hl">{nxt}</span></div>
<div style="display:flex;gap:20px;align-items:stretch">
 <div class="card" style="text-align:center;padding:14px"><img src="{gen29.QR}" style="width:220px;height:220px;display:block"><div style="font-weight:800;font-size:22px;margin-top:4px">Скан хийж бүртгүүл</div></div>
 <div class="card" style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:12px;font-size:27px;font-weight:700">
  <div><span class="blue">Англи</span> · Мя · Пү · Бя · 20:00–21:20</div><div><span class="blue">Math</span> · Да · Лх · Ба · 20:00–21:20</div><div style="color:#556">WhatsApp +1 428 880 1826</div></div></div>'''

POSTS = []

# ---------- 1. Three jobs ----------
fams = [('→', 'Үргэлжлүүлэх', 'Ижил чиглэлд явна: нэмнэ, жишээ өгнө, тодруулна, дараалуулна', 'moreover · for example · in fact · subsequently'),
        ('⇒', 'Үр дагавар', '2 дахь өгүүлбэр нь 1 дэхийнхээ үр дүн', 'therefore · consequently · as a result · thus'),
        ('↩', 'Эсрэг', 'Чиглэл эсрэгээрээ эргэнэ', 'however · nevertheless · still · in contrast')]
f1 = ''.join(f'<div class="card fam"><div class="disc">{a}</div><div><div class="t">{b}</div><div class="d">{c}</div><div class="w">{d}</div></div></div>' for a, b, c, d in fams)
ex = [('→ ҮРГЭЛЖЛҮҮЛЭХ', 'The new library opened with 40,000 volumes. <b>Moreover,</b> it offers free tutoring every weekend.'),
      ('⇒ ҮР ДАГАВАР', 'The bridge failed its safety inspection. <b>Consequently,</b> the city closed it to traffic.'),
      ('↩ ЭСРЭГ', 'The forecast promised sunshine. <b>However,</b> rain fell all afternoon.')]
e1 = ''.join(f'<div class="card"><div class="lab">{a}</div><div class="sen" style="font-size:33px">{b}</div></div>' for a, b in ex)
POSTS.append(dict(
    key='1-Three-Jobs', AC='#4338ca', SOFT='#e7e6fb', TINT='#f6f5ff', nxt='Ижил утгатай 2 сонголт',
    pages=[
        cover('SAT R&amp;W · ШИЛЖИЛТ ҮГ 1/6', '50 гаруй шилжилт үг.<br><span class="blue">Ердөө 3 ажил.</span>',
              'Өмнө үзсэн төрлүүдийг 3 том бүлэгт нэгтгэвэл цээжлэх зүйл багасна.', ['→ Үргэлжлүүлэх', '⇒ Үр дагавар', '↩ Эсрэг'], '1f9ed'),
        f'<div class="pill">3 АЖИЛ</div><div class="h" style="font-size:78px">Шилжилт үг бүр<br><span class="blue">3-ын нэгийг</span> хийнэ</div>{f1}',
        f'<div class="pill">ЖИШЭЭ</div><div class="h" style="font-size:78px">3 жишээ,<br><span class="blue">3 өөр чиглэл</span></div>{e1}',
        qslide(frame(1, 'The recipe looked simple. ______ it took our whole evening.', ['Indeed,', 'Therefore,', 'However,', 'For example,']),
               'Хоосон зайг алгасаад 2 өгүүлбэрийг унш. Ижил чиглэл үү, үр дүн үү, эсрэг үү?'),
        aslide('C) However,', '↩ Эсрэг', [('ХҮЛЭЭЛТ', 'Амархан харагдсан'), ('БОДИТ БАЙДАЛ', 'Бүтэн орой зарцуулсан')],
               [('A) Indeed,', '“Амархан” гэдгийг улам хүчтэй болгоно. Болсон зүйл эсрэгээрээ.'),
                ('B) Therefore,', 'Амархан харагдсан нь удаан болсны шалтгаан биш.'),
                ('D) For example,', 'Удаан болсон нь “амархан” гэдгийн жишээ биш.')],
               'Хүлээлт биелээгүй бол → Эсрэг бүлэг', sep='↩'),
        endp('Ижил утгатай 2 сонголт')]))

# ---------- 2. Twin choices ----------
twins = [('therefore', 'consequently', 'accordingly', 'as a result'), ('moreover', 'furthermore', 'in addition'),
         ('in fact', 'indeed'), ('nevertheless', 'still', 'even so'), ('that is', 'in other words')]
tw = ''.join(f'<div class="wr" style="font-family:S,serif;font-size:31px;align-items:center">{" <span class=hl>=</span> ".join(t)}</div>' for t in twins)
skel = '<div class="skel" style="margin-top:6px"><div style="width:100%"></div><div style="width:94%"></div><div style="width:97%"></div><div style="width:60%"></div></div><div style="font-family:M,sans-serif;font-size:21px;font-weight:700;color:#889;margin-top:10px">Текстийг хараахан уншаагүй байна</div>'
ch2 = ['consequently', 'as a result', 'however', 'for instance']
POSTS.append(dict(
    key='2-Twin-Choices', AC='#8b1e2d', SOFT='#f7e3e6', TINT='#fff6f7', nxt='Өгүүлбэрийн дундах шилжилт үг',
    pages=[
        cover('SAT R&amp;W · ШИЛЖИЛТ ҮГ 2/6', 'Ижил утгатай<br>2 сонголт уу?<br><span class="blue">Хоёулаа буруу.</span>',
              'Текстээ уншихаасаа өмнө 2 сонголтыг хасах арга.', ['therefore = thus', 'moreover = in addition'], '2696'),
        f'''<div class="pill">ЯАГААД?</div><div class="h" style="font-size:78px">Нэг асуулт,<br><span class="blue">ганц зөв хариу</span></div>
<div class="lead">2 сонголт яг ижил ажил хийвэл аль нэгийг нь сонгох шалтгаан байхгүй. Тэгэхээр хоёулаа хасагдана.</div>
<div class="eq"><div class="card x">consequently</div><div class="h" style="font-size:70px;color:#8b1e2d">=</div><div class="card x">as a result</div></div>
<div class="rule">Ихэр сонголт олдвол → 2-уулаа хасна</div>''',
        f'<div class="pill">ИХЭР ҮГС · ХАДГАЛААРАЙ</div><div class="h" style="font-size:78px">Эдгээр нь<br><span class="blue">ижил ажил</span> хийдэг</div><div class="card" style="padding:8px 26px">{tw}</div>',
        qslide(frame(2, skel, ch2, prompt='Which choice completes the text with the most logical transition?'),
               'Текстээ уншаагүй байж юу мэдэж болох вэ? Сонголтуудаа сайн хар.'),
        f'''<div class="pill">ХАРИУ</div><div class="h" style="font-size:70px">A, B <span class="blue">хоёулаа хасагдана</span></div>
{frame(2, skel, ch2, cut=(0, 1))}
<div class="card big" style="padding:16px 24px">consequently = as a result. Үлдсэн 2: <span class="hl">however</span> (эсрэг), <span class="hl">for instance</span> (жишээ). Текстээ уншаад аль нь тохирохыг шийд.</div>''',
        endp('Өгүүлбэрийн дундах шилжилт үг')]))

# ---------- 3. Middle position ----------
POSTS.append(dict(
    key='3-Middle-Position', AC='#4d7c0f', SOFT='#e8f3d6', TINT='#f8fcf1', nxt='Meanwhile-ын 2 утга',
    pages=[
        cover('SAT R&amp;W · ШИЛЖИЛТ ҮГ 3/6', 'Дунд нь байгаа<br><span class="blue">however</span><br>хаашаа заадаг вэ?',
              'Олон хүн нэг өгүүлбэр дотроо харьцуулаад алддаг.', ['Эхэнд', 'Дунд', 'Төгсгөлд'], '1f4cc'),
        f'''<div class="pill">ДҮРЭМ 1</div><div class="h" style="font-size:78px">Байрлал бол<br><span class="blue">зөвхөн хэв маяг</span></div>
<div class="card"><div class="lab">ЭХЭНД</div><div class="sen"><b>Therefore,</b> rehearsals moved indoors.</div></div>
<div class="card"><div class="lab">ДУНД</div><div class="sen">Rehearsals, <b>therefore,</b> moved indoors.</div></div>
<div class="rule">Утга нь яг адилхан</div>''',
        f'''<div class="pill">ДҮРЭМ 2</div><div class="h" style="font-size:78px">Холбоо үргэлж<br><span class="blue">өмнөх өгүүлбэр</span> рүү</div>
<div class="map"><div class="n"><small>ӨМНӨХ ӨГҮҮЛБЭР</small>Саад, бэрхшээл</div><div class="ar">←</div><div class="n hot"><small>ЭНЭ ӨГҮҮЛБЭР</small>…the committee approved the plan, <i>nevertheless.</i></div></div>
<div class="lead">Эхэнд, дунд, төгсгөлд хаана ч байсан шилжилт үг энэ өгүүлбэрийг өмнөх өгүүлбэртэй холбоно.</div>
<div class="rule">Арга: дундах үгийг хаагаад, ЭНЭ өгүүлбэрийг ӨМНӨХ өгүүлбэртэй харьцуул</div>''',
        qslide(frame(3, 'The stadium seats 60,000. Attendance, ______ rarely passes 20,000.', ['therefore,', 'however,', 'likewise,', 'specifically,']),
               'Хоосон зай өгүүлбэрийн дунд байна. Тэгэхээр аль өгүүлбэртэй харьцуулах вэ?'),
        aslide('B) however,', '↩ Эсрэг', [('ӨМНӨХ', '60,000 суудалтай'), ('ЭНЭ', 'Үзэгч 20,000-аас ховор давдаг')],
               [('A) therefore,', 'Үзэгч цөөн ирдэг нь суудал олон байгаагийн үр дүн биш.'),
                ('C) likewise,', '2 баримт ижил биш.'),
                ('D) specifically,', '20,000 бол 60,000-ын дэлгэрэнгүй жишээ биш.')],
               'Дундах зайг алгасаад өмнөх өгүүлбэртэй харьцуул', sep='↔'),
        endp('Meanwhile-ын 2 утга')]))

# ---------- 4. Meanwhile ----------
POSTS.append(dict(
    key='4-Meanwhile', AC='#334155', SOFT='#e2e8f0', TINT='#f5f7fa', nxt='As such урхи',
    pages=[
        cover('SAT R&amp;W · ШИЛЖИЛТ ҮГ 4/6', '<span class="blue">Meanwhile</span><br>2 утгатай',
              'SAT дээр ихэвчлэн 2 талыг эсрэгцүүлэхэд хэрэглэгддэг.', ['Цаг', '2 тал', 'Эсрэгцэл'], '2194'),
        f'''<div class="pill">2 УТГА</div><div class="h" style="font-size:78px">Нэг үг,<br><span class="blue">2 өөр ажил</span></div>
<div class="card fam"><div class="disc">1</div><div><div class="t">Цаг хугацаа</div><div class="d">“Тэр үед зэрэг”. Энгийн утга.</div></div></div>
<div class="card fam"><div class="disc">2</div><div><div class="t">2 талын эсрэгцэл</div><div class="d">Нэг үед 2 тал өөр өөр байдалтай байна. SAT дээр ихэвчлэн энэ утгаар гардаг.</div></div></div>
<div class="map"><div class="n"><small>ТАЛ А</small>Сайн байна</div><div class="ar">↔</div><div class="n hot"><small>ТАЛ Б · НЭГ ҮЕД</small>Муу байна</div></div>''',
        qslide(frame(4, 'Northern farms harvested a record crop. ______ growers in the drought-hit south lost half their fields.', ['Likewise,', 'Meanwhile,', 'Indeed,', 'Accordingly,']),
               'Энд хэдэн тал байна? Тэдний үр дүн ижил үү, эсрэг үү?'),
        aslide('B) Meanwhile,', '↔ 2 тал', [('ТАЛ А · ХОЙД', 'Дээд амжилттай ургац'), ('ТАЛ Б · ӨМНӨД', 'Талбайнхаа хагасыг алдсан')],
               [('A) Likewise,', 'Ижил байдлыг заана. Энд 2 үр дүн эсрэг.'),
                ('C) Indeed,', 'Дээд амжилтыг улам хүчтэй болгоно. Алдагдал руу эргэхгүй.'),
                ('D) Accordingly,', 'Өмнөдийн алдагдал хойдын амжилтаас болоогүй.')],
               'Нэг үед, 2 тал, өөр үр дүн → Meanwhile', sep='↔'),
        endp('As such урхи')]))

# ---------- 5. As such ----------
POSTS.append(dict(
    key='5-As-Such', AC='#7c3f12', SOFT='#f5e6da', TINT='#fdf8f3', nxt='In fact ба That is',
    pages=[
        cover('SAT R&amp;W · ШИЛЖИЛТ ҮГ 5/6', 'As such гэдэг чинь<br><span class="blue">“тиймээс”</span> биш',
              'Олон хүний андуурдаг үгийг 1 тестээр шалга.', ['as such', '= as a + нэр үг'], '1f30b'),
        f'''<div class="pill">ДҮРЭМ</div><div class="h" style="font-size:78px">as such =<br><span class="blue">as a + нэр үг</span></div>
<div class="lead">Тэр нэр үг өмнөх өгүүлбэрт байх ёстой. Дараагийн өгүүлбэрийн эзэн нь яг тэр зүйл байх ёстой.</div>
<div class="card"><div class="lab">ТЕСТ</div><div class="big">“As such”-ийн оронд <b class="hl">“as a + өмнөх нэр үг”</b> тавиад унш. Утгатай бол зөв, утгагүй бол буруу.</div></div>''',
        qslide(frame(5, 'Basalt is a volcanic rock. ______ it formed from cooling lava.', ['As such,', 'Meanwhile,', 'Still,', 'Subsequently,']),
               'Тестээ хийгээд үз: “as a + ?”'),
        aslide('A) As such,', '✓ Тест давлаа', [('ТЕСТ', '<i>As a volcanic rock,</i> it formed from cooling lava.'), ('ДҮГНЭЛТ', 'Basalt бол галт уулын чулуу. Утгатай.')],
               [('B) Meanwhile,', 'Эсрэгцүүлэх 2 тал алга.'),
                ('C) Still,', 'Ямар нэг зүйлийг үл харгалзан болсон зүйл алга.'),
                ('D) Subsequently,', 'Цаг хугацааны дараалал биш.')],
               'as a + нэр үг утгатай байна → as such зөв'),
        f'''<div class="pill">УРХИ</div><div class="h" style="font-size:78px">Энд <span class="blue">as such</span><br>буруу</div>
<div class="card"><div class="sen">The road was icy. <span class="x">As such,</span> the buses ran late.</div></div>
<div class="card"><div class="lab">ТЕСТ</div><div class="big"><i>As an icy road,</i> the buses ran late? Автобус бол зам биш. <b style="color:{RED}">Утгагүй.</b></div></div>
<div class="card okrow"><div class="ok" style="font-size:32px">As a result,</div><div class="big">Жинхэнэ үр дагаврын үг хэрэглэнэ.</div></div>''',
        endp('In fact ба That is')]))

# ---------- 6. In fact vs That is ----------
POSTS.append(dict(
    key='6-In-Fact-vs-That-Is', AC='#0369a1', SOFT='#dff0fa', TINT='#f3f9fd', nxt='Шинэ цуврал удахгүй',
    pages=[
        cover('SAT R&amp;W · ШИЛЖИЛТ ҮГ 6/6', 'In fact<br><span class="blue">≠ That is</span>',
              'Хоёулаа өмнөх санааг үргэлжлүүлдэг. Гэхдээ өөр ажил хийдэг.', ['In fact = улам хүчтэй', 'That is = өөрөөр хэлбэл'], '1f4c8'),
        f'''<div class="pill">ЯЛГАА</div><div class="h" style="font-size:78px">Хүчтэй болгох уу,<br><span class="blue">тайлбарлах уу?</span></div>
<div class="card fam"><div class="disc">↑</div><div><div class="t">in fact · indeed</div><div class="d">Өмнөх санааг улам хүчтэй болгоно. Шинэ, илүү хүчтэй баримт нэмнэ.</div></div></div>
<div class="card fam"><div class="disc">=</div><div><div class="t">that is · in other words</div><div class="d">Ижил санааг өөр үгээр тайлбарлана. Шинэ баримт нэмэхгүй.</div></div></div>''',
        qslide(frame(6, 'The prototype passed every stress test. ______ it survived pressures double the requirement.', ['However,', 'In fact,', 'Whereas,', 'That is,']),
               '2 дахь өгүүлбэр шинэ баримт нэмж байна уу, эсвэл ижил санааг давтаж байна уу?'),
        aslide('B) In fact,', '↑ Улам хүчтэй', [('1', 'Бүх туршилтыг давсан'), ('2', 'Шаардлагаас 2 дахин их даралт даасан')],
               [('A) However,', 'Эсрэг зүйл алга.'),
                ('C) Whereas,', 'Нэг өгүүлбэр дотор 2 зүйлийг эсрэгцүүлдэг. Энд эсрэг зүйл алга.'),
                ('D) That is,', 'Ижил санааг давтана. Энд шинэ, илүү хүчтэй баримт нэмсэн.')],
               'Өмнөх санааг улам хүчтэй болгож байвал → In fact'),
        f'''<div class="pill">ТЭГВЭЛ THAT IS ХЭЗЭЭ ЗӨВ ВЭ?</div><div class="h" style="font-size:78px">Хэцүү үг,<br><span class="blue">энгийн тайлбар</span></div>
<div class="card"><div class="sen">The metal is ductile — <b>that is,</b> it can be drawn into wire without breaking.</div></div>
<div class="map"><div class="n"><small>ХЭЦҮҮ ҮГ</small>ductile</div><div class="ar">=</div><div class="n hot"><small>ТАЙЛБАР</small>Хугарахгүйгээр утас болгон сунгаж болно</div></div>
<div class="rule">That is хэцүү үг, санааг энгийнээр дахин тайлбарлана</div>''',
        endp('Шинэ цуврал удахгүй')]))


def page(C, n, T, body, tag):
    return f'''<!doctype html><html lang="mn"><head><meta charset="utf-8"><style>{C}</style></head><body><div class="pg">
<div class="top"><img src="{gen29.LOGO}"><span>{n:02d} / {T:02d}</span></div>
<div class="mn">{body}</div>
<div class="ft"><span>SAT R&amp;W · ШИЛЖИЛТ ҮГ {tag}</span><span>{"Гүйлгээд үз →" if n < T else "@globalmathprep"}</span></div></div></body></html>'''


def render(post, video):
    out = HERE / ('out30-' + post['key']); out.mkdir(exist_ok=True)
    for f in out.glob('*'): f.unlink() if f.is_file() else shutil.rmtree(f)
    C = css(post['AC'], post['SOFT'], post['TINT']); P = post['pages']; T = len(P)
    tag = post['key'].split('-')[0] + '/6'
    prefix = 'GMP-Transitions-' + post['key']
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page(viewport={'width': 1080, 'height': 1350})
        for i, body in enumerate(P, 1):
            pg.set_content(page(C, i, T, body, tag)); pg.wait_for_timeout(400)
            pg.evaluate("()=>document.getAnimations().forEach(a=>{a.pause();a.currentTime=2500})")
            ov = pg.evaluate("()=>{const m=document.querySelector('.mn');let t=1e9,b=0;for(const c of m.children){const r=c.getBoundingClientRect();t=Math.min(t,r.top);b=Math.max(b,r.bottom)}return [Math.round(t),Math.round(b),m.scrollWidth>m.clientWidth+2]}")
            fn = out / f'{prefix}-{i:02d}-of-{T:02d}.png'; pg.screenshot(path=str(fn))
            print(fn.name, ov, 'OK' if ov[0] >= 130 and ov[1] <= 1240 and not ov[2] else 'OVERFLOW', flush=True)
            if video:
                fr = out / '_f'; fr.mkdir(exist_ok=True)
                for k in range(150):
                    pg.evaluate(f"()=>document.getAnimations().forEach(a=>{{a.pause();a.currentTime={k*1000/30}}})"); pg.screenshot(path=str(fr / f'{k:04d}.png'))
                subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', '30', '-i', str(fr / '%04d.png'), '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '19', '-movflags', '+faststart', str(fn.with_suffix('.mp4'))], check=True)
                shutil.rmtree(fr)
        br.close()

if __name__ == '__main__':
    sel = [a for a in sys.argv[1:] if not a.startswith('--')]
    for post in POSTS:
        if not sel or post['key'][0] in sel:
            render(post, '--video' in sys.argv)
