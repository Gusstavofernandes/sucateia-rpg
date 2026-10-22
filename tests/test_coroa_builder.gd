extends SceneTree

func _initialize() -> void:
	call_deferred("run")

func run() -> void:
	var world := Node2D.new()
	world.name = "CoroaBuilderTestWorld"
	root.add_child(world)
	load("res://scripts/world/coroa_district.gd").new().install(world)
	await process_frame
	await physics_frame
	assert(world.has_node("CoroaDistrict"))
	var crown: Node2D = world.get_node("CoroaDistrict")
	assert(crown.get_meta("function", "") == "civic_administration_and_public_arbitration")
	assert(crown.get_node("Administration/CivicRecordsHouse").get_meta("function", "") == "records_and_public_arbitration")
	assert(crown.has_node("PublicThreshold/BulletinBoard/PublicHearingsAndRegisters"))
	assert(not crown.has_node("Administration/PublicGuardPost"), "a freestanding triangular marker must not represent a building")
	var entry: Vector2 = crown.get_node("Landmark/SafePublicArrival").global_position
	for direction in ["Market", "Cabos", "Core", "Forjas"]:
		var route: Marker2D = crown.get_node("CivicRoutes/" + direction)
		var points: PackedVector2Array = route.get_meta("points")
		assert(points.size() >= 2 and points[-1].distance_to(entry) <= 1.0, "waypoints must reach the safe arrival")
		assert(route.get_meta("clear_width", 0.0) >= 60.0)
		assert(crown.get_node("Approaches/" + direction).global_position.distance_to(entry) <= 1.0)
	for path in ["Administration/RegistroAndArbitrationContact", "PublicThreshold/BulletinBoard/BoardGroundContact", "Landmark/TowerFoundationContact", "PublicThreshold/CivicStepsGroundContact"]:
		var contact: StaticBody2D = crown.get_node(path)
		assert(contact.get_meta("contact", "") != "", "contact intent must be specified at " + path)
	for required in ["assets/region/crown.png", "assets/generated/structures/house.png", "assets/infrastructure/lantern.png", "assets/infrastructure/stairs.png", "assets/terrain/foundation.png"]:
		var tex: Texture2D = load("res://" + required)
		assert(tex != null and tex.get_width() > 0, "builder dependency must load: " + required)
	var service: Node = crown.get_node("Utilities")
	assert(service.get_meta("external_cables") == 0 and service.get_meta("external_pipes") == 0)
	assert(service.get_meta("wick_fixture_count") == 3)
	print("COROA_BUILDER PASS routes=4 contacts=4 source_textures=5 lines=0")
	world.queue_free()
	await process_frame
	quit(0)
