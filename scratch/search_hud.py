import os

for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.gd') or f.endswith('.tscn') or f.endswith('.json') or f.endswith('.txt'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as file:
                c = file.read()
                if 'PASSARELA' in c.upper() or 'OS CABOS' in c.upper() or 'CABOS /' in c.upper():
                    print(f"Match in {p}")
