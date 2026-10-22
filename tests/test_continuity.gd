extends SceneTree
func _initialize() -> void: call_deferred("run")
func run() -> void:
	var data: Dictionary = JSON.parse_string(FileAccess.get_file_as_string("res://maps/ferrugem_baixa/region.json"))
	var failures: Array[String] = []
	for id in data:
		var cfg: Dictionary = data[id]
		if not cfg.has("continuity") or not cfg.has("function"):
			failures.append(id+" has no regional border plan")
			continue
		for dest in cfg.links:
			if not cfg.continuity.has(dest): failures.append(id+" has unplanned boundary "+dest);continue
			var border: Dictionary = cfg.continuity[dest]
			if not data[dest].get("continuity",{}).has(id): failures.append(id+" has unilateral border");continue
			var reverse: Dictionary = data[dest].continuity[id]
			if border.shared_id != reverse.shared_id or border.family != reverse.family: failures.append(id+" mismatched shared infrastructure")
			if border.features.is_empty() or border.get("transition","") == "": failures.append(id+" empty transition")
		var packed: PackedScene = load(cfg.scene)
		var scene: Node = packed.instantiate()
		var continuity: Node = scene.get_node_or_null("RegionalContinuity")
		if not continuity: failures.append(id+" has no built continuity")
		else:
			for dest in cfg.links:
				if not continuity.has_meta("border_"+dest): failures.append(id+" missing rendered border "+dest)
				if continuity.get_meta("route_cells_"+dest,0)==0: failures.append(id+" no interior route to "+dest)
		scene.free()
	if failures.is_empty(): print("PASS: every sector has reciprocal border, shared infrastructure and regional function");quit(0)
	else:
		for failure in failures: push_error(failure)
		quit(1)
