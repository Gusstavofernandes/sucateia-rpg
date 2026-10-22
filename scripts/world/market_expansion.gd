extends RefCounted

# Constantes de Texturas dos novos assets de mercado (100% transparentes)
const WEAPONS_STALL_TEX  := "res://assets/reconstruction/market_weapons_stall.png"
const GADGETS_STALL_TEX  := "res://assets/reconstruction/market_gadgets_stall.png"
const JUNK_CRATES_TEX    := "res://assets/reconstruction/market_junk_crates.png"
const LARGE_PAVILION_TEX := "res://assets/reconstruction/market_large_pavilion.png"

func install(world: Node2D) -> void:
	if world.has_node("MarketRestosExpansion"):
		world.get_node("MarketRestosExpansion").free()
	
	var root := Node2D.new()
	root.name = "MarketRestosExpansion"
	root.y_sort_enabled = true
	root.z_index = 0
	world.add_child(root)

	# -------------------------------------------------------------------------
	# 1. GRANDE PAVILHÃO DO MERCADO (Fundo Norte da praça, sob a passarela)
	# -------------------------------------------------------------------------
	# Posição central de destaque ao fundo, com a praça frontal 100% aberta
	_build_stall(
		root,
		"PavilhaoReliquiasNorte",
		LARGE_PAVILION_TEX,
		Vector2(1130, -180),
		Vector2(0.20, 0.20),
		Vector2(220, 30)
	)

	# -------------------------------------------------------------------------
	# 2. BARRACA DE ARMAS E LÂMINAS DE SUCATA (Margem Noroeste)
	# -------------------------------------------------------------------------
	# Encostada na margem noroeste, junto à fachada de pedra das casas do oeste
	_build_stall(
		root,
		"BancaArmasNoroeste",
		WEAPONS_STALL_TEX,
		Vector2(880, -150),
		Vector2(0.19, 0.19),
		Vector2(160, 28)
	)

	# -------------------------------------------------------------------------
	# 3. BARRACA DE PRÓTESES MECÂNICAS E ENGRENAGENS (Margem Nordeste)
	# -------------------------------------------------------------------------
	# Encostada no recanto nordeste sob a passarela, com respiro do Pavilhão e da Coroa
	_build_stall(
		root,
		"BancaProtesesNordeste",
		GADGETS_STALL_TEX,
		Vector2(1380, -160),
		Vector2(0.19, 0.19),
		Vector2(160, 28)
	)

	# -------------------------------------------------------------------------
	# 4. MOSTRUÁRIOS DE CAIXOTES E SUCATAS (Apenas em cantos e calçadas laterais)
	# -------------------------------------------------------------------------
	# Mostruário 1: Calçada Oeste (junto à casa de pedra, abaixo da banca de armas)
	_build_crates(
		root,
		"MostruarioOeste",
		Vector2(780, -90),
		Vector2(0.15, 0.15),
		Vector2(110, 36)
	)

	# Mostruário 2: Lateral Nordeste (apoio junto ao pilar da passarela leste)
	_build_crates(
		root,
		"MostruarioNordeste",
		Vector2(1440, -90),
		Vector2(0.15, 0.15),
		Vector2(110, 36)
	)

	# Mostruário 3: Margem Sudoeste (calçada lateral entre os comércios do sul)
	_build_crates(
		root,
		"MostruarioSudoeste",
		Vector2(880, 230),
		Vector2(0.15, 0.15),
		Vector2(110, 36)
	)

func _build_stall(
	parent: Node2D,
	stall_name: String,
	tex_path: String,
	base_pos: Vector2,
	stall_scale: Vector2,
	col_size: Vector2
) -> Node2D:
	var stall := Node2D.new()
	stall.name = stall_name
	stall.position = base_pos
	stall.y_sort_enabled = false
	parent.add_child(stall)

	# Sombra suave sob a bancada da barraca
	var shadow := Polygon2D.new()
	shadow.name = "Shadow"
	var pts := PackedVector2Array()
	var sw := col_size.x * 0.55
	var sh := col_size.y * 0.65
	for i in range(16):
		var ang := float(i) / 16.0 * TAU
		pts.append(Vector2(cos(ang) * sw, sin(ang) * sh - col_size.y * 0.35))
	shadow.polygon = pts
	shadow.color = Color(0.02, 0.03, 0.04, 0.35)
	stall.add_child(shadow)

	# Colisão sólida no balcão
	var body := StaticBody2D.new()
	body.name = "Collision"
	body.collision_layer = 1
	body.collision_mask = 0
	var shape := CollisionShape2D.new()
	var rect := RectangleShape2D.new()
	rect.size = col_size
	shape.shape = rect
	shape.position = Vector2(0, -col_size.y * 0.5)
	body.add_child(shape)
	stall.add_child(body)

	# Sprite do asset perfeitamente transparente
	var sprite := Sprite2D.new()
	sprite.name = "Visual"
	sprite.texture = load(tex_path) as Texture2D
	sprite.scale = stall_scale
	var tex_size := sprite.texture.get_size()
	# Alinhar o fundo do sprite na base de apoio Y=0
	sprite.position = Vector2(0, -tex_size.y * stall_scale.y * 0.5)
	stall.add_child(sprite)

	return stall

func _build_crates(
	parent: Node2D,
	group_name: String,
	base_pos: Vector2,
	crates_scale: Vector2,
	col_size: Vector2
) -> Node2D:
	var group := Node2D.new()
	group.name = group_name
	group.position = base_pos
	group.y_sort_enabled = false
	parent.add_child(group)

	# Sombra suave sob os caixotes
	var shadow := Polygon2D.new()
	shadow.name = "Shadow"
	var pts := PackedVector2Array()
	var sw := col_size.x * 0.55
	var sh := col_size.y * 0.60
	for i in range(16):
		var ang := float(i) / 16.0 * TAU
		pts.append(Vector2(cos(ang) * sw, sin(ang) * sh - col_size.y * 0.35))
	shadow.polygon = pts
	shadow.color = Color(0.02, 0.03, 0.04, 0.30)
	group.add_child(shadow)

	# Colisão física dos caixotes
	var body := StaticBody2D.new()
	body.name = "Collision"
	body.collision_layer = 1
	body.collision_mask = 0
	var shape := CollisionShape2D.new()
	var rect := RectangleShape2D.new()
	rect.size = col_size
	shape.shape = rect
	shape.position = Vector2(0, -col_size.y * 0.5)
	body.add_child(shape)
	group.add_child(body)

	# Sprite dos caixotes
	var sprite := Sprite2D.new()
	sprite.name = "Visual"
	sprite.texture = load(JUNK_CRATES_TEX) as Texture2D
	if sprite.texture:
		sprite.scale = crates_scale
		var tex_size := sprite.texture.get_size()
		sprite.position = Vector2(0, -tex_size.y * crates_scale.y * 0.5)
	group.add_child(sprite)

	return group
