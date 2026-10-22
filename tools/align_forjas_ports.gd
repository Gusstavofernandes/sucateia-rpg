extends "res://tools/correct_forjas_direction.gd"
func run() -> void:
	world=load("res://maps/sucateia/sucateia.tscn").instantiate();world.set_script(null);root.add_child(world);district=world.get_node("ForjasRasasDistrict");detail=district.get_node("ProductionDirectionFinish");yards=world.get_node("Structures/ForjasProductionYards")
	if detail.has_meta("ports_aligned"):world.queue_free();await process_frame;print("FORJAS port alignment preserved");quit(0);return
	for file in ["heat_reflection_mask.png","exhaust_reducer_connector.png"]:
		if not ResourceLoader.exists(ART+file):push_error("Unimported final connector: "+file);quit(1);return
	for label in ["AlimentacaoCarvao","AlimentacaoResfriamento","RetornoResfriamento","DescargaRecuperacao"]:
		var old: Node=detail.get_node(label);detail.remove_child(old);old.free()
	conduit("AlimentacaoCarvao",PackedVector2Array([Vector2(2606,-1211),Vector2(2635,-1211),Vector2(2635,-1115),Vector2(2700,-1115)]),26)
	conduit("AlimentacaoResfriamento",PackedVector2Array([Vector2(2823,-343),Vector2(2840,-343),Vector2(2840,-440),Vector2(2790,-440)]),23)
	conduit("RetornoResfriamento",PackedVector2Array([Vector2(2642,-306),Vector2(2630,-306),Vector2(2630,-230),Vector2(2860,-230),Vector2(2860,-45)]),20)
	conduit("DescargaRecuperacao",PackedVector2Array([Vector2(3445,-981),Vector2(3380,-981),Vector2(3380,-800),Vector2(3320,-800)]),24)
	for sprite in detail.get_children():
		if sprite is Sprite2D and sprite.texture.resource_path.ends_with("short_service_catwalk.png"):
			var center: Vector2=sprite.position+(Vector2(887,476)-Vector2(sprite.texture.get_size())*.5)*sprite.scale
			sprite.scale=Vector2.ONE*(220./1606.);sprite.position=center+(Vector2(sprite.texture.get_size())*.5-Vector2(887,476))*sprite.scale
		if sprite is Sprite2D and sprite.texture.resource_path.ends_with("transition_soot_decal.png"):sprite.modulate.a=.32
	for data in [[Vector2(2730,-956),Vector2(230,138)],[Vector2(3170,-915),Vector2(180,105)]]:
		extracted("heat_reflection_mask.png",Rect2(138,121,1307,772),data[0],data[1],detail).modulate=Color(1,1,1,.18)
	var foundry: Node2D=world.get_node("Structures/ForjasIndustrialArchitecture/FundicaoDasCaldeiras")
	var roof := Node2D.new();roof.name="DutoDeExaustaoLigado";foundry.add_child(roof)
	# Large reducer collar overlaps the tower's real west inlet; east cap stays closed.
	var reducer := Sprite2D.new();reducer.texture=load(ART+"exhaust_reducer_connector.png");reducer.scale=Vector2.ONE*(70./1241.)
	reducer.position=Vector2(-78,-306)+(Vector2(reducer.texture.get_size())*.5-Vector2(1280,598))*reducer.scale;roof.add_child(reducer)
	var points := PackedVector2Array([Vector2(-50,-230),Vector2(-150,-230),Vector2(-150,-309),Vector2(-136,-309)])
	for i in range(points.size()-1):
		var delta := points[i+1]-points[i]
		art("res://assets/generated/props/pipe.png",points[i].lerp(points[i+1],.5),Vector2(delta.length()+7,27),roof,delta.angle()).modulate=Color(.82,.74,.57)
	var steam := CPUParticles2D.new();steam.name="VaporDeResfriamento";steam.position=Vector2(12,-69);steam.texture=load("res://assets/fx/smoke_01.png");steam.amount=6;steam.lifetime=1.9;steam.preprocess=2.;steam.direction=Vector2(.1,-1);steam.spread=14.;steam.gravity=Vector2(0,-3);steam.initial_velocity_min=7;steam.initial_velocity_max=11;steam.scale_amount_min=.035;steam.scale_amount_max=.055;steam.color=Color(.58,.59,.54,.16);yards.get_node("TanqueDeResfriamento").add_child(steam)
	detail.set_meta("ports_aligned",true);district.set_meta("direction_status","direction correction integrated and navigation verified; final visual review pending")
	world.set_script(load("res://scripts/world/sucateia.gd"));own(world);var packed := PackedScene.new();var error := packed.pack(world)
	if error==OK:error=ResourceSaver.save(packed,"res://maps/sucateia/sucateia.tscn")
	print("FORJAS final ports aligned saved=",error," actual asset coordinates; reducer, cooling vapor and localized heat")
	world.queue_free();world=null;detail=null;yards=null;district=null;packed=null;await process_frame;await process_frame;quit(error)
