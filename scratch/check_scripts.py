with open('scripts/world/market_urban_layout.gd', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()
    for line in text.splitlines():
        if any(k in line for k in ['744', 'junction', '-504', '-522']):
            print('market_urban_layout:', line)

with open('scripts/world/vhal_builder.gd', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()
    for line in text.splitlines():
        if any(k in line for k in ['744', 'junction', '-504', '-522']):
            print('vhal_builder:', line)
