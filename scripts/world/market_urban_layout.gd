extends RefCounted
func install(m) -> void:
	var subareas: Node2D=m.group("Subareas",m.district)
	for entry in [["EntradaDoMercado",Vector2(1140,240)],["RuaDosCatadores",Vector2(1200,-48)],["PracaDasTrocas",Vector2(1128,-252)],["VielasComerciais",Vector2(744,-504)],["CargaEEstoque",Vector2(1416,-756)],["SaidaParaAltoLixo",Vector2(456,-504)],["SaidaParaForjasRasas",Vector2(1668,132)],["ConexaoComFundoFerro",Vector2(1296,1572)]]:
		var marker := Marker2D.new();marker.name=entry[0];marker.position=entry[1];subareas.add_child(marker)
	var entrance: Node2D=m.group("EntradaDoMercado",m.commerce)
	var plaza: Node2D=m.group("PracaDasTrocas",m.commerce)
	var west: Node2D=m.group("BecoDasFerragens",m.commerce)
	var east: Node2D=m.group("VielaDosTecidos",m.commerce)
	var yard: Node2D=m.group("CargaEEstoque",m.commerce)
	var workshop: Node2D=m.group("OficinaDeAjustes",m.commerce)
	# Central exchange pavilion anchors a small trading plaza; the through street passes to its east.
	m.stall("PavilhaoDeTrocas",Vector2(1050,-354),"reconstruction/exchange_pavilion.png",Vector2(352,239),plaza)
	m.stall("TecidosDaEntrada",Vector2(950,265),"reconstruction/cloth_stall.png",Vector2(176,145),entrance)
	m.stall("PecasDaEntrada",Vector2(1380,250),"generated/props/market_stall.png",Vector2(166,120),entrance)
	m.stall("BancaDosCatadores",Vector2(948,101),"generated/props/market_stall.png",Vector2(165,119),entrance)
	m.stall("ReparoDeInstrumentos",Vector2(1445,95),"generated/props/market_stall.png",Vector2(169,123),entrance)
	m.stall("CarroDasBobinas",Vector2(1534,72),"reconstruction/market_salvage_cart.png",Vector2(147,155),entrance)
	# Counters face routes and share backs with shops; no isolated booths in the plaza.
	m.stall("BalcaoDeFerragens",Vector2(830,-108),"generated/props/market_stall.png",Vector2(168,121),west)
	m.stall("PequenasPecas",Vector2(805,-231),"generated/props/market_stall.png",Vector2(155,112),west)
	m.stall("RodasEReparos",Vector2(665,-414),"reconstruction/market_salvage_cart.png",Vector2(151,159),west)
	m.stall("AtacadoCoberto",Vector2(690,-360),"reconstruction/wholesale_arcade.png",Vector2(338,285),workshop)
	m.stall("CordasELonas",Vector2(1410,-155),"reconstruction/cloth_stall.png",Vector2(167,137),east)
	m.stall("ValvulasDeTroca",Vector2(1458,-318),"generated/props/market_stall.png",Vector2(159,115),east)
	m.stall("CouroDeRemendo",Vector2(1416,-506),"reconstruction/cloth_stall.png",Vector2(171,142),east)
	m.stall("MesaDasCordas",Vector2(1344,-635),"reconstruction/cloth_stall.png",Vector2(158,132),east)
	m.stall("LoteDeBronze",Vector2(835,-651),"generated/props/market_stall.png",Vector2(177,128),west)
	m.stall("SelecaoDeMetais",Vector2(898,-806),"generated/props/market_stall.png",Vector2(162,117),west)
	m.stall("LonasReaproveitadas",Vector2(1440,-870),"reconstruction/cloth_stall.png",Vector2(168,137),yard)
	m.stall("CarroDeColeta",Vector2(1550,-709),"reconstruction/market_salvage_cart.png",Vector2(155,163),yard)
	# Staggered commercial backs define the urban edges, interrupted by deliberate alleys.
	for entry in [[Vector2(565,277),false],[Vector2(569,-41),true],[Vector2(535,-318),false],[Vector2(613,-621),false],[Vector2(729,-941),true],[Vector2(1508,308),false],[Vector2(1630,-63),true],[Vector2(1658,-362),false],[Vector2(1538,-613),true],[Vector2(1456,-1030),false]]:
		m.shop(entry[0],entry[1])
	# Stock is grouped at the loading court and the repair shop, leaving a clear maneuvering pocket.
	for point in [Vector2(1480,-788),Vector2(1518,-804),Vector2(1539,-845),Vector2(1471,-820),Vector2(578,-322),Vector2(591,-354),Vector2(819,250),Vector2(828,224)]:
		m.shadow(point,66);m.art("infrastructure/scrap.png",point,Vector2(87,46),m.commerce,.1);m.solid(point,Vector2(42,23),m.commerce)
	for point in [Vector2(1000,200),Vector2(1326,235),Vector2(1260,-69),Vector2(1213,-260),Vector2(1230,-459),Vector2(1060,-628),Vector2(1175,-919),Vector2(1290,-786)]:m.lamp(point,m.commerce)
	m.lamp(Vector2(1050,-326),m.commerce,true)
	var street := PackedVector2Array([Vector2(1140,450),Vector2(1140,240),Vector2(1200,40),Vector2(1248,-144),Vector2(1296,-336),Vector2(1248,-492),Vector2(1130,-651),Vector2(1128,-885),Vector2(1140,-1420)])
	m.route(street,130,.48)
	m.route(PackedVector2Array([Vector2(1248,-144),Vector2(1130,-205),Vector2(937,-192),Vector2(898,-328),Vector2(935,-480),Vector2(1130,-514),Vector2(1248,-492)]),69,.29)
	var alleys: Node2D=m.group("UrbanRoutes",m.district)
	var paths := {"BecoDasFerragens":PackedVector2Array([Vector2(937,-192),Vector2(868,-252),Vector2(853,-474),Vector2(744,-504),Vector2(795,-590),Vector2(970,-593),Vector2(1130,-651)]),"VielaDosTecidos":PackedVector2Array([Vector2(1296,-336),Vector2(1330,-402),Vector2(1520,-402),Vector2(1510,-470),Vector2(1500,-550),Vector2(1412,-585),Vector2(1416,-756),Vector2(1290,-786)]),"PassagemDosLotes":PackedVector2Array([Vector2(1130,-651),Vector2(1000,-690),Vector2(1032,-944),Vector2(1140,-1104)])}
	for label in paths:
		m.route(paths[label],59,.31)
		var marker := Marker2D.new();marker.name=label;marker.set_meta("points",paths[label]);alleys.add_child(marker)
	# Existing streets continue into neighboring districts; repair materials change gradually.
	m.route(PackedVector2Array([Vector2(1140,240),Vector2(1440,175),Vector2(1668,132),Vector2(1720,500),Vector2(1680,900)]),84,.26)
	m.route(PackedVector2Array([Vector2(1140,450),Vector2(1130,740),Vector2(1120,1060),Vector2(1280,1320),Vector2(1296,1572)]),77,.22)
	for point in [Vector2(1615,145),Vector2(1660,230),Vector2(1710,398)]:m.art("generated/props/pipe.png",point,Vector2(111,27),m.detail,.52)
	for point in [Vector2(1300,1380),Vector2(1272,1510)]:m.art("terrain/oil_hatch.png",point,Vector2(69,57),m.detail,.05)
	for entry in [[Vector2(754,-552),Vector2(118,76)],[Vector2(1530,-812),Vector2(124,82)]]:
		m.shadow(entry[0],120);m.art("infrastructure/walkway.png",entry[0],entry[1],m.detail,-.06);m.art("infrastructure/stairs.png",entry[0]+Vector2(0,41),Vector2(66,44),m.detail)
	for points in [PackedVector2Array([Vector2(565,277),Vector2(1000,200),Vector2(1508,308),Vector2(1730,400)]),PackedVector2Array([Vector2(569,-41),Vector2(1050,-326),Vector2(1658,-362)]),PackedVector2Array([Vector2(729,-941),Vector2(1128,-885),Vector2(1456,-1030)]),PackedVector2Array([Vector2(1128,-885),Vector2(1140,-1520)])]:
		var cable := Line2D.new();cable.points=points;cable.width=2;cable.default_color=Color("635036");cable.z_index=8;m.district.add_child(cable)
	# Receding roofs continue the city beyond the playable cut; no rectangular enclosing wall.
	for entry in [[Vector2(700,-1270),false],[Vector2(1380,-1430),true],[Vector2(340,-790),true],[Vector2(1850,-820),false]]:
		var point: Vector2=entry[0]
		m.art("generated/structures/house_stack.png" if entry[1] else "generated/structures/house.png",point,Vector2(203,236),m.detail).modulate=Color(.52,.54,.46,.78)
	m.district.set_meta("urban_structure","Rua dos Catadores, central exchange plaza, three alleys, loading court and commercial street walls")
	m.district.set_meta("alto_lixo_direction","west/northwest; lateral connection through Beco das Ferragens")
	m.district.set_meta("northeast_reservation","Forjas Rasas; no Alto-Lixo construction in this area")
