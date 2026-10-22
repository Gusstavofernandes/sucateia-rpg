extends CharacterBody2D

@export var speed: float = 240.0
@export var accel: float = 16.0
@export var friction: float = 18.0

@onready var light: PointLight2D = $LanternLight

func _physics_process(delta: float) -> void:
	var input_vector := Vector2.ZERO
	input_vector.x = Input.get_action_strength("ui_right") - Input.get_action_strength("ui_left")
	input_vector.y = Input.get_action_strength("ui_down") - Input.get_action_strength("ui_up")
	input_vector = input_vector.normalized()
	
	if input_vector != Vector2.ZERO:
		velocity = velocity.move_toward(input_vector * speed, accel * speed * delta)
	else:
		velocity = velocity.move_toward(Vector2.ZERO, friction * speed * delta)
		
	move_and_slide()
