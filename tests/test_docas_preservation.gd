extends "res://tests/test_amarras_preservation.gd"
func run() -> void:
	var before: Node=load("res://tools/checkpoints/sucateia_before_docas.tscn").instantiate();var current: Node=load("res://maps/sucateia/sucateia.tscn").instantiate();var good := compare(before,current,"Sucateia")
	before.free();current.free();if good:print("PASS: all approved districts, Cabos/Forjas/Amarras, floors/coast/water/physics/architecture preserved before Docas")
	quit(0 if good else 1)
