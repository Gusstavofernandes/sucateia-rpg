import os

for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.gd') or f.endswith('.tscn'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as file:
                c = file.read()
                if 'navegar pelo corredor' in c or 'GALERIA DE BUEIROS' in c:
                    print(f"Match in {p}")
