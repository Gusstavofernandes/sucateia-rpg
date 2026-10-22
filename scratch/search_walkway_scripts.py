import os, glob

gd_files = []
for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.gd'):
            gd_files.append(os.path.join(root, f))

print(f"Total .gd files: {len(gd_files)}")

for path in gd_files:
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        if 'walkway' in content or 'wood_pier' in content:
            print(f"Match in {path}")
