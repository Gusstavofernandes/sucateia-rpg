extends Node2D
func _ready() -> void:
	# Preserve approved serialized guards; only replace the seam covered by the supported bay.
	for path in get_meta("opened_seam_shapes",[]):
		var shape: CollisionShape2D=get_parent().get_node(path)
		shape.set_deferred("disabled",true)
