import re

with open(r'c:\Users\Usuario\Documents\jogo\maps\sucateia\sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

# Ext resources
ext_ids = re.findall(r'\[ext_resource[^\]]+id="([^"]+)"', text)
print(f"Total ext_resources in sucateia.tscn: {len(ext_ids)}")
print("Sample ext_ids:", ext_ids[:10], "...", ext_ids[-10:])

# Check unique_ids
unique_ids = re.findall(r'unique_id=(\d+)', text)
u_ints = [int(u) for u in unique_ids]
print(f"Total unique_ids: {len(u_ints)}, max={max(u_ints) if u_ints else 0}")
