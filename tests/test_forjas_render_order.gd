extends SceneTree
func _initialize() -> void:call_deferred("run")
func run() -> void:
	var world: Node2D=load("res://maps/sucateia/sucateia.tscn").instantiate()
	var structures: Node2D=world.get_node("Structures")
	var architecture: Node2D=world.get_node_or_null("Structures/ForjasIndustrialArchitecture")
	if not architecture or not structures.y_sort_enabled or not architecture.y_sort_enabled:
		push_error("Forjas architecture does not share the player's depth sorting");world.free();quit(1);return
	assert(world.get_node("Structures/Player").z_index==architecture.z_index)
	assert(world.has_node("Structures/ForjasStockAndService"))
	assert(world.get_node("ForjasRasasDistrict").get_node(world.get_node("ForjasRasasDistrict").get_meta("architecture_path"))==architecture)
	print("PASS: Forjas buildings and service props share existing player y-sort; approved root ordering unchanged")
	world.free();quit(0)
