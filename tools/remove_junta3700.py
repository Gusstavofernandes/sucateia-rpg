import re

with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    content = f.read()

# Remover Junta3700Interior0_0 e Junta3700Interior0_1
p1 = r'\[node name="Junta3700Interior0_0"[\s\S]*?(?=\[node name="Junta3765Interior0_0")'
assert re.search(p1, content), 'Junta3700Interior nao encontrada'
content = re.sub(p1, '', content)

# Remover Junta3700Estaca3090
p2 = r'\[node name="Junta3700Estaca3090"[\s\S]*?(?=\[node name="Junta3765Estaca2840")'
assert re.search(p2, content), 'Junta3700Estaca3090 nao encontrada'
content = re.sub(p2, '', content)

with open('maps/sucateia/sucateia.tscn', 'w', encoding='utf-8') as f:
    f.write(content)

print('Junta3700 removida com sucesso!')
