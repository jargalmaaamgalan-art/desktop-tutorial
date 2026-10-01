import re, pathlib, json
import gen4
B={'M500':'952ad6239d7de2a4ee44367ca3a2ff5f','M600':'7385193ff25ef5408962bd2ac73472b9','M700':'09916d3ed87976b40b83050756f78f92','M800':'eb69af5fbf1142a865a3491d50c77b43',
'S400':'971f8c60c575fa4ff2381fc7321ea24c','S400i':'b2f1d841dcba9d11540101f6c9430bfa','S600':'1a6b1bef9bd4ffa8e9eb2268a80e49b0','S700':'a447d2a5f96b3926c1d81c1e98643c48'}
fonts=''.join(f"@font-face{{font-family:M;font-weight:{w};src:url(/_blob/{B['M'+str(w)]}) format('woff2')}}" for w in (500,600,700,800))
fonts+=''.join(f"@font-face{{font-family:S;font-weight:{w};font-style:normal;src:url(/_blob/{B['S'+str(w)]}) format('woff2')}}" for w in (400,600,700))
fonts+=f"@font-face{{font-family:S;font-weight:400;font-style:italic;src:url(/_blob/{B['S400i']}) format('woff2')}}"
css=gen4.CSS.replace(gen4.ff,fonts)
QRB='/_blob/54da824498fd9f633b694a9167126e50'
out=pathlib.Path('../canvas4/project'); out.mkdir(parents=True,exist_ok=True)
names=[]
for i,body in enumerate(gen4.S,1):
    html=gen4.page(i,len(gen4.S),body)
    inner=html.split('<body>')[1].split('</body>')[0]
    inner=inner.replace(gen4.QR,QRB)
    inner=re.sub(r'<(path|circle|ellipse|rect|line)([^<>]*?)\s*/>',r'<\1\2></\1>',inner)
    doc=f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Ch1 v4 · {i:02d} of 08</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<style>
{css}
</style>
</helmet>
{inner}
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1080,"height":1350}}}}'>
class Component extends DCLogic {{
renderVals() {{ return {{}}; }}
}}
</script>
</body>
</html>
'''
    assert "'" not in doc.split("data-props='")[1].split("'")[0]
    n=f'C1v4-{i:02d}.dc.html'; (out/n).write_text(doc); names.append(n)
print(names, len(doc))
