from gen18 import *
AC = '#7c3aed'; SOFT = '#ddd0ff'; BG = '#fbf9ff'; GRID = 'rgba(124,58,237,.08)'
GREEN = '#15803d'; RED = '#dc2626'
C = css(AC, SOFT, BG, GRID) + f"""
.lab{{font-size:21px;font-weight:800;letter-spacing:1.5px;opacity:.7}}
.old{{background:#f3f1f7;border-color:#9a93ad;box-shadow:7px 7px 0 #9a93ad}}
.old .big{{text-decoration:line-through;text-decoration-color:{RED};text-decoration-thickness:4px;color:#6b647d}}
.big{{font-size:48px;font-weight:800;line-height:1.1;margin-top:8px}}
.sat{{border-color:{AC};box-shadow:7px 7px 0 {AC}}}
.sat .big{{color:{AC}}}
.sent{{font-family:S,serif;font-size:37px;line-height:1.45}}
.sent b{{font-family:M;font-weight:800;background:{SOFT};padding:0 6px;border-radius:6px}}
.clue{{background:{INK};color:#fff;border-radius:26px;padding:22px 28px;font-size:30px;font-weight:700;line-height:1.35}}
.clue .k{{display:inline-block;background:{AC};border-radius:14px;padding:4px 12px;font-size:20px;font-weight:800;letter-spacing:1px;margin-right:10px;vertical-align:middle}}
.clue b{{color:#c4b5fd}}
"""

def word(n, w, pos, emo, old_mn, old_emo, en, mn, sent, clue, bad, good):
    return (f'''<div style="display:flex;align-items:center;justify-content:space-between"><div><div class="pill">SAT УРХИ #{n}</div>
<div style="font-size:112px;font-weight:800;letter-spacing:-3px;line-height:1;margin-top:14px">{w}<span style="font-size:28px;font-weight:700;color:{AC};border:2.5px solid {AC};border-radius:16px;padding:3px 12px;margin-left:16px;vertical-align:middle;letter-spacing:0">{pos}</span></div></div>{E(emo,150,"fl")}</div>
<div style="display:grid;grid-template-columns:1fr 1.25fr;gap:20px">
 <div class="card old"><div class="lab">ТА МЭДНЭ</div><div class="big">{old_mn}</div><div style="margin-top:12px;font-size:24px;font-weight:700;color:{RED}">✗ Энэ өгүүлбэрт биш</div></div>
 <div class="card sat"><div class="lab" style="color:{AC};opacity:1">ЭНД ✓</div><div class="big">{mn}</div><div style="margin-top:10px;font-size:25px;font-weight:600;line-height:1.3">{en}</div></div></div>
<div class="card sent">{sent}</div>
<div class="card" style="padding:20px 26px"><div style="font-size:24px;font-weight:700;opacity:.8">SAT маягийн асуулт: <i style="font-family:S">{("In the first sentence, “sanctioned”" if w=="sanction" else "As used in the text, “"+w.split()[0]+"”")} most nearly means</i></div>
<div style="display:flex;gap:16px;margin-top:12px"><div style="flex:1;border:3px solid {RED};border-radius:16px;padding:10px 18px;font-size:30px;font-weight:800;color:{RED}">✗ {bad}</div><div style="flex:1;border:3px solid {GREEN};background:#ecfdf3;border-radius:16px;padding:10px 18px;font-size:30px;font-weight:800;color:{GREEN}">✓ {good}</div></div></div>
<div class="clue"><span class="k">ТАНИХ АРГА</span>{clue}</div>''', '')

W = [
 ('novel', 'adj.', '1f4a1', 'роман', '1f4da', 'new and original', 'шинэлэг', 'The team proposed a <b>novel</b> method for storing solar energy.', 'Нэр үгийн <b>өмнө</b> байвал: novel <b>idea / method / approach</b> = шинэлэг', 'fictional', 'original'),
 ('qualify', 'verb', '1f4cf', 'тэнцэх, эрх авах', '1f3c6', 'to limit a claim; to make it less absolute', 'хязгаарлах, тодотгох', 'The author <b>qualifies</b> her claim, noting that the results apply only to small towns.', '<b>qualify a claim / statement</b> = “бүх тохиолдолд биш” гэж хязгаарлах', 'pass', 'limit'),
 ('check', 'verb', '1f6a7', 'шалгах', '1f50d', 'to stop or hold back', 'зогсоох, барих', 'Vaccines helped <b>check</b> the spread of the disease.', '<b>check the spread / growth / power</b> = зогсоох', 'examine', 'restrain'),
 ('champion', 'verb', '1f4e2', 'аварга', '1f3c6', 'to support or defend a cause', 'дэмжих, өмгөөлөх', 'Rachel Carson <b>championed</b> the protection of the environment.', '<b>Үйл үг</b> болж ирвэл: champion a cause = дэмжих', 'win', 'support'),
 ('arrest', 'verb', '1f40c', 'баривчлах', '1f6a8' if False else '1f6a7', 'to stop or slow a process', 'зогсоох, саатуулах', 'Cold temperatures can <b>arrest</b> the growth of bacteria.', '<b>arrest the growth / decline / progress</b> = зогсоох', 'capture', 'halt'),
 ('compromise', 'verb', '1f6e1', 'буулт хийх', '1f91d' if False else '1f4ac', 'to weaken or put at risk', 'сулруулах, эрсдэлд оруулах', 'A weak password can <b>compromise</b> the security of your account.', '<b>compromise safety / security / health</b> = сулруулах', 'negotiate', 'weaken'),
 ('sanction', 'noun · verb', '2696', 'зөвхөн шийтгэл', '274c', 'penalty <u>or</u> official approval', 'шийтгэл <u>эсвэл</u> зөвшөөрөл', 'The school <b>sanctioned</b> the new club. <span style="font-family:M;font-size:24px;color:#6b647d">(= approved)</span><br>The UN placed <b>sanctions</b> on the country. <span style="font-family:M;font-size:24px;color:#6b647d">(= penalties)</span>', 'Эсрэг хоёр утгатай! <b>sanctions on</b> = шийтгэл, <b>sanction a plan</b> = зөвшөөрөх', 'punished', 'approved'),
]

P = []
# COVER
P.append((f'''<div class="pill">SAT VOCAB · ЦУВРАЛ #1</div>
<h1 style="font-size:96px;margin-top:8px">Мэддэг үг чинь<br><em>урхи</em> болж<br>магадгүй</h1>
<div style="display:flex;gap:16px;flex-wrap:wrap;margin-top:6px">
 <div class="card" style="padding:16px 22px;font-size:34px;font-weight:800"><span style="text-decoration:line-through;text-decoration-color:{RED};text-decoration-thickness:4px;color:#6b647d">novel = роман</span></div>
 <div class="card" style="padding:16px 22px;font-size:34px;font-weight:800;border-color:{AC};box-shadow:7px 7px 0 {AC}">novel = <span style="color:{AC}">шинэлэг</span></div></div>
<div style="font-size:34px;font-weight:700;line-height:1.35">SAT-д өөр утгаар гардаг <span class="hl">7 энгийн үг</span> + таних арга</div>
<div style="display:flex;justify-content:space-between;align-items:center;margin-top:6px">
 <div style="font-size:24px;font-weight:700;opacity:.75">Хадгалаад ав · Найздаа илгээ</div>
 <div style="background:{AC};color:#fff;border:3px solid {INK};border-radius:34px;padding:14px 28px;font-size:28px;font-weight:800;box-shadow:6px 6px 0 {INK}">Гүйлгээд үз →</div></div>''',
 f'''<div style="position:absolute;right:60px;top:200px;z-index:1">{E("1f92f",200,"fl")}</div>
<div style="position:absolute;right:70px;top:560px;z-index:1" class="pop">{E("1f440",120,"wig")}</div>'''))

# METHOD
steps = [('1f648', 'Сонголтуудыг хаа', 'Эхлээд 4 сонголтыг бүү хар.'),
         ('270d', 'Өөрийн үгээ тааж бич', 'Өгүүлбэрийн санаанаас хоосон зайд юу орохыг таа.'),
         ('2696', '+ / − өнгө аясыг шалга', 'Эерэг үү, сөрөг үү? Энэ нь буруу сонголтыг хасахад тусална.'),
         ('1f3af', 'Хамгийн ойрыг сонго', 'Мэддэг утгаар нь биш, өгүүлбэрт тохирохыг нь.')]
sh = ''.join(f'<div class="card" style="display:flex;align-items:center;gap:20px;padding:20px 26px"><div style="flex:none;width:60px;height:60px;border-radius:50%;background:{AC};color:#fff;border:3px solid {INK};display:flex;align-items:center;justify-content:center;font-size:30px;font-weight:800">{i}</div><div style="flex:1"><div style="font-size:33px;font-weight:800">{t}</div><div style="font-size:25px;font-weight:600;opacity:.8;margin-top:4px">{s}</div></div></div>' for i, (e, t, s) in enumerate(steps, 1))
P.append((f'<div class="pill">WORDS IN CONTEXT · АРГА</div><h1>Үгийн асуултыг<br><em>4 алхмаар</em> бод</h1>' + sh +
          f'<div class="clue"><span class="k">ЯАГААД</span>SAT үгийн <b>өгүүлбэр доторх</b> утгыг асуудаг. Мэддэг утга чинь буруу хариу руу чирнэ.</div>', ''))

for i, w in enumerate(W, 1):
    P.append(word(i, *w))

# CHEAT SHEET
rows = ''.join(f'<div style="display:grid;grid-template-columns:1.1fr 1fr 1.2fr;align-items:center;padding:13px 22px;{"border-top:2px dashed #d9d1ea;" if k else ""}font-size:27px"><div style="font-weight:800">{w[0]}</div><div style="color:#6b647d;text-decoration:line-through;text-decoration-color:{RED};font-weight:600">{w[3]}</div><div style="color:{AC};font-weight:800">{w[6]}</div></div>' for k, w in enumerate(W))
P.append((f'<div style="display:flex;align-items:center;justify-content:space-between"><div><div class="pill">ХАДГАЛАХ ХУУДАС</div><h1 style="margin-top:14px">7 үг,<br><em>нэг дор</em></h1></div>{E("1f4dd",150,"wig")}</div>'
          f'<div class="card" style="padding:10px 0"><div style="display:grid;grid-template-columns:1.1fr 1fr 1.2fr;padding:8px 22px 12px;font-size:21px;font-weight:800;letter-spacing:1px;opacity:.7"><div>ҮГ</div><div>ТА МЭДНЭ</div><div>SAT-Д</div></div>{rows}</div>'
          f'<div class="clue"><span class="k">ДААЛГАВАР</span>Эдгээрээс аль нь чамайг хуурсан бэ? <b>Комментод</b> бич!</div>', ''))

# END
P.append((end_page(AC, SOFT, 'Өдөрт 20 үг,', 'сард 600 үг', 'GMP Vocab Hub-д <b>3,717 үг</b> англи тайлбар, жишээтэйгээ бэлэн.',
                   sched_cell('АНГЛИ (R&amp;W)', 'Мя · Пү · Бя', AC) + sched_cell('MATH', 'Да · Лх · Ба', AC, True),
                   [('1f4da', '3,717 үгтэй Vocab Hub'), ('1f4dd', 'Долоо хоног бүр сорил'), ('1f331', 'Үнэгүй түвшин тогтоох тест')]), ''))

if __name__ == '__main__':
    import sys
    render(C, P, HERE / 'out21', 'GMP-SAT-Vocab-Urhi', video_first=('--video' in sys.argv))
