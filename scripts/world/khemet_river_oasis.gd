extends RefCounted
# =============================================================================
# KHEMET-RA: O RIO SAGRADO DAS DINASTIAS E O GRANDE OÁSIS
# -----------------------------------------------------------------------------
# Nasce no extremo norte do Platô das Dinastias (Y ~ -2860), desce serpenteando
# para o sul pelo deserto e deságua no Grande Oásis, antes das falésias costeiras.
# Do lago partem os antigos canais de irrigação precursores de Khemet-Ra.
#
# O rio é intransponível a pé (no futuro poderá ser atravessado a nado);
# três pontes precursoras de arenito permitem a passagem.
# =============================================================================

const RIVER_SHADER   := "res://assets/reconstruction/khemet_river.gdshader"
const SLAB_TEX       := "res://assets/reconstruction/khemet_ancient_ruins_slab.png"
const STELE_TEX      := "res://assets/reconstruction/khemet_glyph_stele_crystal.png"
const COLUMNS_TEX    := "res://assets/reconstruction/khemet_ruined_columns_cluster.png"
const BRAZIER_TEX    := "res://assets/reconstruction/khemet_bronze_brazier_altar.png"
const VEG_TEX        := "res://assets/reconstruction/chapada_desert_vegetation.png"
const LIGHT_TEX      := "res://assets/fx/light.svg"

# Traçado do leito (norte -> sul). Mantido livre dos marcos monumentais existentes.
const RIVER_COURSE: Array[Vector2] = [
	Vector2(-7900, -2880), Vector2(-7760, -2680), Vector2(-7980, -2470),
	Vector2(-8280, -2280), Vector2(-8200, -2060), Vector2(-7880, -1910),
	Vector2(-7860, -1720)
]
const RIVER_HALF_WIDTH := 78.0
const BANK_WIDTH := 46.0

const LAKE_CENTER := Vector2(-8020, -1560)
const LAKE_RADII := Vector2(460.0, 235.0)

# Pontes ao longo do rio (fração do comprimento total)
const BRIDGE_FRACTIONS: Array[float] = [0.22, 0.52, 0.80]
const BRIDGE_LENGTH := 250.0
const BRIDGE_WIDTH := 66.0

# Canais de irrigação: ângulo de saída do lago e comprimento
const CANALS: Array[Dictionary] = [
	{"angle": 0.10, "length": 620.0},
	{"angle": PI - 0.12, "length": 560.0},
	{"angle": PI * 0.5 + 0.35, "length": 260.0}
]
const CANAL_HALF_WIDTH := 17.0

var _water_polygons: Array[PackedVector2Array] = []
var _bridge_polygons: Array[PackedVector2Array] = []


func install(world: Node2D) -> void:
	if world.has_node("KhemetRiverOasis"):
		world.get_node("KhemetRiverOasis").free()

	var root := Node2D.new()
	root.name = "KhemetRiverOasis"
	root.z_as_relative = false
	root.z_index = -20
	world.add_child(root)

	var banks := _make_layer(root, "RiverBanks", -21)
	var water := _make_layer(root, "RiverWater", -20)
	var bridges := _make_layer(root, "PrecursorBridges", -18)
	var flora := _make_layer(root, "OasisFlora", -15)

	var curve := Curve2D.new()
	for i in RIVER_COURSE.size():
		var pt: Vector2 = RIVER_COURSE[i]
		var tangent := Vector2.ZERO
		if i > 0 and i < RIVER_COURSE.size() - 1:
			tangent = (RIVER_COURSE[i + 1] - RIVER_COURSE[i - 1]) * 0.25
		curve.add_point(pt, -tangent, tangent)
	curve.bake_interval = 24.0
	var path: PackedVector2Array = curve.get_baked_points()

	_build_river(banks, water, path)
	_build_lake(banks, water)
	_build_canals(banks, water)
	_build_bridges(bridges, curve)
	_build_flora(flora, path)

	root.set_meta("water_polygons", _water_polygons)
	root.set_meta("bridge_polygons", _bridge_polygons)


func is_blocked(root: Node, point: Vector2) -> int:
	# 1 = ponte (caminhável), -1 = água (bloqueia), 0 = fora do rio
	for poly in root.get_meta("bridge_polygons", []):
		if Geometry2D.is_point_in_polygon(point, poly):
			return 1
	for poly in root.get_meta("water_polygons", []):
		if Geometry2D.is_point_in_polygon(point, poly):
			return -1
	return 0


# -----------------------------------------------------------------------------
# LEITO DO RIO
# -----------------------------------------------------------------------------
func _build_river(banks: Node2D, water: Node2D, path: PackedVector2Array) -> void:
	var normals := _path_normals(path)
	var lengths := _path_lengths(path)

	water.add_child(_ribbon(path, normals, lengths, RIVER_HALF_WIDTH, 0, "RiverChannel"))
	banks.add_child(_bank_ribbon(path, normals, RIVER_HALF_WIDTH - 6.0, BANK_WIDTH, "RiverWetBanks"))

	# Polígono de bloqueio ligeiramente mais estreito que a água visível
	var outline := PackedVector2Array()
	for i in path.size():
		outline.append(path[i] + normals[i] * (RIVER_HALF_WIDTH - 10.0))
	for i in range(path.size() - 1, -1, -1):
		outline.append(path[i] - normals[i] * (RIVER_HALF_WIDTH - 10.0))
	_water_polygons.append(outline)


# -----------------------------------------------------------------------------
# GRANDE OÁSIS
# -----------------------------------------------------------------------------
func _build_lake(banks: Node2D, water: Node2D) -> void:
	var steps := 72
	var lake_poly := PackedVector2Array()
	var block_poly := PackedVector2Array()
	var bank_outer := PackedVector2Array()
	for i in steps:
		var a := TAU * float(i) / float(steps)
		var dir := Vector2(cos(a), sin(a))
		lake_poly.append(LAKE_CENTER + dir * LAKE_RADII * 1.06)
		block_poly.append(LAKE_CENTER + dir * (LAKE_RADII - Vector2(22, 14)))
		bank_outer.append(LAKE_CENTER + dir * (LAKE_RADII + Vector2(70, 46)))

	# Margem úmida: anel com degradê por cor de vértice
	var ring := Polygon2D.new()
	ring.name = "OasisWetShore"
	var verts := PackedVector2Array()
	var cols := PackedColorArray()
	var polys: Array = []
	for i in steps:
		verts.append(LAKE_CENTER + (lake_poly[i] - LAKE_CENTER) * 0.94)
		cols.append(Color(0.30, 0.22, 0.12, 0.85))
		verts.append(bank_outer[i])
		cols.append(Color(0.42, 0.32, 0.17, 0.0))
	for i in steps:
		var a0 := i * 2
		var b0 := i * 2 + 1
		var a1 := ((i + 1) % steps) * 2
		var b1 := ((i + 1) % steps) * 2 + 1
		polys.append(PackedInt32Array([a0, a1, b0]))
		polys.append(PackedInt32Array([a1, b1, b0]))
	ring.polygon = verts
	ring.vertex_colors = cols
	ring.polygons = polys
	banks.add_child(ring)

	var lake := Polygon2D.new()
	lake.name = "OasisLake"
	lake.polygon = lake_poly
	var mat := ShaderMaterial.new()
	mat.shader = load(RIVER_SHADER) as Shader
	mat.set_shader_parameter("mode", 1)
	mat.set_shader_parameter("lake_center", LAKE_CENTER)
	mat.set_shader_parameter("lake_radii", LAKE_RADII)
	lake.material = mat
	water.add_child(lake)

	_water_polygons.append(block_poly)


# -----------------------------------------------------------------------------
# CANAIS DE IRRIGAÇÃO PRECURSORES (rasos, atravessáveis)
# -----------------------------------------------------------------------------
func _build_canals(banks: Node2D, water: Node2D) -> void:
	var slab := load(SLAB_TEX) as Texture2D
	for c in CANALS:
		var dir := Vector2(cos(c["angle"]), sin(c["angle"]))
		var start: Vector2 = LAKE_CENTER + dir * LAKE_RADII * 0.92
		var end: Vector2 = start + dir * float(c["length"])
		var path := PackedVector2Array()
		var n_pts := int(float(c["length"]) / 24.0) + 1
		for i in n_pts:
			path.append(start.lerp(end, float(i) / float(n_pts - 1)))
		var normals := _path_normals(path)
		var lengths := _path_lengths(path)
		water.add_child(_ribbon(path, normals, lengths, CANAL_HALF_WIDTH, 2, "IrrigationCanal"))

		# Paredes de blocos de arenito precursor nas duas bordas
		var side := dir.orthogonal()
		var step := 70.0
		var count := int(float(c["length"]) / step)
		for i in count:
			var along := start + dir * (step * 0.5 + step * float(i))
			for s: float in [-1.0, 1.0]:
				var block := Sprite2D.new()
				block.texture = slab
				block.position = along + side * (CANAL_HALF_WIDTH + 9.0) * s
				block.rotation = dir.angle()
				block.scale = Vector2(step / float(slab.get_width()), 20.0 / float(slab.get_height())) * 1.08
				block.modulate = Color(1.02, 0.90, 0.72, 1.0)
				banks.add_child(block)


# -----------------------------------------------------------------------------
# PONTES PRECURSORAS
# -----------------------------------------------------------------------------
func _build_bridges(parent: Node2D, curve: Curve2D) -> void:
	var slab := load(SLAB_TEX) as Texture2D
	var stele := load(STELE_TEX) as Texture2D
	var total := curve.get_baked_length()
	for f in BRIDGE_FRACTIONS:
		var center := curve.sample_baked(total * f)
		var ahead := curve.sample_baked(minf(total, total * f + 20.0))
		var flow := (ahead - center).normalized()
		var across := flow.orthogonal()
		var ang := across.angle()

		var bridge := Node2D.new()
		bridge.name = "PrecursorBridge"
		bridge.position = center
		parent.add_child(bridge)

		# Sombra do tabuleiro na água
		var shadow := Polygon2D.new()
		shadow.polygon = _rect(Vector2(8, 14), BRIDGE_LENGTH * 0.92, BRIDGE_WIDTH, ang)
		shadow.color = Color(0.02, 0.06, 0.08, 0.35)
		bridge.add_child(shadow)

		# Tabuleiro: lajes de arenito entalhadas
		var deck := Sprite2D.new()
		deck.texture = slab
		deck.rotation = ang
		deck.scale = Vector2(BRIDGE_LENGTH / float(slab.get_width()), BRIDGE_WIDTH / float(slab.get_height()))
		deck.modulate = Color(1.06, 0.93, 0.74, 1.0)
		bridge.add_child(deck)

		# Guarda-corpos baixos de bronze com pátina
		for s: float in [-1.0, 1.0]:
			var rail := Line2D.new()
			rail.width = 5.0
			rail.default_color = Color(0.36, 0.52, 0.42, 1.0)
			var off: Vector2 = flow * (BRIDGE_WIDTH * 0.5 - 3.0) * s
			rail.add_point(off - across * BRIDGE_LENGTH * 0.42)
			rail.add_point(off + across * BRIDGE_LENGTH * 0.42)
			bridge.add_child(rail)

		# Estelas de cristal solar marcando as cabeceiras
		for s: float in [-1.0, 1.0]:
			var st := Sprite2D.new()
			st.texture = stele
			var h := 110.0
			st.scale = Vector2.ONE * (h / float(stele.get_height()))
			st.position = across * (BRIDGE_LENGTH * 0.5 + 16.0) * s + flow * (BRIDGE_WIDTH * 0.5 + 14.0) + Vector2(0, -h * 0.4)
			bridge.add_child(st)
			var glow := PointLight2D.new()
			glow.texture = load(LIGHT_TEX) as Texture2D
			glow.position = st.position + Vector2(0, -h * 0.35)
			glow.color = Color(0.35, 0.80, 1.0)
			glow.energy = 0.7
			glow.texture_scale = 0.35
			bridge.add_child(glow)

		_bridge_polygons.append(_rect(center, BRIDGE_LENGTH + 30.0, BRIDGE_WIDTH - 8.0, ang))


# -----------------------------------------------------------------------------
# VEGETAÇÃO RIBEIRINHA E SANTUÁRIO DO OÁSIS
# -----------------------------------------------------------------------------
func _build_flora(parent: Node2D, path: PackedVector2Array) -> void:
	var veg := load(VEG_TEX) as Texture2D
	var normals := _path_normals(path)
	var green := Color(0.78, 1.04, 0.62, 1.0)

	# Margens do rio: tufos alternados, evitando as cabeceiras das pontes
	var i := 3
	while i < path.size() - 2:
		for s: float in [-1.0, 1.0]:
			var jitter := sin(float(i) * 1.7 + s) * 18.0
			var pos: Vector2 = path[i] + normals[i] * (RIVER_HALF_WIDTH + 34.0 + jitter) * s
			if not _near_bridge(pos, 170.0):
				_veg(parent, veg, pos, 0.26 + absf(sin(float(i))) * 0.08, green)
		i += 5

	# Anel verde ao redor do lago (mais denso que o deserto)
	var steps := 26
	for k in steps:
		var a := TAU * float(k) / float(steps) + 0.07
		var r := 1.0 + 0.18 + sin(float(k) * 2.3) * 0.06
		var pos := LAKE_CENTER + Vector2(cos(a), sin(a)) * LAKE_RADII * r
		if _near_canal(pos):
			continue
		_veg(parent, veg, pos, 0.32 + absf(cos(float(k))) * 0.10, green)

	# Santuário: colunas precursoras na margem norte e braseiro solar
	var cols := Sprite2D.new()
	cols.texture = load(COLUMNS_TEX) as Texture2D
	cols.position = LAKE_CENTER + Vector2(-300, -LAKE_RADII.y - 95)
	cols.scale = Vector2.ONE * (230.0 / float(cols.texture.get_width()))
	parent.add_child(cols)

	var brazier := Sprite2D.new()
	brazier.texture = load(BRAZIER_TEX) as Texture2D
	brazier.position = LAKE_CENTER + Vector2(260, -LAKE_RADII.y - 70)
	brazier.scale = Vector2.ONE * (95.0 / float(brazier.texture.get_width()))
	parent.add_child(brazier)
	var fire := PointLight2D.new()
	fire.texture = load(LIGHT_TEX) as Texture2D
	fire.position = brazier.position + Vector2(0, -25)
	fire.color = Color(1.0, 0.72, 0.35)
	fire.energy = 0.9
	fire.texture_scale = 0.6
	parent.add_child(fire)


# -----------------------------------------------------------------------------
# UTILITÁRIOS GEOMÉTRICOS
# -----------------------------------------------------------------------------
func _make_layer(root: Node2D, layer_name: String, z: int) -> Node2D:
	var n := Node2D.new()
	n.name = layer_name
	n.z_as_relative = false
	n.z_index = z
	root.add_child(n)
	return n


func _path_normals(path: PackedVector2Array) -> PackedVector2Array:
	var out := PackedVector2Array()
	for i in path.size():
		var a := path[maxi(i - 1, 0)]
		var b := path[mini(i + 1, path.size() - 1)]
		out.append((b - a).normalized().orthogonal())
	return out


func _path_lengths(path: PackedVector2Array) -> PackedFloat32Array:
	var out := PackedFloat32Array()
	var acc := 0.0
	for i in path.size():
		if i > 0:
			acc += path[i].distance_to(path[i - 1])
		out.append(acc)
	return out


func _ribbon(path: PackedVector2Array, normals: PackedVector2Array, lengths: PackedFloat32Array, half_w: float, mode: int, node_name: String) -> Polygon2D:
	var verts := PackedVector2Array()
	var cols := PackedColorArray()
	var polys: Array = []
	for i in path.size():
		var wobble := sin(lengths[i] * 0.011) * 6.0
		verts.append(path[i] - normals[i] * (half_w + wobble))
		cols.append(Color(0.0, lengths[i] / 4000.0, 0.0, 1.0))
		verts.append(path[i] + normals[i] * (half_w - wobble))
		cols.append(Color(1.0, lengths[i] / 4000.0, 0.0, 1.0))
	for i in path.size() - 1:
		var l0 := i * 2
		var r0 := i * 2 + 1
		var l1 := (i + 1) * 2
		var r1 := (i + 1) * 2 + 1
		polys.append(PackedInt32Array([l0, l1, r0]))
		polys.append(PackedInt32Array([l1, r1, r0]))
	var poly := Polygon2D.new()
	poly.name = node_name
	poly.polygon = verts
	poly.vertex_colors = cols
	poly.polygons = polys
	var mat := ShaderMaterial.new()
	mat.shader = load(RIVER_SHADER) as Shader
	mat.set_shader_parameter("mode", mode)
	poly.material = mat
	return poly


func _bank_ribbon(path: PackedVector2Array, normals: PackedVector2Array, inner: float, width: float, node_name: String) -> Polygon2D:
	var verts := PackedVector2Array()
	var cols := PackedColorArray()
	var polys: Array = []
	var wet := Color(0.30, 0.22, 0.12, 0.85)
	var dry := Color(0.42, 0.32, 0.17, 0.0)
	# 4 vértices por seção: borda externa esq, interna esq, interna dir, externa dir
	for i in path.size():
		verts.append(path[i] - normals[i] * (inner + width)); cols.append(dry)
		verts.append(path[i] - normals[i] * inner); cols.append(wet)
		verts.append(path[i] + normals[i] * inner); cols.append(wet)
		verts.append(path[i] + normals[i] * (inner + width)); cols.append(dry)
	for i in path.size() - 1:
		var a := i * 4
		var b := (i + 1) * 4
		for k in 3:
			polys.append(PackedInt32Array([a + k, b + k, a + k + 1]))
			polys.append(PackedInt32Array([b + k, b + k + 1, a + k + 1]))
	var poly := Polygon2D.new()
	poly.name = node_name
	poly.polygon = verts
	poly.vertex_colors = cols
	poly.polygons = polys
	return poly


func _rect(center: Vector2, length: float, width: float, angle: float) -> PackedVector2Array:
	var ax := Vector2.RIGHT.rotated(angle) * length * 0.5
	var ay := Vector2.DOWN.rotated(angle) * width * 0.5
	return PackedVector2Array([center - ax - ay, center + ax - ay, center + ax + ay, center - ax + ay])


func _veg(parent: Node2D, tex: Texture2D, pos: Vector2, scl: float, tint: Color) -> void:
	var s := Sprite2D.new()
	s.texture = tex
	s.position = pos
	var flip := 1.0 if int(pos.x) % 2 == 0 else -1.0
	s.scale = Vector2(scl * flip, scl)
	s.modulate = tint
	parent.add_child(s)


func _near_bridge(pos: Vector2, radius: float) -> bool:
	for poly in _bridge_polygons:
		var c := (poly[0] + poly[2]) * 0.5
		if c.distance_to(pos) < radius:
			return true
	return false


func _near_canal(pos: Vector2) -> bool:
	var rel := (pos - LAKE_CENTER).angle()
	for c in CANALS:
		if absf(wrapf(rel - float(c["angle"]), -PI, PI)) < 0.22:
			return true
	return false
