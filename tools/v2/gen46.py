"""SAT R&W: non-essential information between commas; cross it out and find the verb. One post, 6 slides.
Content verbatim from sat-writing-fragments-lesson.html (GMP module, Ch 3 Sentences and Fragments),
section 05 E Non-essential information: the tomato examples (which-clause, appositive), 'A sentence cannot stop
right after a non-essential clause' (fragments and the repaired sentence) and question 3 (Amelia Griffiths, answer D compiled)."""
import sys
import base64
import gen30, gen32, gen33

def _b(f): return 'data:image/png;base64,' + base64.b64encode(open(f, 'rb').read()).decode()
ROUND, WORD = _b('gmp-round.png'), _b('gmp-name-dark.png')

AC, SOFT, TINT = '#a16207', '#f8ecd0', '#fefaf0'   # mustard gold (new colour, not used by recent posts)
GREEN = '#15803d'; RED = '#c62828'

EXTRA = gen33.EXTRA.replace('#be185d', AC) + """
.lead{font-size:38px!important;line-height:1.35!important}
.rule{font-size:36px!important;padding:24px 30px!important}
.big{font-size:36px!important}
.chips span{font-size:32px!important;padding:12px 24px!important}
.swipe{font-size:30px!important}
.tag{font-size:26px!important;padding:6px 16px!important}
.pill{font-size:28px!important}
.sen{font-size:38px!important}
.sen s{color:#9a9aa5;text-decoration-color:""" + RED + """;text-decoration-thickness:3px}
.note{font-size:30px;font-weight:700;color:#445;margin-top:10px;line-height:1.35}
.rwp{font-size:36px!important;line-height:1.5!important}
.rwq{font-size:31px!important}
.bxc div{font-size:33px!important;padding:10px 18px!important}
.okrow .ok{font-size:46px!important}
.map .n{font-size:31px!important} .map .n small{font-size:22px!important}
.wr{font-size:31px!important} .wr .w{font-size:33px!important;width:270px!important}
.card[style*="font-size:27px"]{font-size:31px!important;white-space:nowrap}
.brand{position:absolute;top:34px;left:56px;right:56px;display:flex;align-items:center;gap:18px;z-index:3}
.brand .r{width:112px;height:112px;border-radius:50%;box-shadow:0 4px 14px rgba(15,30,80,.25)}
.brand .w{height:36px;display:block}
.brand .tx{display:flex;flex-direction:column;gap:12px}
.brand .jg{font-family:S,serif;font-weight:700;font-size:27px;letter-spacing:5px;color:#af7f22;line-height:1}
.brand .n{margin-left:auto;font-weight:800;font-size:26px;letter-spacing:2px;color:""" + AC + """;border:2.5px solid """ + AC + """;border-radius:30px;padding:8px 18px}
.ft b{color:#1e2a5a}
.map .n.hot small{color:#fff3d6!important}
.bxh .s1{margin-right:24px}
"""

def css():
    return gen30.css(AC, SOFT, TINT) + EXTRA

PROMPT = 'Which choice completes the text so that it conforms to the conventions of Standard English?'
PASSAGE = ('Amelia Griffiths, one of the most prominent amateur scientists of the early nineteenth century, ______ '
           'many important collections of algae specimens.')
CH = ['compiling', 'who compiled', 'having compiled', 'compiled']

PAGES = [
    # 1. cover
    gen30.cover('SAT R&amp;W · БҮТЭН ӨГҮҮЛБЭР',
                '2 таслалын<br>дундах хэсгийг<br><span class="blue">хаагаад унш</span>',
                'Эзэн, үйл үгийн дунд урт нэмэлт мэдээлэл орвол үйл үгээ алдахад амархан.',
                [', which …,', ', one of …,'], '1f648').replace('font-size:104px', 'font-size:96px'),
    # 2. the idea
    f'''<div class="pill">ГОЛ САНАА</div><div class="h" style="font-size:70px">Нэмэлт мэдээллийг<br><span class="blue">хасаж болно</span></div>
<div class="lead">Эзэн, үйл үгийн хооронд 2 таслалын дунд нэмэлт мэдээлэл орж болно. Хасахад өгүүлбэр бүтэн хэвээр үлдэнэ.</div>
<div class="card"><div class="tag y">WHICH-ЭЭР ЭХЭЛСЭН</div><div class="sen">The tomato<s>, which is one of the most popular salad ingredients,</s> <b>grows</b> in many shapes and varieties.</div></div>
<div class="card"><div class="tag y">НЭР ҮГЭЭР ЭХЭЛСЭН</div><div class="sen">The tomato<s>, one of the most popular salad ingredients,</s> <b>grows</b> in many shapes and varieties.</div></div>''',
    # 3. the trap
    f'''<div class="pill">УРХИ</div><div class="h" style="font-size:70px">Нэмэлт мэдээллийн дараа<br><span class="blue">зогсож болохгүй</span></div>
<div class="card"><div class="tag n">БҮТЭН БИШ</div><div class="sen">The tomato, which <b>is</b> one of the most popular salad ingredients</div>
<div class="note">is нь which-ийн үйл үг. The tomato үйл үггүй үлдсэн.</div></div>
<div class="card"><div class="tag n">БҮТЭН БИШ</div><div class="sen">The tomato, one of the most popular salad ingredients</div></div>
<div class="card"><div class="tag y">БҮТЭН ӨГҮҮЛБЭР</div><div class="sen">The tomato <b>is</b> one of the most popular salad ingredients.</div></div>''',
    # 4. question
    gen30.qslide(gen30.frame(3, PASSAGE, CH, prompt=PROMPT),
                 '2 таслалын дундах хэсгийг хаа. Үлдсэн өгүүлбэрт хоосон зайд юу хэрэгтэй вэ?'),
    # 5. answer
    gen30.aslide('D) compiled', 'Хаагаад унш', [('ХААХ', ', one of the most prominent … century,'), ('ҮЛДЭНЭ', 'Amelia Griffiths compiled many…')],
                 [('A) compiling', '-ing хэлбэр бол цагтай үйл үг биш. Өгүүлбэр гол үйл үггүй үлдэнэ.'),
                  ('B) who compiled', 'who нь дахин нэг нэмэлт хэсэг эхлүүлнэ. Amelia Griffiths өөрийн үйл үггүй үлдэнэ.'),
                  ('C) having compiled', 'Энэ ч бас цагтай үйл үг биш.')],
                 'Эзэн + цагтай үйл үг → compiled'),
    # 6. end
    gen30.endp('Шинэ сэдэв удахгүй'),
]


def page(C, n, T, body):
    return f'''<!doctype html><html lang="mn"><head><meta charset="utf-8"><style>{C}</style></head><body><div class="pg">
<div class="brand"><img class="r" src="{ROUND}"><div class="tx"><img class="w" src="{WORD}"><div class="jg">JARGALMAA AMGALAN</div></div><span class="n">{n:02d} / {T:02d}</span></div>
<div class="mn">{body}</div>
<div class="ft"><span><b>globalmathprep.academy</b> · SAT R&amp;W · НЭМЭЛТ МЭДЭЭЛЭЛ</span><span>{"Гүйлгээд үз →" if n < T else "@globalmathprep"}</span></div></div></body></html>'''


if __name__ == '__main__':
    gen32.render('--video' in sys.argv, key='Non-Essential', prefix='GMP-SAT-Non-Essential-Commas', pages=PAGES, cssf=css, pagef=page)
