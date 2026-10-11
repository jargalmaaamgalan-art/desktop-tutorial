import sys
from PIL import Image
w=sys.argv[1]; pick=[int(x) for x in sys.argv[2].split(',')] if len(sys.argv)>2 else list(range(1,10))
d=f'out30-W-{w}/GMP-SATWords-{w}-'
ims=[Image.open(f'{d}{i:02d}-of-09.png').resize((540,675)) for i in pick]
cols=3; rows=(len(ims)+2)//3
W=Image.new('RGB',(540*cols,675*rows),'white')
for k,im in enumerate(ims): W.paste(im,((k%cols)*540,(k//cols)*675))
W.save(f'/tmp/claude-0/-home-claude/7b9b247d-7185-5faa-ae2d-e13a2742cc61/scratchpad/sheet_{w}.png')
