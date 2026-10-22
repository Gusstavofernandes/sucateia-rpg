extends SceneTree
func _initialize() -> void:call_deferred("run")
func run() -> void:
	var world: Node2D=load("res://maps/sucateia/sucateia.tscn").instantiate()
	root.add_child(world)
	await physics_frame
	assert(get_nodes_in_group("player").size()==1)
	assert(world.has_node("Structures/MercadoReconstruido"))
	assert(not world.has_node("RegionalSectors"),"Night maps must not be assembled as final visual districts")
	for portal in world.get_node("RegionPortals").get_children():
		assert(portal.get_script()==null,"No scene-switching passage in the original map")
		assert(portal.collision_mask==0)
	var texture: Texture2D=load("res://assets/reconstruction/market_salvage_cart.png")
	assert(texture.get_image().detect_alpha()!=Image.ALPHA_NONE)
	print("PASS: original map is sole playable base, one player, no scene-switch portals, new transparent commercial asset")
	world.queue_free()
	await process_frame
	quit(0)
