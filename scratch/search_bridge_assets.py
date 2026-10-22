import os

for root, dirs, files in os.walk('assets'):
    for f in files:
        if any(k in f.lower() for k in ['bridge', 'ponte', 'passarela', 'pier']):
            print(os.path.join(root, f))
