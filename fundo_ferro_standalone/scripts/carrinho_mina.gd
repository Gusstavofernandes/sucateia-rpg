class_name CarrinhoMinerio
extends Node2D

## Carrinho de Minério Verde do Fundo-Ferro
## Movimentação vertical e efeitos de iluminação luminescente de minério

@export var velocidade_maxima: float = 120.0
@export var aceleracao: float = 60.0
@export var limite_norte_y: float = 330.0
@export var limite_sul_y: float = 620.0

@onready var sprite_carrinho: Sprite2D = $SpriteCarrinho
@onready var sombra: Sprite2D = $SombraCarrinho
@onready var luz_minerio: PointLight2D = $LuzMinerio

var _velocidade_atual: float = 0.0
var _direcao: float = 1.0 # 1 = descendo para o sul, -1 = subindo para o norte
var _tempo_pulso: float = 0.0

func _ready() -> void:
	z_index = 2
	y_sort_enabled = true

func _process(delta: float) -> void:
	# Pulso suave da luz verde do minério radioativo
	_tempo_pulso += delta * 2.5
	if luz_minerio:
		luz_minerio.energy = 1.6 + sin(_tempo_pulso) * 0.35

func mover_ao_longo_do_trilho(delta: float) -> void:
	# Acelerar e desacelerar suavemente
	_velocidade_atual = move_toward(_velocidade_atual, velocidade_maxima * _direcao, aceleracao * delta)
	position.y += _velocidade_atual * delta
	
	# Inverter direção ao atingir limites de teste
	if position.y >= limite_sul_y:
		position.y = limite_sul_y
		_direcao = -1.0
	elif position.y <= limite_norte_y:
		position.y = limite_norte_y
		_direcao = 1.0
