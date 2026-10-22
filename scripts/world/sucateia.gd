extends Node2D
var capture_frames := 0
var capture_mode := ""
var river_oasis: RefCounted
func _ready() -> void:
	load("res://scripts/world/fitted_stairs.gd").new().install(self)
	load("res://scripts/world/connected_utilities.gd").new().install(self)
	load("res://scripts/world/port_approach_finish.gd").new().install(self)
	load("res://scripts/world/coroa_district.gd").new().install(self)
	load("res://scripts/world/market_expansion.gd").new().install(self)
	load("res://scripts/world/alto_west_cais.gd").new().install(self)
	river_oasis = load("res://scripts/world/khemet_river_oasis.gd").new()
	river_oasis.install(self)
	var travel := get_node_or_null("/root/RegionTravel")
	# Viagem intermapas legada desativada (cenário unificado)
	# if travel: travel.setup(self,"centre")
	var layers := get_node_or_null("/root/LayerTravel")
	if layers:layers.setup(self,"surface")
	for arg in OS.get_cmdline_user_args():
		if arg.begins_with("--capture="): capture_mode = arg.trim_prefix("--capture=")
	if capture_mode != "":
		var cam: Camera2D = $Structures/Player/Camera
		cam.position_smoothing_enabled = false
		if capture_mode == "port_approach":
			$Structures/Player.position=Vector2(2240,1370)
			cam.zoom=Vector2(.95,.95)
		elif capture_mode == "utility_core":
			$Structures/Player.position = Vector2(1400,1050)
			cam.zoom = Vector2(.95,.95)
		elif capture_mode == "stairs_coast":
			$Structures/Player.position = Vector2(1512,1505)
			cam.zoom = Vector2(.95,.95)
		elif capture_mode == "channel_test":
			$Structures/Player.position = Vector2(1730,1500)
			cam.zoom = Vector2(.85,.85)
		elif capture_mode == "west_expansion_test":
			$Structures/Player.position = Vector2(400, 850)
			cam.zoom = Vector2(0.85, 0.85)
		elif capture_mode == "khemet_nexus":
			get_viewport().size = Vector2i(1920, 1080)
			$Structures/Player.position = Vector2(-11800, -1480)
			cam.limit_left = -20000; cam.limit_right = 9000; cam.limit_top = -4500; cam.limit_bottom = 4500
		elif capture_mode == "khemet_temple":
			$Structures/Player.position = Vector2(-13600, -1450)
			cam.zoom = Vector2(0.85, 0.85)
			cam.limit_left = -20000; cam.limit_right = 9000; cam.limit_top = -4500; cam.limit_bottom = 4500
		elif capture_mode == "khemet_pyramid":
			$Structures/Player.position = Vector2(-16300, -1850)
			cam.zoom = Vector2(0.85, 0.85)
			cam.limit_left = -20000; cam.limit_right = 9000; cam.limit_top = -4500; cam.limit_bottom = 4500
		elif capture_mode == "mapa_completo":
			get_viewport().size = Vector2i(3840, 1600)
			$Structures/Player.position = Vector2(-7500, -350)
			cam.zoom = Vector2(0.165, 0.165)
			cam.limit_left = -22000; cam.limit_right = 9000; cam.limit_top = -6000; cam.limit_bottom = 6000
		elif capture_mode == "khemet_avenue_close":
			get_viewport().size = Vector2i(2560, 1440)
			$Structures/Player.position = Vector2(-13300, -1500)
			cam.zoom = Vector2(0.62, 0.62)
			cam.limit_left = -22000; cam.limit_right = 9000; cam.limit_top = -6000; cam.limit_bottom = 6000
		elif capture_mode == "khemet_costa_recifes":
			get_viewport().size = Vector2i(1920, 1080)
			$Structures/Player.position = Vector2(-11500, -820)
			cam.zoom = Vector2(0.85, 0.85)
			cam.limit_left = -22000; cam.limit_right = 9000; cam.limit_top = -6000; cam.limit_bottom = 6000
		elif capture_mode == "khemet_oasis":
			get_viewport().size = Vector2i(1920, 1080)
			$Structures/Player.position = Vector2(-8020, -1900)
			cam.zoom = Vector2(0.42, 0.42)
			cam.limit_left = -22000; cam.limit_right = 9000; cam.limit_top = -6000; cam.limit_bottom = 6000
		elif capture_mode == "khemet_rio_completo":
			get_viewport().size = Vector2i(1920, 1080)
			$Structures/Player.position = Vector2(-8020, -2200)
			cam.zoom = Vector2(0.26, 0.26)
			cam.limit_left = -22000; cam.limit_right = 9000; cam.limit_top = -6000; cam.limit_bottom = 6000
		elif capture_mode == "khemet_litoral_templo":
			get_viewport().size = Vector2i(1920, 1080)
			$Structures/Player.position = Vector2(-14600, -1080)
			cam.zoom = Vector2(0.85, 0.85)
			cam.limit_left = -22000; cam.limit_right = 9000; cam.limit_top = -6000; cam.limit_bottom = 6000
		elif capture_mode == "khemet_dunas_relief":
			get_viewport().size = Vector2i(2560, 1440)
			$Structures/Player.position = Vector2(-12800, -1800)
			cam.zoom = Vector2(0.42, 0.42)
			cam.limit_left = -22000; cam.limit_right = 9000; cam.limit_top = -6000; cam.limit_bottom = 6000
		elif capture_mode == "khemet_full":
			get_viewport().size = Vector2i(2560, 1440)
			$Structures/Player.position = Vector2(-14000, -1700)
			cam.zoom = Vector2(0.30, 0.30)
			cam.limit_left = -22000; cam.limit_right = 9000; cam.limit_top = -6000; cam.limit_bottom = 6000
		elif capture_mode == "chapada_full":
			get_viewport().size = Vector2i(2560, 1440)
			$Structures/Player.position = Vector2(-5500, -850)
			cam.zoom = Vector2(0.32, 0.32)
			cam.limit_left = -22000; cam.limit_right = 9000; cam.limit_top = -6000; cam.limit_bottom = 6000
		elif capture_mode == "sucateia_full":
			get_viewport().size = Vector2i(2560, 1440)
			$Structures/Player.position = Vector2(1500, 300)
			cam.zoom = Vector2(0.35, 0.35)
			cam.limit_left = -6000; cam.limit_right = 9000; cam.limit_top = -6000; cam.limit_bottom = 6000
		elif capture_mode.begins_with("docas_"):
			var positions := {"docas_full":Vector2(2735,1910),"docas_district":Vector2(2700,1640),"docas_loading":Vector2(2735,1910),"docas_sorting":Vector2(2500,1575),"docas_repair":Vector2(3030,1640),"docas_urban":Vector2(2240,1370),"docas_technical":Vector2(3280,458)}
			var zooms := {"docas_full":.15,"docas_district":.5,"docas_loading":.95,"docas_sorting":.95,"docas_repair":.95,"docas_urban":.85,"docas_technical":.75}
			$Structures/Player.position=positions.get(capture_mode,Vector2(2700,1640));cam.zoom=Vector2.ONE*zooms.get(capture_mode,.5);cam.limit_left=-4500;cam.limit_right=7800;cam.limit_top=-3400;cam.limit_bottom=4000
			if capture_mode=="docas_full":cam.offset=Vector2(-600,-1260)
			if capture_mode=="docas_district":cam.offset=Vector2(20,-100)
		elif capture_mode.begins_with("cabos_"):
			var positions := {"cabos_full":Vector2(744,-716),"cabos_district":Vector2(744,-716),"cabos_market":Vector2(744,-716),"cabos_alto":Vector2(-400,-992),"cabos_forjas":Vector2(1900,-104),"cabos_junction":Vector2(744,-522.2),"cabos_underpass":Vector2(744,-504)}
			var zooms := {"cabos_full":.16,"cabos_district":.42,"cabos_market":.85,"cabos_alto":.85,"cabos_forjas":.85,"cabos_junction":.9,"cabos_underpass":.9}
			$Structures/Player.position=positions.get(capture_mode,Vector2(744,-716))
			if capture_mode!="cabos_underpass":
				$Structures/Player.navigation_layer="cabos";$Structures/Player.collision_mask=4;$Structures/Player.z_index=8
			cam.zoom=Vector2.ONE*zooms.get(capture_mode,.42);cam.limit_left=-4500;cam.limit_right=7800;cam.limit_top=-3400;cam.limit_bottom=3300
			if capture_mode=="cabos_full":cam.offset=Vector2(1400,760)
			if capture_mode=="cabos_district":cam.offset=Vector2(0,60)
		elif capture_mode.begins_with("fundo_surface_"):
			var id: String=capture_mode.trim_prefix("fundo_surface_")
			$Structures/Player.position=get_node("LayerArrivals/"+id).position;cam.zoom=Vector2(.88,.88)
		elif capture_mode == "amarras_full":
			$Structures/Player.position=Vector2(2250,150);cam.zoom=Vector2(.15,.15);cam.limit_left=-4500;cam.limit_right=7800;cam.limit_top=-3400;cam.limit_bottom=3300
		elif capture_mode == "amarras_district":
			$Structures/Player.position=Vector2(4640,360);cam.zoom=Vector2(.43,.43)
		elif capture_mode == "amarras_transition":
			$Structures/Player.position=Vector2(4070,20);cam.zoom=Vector2(.63,.63)
		elif capture_mode == "ponte_correntes":
			$Structures/Player.position = Vector2(3280, 500)
			cam.zoom = Vector2(0.95, 0.95)
		elif capture_mode == "escada_costa":
			$Structures/Player.position = Vector2(2270, 1720)
			cam.zoom = Vector2(0.85, 0.85)
		elif capture_mode == "amarras_transfer":
			$Structures/Player.position=Vector2(4700,380);cam.zoom=Vector2(.86,.86)
		elif capture_mode == "amarras_anchor":
			$Structures/Player.position=Vector2(4400,180);cam.zoom=Vector2(.86,.86)
		elif capture_mode == "amarras_maintenance":
			$Structures/Player.position=Vector2(4990,660);cam.zoom=Vector2(.86,.86)
		elif capture_mode == "forjas_market_landmark":
			$Structures/Player.position=Vector2(1600,-275)
			cam.zoom=Vector2(.88,.88)
		elif capture_mode == "forjas_cargo":
			$Structures/Player.position=Vector2(2540,-75)
			cam.zoom=Vector2(.9,.9)
		elif capture_mode == "forjas_boilers":
			$Structures/Player.position=Vector2(2860,-1280)
			cam.zoom=Vector2(.88,.88)
		elif capture_mode == "forjas_full":
			$Structures/Player.position=Vector2(1280,110)
			cam.zoom=Vector2(.19,.19);cam.limit_left=-4000;cam.limit_right=6500;cam.limit_top=-3200;cam.limit_bottom=2800
		elif capture_mode == "forjas_district":
			$Structures/Player.position=Vector2(2690,-720)
			cam.zoom=Vector2(.38,.38)
		elif capture_mode == "forjas_market_central_landmark":
			$Structures/Player.position=Vector2(1416,-756)
			cam.zoom=Vector2(.36,.36)
		elif capture_mode == "forjas_frontier":
			$Structures/Player.position=Vector2(1780,-180)
			cam.zoom=Vector2(.78,.78)
		elif capture_mode == "coroa_study":
			$Structures/Player.position = Vector2(1530, 340)
			cam.zoom = Vector2(0.70, 0.70)
		elif capture_mode == "forjas_foundry":
			$Structures/Player.position=Vector2(2830,-860)
			cam.zoom=Vector2(.85,.85)
		elif capture_mode == "forjas_recycling":
			$Structures/Player.position=Vector2(3310,-650)
			cam.zoom=Vector2(.85,.85)
		elif capture_mode == "forjas_drain":
			$Structures/Player.position=Vector2(2900,100)
			cam.zoom=Vector2(.75,.75)
		elif capture_mode == "lower_coast":
			$Structures/Player.position=Vector2(1220,1360)
			cam.zoom=Vector2(.49,.49);cam.limit_left=-800;cam.limit_right=3300;cam.limit_bottom=2600
		elif capture_mode == "lower_detail":
			$Structures/Player.position=Vector2(1050,1630)
			cam.zoom=Vector2(.85,.85);cam.limit_bottom=2600
		elif capture_mode == "alto_full":
			$Structures/Player.position=Vector2(370,170)
			cam.zoom=Vector2(.19,.19);cam.limit_left=-4000;cam.limit_right=4500;cam.limit_top=-3200;cam.limit_bottom=2600
		elif capture_mode == "alto_frontier":
			$Structures/Player.position=Vector2(360,-520)
			cam.zoom=Vector2(.85,.85)
		elif capture_mode == "alto_northwest":
			$Structures/Player.position=Vector2(430,-1090)
			cam.zoom=Vector2(.72,.72)
		elif capture_mode == "alto_court":
			$Structures/Player.position=Vector2(-650,-895)
			cam.zoom=Vector2(.78,.78)
		elif capture_mode == "market_restos":
			$Structures/Player.position = Vector2(1340, -30)
			cam.zoom = Vector2(0.68, 0.68)
		elif capture_mode == "market_expansion":
			$Structures/Player.position=Vector2(1080,-355)
			cam.zoom=Vector2(.54,.54)
		elif capture_mode == "market_plaza":
			$Structures/Player.position=Vector2(1120,-330)
			cam.zoom=Vector2(.85,.85)
		elif capture_mode == "market_full":
			$Structures/Player.position=Vector2(1200,140)
			cam.zoom=Vector2(.23,.23)
			cam.limit_left=-2000;cam.limit_right=4500
		elif capture_mode == "overview":
			$Structures/Player.position = Vector2(1200,970)
			cam.zoom = Vector2(0.47,0.47)
		elif capture_mode == "transition":
			$Structures/Player.position = Vector2(1680,1090)
			cam.zoom = Vector2(.88,.88)
		elif capture_mode == "alto_cais":
			$Structures/Player.position = Vector2(40, 220)
			cam.zoom = Vector2(0.85, 0.85)
		elif capture_mode == "alto_west_cais":
			$Structures/Player.position = Vector2(-880, 50)
			cam.zoom = Vector2(0.75, 0.75)
			cam.limit_left = -3800; cam.limit_right = 3200; cam.limit_top = -2000; cam.limit_bottom = 2000
		elif capture_mode == "litoral_full":
			$Structures/Player.position = Vector2(-6500, -700)
			cam.zoom = Vector2(0.075, 0.075)
			cam.limit_left = -14500; cam.limit_right = 1000; cam.limit_top = -2800; cam.limit_bottom = 2800
		elif capture_mode == "litoral_user_spot":
			$Structures/Player.position = Vector2(-1600, -90)
			cam.zoom = Vector2(0.95, 0.95)
			cam.limit_left = -14500; cam.limit_right = 1000
		elif capture_mode == "wave_anim":
			$Structures/Player.position = Vector2(-1600, -45)
			cam.zoom = Vector2(1.10, 1.10)
			cam.limit_left = -14500; cam.limit_right = 1000
		elif capture_mode == "litoral_transicao":
			$Structures/Player.position = Vector2(-1500, -100)
			cam.zoom = Vector2(0.65, 0.65)
			cam.limit_left = -14500; cam.limit_right = 1000
		elif capture_mode == "litoral_arenito":
			$Structures/Player.position = Vector2(-4800, -520)
			cam.zoom = Vector2(0.65, 0.65)
			cam.limit_left = -14500; cam.limit_right = 1000
		elif capture_mode == "litoral_praia_aberta":
			$Structures/Player.position = Vector2(-8800, -820)
			cam.zoom = Vector2(0.65, 0.65)
			cam.limit_left = -14500; cam.limit_right = 1000
		elif capture_mode == "litoral_cabo_extremo":
			$Structures/Player.position = Vector2(-12200, -1020)
			cam.zoom = Vector2(0.65, 0.65)
			cam.limit_left = -14500; cam.limit_right = 1000
		elif capture_mode == "kemet_deserto_full":
			$Structures/Player.position = Vector2(-8000, -2200)
			cam.zoom = Vector2(0.065, 0.065)
			cam.limit_left = -16500; cam.limit_right = 2000; cam.limit_top = -4800; cam.limit_bottom = 3500
		elif capture_mode == "kemet_canyon_pass":
			$Structures/Player.position = Vector2(-2800, -850)
			cam.zoom = Vector2(0.65, 0.65)
			cam.limit_left = -16500; cam.limit_right = 2000; cam.limit_top = -4800
		elif capture_mode == "kemet_dunas_centrais":
			$Structures/Player.position = Vector2(-5800, -1450)
			cam.zoom = Vector2(0.65, 0.65)
			cam.limit_left = -16500; cam.limit_right = 2000; cam.limit_top = -4800
		elif capture_mode == "kemet_mesa_reis":
			$Structures/Player.position = Vector2(-7900, -2250)
			cam.zoom = Vector2(0.60, 0.60)
			cam.limit_left = -16500; cam.limit_right = 2000; cam.limit_top = -4800
		elif capture_mode == "kemet_plato_norte":
			$Structures/Player.position = Vector2(-8500, -3700)
			cam.zoom = Vector2(0.60, 0.60)
			cam.limit_left = -16500; cam.limit_right = 2000; cam.limit_top = -4800
		elif capture_mode == "maintenance_reactor":
			$Structures/Player.position = Vector2(1180, 1550)
			cam.zoom = Vector2(0.85, 0.85)
		elif capture_mode == "coast":
			$Structures/Player.position = Vector2(1600,1610)
			cam.offset = Vector2(265,60)
			cam.zoom = Vector2(.85,.85)
		elif capture_mode == "cabos_bridge_cleaned":
			$Structures/Player.position = Vector2(2067, 1087)
			cam.zoom = Vector2(0.85, 0.85)
		elif capture_mode == "lixao_full":
			$Structures/Player.position = Vector2(0, -2100)
			cam.zoom = Vector2(0.24, 0.24)
			cam.limit_left = -3200; cam.limit_right = 3200; cam.limit_top = -3600; cam.limit_bottom = 1000
		elif capture_mode == "lixao_montanha":
			$Structures/Player.position = Vector2(-280, -2350)
			cam.zoom = Vector2(0.55, 0.55)
		elif capture_mode == "lixao_dunas":
			$Structures/Player.position = Vector2(650, -2150)
			cam.zoom = Vector2(0.55, 0.55)
		elif capture_mode == "lixao_guindaste":
			$Structures/Player.position = Vector2(-750, -2000)
			cam.zoom = Vector2(0.55, 0.55)
		elif capture_mode == "lixao_colosso":
			$Structures/Player.position = Vector2(850, -1700)
			cam.zoom = Vector2(0.55, 0.55)
		else:
			$Structures/Player.position = Vector2(1240,1040)
			cam.zoom = Vector2(0.9,0.9)
		cam.reset_smoothing()
		if capture_mode != "": $MapInfo/Panel.visible = false
func _process(_delta: float) -> void:
	if capture_mode == "": return
	if capture_mode != "" and has_node("RegionPortals"):
		for portal in $RegionPortals.get_children():
			var p := portal.get_node_or_null("Prompt")
			if p: p.visible = false
			var s := portal.get_node_or_null("Sign")
			if s: s.visible = false
	capture_frames += 1
	if capture_frames == 80:
		await RenderingServer.frame_post_draw
		var path := "res://maps/sucateia/preview_" + capture_mode + ".png"
		var err := get_viewport().get_texture().get_image().save_png(path)
		print("CAPTURE ",path," ",err," draw_calls=",Performance.get_monitor(Performance.RENDER_TOTAL_DRAW_CALLS_IN_FRAME)," nodes=",Performance.get_monitor(Performance.OBJECT_NODE_COUNT))
		get_tree().quit(err)
func is_walkable(point: Vector2) -> bool:
	var cabos: Node2D=get_node_or_null("CabosDistrict")
	if cabos and $Structures/Player.navigation_layer=="cabos":return cabos.is_walkable(point)
	return is_surface_walkable(point)
func is_surface_walkable(point: Vector2) -> bool:
	var lixao: Node2D = get_node_or_null("GrandeLixaoDistrict")
	if lixao and lixao.has_meta("land_polygon"):
		if Geometry2D.is_point_in_polygon(point, lixao.get_meta("land_polygon")): return true
	var river: Node = get_node_or_null("KhemetRiverOasis")
	if river and river_oasis:
		var r: int = river_oasis.is_blocked(river, point)
		if r == 1: return true
		if r == -1: return false
	var cais: Node2D = get_node_or_null("AltoLixoCais")
	if cais and cais.has_meta("land_polygon"):
		if Geometry2D.is_point_in_polygon(point, cais.get_meta("land_polygon")): return true
	var docks: Node2D=get_node_or_null("DocasDistrict")
	if docks and docks.is_walkable(point):return true
	var amarras: Node2D=get_node_or_null("PassagemAmarrasDistrict")
	if amarras:
		for polygon in amarras.get_meta("walk_polygons",[]):
			if Geometry2D.is_point_in_polygon(point,polygon):return true
		if Geometry2D.is_point_in_polygon(point,amarras.get_meta("land_polygon")):
			for polygon in amarras.get_meta("water_polygons",[]):
				if Geometry2D.is_point_in_polygon(point,polygon):return false
			return true
		if point.x>=3800 and point.y>-500 and point.y<1300:return false
	var forjas: Node2D=get_node_or_null("ForjasRasasDistrict")
	if forjas:
		for polygon in forjas.get_meta("water_polygons",[]):
			if Geometry2D.is_point_in_polygon(point,polygon):return false
	if has_node("WestCoastalBarrier"):
		for child in get_node("WestCoastalBarrier").get_children():
			if child is CollisionPolygon2D and Geometry2D.is_point_in_polygon(point, child.polygon):
				return false
	if has_node("EastCoastalBarrier"):
		for child in get_node("EastCoastalBarrier").get_children():
			if child is CollisionPolygon2D and Geometry2D.is_point_in_polygon(point, child.polygon):
				return false
	if has_node("LowerCoastReworked") and point.y>=1170:
		return Geometry2D.is_point_in_polygon(point,get_node("LowerCoastReworked").get_meta("land_polygon"))
	if point.y>=380 or not has_node("MarketDistrict"):return true
	for floor in [$Ground/TerraceFloor,$MarketDistrict/MarketFloor]:
		if floor.get_cell_source_id(floor.local_to_map(floor.to_local(point)))!=-1:return true
	var alto: TileMapLayer=get_node_or_null("AltoLixoDistrict/AltoFloor")
	if alto and alto.get_cell_source_id(alto.local_to_map(alto.to_local(point)))!=-1:return true
	if forjas:
		var floor: TileMapLayer=forjas.get_node("ForjasFloor")
		if floor.get_cell_source_id(floor.local_to_map(floor.to_local(point)))!=-1:return true
	return false
