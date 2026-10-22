extends RefCounted
var world: Node2D
var c
var outline: PackedVector2Array
func erase(node: Node) -> void:node.get_parent().remove_child(node);node.free()
func update_water(label: String, points: PackedVector2Array) -> void:
	var water: Polygon2D=world.get_node(label+"Waterline");water.polygon=points;water.material=c.water_material
	var body: StaticBody2D=world.get_node(label+"CoastalBarrier")
	for child in body.get_children():
		if child is CollisionPolygon2D:child.polygon=points
func install(target: Node2D) -> void:
	world=target
	# Keep the entire upper coast unchanged; only lower control points are reworked.
	var west := PackedVector2Array([Vector2(148,335),Vector2(148,520),Vector2(130,610),Vector2(143,790),Vector2(159,880),Vector2(145,1050),Vector2(120,1160),Vector2(200,1250),Vector2(260,1350),Vector2(290,1415),Vector2(360,1485),Vector2(395,1535)])
	var east := PackedVector2Array([Vector2(2248,335),Vector2(2248,518),Vector2(2270,606),Vector2(2253,782),Vector2(2240,880),Vector2(2260,1030),Vector2(2278,1170),Vector2(2285,1230),Vector2(2285,1400),Vector2(2160,1400),Vector2(2160,1480),Vector2(2255,1510),Vector2(2255,1660)])
	var shore := PackedVector2Array([Vector2(395,1535),Vector2(575,1556),Vector2(575,1650),Vector2(710,1730),Vector2(800,1730),Vector2(820,1620),Vector2(820,1505),Vector2(925,1505),Vector2(925,1610),Vector2(1000,1610),Vector2(1000,1750),Vector2(1010,1750),Vector2(1010,1840),Vector2(1130,1845),Vector2(1130,1750),Vector2(1150,1750),Vector2(1150,1625),Vector2(1310,1625),Vector2(1310,1560),Vector2(1445,1560),Vector2(1445,1675),Vector2(1700,1675),Vector2(1770,1595),Vector2(1770,1515),Vector2(1955,1515),Vector2(2000,1530),Vector2(2140,1530),Vector2(2150,1660),Vector2(2180,1660),Vector2(2180,1725),Vector2(2250,1730),Vector2(2250,1660),Vector2(2255,1660)])
	# The pump footprint leaves only 38 px on its east side; reserve a 68 px maintenance passage.
	for i in range(shore.size()):
		if shore[i].x==1150 and shore[i].y>=1625:shore[i].x=1180
		# Preserve the existing Fundo-Ferro approach, including player radius and navigation grid margin.
		if shore[i].x==1310:shore[i].x=1345
	outline=west.duplicate()
	for i in range(1,shore.size()):outline.append(shore[i])
	for i in range(east.size()-2,-1,-1):outline.append(east[i])
	# Remove the obsolete lower coping, service landing art and dangling decorations.
	var old_quay: Node2D=world.get_node("GoblinIndustrialQuay")
	for child in old_quay.get_children():
		if child is Node2D and child.position.y>=1170:erase(child)
		elif child is Line2D and child.points.size()>0 and child.points[0].y>=1170:erase(child)
	for parent_name in ["FinishedInfrastructure","TerrainIntegration","GroundDetails"]:
		var parent: Node=world.get_node_or_null(parent_name)
		if not parent:continue
		for sprite in parent.find_children("*","Sprite2D",true,false):
			var at: Vector2=sprite.global_position
			if at.y>=1170 and not Geometry2D.is_point_in_polygon(at,outline):erase(sprite)
	c=load("res://scripts/world/coastal_builder.gd").new();c.world=world
	c.coast=Node2D.new();c.coast.name="LowerCoastReworked";c.coast.z_index=-12;world.add_child(c.coast)
	c.water_material=ShaderMaterial.new();c.water_material.shader=load("res://assets/reconstruction/lower_sea.gdshader");c.water_material.set_shader_parameter("grime",load("res://assets/infrastructure/channel.png"))
	var edges: Array[Vector4]=[]
	for line in [west,shore,east]:
		for i in range(line.size()-1):edges.append(Vector4(line[i].x,line[i].y,line[i+1].x,line[i+1].y))
	c.water_material.set_shader_parameter("edge_count",edges.size())
	while edges.size()<64:edges.append(Vector4.ZERO)
	c.water_material.set_shader_parameter("coast_edges",edges)
	var west_water := west.duplicate();west_water.append(Vector2(-900,2600));west_water.append(Vector2(-900,335));update_water("West",west_water)
	var east_water := east.duplicate();east_water.append(Vector2(3300,2600));east_water.append(Vector2(3300,335));update_water("East",east_water)
	var south_water := shore.duplicate();south_water.append(Vector2(3000,2600));south_water.append(Vector2(-800,2600));update_water("South",south_water)
	var floor: TileMapLayer=world.get_node("Ground/TerraceFloor")
	for cell in floor.get_used_cells():
		var at := floor.map_to_local(cell)
		if at.y>=1170 and not Geometry2D.is_point_in_polygon(at,outline):floor.erase_cell(cell)
	for y in range(24,39):
		for x in range(3,48):
			var cell := Vector2i(x,y);var at := Vector2(x*48+24,y*48+24)
			var timber: bool=(at.x>1005 and at.x<1135 and at.y>1750) or (at.x>2170 and at.y>1660)
			if Geometry2D.is_point_in_polygon(at,outline) and not timber and floor.get_cell_source_id(cell)==-1:floor.set_cell(cell,0,Vector2i(posmod(x,16),posmod(y,16)))
	# Texture every new waterfront segment, with different stone/metal repairs and contact stains.
	for line in [west.slice(6),shore,east.slice(6)]:
		for i in range(line.size()-1):
			var delta: Vector2=line[i+1]-line[i];var count := maxi(1,ceili(delta.length()/162))
			# The industrial runoff remains visibly open where it meets the harbor.
			if line[i].distance_to(Vector2(1770,1515))<1:continue
			for j in range(count):
				var at: Vector2=line[i].lerp(line[i+1],(j+.5)/count)
				c.stain(at+Vector2(4,32),Vector2(delta.length()/count+33,91),Color(0,0,0,.58))
				var wall: Sprite2D=c.sprite("infrastructure/coastal_wall.png",at,Vector2(delta.length()/count+12,84+(i%3)*8),delta.angle())
				wall.modulate=Color(.88,.92,.79,1) if i%3==0 else Color(1,1,.94,1)
				c.stain(at+Vector2(0,37),Vector2(90,34),Color(.13,.23,.13,.30))
	# Decks are continuations of coping and stairs; no isolated platform placed in open water.
	for entry in [[Vector2(715,1674),Vector2(158,124),-.06],[Vector2(1065,1766),Vector2(123,124),.03],[Vector2(1068,1831),Vector2(128,81),.02],[Vector2(2217,1668),Vector2(110,108),-.05],[Vector2(2210,1721),Vector2(104,82),.04]]:
		c.stain(entry[0]+Vector2(7,20),entry[1]*1.15,Color(0,0,0,.62));c.sprite("infrastructure/walkway.png",entry[0],entry[1],entry[2])
		for side in [-1,1]:c.sprite("infrastructure/retaining_edge.png",entry[0]+Vector2(side*entry[1].x*.35,entry[1].y*.31),Vector2(44,69),PI/2)
	for entry in [[Vector2(670,1630),-.18],[Vector2(1070,1738),0.0],[Vector2(2206,1640),.08]]:c.sprite("infrastructure/stairs.png",entry[0],Vector2(73,75),entry[1])
	for at in [Vector2(442,1480),Vector2(774,1580),Vector2(970,1570),Vector2(1280,1550),Vector2(1480,1578),Vector2(1650,1620),Vector2(2150,1510)]:
		c.sprite("terrain/metal_repair.png",at,Vector2(115,78),.09).modulate=Color(.84,.81,.64,.83)
		c.sprite("terrain/market_dirt.png",at-Vector2(12,26),Vector2(150,79),-.07).modulate=Color(.76,.69,.52,.34)
	for at in [Vector2(814,1540),Vector2(1344,1540),Vector2(1770,1510),Vector2(2170,1435)]:
		c.sprite("generated/props/pipe.png",at,Vector2(110,34),PI/2)
		c.stain(at+Vector2(16,42),Vector2(100,81),Color(.04,.10,.07,.6))
		c.sprite("terrain/oil_hatch.png",at-Vector2(45,24),Vector2(64,50)).modulate=Color(.73,.78,.61,.8)
	for at in [Vector2(580,1540),Vector2(1128,1710),Vector2(1660,1600),Vector2(2200,1536)]:
		c.sprite("infrastructure/scrap.png",at+Vector2(-22,-15),Vector2(81,42),-.05)
		c.sprite("infrastructure/lantern.png",at-Vector2(0,40),Vector2(25,43))
		c.line(PackedVector2Array([at+Vector2(-30,12),at+Vector2(32,17),at+Vector2(53,4)]),Color("645038"),2)
	c.sprite("infrastructure/crane.png",Vector2(1110,1778),Vector2(80,112))
	c.coast.set_meta("land_polygon",outline);c.coast.set_meta("shore_points",shore);c.coast.set_meta("recess_count",4)
	c.coast.set_meta("layers","urban core; worn transition; coastal maintenance; piled docks")
	var markers := Node2D.new();markers.name="Destinations";c.coast.add_child(markers)
	for data in [["Transicao",Vector2(1512,1490)],["PatioRemendado",Vector2(500,1500)],["CaisManutencao",Vector2(1610,1600)],["DocaOeste",Vector2(735,1700)],["DocaDaBomba",Vector2(1060,1815)],["DocaLeste",Vector2(2210,1700)]]:
		var marker := Marker2D.new();marker.name=data[0];marker.position=data[1];markers.add_child(marker)
	print("LOWER COAST: structural recesses, open runoff and three attached docks; upper map retained")
