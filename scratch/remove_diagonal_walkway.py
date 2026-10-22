with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    content = f.read()

target = '''[node name="@Sprite2D@38" type="Sprite2D" parent="RegionalContinuity" unique_id=1144126617]
modulate = Color(0.83, 0.85, 0.7, 0.23)
position = Vector2(2100, 1116)
scale = Vector2(0.3515625, 0.234375)
texture = ExtResource("25_ritys")

[node name="@Sprite2D@39" type="Sprite2D" parent="RegionalContinuity" unique_id=392417570]
position = Vector2(2122.5288, 1125.7703)
rotation = 0.61072576
scale = Vector2(0.21874991, 0.4027778)
texture = ExtResource("28_f3eo0")

[node name="@Sprite2D@40" type="Sprite2D" parent="RegionalContinuity" unique_id=782877592]
position = Vector2(2167.5867, 1157.3105)
rotation = 0.61072576
scale = Vector2(0.21874991, 0.4027778)
texture = ExtResource("28_f3eo0")

[node name="@Line2D@41" type="Line2D" parent="RegionalContinuity" unique_id=98320683]
points = PackedVector2Array(2100, 1074, 2190.1155, 1137.0808)
width = 4.0
default_color = Color(0.09019608, 0.14509805, 0.12156863, 1)
joint_mode = 2
antialiased = true

[node name="@Line2D@42" type="Line2D" parent="RegionalContinuity" unique_id=1505096517]
points = PackedVector2Array(2100, 1074, 2190.1155, 1137.0808)
width = 1.0
default_color = Color(0.5254902, 0.44313726, 0.3019608, 1)
joint_mode = 2
antialiased = true

[node name="@Sprite2D@43" type="Sprite2D" parent="RegionalContinuity" unique_id=233591039]
position = Vector2(2067.2307, 1087.0615)
rotation = 0.61072546
scale = Vector2(0.30555555, 0.4027778)
texture = ExtResource("28_f3eo0")

[node name="@Line2D@44" type="Line2D" parent="RegionalContinuity" unique_id=187893452]
points = PackedVector2Array(2034.4614, 1028.123, 2100, 1074)
width = 4.0
default_color = Color(0.09019608, 0.14509805, 0.12156863, 1)
joint_mode = 2
antialiased = true

[node name="@Line2D@45" type="Line2D" parent="RegionalContinuity" unique_id=189322572]
points = PackedVector2Array(2034.4614, 1028.123, 2100, 1074)
width = 1.0
default_color = Color(0.5254902, 0.44313726, 0.3019608, 1)
joint_mode = 2
antialiased = true
'''

# Normalize newlines
target_crlf = target.replace('\n', '\r\n')
target_lf = target.replace('\r\n', '\n')

found = False
if target_crlf in content:
    content = content.replace(target_crlf, '')
    found = True
elif target_lf in content:
    content = content.replace(target_lf, '')
    found = True
else:
    print("Warning: exact target block not found directly, checking variations...")

if found:
    with open('maps/sucateia/sucateia.tscn', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully removed diagonal walkway nodes from maps/sucateia/sucateia.tscn!")
else:
    print("Failed to remove nodes!")
