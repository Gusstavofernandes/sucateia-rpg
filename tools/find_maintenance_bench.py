import re

with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

m_ext = re.findall(r'\[ext_resource[^\]]+maintenance_bench_cluster\.png"[^\]]+id="([^"]+)"', text)
print('ext_id:', m_ext)
if m_ext:
    for ext_id in m_ext:
        for m in re.finditer(rf'ExtResource\("{ext_id}"\)', text):
            start = max(0, m.start() - 300)
            end = min(len(text), m.end() + 200)
            print("--- Ocorrência ---")
            print(text[start:end])
