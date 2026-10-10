"""Conjunction + transition lists post (replaces the Oct 13 'Three jobs' post).
Word lists come from the owner's own cheat sheet (sat-writing-cheat-sheet.html, 'Transitions' and 'Dependent openers / FANBOYS' lines).
Model: gen30.py. Run: python3 gen34.py [--video]"""
import sys
import gen30
from gen18 import E

AC, SOFT, TINT = '#0f766e', '#d9f2ee', '#f2fbfa'   # teal: not used by any other scheduled post

EXTRA = """
.lr{display:flex;align-items:center;gap:18px;padding:9px 0;border-bottom:2px dashed #cfe3e0}
.lr:last-child{border-bottom:none}
.lr .lt{flex:none;width:54px;height:54px;border-radius:50%;background:@AC@;color:#fff;display:flex;align-items:center;justify-content:center;font-size:30px;font-weight:900}
.lr .wd{flex:none;width:150px;font-family:S,serif;font-size:38px;font-weight:700;color:#1e1e1e}
.lr .mg{font-size:29px;font-weight:700;color:#334}
.lr .mg small{font-size:26px;font-weight:600;color:#445}
.grp{background:#fff;border-radius:22px;padding:14px 24px 16px;border:2.5px solid @SOFT@}
.grp .lab{margin-bottom:4px}
.grp .ws{font-family:S,serif;font-size:31px;line-height:1.35;color:#1e1e1e}
.grp .ws i{font-style:normal;color:@AC@;font-weight:700;padding:0 6px}
.trap{background:#fff;border:3px solid #c62828;border-radius:22px;padding:14px 24px 16px}
.trap .lab{color:#c62828}
.trap .note{font-size:25px;font-weight:700;color:#445;margin-top:4px}
""".replace("@AC@", AC).replace("@SOFT@", SOFT)

_css = gen30.css
gen30.css = lambda a, s, t: _css(a, s, t) + EXTRA

H = 'font-size:74px'

# 1. cover
cov = gen30.cover('SAT R&amp;W · ШИЛЖИЛТ ҮГ 1/6', '3 жагсаалт.<br><span class="blue">Гол холбоос үгс.</span>',
                  'Аль нь аль жагсаалтад хамаарахыг мэдвэл цэг, таслал алдахгүй.',
                  ['FANBOYS', 'although · because', 'however · therefore'], '1f517')

# 2. coordinating (FANBOYS)
fan = [('F', 'for', 'учир нь (because)', 'шалтгаан'), ('A', 'and', 'ба', 'нэмнэ'), ('N', 'nor', 'бас биш', 'үгүйсгэл нэмнэ'),
       ('B', 'but', 'харин', 'эсрэг'), ('O', 'or', 'эсвэл', 'сонголт'), ('Y', 'yet', 'гэсэн ч', 'эсрэг'), ('S', 'so', 'тиймээс', 'үр дүн')]
rows = ''.join(f'<div class="lr"><div class="lt">{a}</div><div class="wd">{b}</div><div class="mg">{c} <small>· {d}</small></div></div>' for a, b, c, d in fan)
p2 = f'''<div class="pill">1-Р ЖАГСААЛТ · COORDINATING</div>
<div class="h" style="{H}">FANBOYS: <span class="blue">7 үг</span></div>
<div class="lead" style="font-size:29px">2 бүрэн өгүүлбэрийг холбоно. Үг холбоход таслал хэрэггүй.</div>
<div class="card" style="padding:6px 26px">{rows}</div>
<div class="card" style="padding:14px 24px"><div class="lab">ЖИШЭЭ</div><div class="sen" style="font-size:33px">The test was hard<b>, but</b> she finished early.</div></div>
<div class="rule">Бүрэн өгүүлбэр + <u>таслал</u> + FANBOYS + бүрэн өгүүлбэр</div>'''

# 3. subordinating
sub = [('ШАЛТГААН', ['because', 'since', 'as']), ('ЭСРЭГ', ['although', 'though', 'even though', 'while', 'whereas']),
       ('НӨХЦӨЛ', ['if', 'unless', 'as long as']), ('ЦАГ', ['when', 'after', 'before', 'until', 'once'])]
g3 = ''.join(f'<div class="grp" style="padding:10px 24px 12px"><div class="lab">{a}</div><div class="ws" style="font-size:30px">{"<i>·</i>".join(b)}</div></div>' for a, b in sub)
p3 = f'''<div class="pill">2-Р ЖАГСААЛТ · SUBORDINATING</div>
<div class="h" style="font-size:62px">Хамаарах холбоос: <span class="blue">4 утга</span></div>
<div class="lead" style="font-size:29px">Хамаарах хэсгийг нээнэ. Ганцаараа бүрэн өгүүлбэр биш.</div>
{g3}
<div class="card" style="padding:14px 24px"><div class="lab">ЖИШЭЭ</div><div class="sen" style="font-size:32px"><b>Although</b> it was late<b>,</b> we kept working.</div>
<div class="sen" style="font-size:32px;margin-top:6px">We kept working <b>because</b> it was late.</div></div>
<div class="rule" style="font-size:25px">Эхэнд бол таслал, төгсгөлд таслалгүй. Цэгээр салгавал fragment.</div>'''

# 4. transition words
tr = [('ҮРГЭЛЖЛҮҮЛЭХ', ['moreover', 'furthermore', 'in addition', 'likewise', 'similarly']),
      ('ЭСРЭГ', ['however', 'nevertheless', 'nonetheless', 'still', 'in contrast', 'on the other hand']),
      ('ҮР ДАГАВАР', ['therefore', 'thus', 'hence', 'consequently', 'accordingly', 'as a result']),
      ('ЖИШЭЭ ӨГӨХ', ['for example', 'for instance', 'to illustrate', 'namely', 'specifically']),
      ('ТОДРУУЛАХ', ['indeed', 'in fact', 'in other words', 'that is'])]
g4 = ''.join(f'<div class="grp" style="padding:10px 22px 12px"><div class="lab">{a}</div><div class="ws" style="font-size:28px;line-height:1.3">{"<i>·</i>".join(b)}</div></div>' for a, b in tr)
p4 = f'''<div class="pill">3-Р ЖАГСААЛТ · ШИЛЖИЛТ ҮГ</div>
<div class="h" style="font-size:60px">Түгээмэл шилжилт үг: <span class="blue">5 бүлэг</span></div>
{g4}
<div class="rule" style="font-size:27px">Ихэнхдээ өмнө нь цэг эсвэл цэгтэй таслал (;), ард нь таслал:<br>X<b>; however,</b> Y &nbsp;·&nbsp; X<b>. However,</b> Y</div>'''

# 5. same idea, three patterns + traps
def row(lab, sen):
    return f'<div class="card" style="padding:12px 24px"><div class="lab">{lab}</div><div class="sen" style="font-size:31px">{sen}</div></div>'
p5 = f'''<div class="pill">НЭГ САНАА · 3 БИЧЛЭГ</div>
<div class="h" style="font-size:70px">Утга ижил,<br><span class="blue">цэг таслал өөр</span></div>
{row('FANBOYS · X, but Y', 'The test was hard<b>, but</b> she finished early.')}
{row('ХАМААРАХ ХОЛБООС · Although X, Y', '<b>Although</b> the test was hard<b>,</b> she finished early.')}
{row('ШИЛЖИЛТ ҮГ · X; however, Y', 'The test was hard<b>; however,</b> she finished early.')}
<div class="trap"><div class="lab">АЛДАА 1 · ТАСЛАЛААР ЗАЛГАСАН</div><div class="sen" style="font-size:30px"><b class="x">The test was hard, however, she finished early.</b></div><div class="note">Ганц таслал = comma splice. Засвар: ; эсвэл цэг</div></div>
<div class="trap"><div class="lab">АЛДАА 2 · 2 ХОЛБООС ХАМТ</div><div class="sen" style="font-size:30px"><b class="x">Although the test was hard, but she finished early.</b></div><div class="note">Although + but хамт хэрэглэхгүй</div></div>'''

gen30.POSTS[:] = [dict(key='1-Conjunction-Lists', AC=AC, SOFT=SOFT, TINT=TINT, nxt='Ижил утгатай 2 сонголт',
                       pages=[cov, p2, p3, p4, p5, gen30.endp('Ижил утгатай 2 сонголт')])]

if __name__ == '__main__':
    gen30.render(gen30.POSTS[0], '--video' in sys.argv)
