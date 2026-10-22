extends Node2D

## Script controlador da Arena Coliseu Imponente de Fundo-Ferro (Escala Gigante)
## Arquitetura Godot 4.7 com tipagem estática.

enum EstadoPortao {
	FECHADO,
	ABRINDO,
	ABERTO
}

enum EstadoAmbiental {
	SECA,
	INUNDADA,
	ELETRICA,
	TOXICA,
	VAPOR
}

@export var estado_portao_atual: EstadoPortao = EstadoPortao.FECHADO
@export var estado_ambiente: EstadoAmbiental = EstadoAmbiental.SECA

# Nós principais do Coliseu Imponente
@onready var arquibancada_norte: Sprite2D = get_node_or_null("ArquibancadaMeiaLuaNorte") as Sprite2D
@onready var muralha_sul: Sprite2D = get_node_or_null("MuralhaSulArredondada") as Sprite2D

# Limites da câmera para a arena ampliada
const CAMERA_LIMIT_LEFT   := 3500
const CAMERA_LIMIT_TOP    := 80
const CAMERA_LIMIT_RIGHT  := 7000
const CAMERA_LIMIT_BOTTOM := 1550

# Jogador para cálculo do fade por proximidade
var _player: CharacterBody2D = null
var _alpha_muralha_sul: float = 1.0


func _ready() -> void:
	var parent_node := get_parent()
	if parent_node != null:
		_player = parent_node.get_node_or_null("Player") as CharacterBody2D


func _process(delta: float) -> void:
	_processar_fade_proximidade(delta)


func _processar_fade_proximidade(delta: float) -> void:
	if _player == null or muralha_sul == null:
		return
		
	var py: float = _player.global_position.y
	var px: float = _player.global_position.x
	
	# O fade ocorre quando o jogador se aproxima por trás da borda sul do fosso (escala colossal)
	var perto_sul: bool = (py >= 580.0 and py <= 1060.0 and px >= 4300.0 and px <= 5600.0)
	var target_alpha: float = 0.55 if perto_sul else 1.0
	
	_alpha_muralha_sul = move_toward(_alpha_muralha_sul, target_alpha, delta * 3.5)
	muralha_sul.modulate.a = _alpha_muralha_sul
