from pathlib import Path
root=Path(__file__).resolve().parents[1]
path=root/'scripts/world/market_expansion_builder.gd'
source=path.read_text(encoding='utf-8')
source=source[:source.index('\tvar subareas := group("Subareas",district)')]+'''\tload("res://scripts/world/market_urban_layout.gd").new().install(self)
\tvar camera: Camera2D=b.world.get_node("Structures/Player/Camera");camera.limit_top=-1740
\tdistrict.set_meta("new_ground_cells",floor.get_used_cells().size())
\tdistrict.set_meta("function","commercial circulation, bargaining, stock and connection to adjacent districts")
\tdistrict.set_meta("original_scale_preserved",true)
'''
source=source.replace('background.polygon=PackedVector2Array([Vector2(-300,-1800),Vector2(2500,-1800),Vector2(2500,125),Vector2(2075,270),Vector2(1850,395),Vector2(1660,500),Vector2(310,500),Vector2(210,370),Vector2(-80,260),Vector2(-300,95)])','background.polygon=PackedVector2Array([Vector2(-1500,-3200),Vector2(3600,-3200),Vector2(3600,600),Vector2(-1500,600)])')
path.write_text(source,encoding='utf-8')
print('Reorganized commerce; original MarketFloor generation retained verbatim')
