extends Area2D
var nearby := false
func _ready() -> void:
	body_entered.connect(func(body: Node2D):
		if body.is_in_group("player"):nearby=true;$Prompt.visible=true)
	body_exited.connect(func(body: Node2D):
		if body.is_in_group("player"):nearby=false;$Prompt.visible=false)
func _unhandled_input(event: InputEvent) -> void:
	if nearby and event is InputEventKey and event.pressed and not event.echo and event.keycode==KEY_F:
		var travel := get_node_or_null("/root/LayerTravel")
		if travel:
			get_viewport().set_input_as_handled()
			travel.request(self)
