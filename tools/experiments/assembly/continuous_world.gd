extends "res://scripts/world/sucateia.gd"
var floors: Array[TileMapLayer] = []
var overview := false
func _ready() -> void:
	for node in find_children("*","TileMapLayer",true,false): floors.append(node)
	super._ready()
	$Structures/Player.spawn_point=$Structures/Player.position
	for arg in OS.get_cmdline_user_args():
		if arg=="--capture=world":
			overview=true
			$Structures/Player.position=Vector2(6000,2600)
			$Structures/Player/Camera.zoom=Vector2(.09,.09)
		elif arg=="--capture=connection":
			$Structures/Player.position=Vector2(1130,60)
			$Structures/Player/Camera.zoom=Vector2(.53,.53)
	if capture_mode!="": $Structures/Player.set_physics_process(false)
func is_walkable(point: Vector2) -> bool:
	for floor in floors:
		var cell := floor.local_to_map(floor.to_local(point))
		if floor.get_cell_source_id(cell)!=-1:return true
	return false
func _process(delta: float) -> void:
	if not overview:
		for sector in $RegionalSectors.get_children():
			sector.visible=Rect2(sector.position-Vector2(500,500),Vector2(3300,2600)).grow(1100).has_point($Structures/Player.global_position)
	super._process(delta)
