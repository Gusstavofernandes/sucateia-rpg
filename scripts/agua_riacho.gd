@tool
extends Node2D
class_name AguaRiacho

@export var pontos_caminho: PackedVector2Array = []
@export var altura_parede_topo: float = 52.0
@export var altura_parede_base: float = 40.0
@export var largura_maxima: float = 34.0
@export var largura_parede_frac: float = 0.55
@export var z_index_agua: int = -5
@export var seed_offset: float = 0.0
@export var fator_velocidade: float = 1.0
@export var cena_impacto: PackedScene = preload("res://scenes/Impacto.tscn")
@export var usar_sulco_pedra: bool = true

var linha_agua: Line2D
var linha_umidade: Line2D
var linha_sulco: Line2D
var impacto_topo: Node2D
var impacto_canal: Node2D

func _ready() -> void:
	_construir_riacho()

func _construir_riacho() -> void:
	for c in get_children():
		c.queue_free()

	# 1. Gera pontos com foz situada seguramente DENTRO da lâmina de água do canal
	# (Foz termina em Y=265 relative, world Y = 240 + 265 = 505px, dentro do canal 485..565)
	var pontos := pontos_caminho
	if pontos.size() < 2:
		pontos = _gerar_pontos_padrao()

	# 2. Distâncias e frações
	var distancias: Array[float] = [0.0]
	var total_len: float = 0.0
	for i in range(pontos.size() - 1):
		total_len += pontos[i].distance_to(pontos[i + 1])
		distancias.append(total_len)

	var fim_parede_topo: float = clamp(altura_parede_topo / total_len, 0.05, 0.35)
	var inicio_parede_base: float = clamp((total_len - altura_parede_base) / total_len, 0.65, 0.95)

	# 3. Line2D de Umidade na Pedra (no trecho do chão)
	var pontos_chao := _extrair_pontos_chao(pontos, distancias, altura_parede_topo, total_len - altura_parede_base)
	if pontos_chao.size() >= 2:
		linha_umidade = Line2D.new()
		linha_umidade.name = "UmidadeChao"
		linha_umidade.z_index = z_index_agua - 2
		linha_umidade.points = pontos_chao
		linha_umidade.width = largura_maxima * 1.85
		linha_umidade.texture_mode = Line2D.LINE_TEXTURE_STRETCH
		linha_umidade.begin_cap_mode = Line2D.LINE_CAP_ROUND
		linha_umidade.end_cap_mode = Line2D.LINE_CAP_ROUND
		linha_umidade.joint_mode = Line2D.LINE_JOINT_ROUND
		
		var mat_umidade = ShaderMaterial.new()
		mat_umidade.shader = load("res://shaders/agua_umidade.gdshader")
		mat_umidade.set_shader_parameter("ruido", load("res://resources/ruido_a.tres"))
		mat_umidade.set_shader_parameter("cor_umidade", Color(0.01, 0.03, 0.02, 0.58))
		linha_umidade.material = mat_umidade
		add_child(linha_umidade)

	# 4. Sulco escuro na pedra
	if usar_sulco_pedra and pontos_chao.size() >= 2:
		linha_sulco = Line2D.new()
		linha_sulco.name = "SulcoPedra"
		linha_sulco.z_index = z_index_agua - 1
		linha_sulco.points = pontos_chao
		linha_sulco.width = largura_maxima * 0.58
		linha_sulco.default_color = Color(0.02, 0.05, 0.04, 0.45)
		linha_sulco.begin_cap_mode = Line2D.LINE_CAP_ROUND
		linha_sulco.end_cap_mode = Line2D.LINE_CAP_ROUND
		linha_sulco.joint_mode = Line2D.LINE_JOINT_ROUND
		add_child(linha_sulco)

	# 5. Line2D da Água Principal
	linha_agua = Line2D.new()
	linha_agua.name = "LinhaAgua"
	linha_agua.z_index = z_index_agua
	linha_agua.points = pontos
	linha_agua.width = largura_maxima
	linha_agua.texture_mode = Line2D.LINE_TEXTURE_STRETCH
	linha_agua.begin_cap_mode = Line2D.LINE_CAP_ROUND
	linha_agua.end_cap_mode = Line2D.LINE_CAP_ROUND
	linha_agua.joint_mode = Line2D.LINE_JOINT_ROUND

	var curve = Curve.new()
	curve.add_point(Vector2(0.0, largura_parede_frac))
	curve.add_point(Vector2(fim_parede_topo, largura_parede_frac))
	curve.add_point(Vector2(fim_parede_topo + 0.04, 1.0))
	curve.add_point(Vector2(inicio_parede_base - 0.04, 1.0))
	curve.add_point(Vector2(inicio_parede_base, largura_parede_frac))
	curve.add_point(Vector2(1.0, largura_parede_frac * 0.8))
	linha_agua.width_curve = curve

	var mat_agua = ShaderMaterial.new()
	mat_agua.shader = load("res://shaders/agua_riacho.gdshader")
	mat_agua.set_shader_parameter("ruido_a", load("res://resources/ruido_a.tres"))
	mat_agua.set_shader_parameter("ruido_b", load("res://resources/ruido_b.tres"))
	mat_agua.set_shader_parameter("fim_parede_topo", fim_parede_topo)
	mat_agua.set_shader_parameter("inicio_parede_base", inicio_parede_base)
	mat_agua.set_shader_parameter("vel_parede", 0.90 * fator_velocidade)
	mat_agua.set_shader_parameter("vel_chao", 0.22 * fator_velocidade)
	mat_agua.set_shader_parameter("seed_tempo", seed_offset)
	mat_agua.set_shader_parameter("cor_fundo", Color(0.03, 0.12, 0.09, 0.92))
	mat_agua.set_shader_parameter("cor_raso", Color(0.10, 0.30, 0.22, 0.92))
	mat_agua.set_shader_parameter("cor_nucleo", Color(0.58, 0.85, 0.62, 1.0))
	mat_agua.set_shader_parameter("cor_espuma", Color(0.68, 0.84, 0.70, 0.95))
	mat_agua.set_shader_parameter("cor_borda", Color(0.02, 0.07, 0.05, 0.95))
	linha_agua.material = mat_agua
	add_child(linha_agua)

	# 6. Impacto sutil na foz do canal (na lâmina de água verde, sem esfera branca)
	if cena_impacto:
		impacto_canal = cena_impacto.instantiate()
		impacto_canal.name = "ImpactoCanal"
		impacto_canal.position = pontos[-1]
		impacto_canal.z_index = z_index_agua
		impacto_canal.scale = Vector2(0.45, 0.25)
		add_child(impacto_canal)

func _gerar_pontos_padrao() -> PackedVector2Array:
	# Trajeto de 248px: deságua logo na face norte do canal (para trás), integrando-se diretamente ao espelho d'água
	return PackedVector2Array([
		Vector2(0, 0),         # 1. Grade do bueiro (Y=240)
		Vector2(0, 52),        # 2. Pé da parede vertical (Y=292)
		Vector2(-5, 92),       # 3. Serpenteio suave à esquerda
		Vector2(8, 138),       # 4. Fresta na pedra à direita
		Vector2(-6, 182),      # 5. Escoamento à esquerda
		Vector2(0, 226),       # 6. Quina do vertedouro (mureta norte do canal, Y=466)
		Vector2(0, 248)        # 7. FOZ NO CANAL (queda de 22px até a lâmina d'água, Y=488)
	])

func _extrair_pontos_chao(pontos: PackedVector2Array, dists: Array[float], d_inicio: float, d_fim: float) -> PackedVector2Array:
	var res := PackedVector2Array()
	res.append(_interpolar_ponto_na_distancia(pontos, dists, d_inicio))
	for i in range(pontos.size()):
		if dists[i] > d_inicio and dists[i] < d_fim:
			res.append(pontos[i])
	res.append(_interpolar_ponto_na_distancia(pontos, dists, d_fim))
	return res

func _interpolar_ponto_na_distancia(pontos: PackedVector2Array, dists: Array[float], target_d: float) -> Vector2:
	if target_d <= 0.0:
		return pontos[0]
	if target_d >= dists[-1]:
		return pontos[-1]
	for i in range(dists.size() - 1):
		if target_d >= dists[i] and target_d <= dists[i + 1]:
			var seg_len = dists[i + 1] - dists[i]
			var t = 0.0 if seg_len <= 0.001 else (target_d - dists[i]) / seg_len
			return pontos[i].lerp(pontos[i + 1], t)
	return pontos[-1]
