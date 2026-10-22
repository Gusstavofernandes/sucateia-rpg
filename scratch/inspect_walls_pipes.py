import re

with open('fundo_ferro_standalone/scenes/fundo_ferro_master.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

def inspect_group(group_name):
    print(f"\n==================== {group_name} ====================")
    pattern = rf'\[node name="([^"]+)" type="([^"]+)" parent="[^"]*{group_name}[^"]*"\]([^\[]*)'
    matches = re.findall(pattern, text)
    for name, ntype, body in matches:
        print(f"Node: {name} ({ntype})")
        for line in body.splitlines()[:6]:
            if any(k in line for k in ['position', 'scale', 'texture', 'z_index']):
                print(f"   {line.strip()}")

inspect_group("MuralhaNorte")
inspect_group("TuboParedeOesteModular")
inspect_group("PisoBaseGeral")
