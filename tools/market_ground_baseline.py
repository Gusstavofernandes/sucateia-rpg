from pathlib import Path
import json,re,hashlib
root=Path(__file__).resolve().parents[1]
scene=(root/'maps/sucateia/sucateia.tscn').read_text(encoding='utf-8')
block=next(b for b in scene.split('[node ') if b.startswith('name="MarketFloor"'))
encoded=re.search(r'tile_map_data = PackedByteArray\("([^"]+)"\)',block).group(1)
path=root/'tools/checkpoints/market_ground_before_urban.json'
assert not path.exists(),'Do not overwrite terrain baseline'
path.write_text(json.dumps({'tile_map_sha256':hashlib.sha256(encoded.encode()).hexdigest(),'camera_top':-1740},indent=2),encoding='utf-8')
print('Saved unchanged-ground baseline')
