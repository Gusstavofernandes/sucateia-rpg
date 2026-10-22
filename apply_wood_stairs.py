import shutil
import re

# 1. Backup
shutil.copy2('maps/sucateia/sucateia.tscn', 'maps/sucateia/sucateia.tscn.bak6')
print("Created backup sucateia.tscn.bak6")

with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    content = f.read()

# 2. Add ext_resource if not present
res_line = '[ext_resource type="Texture2D" path="res://assets/generated/props/wood_dock_stairs.png" id="114_woodstairs"]\n'
if 'id="114_woodstairs"' not in content:
    content = content.replace('[sub_resource type="ShaderMaterial"', res_line + '[sub_resource type="ShaderMaterial"', 1)
    print("Added 114_woodstairs ext_resource")

# 3. Replace @Sprite2D@162 in LowerCoastReworked
old_node = '''[node name="@Sprite2D@162" type="Sprite2D" parent="LowerCoastReworked" unique_id=1411985917]
position = Vector2(2206, 1640)
rotation = 0.08
scale = Vector2(0.2534722, 0.3409091)
texture = ExtResource("29_am22u")'''

new_node = '''[node name="@Sprite2D@162" type="Sprite2D" parent="LowerCoastReworked" unique_id=1411985917]
position = Vector2(2210, 1654)
scale = Vector2(0.103, 0.103)
texture = ExtResource("114_woodstairs")'''

if old_node in content:
    content = content.replace(old_node, new_node)
    print("Replaced @Sprite2D@162 with wood_dock_stairs")
else:
    print("WARNING: old_node not found verbatim")

# Also hide or adjust the redundant metal walkway @Sprite2D@153 and @Sprite2D@408 under the stairs
# Let's check @Sprite2D@408 in FinishedInfrastructure
old_408 = '''[node name="@Sprite2D@408" type="Sprite2D" parent="FinishedInfrastructure" unique_id=117853899]
modulate = Color(0.98, 0.93, 0.84, 1)
position = Vector2(2190, 1640)
rotation = 0.022
scale = Vector2(0.5451389, 0.5138889)
texture = ExtResource("28_f3eo0")'''

new_408 = '''[node name="@Sprite2D@408" type="Sprite2D" parent="FinishedInfrastructure" unique_id=117853899]
visible = false
position = Vector2(2190, 1640)
rotation = 0.022
scale = Vector2(0.5451389, 0.5138889)
texture = ExtResource("28_f3eo0")'''

if old_408 in content:
    content = content.replace(old_408, new_408)
    print("Made old FinishedInfrastructure walkway @Sprite2D@408 hidden")

with open('maps/sucateia/sucateia.tscn', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved updated maps/sucateia/sucateia.tscn")
