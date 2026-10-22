extends CharacterBody2D
const WALK_SPEED := 155.0
var spawn_point := Vector2(1152, 1248)
var navigation_layer := "surface"
var elapsed := 0.0
func _physics_process(delta: float) -> void:
	var direction := Vector2(float(Input.is_physical_key_pressed(KEY_D) or Input.is_physical_key_pressed(KEY_RIGHT)) - float(Input.is_physical_key_pressed(KEY_A) or Input.is_physical_key_pressed(KEY_LEFT)), float(Input.is_physical_key_pressed(KEY_S) or Input.is_physical_key_pressed(KEY_DOWN)) - float(Input.is_physical_key_pressed(KEY_W) or Input.is_physical_key_pressed(KEY_UP)))
	velocity = direction.normalized() * WALK_SPEED * (1.65 if Input.is_physical_key_pressed(KEY_SHIFT) else 1.0)
	var previous := global_position
	move_and_slide()
	var world := get_tree().current_scene
	if world and world.has_method("is_walkable") and not world.is_walkable(global_position):global_position=previous
	elapsed += delta
	var art: Sprite2D = $Sprite
	art.position.y = -22.0 + sin(elapsed * 12.0) * (1.5 if velocity.length() > 1.0 else 0.0)
	if direction.x != 0.0: art.flip_h = direction.x < 0.0
func _unhandled_input(event: InputEvent) -> void:
	if event is InputEventKey and event.pressed and not event.echo:
		if event.keycode == KEY_R: position = spawn_point
		if event.keycode == KEY_F1: get_tree().call_group("slice_hud", "toggle")
	if event is InputEventMouseButton and event.pressed:
		var camera: Camera2D = $Camera
		if event.button_index == MOUSE_BUTTON_WHEEL_UP: camera.zoom = (camera.zoom * 1.1).clamp(Vector2(0.65,0.65),Vector2(1.5,1.5))
		if event.button_index == MOUSE_BUTTON_WHEEL_DOWN: camera.zoom = (camera.zoom / 1.1).clamp(Vector2(0.65,0.65),Vector2(1.5,1.5))
