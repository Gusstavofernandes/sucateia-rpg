import re

scene_path = r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\scenes\fundo_ferro_master.tscn'
with open(scene_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update load_steps header
# Find load_steps=\d+
m_steps = re.search(r'load_steps=(\d+)', text)
current_steps = int(m_steps.group(1)) if m_steps else 17
new_steps = current_steps + 12
text = re.sub(r'load_steps=\d+', f'load_steps={new_steps}', text, count=1)

# 2. Add ext_resources for the new water textures and shaders
ext_resources_to_add = """[ext_resource type="Texture2D" path="res://assets/sewer_water_flow.png" id="16_sewer_water_flow"]
[ext_resource type="Shader" path="res://shaders/canal_water.gdshader" id="17_canal_water_shader"]
[ext_resource type="Texture2D" path="res://assets/bueiro_cascade_stream.png" id="18_bueiro_cascade_stream"]
[ext_resource type="Shader" path="res://shaders/bueiro_cascade.gdshader" id="19_bueiro_cascade_shader"]
[ext_resource type="Texture2D" path="res://assets/bueiro_impact_foam.png" id="20_bueiro_impact_foam"]
[ext_resource type="Shader" path="res://shaders/bueiro_splash.gdshader" id="21_bueiro_splash_shader"]
[ext_resource type="Texture2D" path="res://assets/drain_stain.png" id="22_drain_stain"]
[ext_resource type="Script" path="res://scripts/capture_multi.gd" id="23_capture_multi"]
"""

# Insert before the first sub_resource
first_sub = text.find('[sub_resource')
if first_sub != -1:
    text = text[:first_sub] + ext_resources_to_add + "\n" + text[first_sub:]

# 3. Add sub_resources for ShaderMaterials
sub_resources_to_add = """[sub_resource type="ShaderMaterial" id="ShaderMaterial_canal_water"]
shader = ExtResource("17_canal_water_shader")
shader_parameter/flow_direction = Vector2(1, 0)
shader_parameter/flow_speed = 0.08
shader_parameter/wave_frequency = 0.04
shader_parameter/wave_amplitude = 0.012
shader_parameter/water_tint = Color(0.95, 1.15, 1.05, 1)
shader_parameter/foam_boost = 1.35
shader_parameter/depth_darkening = 0.45
shader_parameter/water_texture = ExtResource("16_sewer_water_flow")

[sub_resource type="ShaderMaterial" id="ShaderMaterial_bueiro_cascade"]
shader = ExtResource("19_bueiro_cascade_shader")
shader_parameter/cascade_speed = 0.35
shader_parameter/turbulence_freq = 14.0
shader_parameter/turbulence_amp = 0.015
shader_parameter/water_tint = Color(0.95, 1.15, 1.05, 1)
shader_parameter/foam_surge = 1.3
shader_parameter/cascade_texture = ExtResource("18_bueiro_cascade_stream")

[sub_resource type="ShaderMaterial" id="ShaderMaterial_bueiro_splash"]
shader = ExtResource("21_bueiro_splash_shader")
shader_parameter/ripple_speed = 0.55
shader_parameter/pulse_intensity = 0.25
shader_parameter/foam_tint = Color(0.95, 1.15, 1.05, 1)
"""

first_node = text.find('[node name="FundoFerroMaster"')
if first_node != -1:
    text = text[:first_node] + sub_resources_to_add + "\n" + text[first_node:]

# 4. Update AguaCanalContinua material to ShaderMaterial_canal_water
text = text.replace(
    'material = SubResource("ShaderMaterial_water")',
    'material = SubResource("ShaderMaterial_canal_water")'
)

# 5. Set MuretasCanal z_index = -6
text = text.replace(
    '[node name="MuretasCanal" type="Node2D" parent="."]\n',
    '[node name="MuretasCanal" type="Node2D" parent="."]\nz_index = -6\n'
)

# 6. Update Bueiros 1, 2, 3 with Runoff Cascade, Stain, and Impact Splash
def make_bueiro_replacement(num, x_pos):
    return f"""[node name="Bueiro_{num}" type="Node2D" parent="."]
position = Vector2({x_pos}, 240)

[node name="CalhaMancha" type="Sprite2D" parent="Bueiro_{num}"]
z_index = -15
position = Vector2(0, 115)
scale = Vector2(0.38, 0.48)
texture = ExtResource("22_drain_stain")
modulate = Color(0.35, 0.35, 0.35, 0.75)

[node name="EscorrimentoAgua" type="Sprite2D" parent="Bueiro_{num}"]
z_index = -5
material = SubResource("ShaderMaterial_bueiro_cascade")
position = Vector2(0, 118)
scale = Vector2(0.26, 0.25)
texture = ExtResource("18_bueiro_cascade_stream")

[node name="EspumaImpacto" type="Sprite2D" parent="Bueiro_{num}"]
z_index = -5
material = SubResource("ShaderMaterial_bueiro_splash")
position = Vector2(0, 248)
scale = Vector2(0.42, 0.35)
texture = ExtResource("20_bueiro_impact_foam")

[node name="ArcoPedra" type="Sprite2D" parent="Bueiro_{num}"]
z_index = -4
position = Vector2(0, -35)
scale = Vector2(1.15, 1.15)
texture = ExtResource("4_service_arch")
"""

# Replace each bueiro
for num, x_pos in [(1, 550), (2, 1550), (3, 2550)]:
    pattern = rf'\[node name="Bueiro_{num}" type="Node2D" parent="\."\]\s+position = Vector2\({x_pos}, 240\)\s+\[node name="ArcoPedra"[^\]]+\]\s+z_index = -6\s+position = Vector2\(0, -35\)\s+scale = Vector2\(1\.15, 1\.15\)\s+texture = ExtResource\("4_service_arch"\)'
    match = re.search(pattern, text)
    if match:
        text = text[:match.start()] + make_bueiro_replacement(num, x_pos) + text[match.end():]
        print(f"Bueiro {num} successfully replaced!")
    else:
        print(f"WARNING: Regex did not match Bueiro {num}")

# 7. Add MultiCapture node at the bottom of the scene
text += """
[node name="MultiCapture" type="Node" parent="."]
script = ExtResource("23_capture_multi")
"""

with open(scene_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Scene successfully written!")
