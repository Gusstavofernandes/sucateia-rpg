extends SceneTree

func _init() -> void:
	var root = Node2D.new()
	root.name = "Impacto"
	
	# 1. Poça e anéis de espuma (Sprite2D com shader)
	var poca = Sprite2D.new()
	poca.name = "PocaEspuma"
	
	var placeholder = PlaceholderTexture2D.new()
	placeholder.size = Vector2(80, 40)
	poca.texture = placeholder
	
	var shader_impacto = load("res://shaders/agua_impacto.gdshader")
	var mat_impacto = ShaderMaterial.new()
	mat_impacto.shader = shader_impacto
	mat_impacto.set_shader_parameter("cor_espuma", Color(0.65, 0.80, 0.65, 1.0))
	mat_impacto.set_shader_parameter("velocidade", 1.6)
	poca.material = mat_impacto
	root.add_child(poca)
	poca.owner = root
	
	# 2. Respingos (GPUParticles2D)
	var particulas = GPUParticles2D.new()
	particulas.name = "Respingos"
	particulas.amount = 24
	particulas.lifetime = 0.5
	particulas.explosiveness = 0.0
	particulas.local_coords = false
	particulas.texture = load("res://resources/splash_particle.tres")
	
	var pmat = ParticleProcessMaterial.new()
	pmat.direction = Vector3(0, -1, 0)
	pmat.spread = 55.0
	pmat.initial_velocity_min = 40.0
	pmat.initial_velocity_max = 90.0
	pmat.gravity = Vector3(0, 400, 0)
	pmat.scale_min = 0.6
	pmat.scale_max = 1.2
	
	# Curve de escala caindo para zero no final
	var curve = Curve.new()
	curve.add_point(Vector2(0, 1.0))
	curve.add_point(Vector2(1.0, 0.0))
	var curve_tex = CurveTexture.new()
	curve_tex.curve = curve
	pmat.scale_curve = curve_tex
	
	# Gradiente de cor de verde-claro quase branco (alfa 0.9) para alfa 0.0
	var grad = Gradient.new()
	grad.colors = PackedColorArray([
		Color(0.82, 0.95, 0.85, 0.90),
		Color(0.65, 0.82, 0.68, 0.0)
	])
	var grad_tex = GradientTexture1D.new()
	grad_tex.gradient = grad
	pmat.color_ramp = grad_tex
	
	particulas.process_material = pmat
	root.add_child(particulas)
	particulas.owner = root
	
	# 3. VisibleOnScreenNotifier2D para otimizacao
	var notifier = VisibleOnScreenNotifier2D.new()
	notifier.name = "OtimizadorVisivel"
	notifier.rect = Rect2(-60, -40, 120, 80)
	root.add_child(notifier)
	notifier.owner = root
	
	# Script para desativar emitting quando fora da tela
	var script = GDScript.new()
	script.source_code = """extends Node2D

@onready var particulas: GPUParticles2D = $Respingos
@onready var notifier: VisibleOnScreenNotifier2D = $OtimizadorVisivel

func _ready() -> void:
	notifier.screen_entered.connect(func(): particulas.emitting = true)
	notifier.screen_exited.connect(func(): particulas.emitting = false)
"""
	root.set_script(script)
	
	var scene = PackedScene.new()
	scene.pack(root)
	ResourceSaver.save(scene, "res://scenes/Impacto.tscn")
	print("Impacto.tscn criado com sucesso!")
	quit()
