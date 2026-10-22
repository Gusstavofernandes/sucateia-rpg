import os

for root, dirs, files in os.walk('.'):
    if '.godot' in root:
        continue
    for f in files:
        if f.endswith('.tscn'):
            print(os.path.join(root, f))
