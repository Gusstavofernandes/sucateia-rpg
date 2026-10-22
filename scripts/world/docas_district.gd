extends Node2D
var water_bodies: Array[StaticBody2D]=[]
var ignoring_water := false
func _ready() -> void:
	# Refresh localized water exceptions before the player's first move after R.
	process_physics_priority=-20
	for label in ["EastCoastalBarrier","SouthCoastalBarrier"]:water_bodies.append(get_parent().get_node(label))
func is_walkable(point: Vector2) -> bool:
	for polygon in get_meta("walk_polygons",[]):
		if Geometry2D.is_point_in_polygon(point,polygon):return true
	return false
func water_exclusions(point: Vector2) -> Array[RID]:
	var excluded: Array[RID]=[]
	if is_walkable(point):
		for body in water_bodies:excluded.append(body.get_rid())
	return excluded
func update_player_water() -> void:
	var player: CharacterBody2D=get_parent().get_node("Structures/Player")
	var active: bool=player.navigation_layer=="surface" and is_walkable(player.position)
	if active==ignoring_water:return
	for body in water_bodies:
		if active:player.add_collision_exception_with(body)
		else:player.remove_collision_exception_with(body)
	ignoring_water=active
func update_safe_spawn() -> void:
	var player: CharacterBody2D=get_parent().get_node("Structures/Player")
	if player.navigation_layer!="surface":return
	for landing in get_node("SafeLandings").get_children():
		if player.position.distance_to(landing.position)<35:player.spawn_point=landing.position;break
func _physics_process(_delta: float) -> void:
	update_player_water();update_safe_spawn()
