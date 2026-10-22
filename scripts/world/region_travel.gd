extends Node
const PORTAL_SCRIPT: Script = preload("res://scripts/world/region_portal.gd")
var pending_from := ""
var changing := false
var catalog: Dictionary = {}
var current_region := "centre"
func _ready() -> void:
	catalog = JSON.parse_string(FileAccess.get_file_as_string("res://maps/ferrugem_baixa/region.json"))
func setup(world: Node2D, id: String) -> void:
	current_region = id
	_setup_portals(world)
	var player: CharacterBody2D = world.get_node_or_null("Structures/Player")
	if not player: return
	if pending_from != "":
		var portal := world.get_node_or_null("RegionPortals/To_"+pending_from)
		if portal: player.position = portal.position+portal.get_meta("arrival_offset",Vector2(0,58))
	pending_from = ""
	player.spawn_point = player.position
	changing = false

func _setup_portals(world: Node2D) -> void:
	var portal_root := world.get_node_or_null("RegionPortals")
	if portal_root == null:
		return
	for portal: Area2D in portal_root.get_children():
		if portal.get_script() != PORTAL_SCRIPT:
			portal.set_script(PORTAL_SCRIPT)
		portal.destination = str(portal.get_meta("destination", str(portal.name).trim_prefix("To_")))
		portal.initialize()
func travel(destination: String) -> void:
	# Transições legadas para mapas de protótipos antigos desativadas
	return
	if get_tree().current_scene and get_tree().current_scene.has_node("ContinuousRoutes"):return
	if changing or not catalog.has(destination): return
	changing = true
	pending_from = current_region
	var error := get_tree().change_scene_to_file(catalog[destination].scene)
	if error != OK:
		changing = false
		pending_from = ""
		push_error("Region transition failed: "+destination)
