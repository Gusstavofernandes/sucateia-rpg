extends RefCounted

func install(world: Node2D) -> void:
	if not world.has_node("DocasDistrict"):return
	var finish:=Node2D.new()
	finish.name="PortApproachFinish"
	finish.z_index=-13
	world.add_child(finish)
	var hidden: Array[String]=[]
	# Grate bays and upright repair pipes used to overlap the house and the
	# street in this short approach. The original physical bank remains.
	var area:=Rect2(1985,1115,280,405)
	for old in world.get_node("FinishedInfrastructure").get_children():
		if not old is Sprite2D or not old.texture or not area.has_point(old.position):continue
		var file: String=old.texture.resource_path.get_file()
		var obsolete_shadow: bool = file == "light.svg" and old.modulate.r < .1 and old.modulate.g < .1 and old.modulate.a >= .5
		if file in ["walkway.png","stairs.png","pipe.png","metal_repair.png"] or obsolete_shadow:
			old.hide()
			hidden.append(str(world.get_path_to(old)))
	var district: Node2D=world.get_node("DocasDistrict")
	for parent_name in ["WorkingDecks","WetSupports"]:
		for old in district.get_node(parent_name).get_children():
			var label:=String(old.name)
			if label.begins_with("ChegadaUrbana") or label.begins_with("EntradaInterior") or label.begins_with("EntradaEstaca"):
				old.hide()
				hidden.append(str(world.get_path_to(old)))
	# Paving uses the existing bank contour: it never paints new land over
	# the harbor or the canal, and stays below architecture and thresholds.
	var apron:=Polygon2D.new()
	apron.name="StoneQuay"
	apron.z_index=-3
	apron.polygon=PackedVector2Array([Vector2(2040,1120),Vector2(2270,1120),Vector2(2285,1230),Vector2(2285,1400),Vector2(2160,1400),Vector2(2160,1480),Vector2(2255,1510),Vector2(2255,1535),Vector2(2005,1525),Vector2(1995,1410),Vector2(2020,1320),Vector2(2015,1220)])
	apron.texture=load("res://assets/reconstruction/port_approach/maintained_quay_paving.png")
	var uv:=PackedVector2Array()
	for point in apron.polygon:uv.append((point-Vector2(1980,1100))*2.75)
	apron.uv=uv
	apron.color=Color(.87,.87,.79,1)
	finish.add_child(apron)
	var threshold:=Sprite2D.new()
	threshold.name="StoneToTimberThreshold"
	threshold.texture=load("res://assets/reconstruction/port_approach/stone_timber_threshold.png")
	threshold.scale=Vector2(.14,.27)
	threshold.position=Vector2(2230,1355)-(Vector2(120,392)-Vector2(threshold.texture.get_size())*.5)*threshold.scale
	threshold.z_index=3
	threshold.modulate=Color(.83,.83,.75,1)
	finish.add_child(threshold)
	# Cover the existing landing's north band with the same planking. The
	# newly generated threshold supplies the actual stone/wood seam and base.
	var landing:=Polygon2D.new()
	landing.name="UpperLandingPlanks"
	landing.polygon=PackedVector2Array([Vector2(2275,1294),Vector2(2441,1294),Vector2(2441,1340),Vector2(2275,1340)])
	landing.texture=threshold.texture
	landing.uv=PackedVector2Array([Vector2(760,250),Vector2(1660,250),Vector2(1660,480),Vector2(760,480)])
	landing.z_index=2
	landing.color=threshold.modulate
	finish.add_child(landing)
	finish.set_meta("hidden_legacy_art",hidden)
	finish.set_meta("scope","local city-to-port approach; physical coastline, routes, architecture and player arrivals retained")
