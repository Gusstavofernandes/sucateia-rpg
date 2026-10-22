extends RefCounted

const DECK_TEXTURE = "res://assets/reconstruction/stair_fits/deck_timber_stair.png"
const COAST_TEXTURE = "res://assets/reconstruction/stair_fits/coastal_stone_stair.png"

func fit(parent: Node2D, label: String, path: String, ports: PackedVector2Array, targets: PackedVector2Array, horizontal_scale: float) -> Sprite2D:
	var art := Sprite2D.new()
	art.name = label
	art.texture = load(path)
	art.scale = Vector2(horizontal_scale, (targets[1].y-targets[0].y)/(ports[1].y-ports[0].y))
	parent.add_child(art)
	art.global_position = targets[0] - (ports[0]-Vector2(art.texture.get_size())*.5)*art.scale
	art.set_meta("fitted_stair",true)
	art.set_meta("ports_pixels",ports)
	art.set_meta("ports_world",targets)
	return art

func install(world: Node2D) -> void:
	if not world.has_node("CabosDistrict") or not world.has_node("FinishedInfrastructure"):
		return
	var district: Node2D = world.get_node("CabosDistrict")
	var decks: Node2D = district.get_node("ElevatedDecks")
	var street_stairs := Node2D.new()
	street_stairs.name = "CabosGroundStairs"
	street_stairs.y_sort_enabled = true
	world.get_node("Structures").add_child(street_stairs)
	# Replace the six loosely stacked grate sprites with one coherent wooden
	# stair per F connection. Preserve the source scene and navigation ports.
	for child in decks.get_children():
		if child is Sprite2D and child.texture.resource_path.ends_with("/stairs.png"):
			child.hide()
	for access in district.get_node("Accesses").get_children():
		var upper: Vector2 = access.get_meta("elevated_arrival")
		var ground: Vector2 = access.get_meta("surface_arrival")
		# 32px from the walking center puts the top tread inside the front
		# deck plank band, rather than underneath an uninterrupted front rail.
		var stair := fit(decks,"Deck"+String(access.name),DECK_TEXTURE,PackedVector2Array([Vector2(423,160),Vector2(423,1690)]),PackedVector2Array([upper+Vector2(0,32),ground]),.15)
		stair.material = district.occlusion
		# The complete flight sits behind houses whose feet are in front of
		# its ground arrival, rather than painting over their roof silhouettes.
		var pivot := Node2D.new()
		pivot.name = String(access.name)
		street_stairs.add_child(pivot)
		pivot.global_position = ground
		stair.reparent(pivot,true)
		stair.z_index = 0
		stair.modulate = Color(.90,.90,.86,1)
	var infrastructure: Node2D = world.get_node("FinishedInfrastructure")
	for child in infrastructure.get_children():
		if child is Sprite2D and child.texture.resource_path.ends_with("/stairs.png") and child.position.distance_to(Vector2(1512,1428))<.1:
			child.hide()
	var coast: Sprite2D = fit(infrastructure,"CoastalWallStair",COAST_TEXTURE,PackedVector2Array([Vector2(720,285),Vector2(720,870)]),PackedVector2Array([Vector2(1512,1378),Vector2(1512,1472)]),.155)
	coast.modulate = Color(.79,.80,.72,1)
	# This flight joins the existing 144px collision gap. Draw its stone
	# shoulders above the coping so their seams overlap the actual wall ends.
	coast.z_index = 2
