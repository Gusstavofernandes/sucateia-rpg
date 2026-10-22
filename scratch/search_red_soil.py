import os

for root, dirs, files in os.walk('.'):
    if '.git' in root or '.gemini' in root: continue
    for f in files:
        if f.endswith('.gd') or f.endswith('.tscn') or f.endswith('.gdshader'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fl:
                content = fl.read()
                if 'red_soil' in content or 'alto_ground' in content or 'vermelh' in content.lower():
                    print(f"Match in {p}")
