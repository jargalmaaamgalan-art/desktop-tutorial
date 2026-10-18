"""SAT R&W: an -ing word is not a verb; 'being' is usually wrong. One post, 6 slides.
Content verbatim from sat-writing-fragments-lesson.html (GMP module, Ch 3 Sentences and Fragments),
section 06 F Participles and gerunds: the -ing rule (Tomatoes growing / grow), 'Being, the word to distrust'
(is/was/are/were table, Today the tomato being grown / is grown) and question 4 (Great Lakes, answer C were) with its notes."""
import sys
import base64
import gen29, gen30, gen32, gen33

def _b(f): return 'data:image/png;base64,' + base64.b64encode(open(f, 'rb').read()).decode()
ROUND, WORD = _b('gmp-round.png'), _b('gmp-name-dark.png')

AC, SOFT, TINT = '#a21caf', '#f6e1f8', '#fdf6fe'   # fuchsia (new colour, not used by recent posts)
GREEN = '#15803d'; RED = '#c62828'

EXTRA = gen33.EXTRA.replace('#be185d', AC) + """
.lead{font-size:40px!important;line-height:1.35!important}
.rule{font-size:36px!important;padding:24px 30px!important}
.big{font-size:36px!important}
.chips span{font-size:32px!important;padding:12px 24px!important}
.swipe{font-size:30px!important}
.tag{font-size:26px!important;padding:6px 16px!important}
.pill{font-size:28px!important}
.sen{font-size:40px!important}
.rwp{font-size:36px!important;line-height:1.5!important}
.rwq{font-size:31px!important}
.bxc div{font-size:33px!important;padding:10px 18px!important}
.okrow .ok{font-size:46px!important}
.map .n{font-size:32px!important} .map .n small{font-size:22px!important}
.wr{font-size:31px!important} .wr .w{font-size:33px!important;width:250px!important}
.card[style*="font-size:27px"]{font-size:31px!important;white-space:nowrap}
.tb{display:grid;grid-template-columns:1.2fr 1fr 1fr;border:2px solid #ead3ee;border-radius:16px;overflow:hidden;background:#fff}
.tb div{padding:14px 18px;font-size:32px;font-weight:700;text-align:center;border-top:2px solid #f2e4f4}
.tb .hd{background:""" + AC + """;color:#fff;border-top:0;font-size:28px;letter-spacing:1px}
.tb .v{font-family:S,serif;font-size:44px;color:""" + AC + """}
.brand{position:absolute;top:34px;left:56px;right:56px;display:flex;align-items:center;gap:18px;z-index:3}
.brand .r{width:112px;height:112px;border-radius:50%;box-shadow:0 4px 14px rgba(15,30,80,.25)}
.brand .w{height:36px;display:block}
.brand .tx{display:flex;flex-direction:column;gap:12px}
.brand .jg{font-family:S,serif;font-weight:700;font-size:27px;letter-spacing:5px;color:#af7f22;line-height:1}
.brand .n{margin-left:auto;font-weight:800;font-size:26px;letter-spacing:2px;color:""" + AC + """;border:2.5px solid """ + AC + """;border-radius:30px;padding:8px 18px}
.ft b{color:#1e2a5a}
"""

def css():
    return gen30.css(AC, SOFT, TINT) + EXTRA

PROMPT = 'Which choice completes the text so that it conforms to the conventions of Standard English?'
PASSAGE = ('In the nineteenth century, the Great Lakes ______ a major highway for transportation, migration, and trade, '
           'as well as home to a large number of aquatic species.')
CH = ['being', 'was', 'were', 'having been']

PAGES = [
    # 1. cover
    gen30.cover('SAT R&amp;W · БҮТЭН ӨГҮҮЛБЭР',
                '-ing үг<br><span class="blue">үйл үг биш</span>',
                'Сонголтод <b>being</b> байвал эхлээд буруу гэж үз. Яагаад гэдгийг 1 дасгалаар харъя.',
                ['growing ✗ → grow ✓', 'being ✗ → were ✓'], '1f6a7'),
    # 2. the -ing rule
    f'''<div class="pill">ГОЛ САНАА</div><div class="h" style="font-size:72px">Эзэн + <span class="blue">-ing үг</span><br>= бүтэн биш</div>
<div class="lead">-ing-ээр төгссөн үг бол хувирсан үйл үг биш. Өгүүлбэрт эзэн, хувирсан үйл үг хоёулаа хэрэгтэй.</div>
<div class="card"><div class="tag n">БҮТЭН БИШ</div><div class="sen">Tomatoes <b>growing</b> in many shapes and varieties in greenhouses around the world</div></div>
<div class="card"><div class="tag y">БҮТЭН ӨГҮҮЛБЭР</div><div class="sen">Tomatoes <b>grow</b> in many shapes and varieties in greenhouses around the world.</div></div>
<div class="rule">Засах арга: -ing үгийг хувирсан үйл үг болго</div>''',
    # 3. being
    f'''<div class="pill">ИТГЭЖ БОЛОХГҮЙ ҮГ</div><div class="h" style="font-size:72px"><span class="blue">Being</span>-ийн оронд<br>юу тавих вэ?</div>
<div class="tb"><div class="hd">to be</div><div class="hd">ОДОО</div><div class="hd">ӨНГӨРСӨН</div>
<div>Ганц тоо</div><div class="v">is</div><div class="v">was</div>
<div>Олон тоо</div><div class="v">are</div><div class="v">were</div></div>
<div class="card"><div class="tag n">БҮТЭН БИШ</div><div class="sen">Today, the tomato <b>being</b> grown in greenhouses around the world</div></div>
<div class="card"><div class="tag y">БҮТЭН ӨГҮҮЛБЭР</div><div class="sen">Today, the tomato <b>is</b> grown in greenhouses around the world.</div></div>''',
    # 4. question
    gen30.qslide(gen30.frame(4, PASSAGE, CH, prompt=PROMPT),
                 'Эхлээд хувирсан үйл үг биш сонголтуудыг хас. Дараа нь эзэн ганц уу, олон уу, цаг нь хэзээ вэ?'),
    # 5. answer
    gen30.aslide('C) were', '2 шалгуур', [('ЭЗЭН', 'Great Lakes: олон тоо'), ('ЦАГ', 'In the nineteenth century: өнгөрсөн')],
                 [('A) being', 'Being хэзээ ч хувирсан үйл үг биш. Бүтэн биш өгүүлбэр үүснэ.'),
                  ('B) was', 'Цаг нь зөв, гэхдээ ганц тоо. Эзэн нь олон тоо.'),
                  ('D) having been', 'Энэ ч бас хувирсан үйл үг биш. Өгүүлбэрт гол үйл үг дутна.')],
                 'Олон тоо + өнгөрсөн цаг → were', sep='+'),
    # 6. end
    gen30.endp('Шинэ сэдэв удахгүй'),
]


def page(C, n, T, body):
    return f'''<!doctype html><html lang="mn"><head><meta charset="utf-8"><style>{C}</style></head><body><div class="pg">
<div class="brand"><img class="r" src="{ROUND}"><div class="tx"><img class="w" src="{WORD}"><div class="jg">JARGALMAA AMGALAN</div></div><span class="n">{n:02d} / {T:02d}</span></div>
<div class="mn">{body}</div>
<div class="ft"><span><b>globalmathprep.academy</b> · SAT R&amp;W · -ING БА BEING</span><span>{"Гүйлгээд үз →" if n < T else "@globalmathprep"}</span></div></div></body></html>'''


if __name__ == '__main__':
    gen32.render('--video' in sys.argv, key='Ing-Being', prefix='GMP-SAT-Ing-Not-A-Verb', pages=PAGES, cssf=css, pagef=page)
