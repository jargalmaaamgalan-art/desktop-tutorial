# Run next to reel-exam.py saved as exam.py (scratchpad reel folder). 
"""Builds nov1.py (the 1 November checklist Reel) from the exam-paper builder exam.py.
Facts: research_notes/Full aid for international students/testing_and_deadlines.md (official pages, checked 2026-10-06)."""
import re
s = open('exam.py').read()
a = s.index('ST = ['); b = s.index('\n', a)
s = s[:a] + 'ST = [0, 2.6, 6.6, 11.4, 14.8, 18.0, 21.6, 25.2]; DUR = 28.6' + s[b:]

PAGES = r'''PAGES = [
 # 0 hook
 f\'\'\'<div class="top"><span>ЭРТ ӨРГӨДӨЛ · 2027 ЭЛСЭЛТ</span><span>30 сек</span></div>
 <div class="rule"></div>
 <div class="hook"><u class="mk">11-р сарын 1</u> бол оны хамгийн <span class="red">чухал</span> өдөр</div>
 <div class="hw w1" data-t="0.9" data-d="1.0" style="font-size:80px;white-space:nowrap">Яагаад? → дуустал нь үз</div>\'\'\',
 # 1 early deadline
 f\'\'\'<div class="q"><b>1</b><span>Эрт өргөдлийн (Early) эцсийн хугацаа хэзээ вэ?</span><i>[1]</i></div>
 <div class="hw" data-t="0.4" data-d="0.8">11-р сарын 1</div>
 <div class="tk" data-t="1.3">{TICK}</div>
 <div class="note" data-t="1.6">Harvard · MIT · Yale · Princeton · Stanford · Cornell</div>
 <div class="note" data-t="2.4" style="font-size:44px;color:#555">Ихэнх сургуулийн Early өргөдөл энэ өдөр хаагдана.</div>\'\'\',
 # 2 aid forms have their own dates
 f\'\'\'<div class="q"><b>2</b><span>Тэтгэлгийн маягтын эцсийн хугацаа ижил үү?</span><i>[2]</i></div>
 <div class="hw" data-t="0.3" data-d="0.8">Үгүй! Өөр өөр.</div>
 <div class="rows">
  <div class="note" data-t="1.3"><b>Harvard</b><span>11-р сарын 1</span></div>
  <div class="note" data-t="1.7"><b>Cornell</b><span>11-р сарын 1</span></div>
  <div class="note" data-t="2.1"><b>Princeton</b><span>11-р сарын 9</span></div>
  <div class="note" data-t="2.5"><b>MIT</b><span>11-р сарын 30</span></div>
  <div class="note" data-t="2.7"><b>Stanford</b><span>11-р сарын 15</span></div>
  <div class="note" data-t="2.9"><b>Yale</b><span>12-р сарын 1</span></div>
 </div>
 <div class="src" data-t="3.1">Early үеийн, олон улсын сурагчийн огноо.</div>\'\'\',
 # 3 Cornell hard cut-off
 f\'\'\'<div class="q"><b>3</b><span>Тэтгэлгийн маягтаа хугацаанаас нь хоцроовол?</span><i>[1]</i></div>
 <div class="hw" data-t="0.3" data-d="1.1">Cornell: бакалаврын бүх хугацаанд тэтгэлэг хүсэх эрхгүй.</div>
 <div class="note" data-t="1.6"><span class="red">Огноогоо</span> заавал тэмдэглэ.</div>\'\'\',
 # 4 Princeton
 f\'\'\'<div class="q"><b>4</b><span>Princeton CSS Profile хүлээж авдаг уу?</span><i>[1]</i></div>
 <div class="hw" data-t="0.3" data-d="0.6">Үгүй.</div>
 <div class="tk" data-t="0.9">{TICK}</div>
 <div class="hw" data-t="1.2" data-d="0.9">Өөрийн үнэгүй маягттай.</div>\'\'\',
 # 5 after admission
 f\'\'\'<div class="q"><b>5</b><span>Bowdoin, Swarthmore?</span><i>[1]</i></div>
 <div class="hw" data-t="0.3" data-d="1.0">Тэтгэлгийн баримтаа тэнцсэний дараа өгнө.</div>
 <div class="note" data-t="1.6">Тэнцсэнээс хойш <span class="red">7 хоногийн дотор</span>. Гэхдээ өргөдөл дээрээ тэтгэлэг хүсэхээ тэмдэглэ.</div>\'\'\',
 # 6 Анхаар
 f\'\'\'<div class="info"><div class="ih">АНХААР</div>
 <p data-t="0.3">• Тэтгэлэг хэрэгтэй бол өргөдөл өгөхдөө <b>заавал</b> хүс. Хэд хэдэн сургууль дараа нь хүсэхийг зөвшөөрдөггүй.</p>
 <p data-t="1.2">• Огноо жил бүр <b>өөрчлөгдөж</b> болно. Сургууль бүрийн сайтыг шалга.</p></div>
 <div class="src" data-t="2.0">Эх сурвалж: сургууль бүрийн албан ёсны admissions болон financial aid хуудас, 2026.10.06-нд шалгасан.</div>\'\'\',
 # 7 end
 f\'\'\'<div class="q"><b>6</b><span>Чи аль сургуульд Early өгөх вэ?</span><i></i></div>
 <div class="hw" data-t="0.3" data-d="0.9">Harvard? MIT? Yale?</div>
 <div class="cta" data-t="1.2"><span class="p1">Коммент бичээрэй</span><span class="p2">Хадгалаад, найздаа илгээгээрэй</span></div>
 <div class="disc" data-t="1.2">Developed independently by Global Math Prep. Not affiliated with or endorsed by any university named. Deadlines checked on official university pages on 6 Oct 2026 and may change.<br>Огноог 2026.10.06-нд албан ёсны сайтаас шалгасан, өөрчлөгдөж болно.</div>\'\'\',
]
'''
PAGES = PAGES.replace("\\'", "'")
a = s.index('PAGES = ['); b = s.index('\n]\n', a) + 3
s = s[:a] + PAGES + s[b:]
s = s.replace("<span>{i+1} / 9</span>", "<span>{i+1} / {len(PAGES)}</span>")
# a small table style for page 2, and this post's own colour (deep green desk)
s = s.replace(".src{{font:400 34px/1.3 S;color:#555;", ".src{{font:400 36px/1.3 S;color:#333;").replace(".disc{{position:absolute;left:130px;right:100px;bottom:200px;font:400 27px/1.35 S;color:#666;", ".disc{{position:absolute;left:130px;right:100px;bottom:200px;font:400 30px/1.35 S;color:#444;")
s = s.replace("'''\nJS = f'''", ".rows{{margin-top:28px;display:grid;gap:4px}}\n.rows .note{{display:grid;grid-template-columns:330px 1fr;margin-top:0;font-size:56px;border-bottom:2px dashed #c9ccd2;padding-bottom:4px}}\n.rows .note b{{font:800 56px S}}\n'''\nJS = f'''", 1)
s = s.replace(".desk{{position:absolute;inset:0;background:radial-gradient(ellipse 90% 60% at 50% 45%,#34404f,#1a2029 80%)}}",
              ".desk{{position:absolute;inset:0;background:radial-gradient(ellipse 90% 60% at 50% 45%,#1f5a4c,#0f2a24 80%)}}")
# cover
a = s.index("<div class=\"top\"><span>КРЕДИТ · ЖИШЭЭ ХУУДАС</span><span>7 асуулт</span>"); b = s.index("</div></div>{bhtml}</body></html>'''", a)
s = s[:a] + '''<div class="top"><span>ЭРТ ӨРГӨДӨЛ · 2027 ЭЛСЭЛТ</span><span>6 асуулт</span></div><div class="rule"></div>
<div class="lab">HARVARD · MIT · YALE</div>
<div class="ttl"><span class="red">11-р сарын 1</span>: оны хамгийн чухал өдөр</div>
<div class="sub">Early өргөдөл + тэтгэлгийн маягтын огноо</div>''' + s[b:]
s = s.replace(".lab{{display:inline-block;background:#ff9a1f;", ".lab{{display:inline-block;background:#2bb38f;")
s = s.replace("pg.screenshot(path='exam-cover.png')", "pg.screenshot(path='nov1-cover.png')")
s = s.replace("for t in (2.3, 5.9, 9.7, 13.9, 17.3, 20.3, 23.3, 26.3, 29.4):", "for t in [x - 0.3 for x in ST[1:]] + [DUR - 0.2]:")
s = s.replace("pg.screenshot(path=f'ex_{t}.png')", "pg.screenshot(path=f'n1_{round(t,1)}.png')")
s = s.replace("'framesX'", "'framesN1'").replace("f'framesX/f{i:04d}.png'", "f'framesN1/f{i:04d}.png'")
open('nov1.py', 'w').write(s)
print('ok')
