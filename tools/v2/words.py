"""Content for the SAT multi-meaning word posts. Examples and quips are original GMP text.
Mongolian meanings are drafted by Claude and need Jg's review."""

# each expression: title, english meaning, mongolian, example, key phrase in example, bear quip, mood, prop emoji, sticker emoji, YOUR TURN question
def X(t, en, mg, ex, key, quip, mood, prop, stick, q): return dict(t=t, en=en, mg=mg, ex=ex, key=key, quip=quip, mood=mood, prop=prop, stick=stick, q=q)

WORDS = {}

WORDS['DRAW'] = dict(
  pov='POV: you think DRAW means making a picture ✏️', cover_em='✏️', hook='Нэг үг, 6 өөр утга!',
  exps=[
   X('DRAW A CONCLUSION', 'To decide something after thinking about the facts.', 'Дүгнэлт хийх', 'After reading the data, the team drew a conclusion.', 'drew a conclusion', 'I draw a conclusion: nap time.', 'think', '🧠', '💡', 'Did you know this one? Comment <b>YES</b> or <b>NO</b>'),
   X('DRAW ATTENTION TO', 'To make people notice something.', 'Анхаарлыг татах', 'The poster draws attention to the school sale.', 'draws attention to', 'Draw attention to me! I am cute.', 'point', '📢', '👀', 'What draws <b>your</b> attention first? 👇'),
   X('DRAW ON', 'To use knowledge or experience.', 'Туршлага, мэдлэгээ ашиглах', 'The author draws on her childhood memories.', 'draws on', 'I draw on my honey experience.', 'out', '📚', '🧠', 'Tag a friend who <b>draws on</b> notes before a test'),
   X('DRAWBACK', 'A bad side of something.', 'Сул тал', 'The main drawback of the plan is its cost.', 'drawback', 'Drawback: my honey jar is empty.', 'cost', '🍯', '😬', 'Name one <b>drawback</b> of homework 😅'),
   X('DRAW A DISTINCTION', 'To show the difference between two things.', 'Ялгааг тодруулах', 'The essay draws a distinction between speed and quality.', 'draws a distinction', 'I draw a distinction: honey, not jam.', 'point', '⚖️', '🤓', '<b>Save</b> this post for your SAT revision'),
   X('DRAW TO A CLOSE', 'To be ending, or to end.', 'Дуусах дөхөх', 'The meeting drew to a close at noon.', 'drew to a close', 'The movie draws to a close. More snacks!', 'sleepy', '🎬', '🏁', 'Which slide was your favourite? Comment <b>1 to 6</b>'),
  ],
  quiz=dict(word='draws on', sent='The historian draws on letters from soldiers to describe daily life.', key='draws on',
            opts=['makes a picture of', 'uses as a source', 'pulls with force'], ans='B', expl='“Draw on” = use something as a source.', quip='Careful! Nobody is making a picture here. ✏️'),
  cells=[('DECIDE', 'draw a conclusion', 'The team drew a conclusion.', 'дүгнэлт хийх'), ('USE', 'draw on', 'She draws on experience.', 'ашиглах'), ('NOTICE', 'draw attention to', 'It draws attention to the sale.', 'анхаарал татах'), ('FINISH', 'draw to a close', 'The talk drew to a close.', 'дуусах дөхөх')],
)

WORDS['ACCOUNT'] = dict(
  pov='POV: you think ACCOUNT is only about money 💰', cover_em='💰', hook='Нэг үг, 6 өөр утга!',
  exps=[
   X('ACCOUNT FOR (WHY)', 'To explain the reason for something.', 'Шалтгааныг тайлбарлах', 'Bad weather accounts for the low attendance.', 'accounts for', 'Rain accounts for my bad mood.', 'cost', '☔', '🤔', 'Did you know this one? Comment <b>YES</b> or <b>NO</b>'),
   X('ACCOUNT FOR (A SHARE)', 'To make up a part of a total.', 'Тодорхой хувийг эзлэх', 'Exports account for 40 percent of the company’s sales.', 'account for', 'Honey accounts for 90% of my diet.', 'happy', '🥧', '📊', 'What <b>accounts for</b> most of your day? 👇'),
   X('TAKE INTO ACCOUNT', 'To think about something before you decide.', 'Тооцоолох, анхаарч үзэх', 'The plan must take the cost into account.', 'take the cost into account', 'Take my nap into account, please.', 'sleepy', '😴', '🧐', 'Tag a friend who never <b>takes</b> time <b>into account</b>'),
   X('ON ACCOUNT OF', 'Because of.', '…-ын улмаас, учраас', 'The game was moved on account of the rain.', 'on account of', 'I stayed in on account of the rain.', 'please', '🏠', '🌧️', 'What do you skip <b>on account of</b> homework?'),
   X('AN ACCOUNT OF', 'A report or story of what happened.', 'Тайлан, түүх', 'She wrote an account of her trip to Japan.', 'an account of', 'My account of the honey theft: it was a bee.', 'shrug', '📖', '📝', '<b>Save</b> this post for your SAT revision'),
   X('BY ALL ACCOUNTS', 'According to what most people say.', 'Бүгдийн ярьж байгаагаар', 'By all accounts, the new teacher is excellent.', 'By all accounts', 'By all accounts, I am the cutest.', 'sun', '⭐', '🌟', 'Which slide was your favourite? Comment <b>1 to 6</b>'),
  ],
  quiz=dict(word='accounts for', sent='Tourism accounts for most of the island’s income.', key='accounts for',
            opts=['explains why', 'makes up a large part of', 'keeps a bank record of'], ans='B', expl='“Accounts for” + a number or share = makes up that part.', quip='Careful! This is not about a bank. 💳'),
  cells=[('EXPLAIN', 'account for', 'Rain accounts for the delay.', 'тайлбарлах'), ('SHARE', 'account for 40%', 'Exports account for 40%.', 'хувийг эзлэх'), ('CONSIDER', 'take into account', 'Take the cost into account.', 'тооцох'), ('REPORT', 'an account of', 'An account of her trip.', 'тайлан, түүх')],
)

WORDS['HOLD'] = dict(
  pov='POV: you think HOLD means to grab something ✋', cover_em='✋', hook='Нэг үг, 6 өөр утга!',
  exps=[
   X('HOLD TRUE', 'To still be correct.', 'Үнэн хэвээр байх', 'The rule holds true for every triangle.', 'holds true', 'It holds true: bears love honey.', 'out', '✅', '💯', 'Did you know this one? Comment <b>YES</b> or <b>NO</b>'),
   X('HOLD BACK', 'To stop yourself or something from moving forward.', 'Барьж зогсоох, ухрах', 'Fear held her back from speaking.', 'held her back', 'Fear held me back from the honey.', 'cost', '😨', '🛑', 'What <b>holds you back</b> the most? 👇'),
   X('HOLD UP', 'To stay strong when tested.', 'Тэсвэрлэх, бат бэх байх', 'The old bridge still holds up well.', 'holds up', 'This branch holds up well.', 'flex', '🌉', '💪', 'Tag a friend who <b>holds up</b> under stress'),
   X('HOLD A VIEW', 'To have an opinion.', 'Үзэл бодолтой байх', 'Many scientists hold the view that the climate is changing.', 'hold the view', 'I hold the view that naps are good.', 'think', '💭', '🗣️', 'Your view: <b>naps are good</b>. YES or NO?'),
   X('ON HOLD', 'Stopped for now.', 'Түр зогсоосон', 'The project is on hold until next month.', 'on hold', 'My dinner is on hold.', 'please', '⏸️', '⏳', '<b>Save</b> this post for your SAT revision'),
   X('HOLD OFF', 'To wait before doing something.', 'Хойшлуулах, хүлээх', 'We will hold off on the vote until Friday.', 'hold off', 'Hold off! The honey is hot.', 'point', '✋', '🔥', 'Which slide was your favourite? Comment <b>1 to 6</b>'),
  ],
  quiz=dict(word='holds up', sent='Her argument holds up under close study.', key='holds up',
            opts=['lifts into the air', 'stays strong when tested', 'waits for a while'], ans='B', expl='“Holds up” = stays strong when it is tested.', quip='Careful! Nothing is being lifted. 🏋️'),
  cells=[('STAY TRUE', 'hold true', 'The rule holds true.', 'үнэн хэвээр байх'), ('STAY STRONG', 'hold up', 'The bridge holds up.', 'тэсвэрлэх'), ('STOP', 'hold back', 'Fear held her back.', 'барьж зогсоох'), ('WAIT', 'hold off', 'Hold off on the vote.', 'хойшлуулах')],
)

WORDS['SUPPORT'] = dict(
  pov='POV: you think SUPPORT only means to help 🏗️', cover_em='🏗️', hook='Нэг үг, 6 өөр утга!',
  exps=[
   X('SUPPORT A CLAIM', 'To give proof that an idea is true.', 'Санааг нотлох, баталгаа өгөх', 'The data support the author’s claim.', 'support', 'The data support my honey theory.', 'out', '📊', '🔬', 'Did you know this one? Comment <b>YES</b> or <b>NO</b>'),
   X('SUPPORT A WEIGHT', 'To hold something up so it does not fall.', 'Даах, дэмжин барих', 'Four columns support the roof.', 'support the roof', 'These columns support the roof.', 'flex', '🏛️', '💪', 'What <b>supports</b> you every day? 👇'),
   X('SUPPORT A FAMILY', 'To give money for food and a home.', 'Гэр бүлээ тэжээх', 'She works two jobs to support her family.', 'support her family', 'I support my family with honey.', 'happy', '👨‍👩‍👧', '🏡', 'Tag someone who <b>supports</b> a whole family'),
   X('IN SUPPORT OF', 'For, on the side of.', 'Талд нь, дэмжиж', 'Hundreds marched in support of the new law.', 'in support of', 'I march in support of snacks.', 'point', '📣', '🚩', 'What would you march <b>in support of</b>?'),
   X('SUPPORTING EVIDENCE', 'Facts that help prove a point.', 'Нотлох баримт', 'The essay needs more supporting evidence.', 'supporting evidence', 'Supporting evidence: honey is sticky.', 'out', '🔎', '🧪', '<b>Save</b> this post for your SAT revision'),
   X('EMOTIONAL SUPPORT', 'Kind help for someone’s feelings.', 'Сэтгэл санааны дэмжлэг', 'Friends give emotional support in hard times.', 'emotional support', 'Emotional support: one big hug.', 'happy', '🤗', '❤️', 'Which slide was your favourite? Comment <b>1 to 6</b>'),
  ],
  quiz=dict(word='supports', sent='The new study supports the theory.', key='supports',
            opts=['holds up a heavy thing', 'gives evidence that it is true', 'pays the costs of it'], ans='B', expl='A study that “supports” a theory gives evidence for it.', quip='Careful! No one is lifting anything. 🏗️'),
  cells=[('PROVE', 'support a claim', 'The data support the claim.', 'нотлох'), ('HOLD UP', 'support the roof', 'Columns support the roof.', 'даах'), ('PROVIDE', 'support a family', 'She supports her family.', 'тэжээх'), ('BACK', 'in support of', 'They marched in support of it.', 'дэмжиж')],
)

WORDS['ADDRESS'] = dict(
  pov='POV: you think ADDRESS is only where you live 🏠', cover_em='🏠', hook='Нэг үг, 6 өөр утга!',
  exps=[
   X('ADDRESS A PROBLEM', 'To start dealing with a problem.', 'Асуудлыг шийдвэрлэх', 'The city must address the traffic problem.', 'address the traffic problem', 'The city must address the bees.', 'please', '🐝', '🛠️', 'Did you know this one? Comment <b>YES</b> or <b>NO</b>'),
   X('ADDRESS AN AUDIENCE', 'To speak to a group of people.', 'Үзэгчдэд хандаж үг хэлэх', 'The principal addressed the whole school.', 'addressed the whole school', 'I address the forest: I am hungry!', 'point', '🎤', '🗣️', 'Would you <b>address</b> a big crowd? YES or NO'),
   X('ADDRESS A CONCERN', 'To answer a worry.', 'Санаа зовнилд хариу өгөх', 'The report addresses parents’ concerns.', 'addresses parents’ concerns', 'I address your concern: yes, snacks.', 'out', '💬', '🤝', 'Tag a friend who <b>addresses</b> every concern'),
   X('ADDRESS A LETTER', 'To write who a letter is for.', 'Захидал хаяглах', 'She addressed the envelope to her aunt.', 'addressed the envelope', 'I address a letter to Mama Bear.', 'happy', '✉️', '📮', '<b>Save</b> this post for your SAT revision'),
   X('ADDRESS SOMEONE AS', 'To call a person by a name or title.', '…гэж дуудах, хандах', 'Students address the teacher as “Ms. Lee”.', 'address the teacher as', 'Please address me as Sir Honey.', 'sun', '🎩', '👑', 'How do you <b>address</b> your teacher? 👇'),
   X('HOME ADDRESS', 'The place where someone lives.', 'Оршин суугаа хаяг', 'Write your home address on the form.', 'home address', 'My home address: the big cave.', 'shrug', '🏔️', '🏠', 'Which slide was your favourite? Comment <b>1 to 6</b>'),
  ],
  quiz=dict(word='addresses', sent='The article addresses the problem of plastic waste.', key='addresses',
            opts=['writes a letter to', 'deals with', 'lives at'], ans='B', expl='“Addresses a problem” = starts dealing with it.', quip='Careful! No one is writing a letter. ✉️'),
  cells=[('DEAL WITH', 'address a problem', 'Address the traffic problem.', 'шийдвэрлэх'), ('SPEAK TO', 'address an audience', 'She addressed the school.', 'хандаж үг хэлэх'), ('WRITE TO', 'address a letter', 'Address the envelope.', 'хаяглах'), ('CALL', 'address someone as', 'Address her as “Ms. Lee”.', 'гэж дуудах')],
)

WORDS['FIGURE'] = dict(
  pov='POV: you think FIGURE means a number 🔢', cover_em='🔢', hook='Нэг үг, 6 өөр утга!',
  exps=[
   X('FIGURE OUT', 'To find the answer or understand.', 'Олж мэдэх, бодож гаргах', 'I finally figured out the puzzle.', 'figured out', 'I figured out the honey puzzle.', 'think', '🧩', '💡', 'Did you know this one? Comment <b>YES</b> or <b>NO</b>'),
   X('FIGURE OF SPEECH', 'Words used in a creative way, not word for word.', 'Дүрслэлт хэллэг', '“Time is money” is a figure of speech.', 'figure of speech', 'Honey is life: a figure of speech.', 'happy', '🗣️', '✨', 'Write your own <b>figure of speech</b> 👇'),
   X('PUBLIC FIGURE', 'A well-known person.', 'Олонд танигдсан хүн', 'The mayor is a public figure.', 'public figure', 'I am a public figure now.', 'sun', '⭐', '📸', 'Who is your favourite <b>public figure</b>?'),
   X('THE FIGURES', 'Numbers in facts, reports or charts.', 'Тоон мэдээлэл, үзүүлэлт', 'The figures show that sales rose 12 percent.', 'The figures', 'The figures show I ate 12 jars.', 'cost', '📈', '🔢', '<b>Save</b> this post for your SAT revision'),
   X('FIGURE PROMINENTLY', 'To be an important part of something.', 'Чухал байр суурь эзлэх', 'Honesty figures prominently in the novel.', 'figures prominently', 'Snacks figure prominently in my day.', 'happy', '🍪', '🥇', 'What <b>figures prominently</b> in your day?'),
   X('A FIGURE IN A PICTURE', 'A person or shape you can see.', 'Дүр, дүрс', 'The small figure in the painting is a girl.', 'small figure', 'The small figure in the painting is me.', 'point', '🖼️', '🎨', 'Which slide was your favourite? Comment <b>1 to 6</b>'),
  ],
  quiz=dict(word='figures prominently', sent='Music figures prominently in her stories.', key='figures prominently',
            opts=['is counted as a number', 'plays an important part', 'is drawn as a shape'], ans='B', expl='“Figures prominently” = plays an important part.', quip='Careful! There is no maths here. 🔢'),
  cells=[('SOLVE', 'figure out', 'I figured out the puzzle.', 'олж мэдэх'), ('PERSON', 'public figure', 'The mayor is a public figure.', 'олонд танигдсан хүн'), ('NUMBERS', 'the figures', 'The figures show a rise.', 'тоон мэдээлэл'), ('ROLE', 'figure prominently', 'It figures prominently.', 'чухал байр эзлэх')],
)

WORDS['CHARGE'] = dict(
  pov='POV: you think CHARGE is only for phones 🔋', cover_em='🔋', hook='Нэг үг, 6 өөр утга!',
  exps=[
   X('CHARGE A FEE', 'To ask for money for something.', 'Хураамж авах', 'The museum charges ten dollars.', 'charges ten dollars', 'The cave charges ten dollars.', 'cost', '💵', '🎟️', 'Did you know this one? Comment <b>YES</b> or <b>NO</b>'),
   X('IN CHARGE', 'Responsible for; in control of.', 'Хариуцсан, эрхлэгч', 'Who is in charge of the club?', 'in charge', 'I am in charge of the honey.', 'flex', '👑', '😎', 'Who is <b>in charge</b> at your home? 👇'),
   X('TAKE CHARGE', 'To start leading.', 'Удирдаж эхлэх', 'She took charge of the project.', 'took charge', 'I take charge: everyone, dinner!', 'point', '🍽️', '📣', 'Tag a friend who always <b>takes charge</b>'),
   X('CHARGE WITH (A CRIME)', 'To officially say that someone committed a crime.', 'Буруутгах, яллах', 'Police charged him with theft.', 'charged him with theft', 'They charged me with cookie theft.', 'please', '🚔', '😱', '<b>Save</b> this post for your SAT revision'),
   X('CHARGE A PHONE', 'To fill a battery with power.', 'Цэнэглэх', 'I need to charge my phone.', 'charge my phone', 'Charge me! I am at 1 percent.', 'sleepy', '🔋', '🔌', 'What is your phone battery now? Comment <b>%</b>'),
   X('CHARGE AHEAD', 'To go ahead boldly.', 'Давшин гарах', 'The team charged ahead with the plan.', 'charged ahead', 'Charge ahead! Honey is near.', 'wow', '🏃', '🚀', 'Which slide was your favourite? Comment <b>1 to 6</b>'),
  ],
  quiz=dict(word='charges', sent='The company charges a fee for late returns.', key='charges',
            opts=['attacks', 'asks for payment', 'fills with power'], ans='B', expl='“Charges a fee” = asks for money.', quip='Careful! No batteries here. 🔋'),
  cells=[('PAY', 'charge a fee', 'It charges ten dollars.', 'хураамж авах'), ('LEAD', 'take charge', 'She took charge.', 'удирдах'), ('ACCUSE', 'charge with', 'He was charged with theft.', 'буруутгах'), ('POWER', 'charge a phone', 'Charge my phone.', 'цэнэглэх')],
)

WORDS['MAINTAIN'] = dict(
  pov='POV: you think MAINTAIN only means to fix 🔧', cover_em='🔧', hook='Нэг үг, 6 өөр утга!',
  exps=[
   X('MAINTAIN THAT', 'To say firmly that something is true.', 'Үнэн гэж батлан хэлэх', 'She maintains that the plan is fair.', 'maintains that', 'I maintain that honey is a fruit.', 'point', '🍯', '🗞️', 'Did you know this one? Comment <b>YES</b> or <b>NO</b>'),
   X('MAINTAIN A BRIDGE', 'To keep it in good condition.', 'Засварлан хадгалах', 'Workers maintain the old bridge.', 'maintain the old bridge', 'I maintain my cave every spring.', 'flex', '🛠️', '🏗️', 'What do you <b>maintain</b> every day? 👇'),
   X('MAINTAIN A PACE', 'To keep the same speed.', 'Хурдаа хэвээр барих', 'Runners must maintain a steady pace.', 'maintain a steady pace', 'Maintain your pace, bear!', 'happy', '🏃', '⏱️', 'Tag a friend who <b>maintains</b> a good pace'),
   X('MAINTAIN CONTACT', 'To stay in touch.', 'Холбоо тогтмол барих', 'They maintain contact by email.', 'maintain contact', 'We maintain contact by email.', 'out', '📧', '🤝', '<b>Save</b> this post for your SAT revision'),
   X('MAINTAIN ORDER', 'To keep things calm and safe.', 'Дэг журам сахих', 'Guards maintain order in the hall.', 'maintain order', 'I maintain order in the forest.', 'sun', '👮', '🛡️', 'Who <b>maintains order</b> in your class?'),
   X('MAINTAIN INNOCENCE', 'To keep saying you did not do it.', 'Гэм буруугүй гэдгээ хэлсээр байх', 'He maintains his innocence.', 'maintains his innocence', 'I maintain my innocence: no cookies!', 'please', '🍪', '😇', 'Which slide was your favourite? Comment <b>1 to 6</b>'),
  ],
  quiz=dict(word='maintains', sent='The author maintains that cities should grow slowly.', key='maintains',
            opts=['repairs', 'states firmly', 'keeps running'], ans='B', expl='“Maintains that” = states firmly that it is true.', quip='Careful! Nothing is broken here. 🔧'),
  cells=[('SAY', 'maintain that', 'She maintains that it is fair.', 'батлан хэлэх'), ('UPKEEP', 'maintain a bridge', 'Maintain the old bridge.', 'засварлах'), ('KEEP', 'maintain a pace', 'Maintain a steady pace.', 'хэвээр барих'), ('KEEP ORDER', 'maintain order', 'Guards maintain order.', 'дэг журам сахих')],
)

WORDS['TRACE'] = dict(
  pov='POV: you think TRACE means to copy a drawing 🔍', cover_em='🔍', hook='Нэг үг, 6 өөр утга!',
  exps=[
   X('TRACE THE ORIGIN', 'To find where something started.', 'Эх сурвалжийг олох', 'Scientists trace the virus to a market.', 'trace the virus', 'Trace the origin of the honey.', 'out', '🔍', '🕵️', 'Did you know this one? Comment <b>YES</b> or <b>NO</b>'),
   X('A TRACE OF', 'A very small amount.', 'Бага зэрэг, ор мөр', 'There was a trace of sadness in his voice.', 'a trace of sadness', 'A trace of honey on my nose.', 'shrug', '👃', '🤏', 'Name something with <b>a trace of</b> sugar 👇'),
   X('TRACE BACK TO', 'To come from an earlier time or cause.', 'Эх үүсвэр нь …', 'The word traces back to Latin.', 'traces back to Latin', 'This word traces back to Latin.', 'think', '🏛️', '📜', 'Tag a friend who loves <b>word origins</b>'),
   X('TRACE A PATH', 'To follow a route step by step.', 'Замыг мөшгөх', 'Detectives trace the thief’s path.', 'trace the thief’s path', 'I trace the paw prints.', 'point', '🐾', '🗺️', '<b>Save</b> this post for your SAT revision'),
   X('TRACE A DRAWING', 'To copy lines through thin paper.', 'Хуулан зурах', 'She traced the map onto thin paper.', 'traced the map', 'I traced the map onto paper.', 'flex', '🗺️', '✏️', 'Do you <b>trace</b> or draw freehand? Comment <b>TRACE</b> or <b>FREE</b>'),
   X('WITHOUT A TRACE', 'Leaving no sign at all.', 'Ор мөргүй', 'The ship vanished without a trace.', 'without a trace', 'The honey vanished without a trace.', 'wow', '💨', '👻', 'Which slide was your favourite? Comment <b>1 to 6</b>'),
  ],
  quiz=dict(word='trace', sent='Historians trace the tradition back to the 1600s.', key='trace',
            opts=['draw over', 'find the starting point of', 'hide'], ans='B', expl='“Trace back to” = find where it started.', quip='Careful! Nobody is drawing here. 🔍'),
  cells=[('FIND', 'trace the origin', 'Trace the virus to a market.', 'эх сурвалжийг олох'), ('SMALL', 'a trace of', 'A trace of sadness.', 'бага зэрэг'), ('COPY', 'trace a drawing', 'She traced the map.', 'хуулан зурах'), ('FOLLOW', 'trace a path', 'Trace the thief’s path.', 'замыг мөшгөх')],
)
