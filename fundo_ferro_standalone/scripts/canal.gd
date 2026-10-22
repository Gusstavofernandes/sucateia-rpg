extends Node2D

@export var lanternas: Array[Node2D] = []
@onready var agua: Sprite2D = $Agua

func _ready() -> void:
	if not agua or not agua.material:
		return
	
	# Duplica o material por trecho para permitir lanternas locais sem perder a continuidade
	# (o shader usa world_pos, portanto a correnteza e o ruído são 100% contínuos e sem emendas)
	agua.material = agua.material.duplicate()
	var mat := agua.material as ShaderMaterial
	
	var pos := PackedVector2Array()
	for l in lanternas:
		if is_instance_valid(l):
			pos.append(l.global_position)
	
	# O array do shader tem tamanho fixo (4), então completa com zeros
	while pos.size() < 4:
		pos.append(Vector2.ZERO)
	
	mat.set_shader_parameter("luzes", pos)
	mat.set_shader_parameter("n_luzes", min(lanternas.size(), 4))
