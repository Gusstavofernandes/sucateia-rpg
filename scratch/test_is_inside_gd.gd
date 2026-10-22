extends SceneTree

func _init() -> void:
	var script = load("res://scripts/world/sucateia_west_ground.gd").new()
	var test_points = [
		Vector2(0, 700),
		Vector2(-200, 700),
		Vector2(-500, 700),
		Vector2(-800, 700),
		Vector2(-900, 700)
	]
	for pt in test_points:
		print("Point ", pt, " -> is_inside: ", script._is_inside_land(pt.x, pt.y))
	quit(0)
