class_name PassarelaCano
extends Area2D

## Script de gerenciamento da travessia sobre a tubulação industrial.
## Ao cruzar a passarela no eixo Y (norte-sul), ajusta suavemente a elevação vertical
## dos nós visuais do jogador (cabeça, cabelo, colete, lanterna) sem afetar a colisão física ou causar teleporte.

@export var max_elevation: float = 6.0
var _players_inside: Array[Node2D] = []

func _ready() -> void:
	body_entered.connect(_on_body_entered)
	body_exited.connect(_on_body_exited)

func _on_body_entered(body: Node2D) -> void:
	if body is CharacterBody2D:
		if not _players_inside.has(body):
			_players_inside.append(body)

func _on_body_exited(body: Node2D) -> void:
	if _players_inside.has(body):
		_players_inside.erase(body)
		_reset_player_visuals(body)

func _process(_delta: float) -> void:
	for body: Node2D in _players_inside:
		if is_instance_valid(body):
			var rel_y: float = body.global_position.y - global_position.y
			var factor: float = 0.0
			# Intervalo de transição da passarela (rampa norte / centro / rampa sul)
			if rel_y >= -55.0 and rel_y <= 55.0:
				var norm: float = 1.0 - absf(rel_y) / 55.0
				factor = clampf(norm * 1.5, 0.0, 1.0)
			_apply_player_visuals(body, factor * -max_elevation)

func _apply_player_visuals(player: Node2D, offset_y: float) -> void:
	for node_name: String in ["GoblinHead", "GoblinHair", "GoblinVest", "LanternLight"]:
		var n: Node2D = player.get_node_or_null(node_name) as Node2D
		if n:
			if not n.has_meta("orig_y"):
				n.set_meta("orig_y", n.position.y)
			n.position.y = (n.get_meta("orig_y") as float) + offset_y

func _reset_player_visuals(player: Node2D) -> void:
	for node_name: String in ["GoblinHead", "GoblinHair", "GoblinVest", "LanternLight"]:
		var n: Node2D = player.get_node_or_null(node_name) as Node2D
		if n and n.has_meta("orig_y"):
			n.position.y = n.get_meta("orig_y") as float
