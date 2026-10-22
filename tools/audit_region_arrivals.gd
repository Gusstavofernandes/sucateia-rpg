extends SceneTree

const SCENE_PATH := "res://maps/sucateia/sucateia.tscn"
const OFFSETS := [
	Vector2(0, 58), Vector2(0, -58), Vector2(58, 0), Vector2(-58, 0),
	Vector2(41, 41), Vector2(-41, 41), Vector2(41, -41), Vector2(-41, -41),
	Vector2(0, 80), Vector2(0, -80), Vector2(80, 0), Vector2(-80, 0),
]

func _initialize() -> void:
	call_deferred("_run")

func _run() -> void:
	var world: Node2D = load(SCENE_PATH).instantiate()
	root.add_child(world)
	current_scene = world
	await physics_frame
	await physics_frame
	var result: Array[Dictionary] = []
	var player: CharacterBody2D = world.get_node("Structures/Player")
	var state := world.get_world_2d().direct_space_state
	var shape := CircleShape2D.new()
	shape.radius = 11.0
	for portal: Area2D in world.get_node("RegionPortals").get_children():
		var current: Vector2 = portal.position + portal.get_meta("arrival_offset", Vector2(0, 58))
		var candidates: Array[Dictionary] = []
		for offset: Vector2 in OFFSETS:
			var point: Vector2 = portal.position + offset
			var query := PhysicsShapeQueryParameters2D.new()
			query.shape = shape
			query.collision_mask = 1
			query.transform = Transform2D(0, point)
			var blockers := state.intersect_shape(query, 8)
			var walkable: bool = true
			if world.has_method("is_walkable"):
				walkable = bool(world.call("is_walkable", point))
			candidates.append({"offset": [offset.x, offset.y], "walkable": walkable, "blockers": blockers.size(), "safe": walkable and blockers.is_empty()})
		var current_walkable: bool = true
		if world.has_method("is_walkable"):
			current_walkable = bool(world.call("is_walkable", current))
		result.append({"portal": portal.name, "current": [current.x, current.y], "current_walkable": current_walkable, "candidate_offsets": candidates})
	print(JSON.stringify(result))
	player.queue_free()
	world.queue_free()
	await process_frame
	quit(0)
