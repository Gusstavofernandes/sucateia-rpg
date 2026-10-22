import glob
import os

for f in glob.glob('scripts/world/*.gd'):
    with open(f, 'r', encoding='utf-8', errors='ignore') as fl:
        content = fl.read()
        for idx, line in enumerate(content.split('\n'), 1):
            if 'pipe' in line.lower() or 'fo6ws' in line:
                print(f"{os.path.basename(f)}:{idx} -> {line.strip()}")
