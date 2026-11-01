"""SAT R&W: comma splices. A comma alone can never join two sentences; comma + pronoun or comma + time word is the warning sign. One post, 6 slides.
Content verbatim from sat-writing-joining-lesson.html (GMP module, Ch 4 Joining), screens 'Three legal joints'
(the four joints, 'The museum closed at noon, the staff stayed late.') and 'Comma splices' (two warning signs,
adverb/time-word list), with poll q7 (Euripides, answer D 'drama. He is particularly known') and its notes."""
import sys
import gen30, gen32, gen46

AC, SOFT, TINT = '#166534', '#dcefe2', '#f4faf6'   # forest green (new colour, not used by recent posts)
GREEN = '#15803d'; RED = '#c62828'

EXTRA = gen46.EXTRA.replace('#a16207', AC) + """
.words{display:flex;flex-wrap:wrap;gap:10px;margin-top:12px}
.words span{font-family:S,serif;font-size:31px;border-radius:12px;padding:5px 14px;background:#eef0f4;color:#334;font-weight:700}
.ct{font-size:34px;font-weight:900}
.jt{display:flex;align-items:center;gap:22px;padding:12px 0;border-top:2px dashed #e0e3ef}
.jt:first-child{border-top:0}
.jt .mk{flex:none;width:130px;text-align:center;font-family:S,serif;font-size:44px;font-weight:700;color:""" + AC + """}
.jt .tx{font-size:31px;font-weight:700;line-height:1.3}
.jt .ic{margin-left:auto;font-size:38px;font-weight:900}
.rwp{font-size:31px!important;line-height:1.45!important}
.bxc div{font-size:29px!important;padding:8px 16px!important}
.jt.no .mk{color:""" + RED + """}
"""


def css():
    return gen30.css(AC, SOFT, TINT) + EXTRA


PROMPT = 'Which choice completes the text so that it conforms to the conventions of Standard English?'
PASSAGE = ('Euripides is identified with many theatrical innovations that have profoundly influenced modern _____ '
           'for the representation of heroes as ordinary people who find themselves in extraordinary circumstances.')
CH = ['drama; and he is particularly known', 'drama, he is particularly known', 'drama particularly being known',
      'drama. He is particularly known']

JOINTS = [('. ;', 'Цэг эсвэл цэг таслал', '✓', ''), (', and', 'Таслал + FANBOYS', '✓', ''),
          (': —', 'Хоёр цэг эсвэл зураас: 2 дахь өгүүлбэр эхнийхээ тайлбар бол', '✓', ''), (',', 'Таслал дангаараа: хэзээ ч болохгүй', '✗', 'no')]
jt = ''.join(f'<div class="jt {c}"><span class="mk">{a}</span><span class="tx">{b}</span><span class="ic" style="color:{RED if c else GREEN}">{i}</span></div>' for a, b, i, c in JOINTS)
TIME = ['however', 'moreover', 'therefore', 'thus', 'meanwhile', 'still', 'today', 'currently', 'later', 'then', 'next', 'finally']

PAGES = [
    # 1. cover
    gen30.cover('SAT R&amp;W · 2 ӨГҮҮЛБЭР ХОЛБОХ',
                'Таслалын ард<br><span class="blue">he</span> байвал<br>сэжиглэ',
                'Таслал дангаараа 2 бүтэн өгүүлбэрийг холбож чадахгүй. Үүнийг comma splice гэдэг.',
                [', he', ', today', '. эсвэл ;'], '1f6a7').replace('font-size:104px', 'font-size:94px'),
    # 2. the idea: three legal joints
    f'''<div class="pill">ГОЛ САНАА</div><div class="h" style="font-size:66px">2 өгүүлбэрийг<br><span class="blue">зөв холбох 3 арга</span></div>
<div class="card" style="padding:8px 26px">{jt}</div>
<div class="card"><div class="tag n">COMMA SPLICE</div><div class="sen">The museum closed at noon<span style="color:{RED};font-weight:700">,</span> the staff stayed late.</div>
<div class="note">2 бүтэн өгүүлбэр, дунд нь зөвхөн таслал. Буруу.</div></div>''',
    # 3. two warning signs
    f'''<div class="pill">2 ДОХИО</div><div class="h" style="font-size:66px">Comma splice-ийг<br><span class="blue">хурдан олох</span></div>
<div class="card"><div class="ct">, + it / he / she / they</div>
<div class="sen" style="margin-top:8px">…influenced modern drama<b style="color:{RED}">, he</b> is particularly known…</div>
<div class="note">Таслалын 2 талд бүтэн өгүүлбэр байвал таслал цэгийн ажил хийж байна. Comma splice гэж сэжиглэ.</div></div>
<div class="card"><div class="ct">Дайвар үг, цаг заасан үг</div>{''.join([])}<div class="words">{''.join(f'<span>{x}</span>' for x in TIME)}</div>
<div class="note">Шинэ бүтэн өгүүлбэр эхлүүлж байвал өмнө нь . эсвэл ; хэрэгтэй.</div></div>''',
    # 4. question
    gen30.qslide(gen30.frame(7, PASSAGE, CH, prompt=PROMPT),
                 'Хоосон зайн 2 талд бүтэн өгүүлбэр байна уу?'),
    # 5. answer
    gen30.aslide('D) drama. He', '2 өгүүлбэр, цэгээр', [('ӨГҮҮЛБЭР 1', 'Euripides is identified with… modern drama.'), ('ӨГҮҮЛБЭР 2', 'He is particularly known for…')],
                 [('A) ; and he', 'SAT-д цэг таслалын ард FANBOYS тавьдаггүй. Харсан даруйдаа хас.'),
                  ('B) , he', 'Таслал + he. Comma splice.'),
                  ('C) being known', 'Цэг ч, таслал ч алга, being нь өгүүлбэрийг эвдэнэ.')],
                 'Таслал + he → цэг эсвэл цэг таслалтай (FANBOYS-гүй) сонголтыг хай', sep='.'),
    # 6. end
    gen30.endp('Шинэ сэдэв удахгүй').replace('Дараагийн хичээл', 'Дараагийн пост').replace('<div style="color:#556">WhatsApp', '<div style="color:#556">Улаанбаатарын цагаар</div><div style="color:#556">WhatsApp'),
]


def page(C, n, T, body):
    return gen46.page(C, n, T, body).replace('SAT R&amp;W · НЭМЭЛТ МЭДЭЭЛЭЛ', 'SAT R&amp;W · COMMA SPLICE')


if __name__ == '__main__':
    gen32.render('--video' in sys.argv, key='Comma-Splice', prefix='GMP-SAT-Comma-Splice', pages=PAGES, cssf=css, pagef=page)
