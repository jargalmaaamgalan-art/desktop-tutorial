"""SAT R&W: conjunctions. FANBOYS join two sentences; subordinators make a clause dependent. One post, 6 slides.
Content verbatim from sat-writing-fragments-lesson.html (GMP module, Ch 3 Sentences and Fragments),
section 07 G Conjunctions (screen scConj): the two word lists, 'one joining word per join' with poll t5
(When they catch sight of their prey, [DELETE] peregrine falcons...) and poll t6 (meteorites, answer B DELETE)."""
import sys
import gen30, gen32, gen46

AC, SOFT, TINT = '#1d4ed8', '#e1e9fd', '#f6f8ff'   # cobalt blue (new colour, not used by recent posts)
GREEN = '#15803d'; RED = '#c62828'

EXTRA = gen46.EXTRA.replace('#a16207', AC) + """
.words{display:flex;flex-wrap:wrap;gap:10px;margin-top:12px}
.words span{font-family:S,serif;font-size:31px;border-radius:12px;padding:5px 14px;background:""" + SOFT + """;color:""" + AC + """;font-weight:700}
.words.sub span{background:#eef0f4;color:#334}
.ct{font-size:34px;font-weight:900}
.ct small{display:block;font-size:27px;font-weight:700;color:#556;margin-top:4px}
"""


def css():
    return gen30.css(AC, SOFT, TINT) + EXTRA


PROMPT = 'Which choice completes the text so that it conforms to the conventions of Standard English?'
PASSAGE = ('______ findings from one recent study about meteorites suggest that water has been present on Earth '
           'since the planet was formed.')
CH = ['Although', '[DELETE the underlined portion]', 'Because', 'Since']

FAN = ['for', 'and', 'nor', 'but', 'or', 'yet', 'so']
SUB = ['after', 'although', 'as', 'because', 'before', 'even though', 'if', 'since', 'though', 'unless', 'until',
       'when', 'whenever', 'whereas', 'while']
w = lambda L, c='': f'<div class="words {c}">' + ''.join(f'<span>{x}</span>' for x in L) + '</div>'

PAGES = [
    # 1. cover
    gen30.cover('SAT R&amp;W · БҮТЭН ӨГҮҮЛБЭР',
                'Бүтэн өгүүлбэрийн<br>өмнө Although нэмбэл<br><span class="blue">бүтэн биш болно</span>',
                'Холбоос үг бүхэн өгүүлбэр холбодоггүй. Зарим нь өгүүлбэрийг бие дааж чадахгүй болгодог.',
                ['FANBOYS', 'although · because', '1 холболт = 1 үг'], '1f517').replace('font-size:104px', 'font-size:90px'),
    # 2. the idea: two types, opposite jobs
    f'''<div class="pill">ГОЛ САНАА</div><div class="h" style="font-size:66px">Холбоос үгийн 2 төрөл,<br><span class="blue">эсрэг 2 ажил</span></div>
<div class="card"><div class="ct">FANBOYS<small>2 өгүүлбэрийг холбоно</small></div>{w(FAN)}
<div class="note">2 бүтэн өгүүлбэрийг холбохдоо өмнө нь таслал тавина: , and / , but</div></div>
<div class="card"><div class="ct">Хамааруулагч үг<small>Хэсгийг дангаараа зогсож чадахгүй болгоно</small></div>{w(SUB, 'sub')}
<div class="note">Эхэнд байж болно. Гэхдээ ард нь бүтэн өгүүлбэр ирэх ёстой.</div></div>''',
    # 3. the trap: one joining word per join
    f'''<div class="pill">УРХИ</div><div class="h" style="font-size:70px">1 холболтод<br><span class="blue">1 л холбоос үг</span></div>
<div class="card"><div class="tag n">2 ХОЛБООС ҮГ</div><div class="sen"><b>When</b> they catch sight of their prey, <s>and</s> peregrine falcons drop into a steep, swift dive at more than 200 miles an hour.</div>
<div class="note">When… хэсэг аль хэдийн таслалаар гол өгүүлбэртэй холбогдсон. and нэмбэл бүтэн өгүүлбэр үлдэхгүй.</div></div>
<div class="card"><div class="tag y">ЗӨВ</div><div class="sen"><b>When</b> they catch sight of their prey, peregrine falcons drop into a steep, swift dive…</div></div>
<div class="rule">When…, and… → and-ийг хас</div>''',
    # 4. question
    gen30.qslide(gen30.frame(2, PASSAGE, CH, prompt=PROMPT),
                 'Хоосон зайг алгасаад унш. Эзэн, үйл үг байна уу? Тэгвэл урд нь юу хэрэгтэй вэ?'),
    # 5. answer
    gen30.aslide('B) DELETE', 'Юу ч нэмэхгүй', [('ЭЗЭН', 'findings'), ('ҮЙЛ ҮГ', 'suggest')],
                 [('A) Although', 'Бүтэн өгүүлбэрийг бие даахгүй хэсэг болгоно. Араас нь гол өгүүлбэр ирэхгүй тул бүтэн биш өгүүлбэр үлдэнэ.'),
                  ('C) Because', 'Although-тай яг адил ажил хийнэ. Мөн бүтэн биш өгүүлбэр үүсгэнэ.'),
                  ('D) Since', 'Мөн адил. 3 ижил сонголт → 3-уулаа хасагдана.')],
                 'Ганц эзэн + үйл үгтэй өгүүлбэрийн урд хамааруулагч үг бүү нэм', sep='+'),
    # 6. end
    gen30.endp('Шинэ сэдэв удахгүй').replace('Дараагийн хичээл', 'Дараагийн пост').replace('<div style="color:#556">WhatsApp', '<div style="color:#556">Улаанбаатарын цагаар</div><div style="color:#556">WhatsApp'),
]


def page(C, n, T, body):
    return gen46.page(C, n, T, body).replace('SAT R&amp;W · НЭМЭЛТ МЭДЭЭЛЭЛ', 'SAT R&amp;W · ХОЛБООС ҮГ')


if __name__ == '__main__':
    gen32.render('--video' in sys.argv, key='Conjunctions', prefix='GMP-SAT-Conjunctions', pages=PAGES, cssf=css, pagef=page)
