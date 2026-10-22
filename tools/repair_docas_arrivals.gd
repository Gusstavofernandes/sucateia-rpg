extends "res://tools/build_docas_navigation.gd"
func run() -> void:
	world=load("res://maps/sucateia/sucateia.tscn").instantiate();world.set_script(null);district=world.get_node("DocasDistrict");floors.assign(district.get_meta("walk_polygons"))
	if not district.has_meta("arrivals_repaired"):
		district.get_node("Connections/NucleoUrbano").position=Vector2(2240,1370)
		district.get_node("Routes/ChegadaUrbana").set_meta("points",PackedVector2Array([Vector2(2240,1370),Vector2(2350,1370)]))
		for i in range(floors[0].size()):floors[0][i].y+=40
		district.get_node("WorkingDecks/ChegadaUrbana00").position.y+=40;district.get_node("WetSupports/ChegadaUrbanaContencao00").position.y+=40
		district.set_meta("arrivals_repaired",true)
	district.get_node("DeckBoundaries").free();district.set_meta("walk_polygons",floors);district.set_meta("boundary_segments",make_guards())
	world.set_script(load("res://scripts/world/sucateia.gd"));own(world);var packed := PackedScene.new();var error := packed.pack(world)
	if error==OK:error=ResourceSaver.save(packed,"res://maps/sucateia/sucateia.tscn")
	print("DOCAS arrivals saved=",error," urban entrance below existing footprint; Forjas joins open on actual old floor")
	world.free();world=null;district=null;packed=null;quit(error)
