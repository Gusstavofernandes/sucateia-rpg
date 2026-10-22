import re

scene_path = r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\scenes\fundo_ferro_master.tscn'
with open(scene_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add ExtResources for Canal.tscn, Queda.tscn and CaptureMulti
# Let's inspect highest id in ext_resources
ext_ids = [int(m) for m in re.findall(r'id="(\d+)_', text)]
next_id = max(ext_ids) + 1 if ext_ids else 24

ext_canal_id = f"{next_id}_canal_scene"
ext_queda_id = f"{next_id+1}_queda_scene"
ext_capture_id = f"{next_id+2}_capture_multi"

ext_to_add = f"""[ext_resource type="PackedScene" path="res://scenes/Canal.tscn" id="{ext_canal_id}"]
[ext_resource type="PackedScene" path="res://scenes/Queda.tscn" id="{ext_queda_id}"]
[ext_resource type="Script" path="res://scripts/capture_multi.gd" id="{ext_capture_id}"]
"""

# Insert before first sub_resource
first_sub = text.find('[sub_resource')
text = text[:first_sub] + ext_to_add + "\n" + text[first_sub:]

# Update load_steps header
m_steps = re.search(r'load_steps=(\d+)', text)
if m_steps:
    cur_steps = int(m_steps.group(1))
    text = re.sub(r'load_steps=\d+', f'load_steps={cur_steps + 4}', text, count=1)

# 2. Replace Bueiros with Queda instance
def make_bueiro_content(num, x_pos):
    return f"""[node name="Bueiro_{num}" type="Node2D" parent="."]
position = Vector2({x_pos}, 240)

[node name="QuedaAgua" parent="Bueiro_{num}" instance=ExtResource("{ext_queda_id}")]
position = Vector2(0, 0)

[node name="LuzLanternaBueiro" type="PointLight2D" parent="Bueiro_{num}"]
position = Vector2(-65, -45)
color = Color(1, 0.74, 0.38, 1)
energy = 1.4
texture = SubResource("GradientTexture2D_light")
texture_scale = 3.8

[node name="ArcoPedra" type="Sprite2D" parent="Bueiro_{num}"]
z_index = -4
position = Vector2(0, -35)
scale = Vector2(1.15, 1.15)
texture = ExtResource("4_service_arch")
"""

for num, x_pos in [(1, 550), (2, 1550), (3, 2550)]:
    pattern = rf'\[node name="Bueiro_{num}" type="Node2D" parent="\."\](?:(?!\[node name="Bueiro_|\n\[node name="CanalDeEsgoto"|\n\[node name="PonteServico_).)*'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        text = text[:match.start()] + make_bueiro_content(num, x_pos) + "\n" + text[match.end():]
        print(f"Bueiro {num} successfully updated with Queda.tscn!")

# 3. Replace CanalDeEsgoto with Canal instances
canal_replacement = f"""[node name="CanalDeEsgoto" type="Node2D" parent="."]
z_index = -8

[node name="Canal_1" parent="CanalDeEsgoto" node_paths=PackedStringArray("lanternas") instance=ExtResource("{ext_canal_id}")]
position = Vector2(0, 525)
lanternas = [NodePath("../../LanternasMuralha/LanternaMuralha_1"), NodePath("../../LanternasMuralha/LanternaMuralha_2")]

[node name="Canal_2" parent="CanalDeEsgoto" node_paths=PackedStringArray("lanternas") instance=ExtResource("{ext_canal_id}")]
position = Vector2(850, 525)
lanternas = [NodePath("../../Bueiro_1/LuzLanternaBueiro"), NodePath("../../PonteServico_1/LanternaPonte")]

[node name="Canal_3" parent="CanalDeEsgoto" node_paths=PackedStringArray("lanternas") instance=ExtResource("{ext_canal_id}")]
position = Vector2(1700, 525)
lanternas = [NodePath("../../Bueiro_2/LuzLanternaBueiro"), NodePath("../../EstacaoBombeamento/LuzFornalhaBomba"), NodePath("../../PonteServico_2/LanternaPonte")]

[node name="Canal_4" parent="CanalDeEsgoto" node_paths=PackedStringArray("lanternas") instance=ExtResource("{ext_canal_id}")]
position = Vector2(2550, 525)
lanternas = [NodePath("../../Bueiro_3/LuzLanternaBueiro"), NodePath("../../PonteServico_3/LanternaPonte")]

[node name="Canal_5" parent="CanalDeEsgoto" node_paths=PackedStringArray("lanternas") instance=ExtResource("{ext_canal_id}")]
position = Vector2(3400, 525)
lanternas = [NodePath("../../LanternasMuralha/LanternaMuralha_6"), NodePath("../../LanternasMuralha/LanternaMuralha_7")]
"""

# Replace existing CanalDeEsgoto block (up to ColisaoCanal_1)
canal_pattern = r'\[node name="CanalDeEsgoto" type="Node2D" parent="\."\]\s+z_index = -8\s+\[node name="AguaCanalContinua"[^\]]+\](?:[^\n]+\n)+'
text = re.sub(canal_pattern, canal_replacement, text)

# 4. Add MultiCapture node at bottom for instant test captures
text += f"""
[node name="MultiCapture" type="Node" parent="."]
script = ExtResource("{ext_capture_id}")
"""

with open(scene_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Master scene updated successfully with modular water system!")
