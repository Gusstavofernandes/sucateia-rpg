extends "res://tests/test_amarras_preservation.gd"
func run() -> void:
	var before: Node=load("res://tools/checkpoints/sucateia_before_cabos.tscn").instantiate();var current: Node=load("res://maps/sucateia/sucateia.tscn").instantiate()
	var good := compare(before,current,"Sucateia");before.free();current.free()
	if good:print("PASS: all approved city nodes, Amarras/Forjas architecture, floor cells, materials, coast, physics and access placements preserved")
	quit(0 if good else 1)
