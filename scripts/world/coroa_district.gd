extends RefCounted

const CROWN_ART := "res://assets/region/crown.png"
const LANTERN_ART := "res://assets/infrastructure/lantern.png"
const LIGHT_TEX := "res://assets/fx/light.svg"

func _node(parent: Node, name: String, z: int = 0) -> Node2D:
	var node := Node2D.new()
	node.name = name
	node.z_index = z
	parent.add_child(node)
	return node

func _route(parent: Node2D, label: String, points: PackedVector2Array, width: float = 70.0) -> Marker2D:
	var marker := Marker2D.new()
	marker.name = label
	marker.position = points[points.size() - 1]
	marker.set_meta("points", points)
	marker.set_meta("clear_width", width)
	parent.add_child(marker)
	return marker

func install(world: Node2D) -> void:
	if world.has_node("CoroaDistrict"):
		return
	var district := _node(world, "CoroaDistrict")
	district.y_sort_enabled = true
	district.set_meta("function", "coracao_de_ferro_monumental")
	district.set_meta("lore", "O Coração de Ferro — imponente fortaleza e coração de poder de Sucateia")

	# Rotas públicas conectando os distritos ao platô do Coração de Ferro
	var routes := _node(district, "CivicRoutes", -5)
	_route(routes, "Market", PackedVector2Array([Vector2(1120, 1060), Vector2(1116, 948), Vector2(1236, 756), Vector2(1356, 636), Vector2(1428, 564)]))
	_route(routes, "Cabos", PackedVector2Array([Vector2(2100, 1110), Vector2(1716, 1044), Vector2(1716, 612), Vector2(1668, 564)]), 64.0)
	_route(routes, "Core", PackedVector2Array([Vector2(1152, 1248), Vector2(1236, 948), Vector2(1356, 804), Vector2(1476, 660), Vector2(1530, 564)]))
	_route(routes, "Forjas", PackedVector2Array([Vector2(1580, 1050), Vector2(1716, 972), Vector2(1716, 732), Vector2(1596, 636), Vector2(1530, 564)]))
	
	var approaches := _node(district, "Approaches", 1)
	var civic_entry := Vector2(1530, 480)
	for key in ["Market", "Cabos", "Core", "Forjas"]:
		var route: Marker2D = routes.get_node(key)
		var civic_points: PackedVector2Array = route.get_meta("points")
		civic_points.append(civic_entry)
		route.set_meta("points", civic_points)
		route.position = civic_entry
		var entry := Marker2D.new()
		entry.name = key
		entry.position = route.position
		entry.set_meta("arrival_clearance", 70.0)
		approaches.add_child(entry)

	# --- O CORAÇÃO DE FERRO: ESTRUTURA GIGANTESCA E IMPONENTE ---
	var heart_center_x := 1530.0
	var heart_sprite_center_y := 190.0
	var heart_scale := 0.58

	var landmark := _node(district, "Landmark", 0)
	landmark.y_sort_enabled = true

	# Sombra de solo suave e integrada sob a fundação circular
	var ground_shadow := Polygon2D.new()
	ground_shadow.name = "MonumentalShadow"
	ground_shadow.z_index = -1
	var shadow_pts := PackedVector2Array()
	var shadow_w := 240.0
	var shadow_h := 48.0
	var shadow_center_y := 415.0
	for i in range(24):
		var ang := float(i) / 24.0 * TAU
		shadow_pts.append(Vector2(heart_center_x + cos(ang) * shadow_w, shadow_center_y + sin(ang) * shadow_h))
	ground_shadow.polygon = shadow_pts
	ground_shadow.color = Color(0.04, 0.05, 0.07, 0.28)
	landmark.add_child(ground_shadow)

	# Colisão física da base sólida (bloqueia o corpo da fortaleza, libera a frente do pátio)
	var body := StaticBody2D.new()
	body.name = "CoracaoDeFerroColisao"
	body.collision_layer = 1
	body.collision_mask = 0
	var col_shape := CollisionPolygon2D.new()
	col_shape.polygon = PackedVector2Array([
		Vector2(heart_center_x - 225, 330),
		Vector2(heart_center_x - 170, 300),
		Vector2(heart_center_x + 170, 300),
		Vector2(heart_center_x + 225, 330),
		Vector2(heart_center_x + 235, 410),
		Vector2(heart_center_x + 160, 440),
		Vector2(heart_center_x - 160, 440),
		Vector2(heart_center_x - 235, 410)
	])
	body.add_child(col_shape)
	landmark.add_child(body)

	# Sprite monumental do Coração de Ferro (crown.png em escala colossal)
	var tower := Sprite2D.new()
	tower.name = "CoracaoDeFerro"
	tower.texture = load(CROWN_ART) as Texture2D
	tower.position = Vector2(heart_center_x, heart_sprite_center_y)
	tower.scale = Vector2.ONE * heart_scale
	tower.z_index = 0
	landmark.add_child(tower)

	# Iluminação atmosférica interna do grande portal de entrada (dourado profundo da forja interior)
	var portal_light := PointLight2D.new()
	portal_light.name = "PortalLuz"
	portal_light.texture = load(LIGHT_TEX) as Texture2D
	portal_light.texture_scale = 0.55
	portal_light.energy = 0.65
	portal_light.color = Color("#ff9e3b")
	portal_light.position = Vector2(1515, 392)
	portal_light.z_index = 2
	landmark.add_child(portal_light)

	# Iluminação de vitrais das alas laterais
	for wx in [1390.0, 1640.0]:
		var window_light := PointLight2D.new()
		window_light.name = "VitralLuz" + str(int(wx))
		window_light.texture = load(LIGHT_TEX) as Texture2D
		window_light.texture_scale = 0.35
		window_light.energy = 0.40
		window_light.color = Color("#e5b364")
		window_light.position = Vector2(wx, 368)
		window_light.z_index = 2
		landmark.add_child(window_light)

	# Núcleo de energia do cume (o Coração / orbe místico no topo da Coroa)
	var core_light := PointLight2D.new()
	core_light.name = "NucleoArcano"
	core_light.texture = load(LIGHT_TEX) as Texture2D
	core_light.texture_scale = 0.80
	core_light.energy = 0.90
	core_light.color = Color("#2bf0ff") # Ciano luminoso brilhante
	core_light.position = Vector2(1525, -4)
	core_light.z_index = 3
	landmark.add_child(core_light)

	# Lanternas decorativas de poste no pátio frontal
	for lx in [heart_center_x - 180.0, heart_center_x + 180.0]:
		var lamp := Sprite2D.new()
		lamp.name = "Lantern" + str(int(lx))
		lamp.texture = load(LANTERN_ART) as Texture2D
		lamp.position = Vector2(lx, 470)
		lamp.scale = Vector2(0.32, 0.32)
		lamp.z_index = 1
		landmark.add_child(lamp)
		var lamp_light := PointLight2D.new()
		lamp_light.texture = load(LIGHT_TEX) as Texture2D
		lamp_light.texture_scale = 0.25
		lamp_light.energy = 0.35
		lamp_light.color = Color("#f5c46c")
		lamp_light.position = Vector2(lx, 465)
		landmark.add_child(lamp_light)

	# Marcador de chegada do pátio público
	var entrance := Marker2D.new()
	entrance.name = "SafePublicArrival"
	entrance.position = civic_entry
	entrance.set_meta("safe_clearance", 70.0)
	landmark.add_child(entrance)
