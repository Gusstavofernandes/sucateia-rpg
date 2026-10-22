extends Area2D
@export var destination := ""
var nearby := false
var initialized := false

func _ready() -> void:
	initialize()

func initialize() -> void:
	if initialized:
		return
	initialized = true
	collision_layer = 0
	collision_mask = 2
	monitoring = true
	monitorable = false
	if get_node_or_null("TravelSensor") == null:
		var sensor := CollisionShape2D.new()
		sensor.name = "TravelSensor"
		var shape := CircleShape2D.new()
		shape.radius = 48.0
		sensor.shape = shape
		add_child(sensor)
	body_entered.connect(_on_body_entered)
	body_exited.connect(_on_body_exited)
	set_process_unhandled_input(true)
	var prompt := get_node_or_null("Prompt")
	if prompt is CanvasItem:
		prompt.visible = false

func _on_body_entered(body: Node2D) -> void:
	if body.is_in_group("player"):
		nearby = true
		var prompt := get_node_or_null("Prompt")
		if prompt is CanvasItem:
			prompt.visible = true

func _on_body_exited(body: Node2D) -> void:
	if body.is_in_group("player"):
		nearby = false
		var prompt := get_node_or_null("Prompt")
		if prompt is CanvasItem:
			prompt.visible = false
func _unhandled_input(event: InputEvent) -> void:
	if nearby and event is InputEventKey and event.pressed and not event.echo and event.keycode == KEY_E:
		var travel := get_node_or_null("/root/RegionTravel")
		get_viewport().set_input_as_handled()
		if travel: travel.travel(destination)
