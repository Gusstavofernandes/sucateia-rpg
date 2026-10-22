extends Node2D
func _process(_delta: float) -> void:
	var player: Node2D=get_parent().get_parent().get_parent().get_node_or_null("Structures/Player")
	if not player:return
	var up: bool=player.get("navigation_layer")=="surface"
	var point: Vector2=get_meta("surface_arrival" if up else "elevated_arrival")
	$Prompt.position=point+Vector2(-40,16);$Prompt.text="F • Subir" if up else "F • Descer";$Prompt.visible=player.position.distance_to(point)<=42
func _unhandled_input(event: InputEvent) -> void:
	if event is InputEventKey and event.pressed and not event.echo and event.keycode==KEY_F:
		if get_parent().get_parent().change_layer(self):get_viewport().set_input_as_handled()
