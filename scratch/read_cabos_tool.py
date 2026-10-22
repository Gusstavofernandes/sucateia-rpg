with open('tools/integrate_cabos_art.gd', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()
    print("integrate_cabos_art.gd lines:", len(text.splitlines()))
    for line in text.splitlines()[:60]:
        print(line)
