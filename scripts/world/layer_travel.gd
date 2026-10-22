extends Node
const SURFACE := "res://maps/sucateia/sucateia.tscn"
const UNDERGROUND := "res://maps/fundo_ferro/fundo_ferro.tscn"
const ACCESS_IDS := ["PocoVelho","DocaLeste","ForjasManutencao"]
var pending_id := ""
var current_layer := "surface"
var changing := false
var transition_count := 0
func setup(world: Node2D, layer: String) -> void:
	current_layer=layer
	var player: CharacterBody2D=world.get_node("Structures/Player")
	if pending_id!="":
		var marker: Marker2D=world.get_node("LayerArrivals/"+pending_id)
		player.position=marker.position;player.get_node("Camera").reset_smoothing()
	pending_id="";player.spawn_point=player.position;changing=false
func request(entry: Area2D) -> bool:
	var world := get_tree().current_scene
	if changing or not world or not ACCESS_IDS.has(str(entry.name)) or entry.get_parent()!=world.get_node_or_null("LayerEntrances"):return false
	var player: CharacterBody2D=world.get_node("Structures/Player")
	if player.global_position.distance_to(entry.global_position)>52:return false
	if player.get("navigation_layer")=="cabos":return false
	var source: String=world.get_meta("world_layer","surface")
	if source!=current_layer:return false
	pending_id=str(entry.name);changing=true
	var error := get_tree().change_scene_to_file(UNDERGROUND if source=="surface" else SURFACE)
	if error!=OK:pending_id="";changing=false;push_error("Layer access failed");return false
	transition_count+=1;return true
