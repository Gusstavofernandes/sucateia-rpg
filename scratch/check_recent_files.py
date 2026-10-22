import os, time

now = time.time()
print("Recently modified files in the last 4 hours:")
for root, dirs, files in os.walk('.'):
    # skip .godot
    if '.godot' in root:
        continue
    for f in files:
        p = os.path.join(root, f)
        try:
            mtime = os.path.getmtime(p)
            if now - mtime < 4 * 3600:
                print(f"{time.ctime(mtime)} | {p}")
        except:
            pass
