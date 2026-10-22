extends SceneTree

const SCENE_PATH := "res://maps/fundo_ferro/fundo_ferro.tscn"
const FOOTBOXES := [
	Rect2(27, 176, 48, 28), Rect2(181, 176, 48, 28),
	Rect2(79, 187, 44, 26), Rect2(133, 187, 44, 26),
]
const SCALE := 0.52
const ANCHOR_PX := Vector2(128, 213)
const CANDIDATES := {
	"Valvulas_east_service_margin": Vector2(3290, 820),
	"Valvulas_south_east_margin": Vector2(3260, 850),
	"Valvulas_center_south": Vector2(3160, 820),
}
const COLLAPSE_SCALE := 0.075
const COLLAPSE_FOOT_PROBES := [Vector2(180, 910), Vector2(520, 922), Vector2(1160, 922), Vector2(1515, 910)]
const COLLAPSE_ANCHORS := {
	"Ruinas_upper_west_margin": Vector2(1580, 990),
	"Ruinas_west_north_margin": Vector2(1540, 970),
	"Ruinas_southwest_recess": Vector2(1510, 1010),
	"Ruinas_west_service_shelf": Vector2(1580, 1025),
	"Ruinas_west_lower_shelf": Vector2(1535, 1050),
	"Ruinas_south_shelf": Vector2(1600, 1070),
}

func _initialize() -> void:
	var packed: PackedScene = load(SCENE_PATH)
	var world: Node2D = packed.instantiate()
	var results: Array[Dictionary] = []
	for id in CANDIDATES:
		var anchor: Vector2 = CANDIDATES[id]
		var feet: Array[Vector2] = []
		var all_floor := true
		for box: Rect2 in FOOTBOXES:
			var point := (box.get_center() - ANCHOR_PX) * SCALE + anchor
			feet.append(point)
			all_floor = all_floor and world.call("is_walkable", point)
		results.append({"id": id, "anchor": [anchor.x, anchor.y], "feet": feet.map(func(p: Vector2): return [p.x, p.y]), "all_foot_contacts_on_floor_outside_water": all_floor})
	for id in COLLAPSE_ANCHORS:
		var anchor: Vector2 = COLLAPSE_ANCHORS[id]
		var feet: Array[Vector2] = []
		var all_floor := true
		for pixel: Vector2 in COLLAPSE_FOOT_PROBES:
			var point := Vector2(0, -32.7) + (pixel - Vector2(848.5, 463.5)) * COLLAPSE_SCALE + anchor
			feet.append(point)
			all_floor = all_floor and world.call("is_walkable", point)
		results.append({"id": id, "anchor": [anchor.x, anchor.y], "feet": feet.map(func(p: Vector2): return [p.x, p.y]), "all_foot_contacts_on_floor_outside_water": all_floor})
	print(JSON.stringify(results))
	world.free()
	quit(0)
