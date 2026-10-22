from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]
path=root/'maps/sucateia/sucateia.tscn'
before=(root/'tools/checkpoints/sucateia_before_cabos.tscn').read_text(encoding='utf-8-sig')
current=path.read_text(encoding='utf-8-sig')
headers=lambda text:list(re.finditer(r'^\[node [^\n]+\]$',text,re.M))
old=headers(before);new=headers(current)
assert len(new)>len(old)
extract=lambda line,key: re.search(r'\b'+key+r'="([^"]+)"',line).group(1) if re.search(r'\b'+key+r'="([^"]+)"',line) else None
pieces=[];start=0;changed=0
for original,now in zip(old,new):
    a=original.group();b=now.group()
    assert extract(a,'type')==extract(b,'type'),(a,b)
    if not extract(a,'name').startswith('@'):
        assert extract(a,'name')==extract(b,'name'),(a,b)
    fixed=b
    for key in ['name','parent']:
        value=extract(a,key)
        if value is not None:fixed=re.sub(r'\b'+key+r'="[^"]+"',lambda m:key+'="'+value+'"',fixed)
    pieces.append(current[start:now.start()]+fixed);start=now.end();changed+=fixed!=b
assert extract(new[len(old)].group(),'name')=='CabosDistrict','New district is not appended after approved node tree'
pieces.append(current[start:]);path.write_text(''.join(pieces),encoding='utf-8')
print('PASS: restored',changed,'approved serialized paths by verified node order; transforms/materials/physics untouched')
