import re

with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

# Vamos achar MarketFloor
m_floor = re.search(r'\[node name="MarketFloor" type="TileMapLayer" parent="MarketDistrict"[^\]]*\](.*?)(?=\n\[node name=|\Z)', text, re.DOTALL)
if m_floor:
    print("MarketFloor encontrado!")
    # ver tile_map_data ou células usadas se houver
    lines = m_floor.group(1).split('\n')
    for l in lines[:10]:
        print(l)
