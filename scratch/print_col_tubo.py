import re

with open('scenes/fundo_ferro_master.tscn', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

start = text.find('[node name="ColisaoTubulacaoIndustrial"')
end = text.find('\n[node name="', start + 100)
# print the whole block
print(text[start:start+2500])
