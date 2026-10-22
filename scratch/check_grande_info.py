import os
import re

with open(r'c:\Users\Usuario\Documents\jogo\maps\ferrugem_baixa\grande.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'text = "([^"]+)"', text)
print("Texts in grande.tscn:", matches)

region_id = re.findall(r'region_id = "([^"]+)"', text)
print("region_id in grande.tscn:", region_id)
