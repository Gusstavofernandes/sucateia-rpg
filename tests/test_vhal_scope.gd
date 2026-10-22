extends SceneTree
func _initialize() -> void:
	call_deferred("run")
func run() -> void:
	var data: Dictionary = JSON.parse_string(FileAccess.get_file_as_string("res://maps/ferrugem_baixa/region.json"))
	var chain := ["chamines","north_expedition","river_route","caelporto","vhal_lower","twin_plaza"]
	var failures: Array[String] = []
	for id in chain:
		if not data.has(id): failures.append("Missing northern locality: "+id)
	for i in range(chain.size()-1):
		if not data.has(chain[i]) or not data.has(chain[i+1]): continue
		if not data[chain[i]].links.has(chain[i+1]) or not data[chain[i+1]].links.has(chain[i]): failures.append("Disconnected north route")
	for id in ["caelporto","vhal_lower","twin_plaza"]:
		if not data.has(id): continue
		if data[id].get("region","") != "VHAL-KOR": failures.append("Wrong region: "+id)
		if data[id].get("floor_texture","") != "vhal/stone_ground.png": failures.append("Missing human paving: "+id)
		for asset in data[id].buildings:
			if asset[0] in ["house","house_stack","tenement","workshop","crown"]: failures.append("Goblin architecture reused in human core: "+id)
	if data.has("vhal_lower") and data.vhal_lower.buildings.size()<10: failures.append("Lower city lacks urban density")
	if data.has("twin_plaza") and not data.twin_plaza.markers.has("TorresGemeas"): failures.append("Twin landmark not explorable")
	for name in ["gothic_block","port_warehouse","twin_towers","arcane_station","river_crossing","stone_quay","stone_ground"]:
		if not FileAccess.file_exists("res://assets/vhal/"+name+".png"): failures.append("Missing dedicated visual: "+name)
	if failures.is_empty():
		print("PASS: northern geography chain, distinct human core and dedicated art")
		quit(0)
	else:
		for failure in failures: push_error(failure)
		quit(1)
