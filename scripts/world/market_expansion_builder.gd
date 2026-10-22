extends RefCounted
var b
var district: Node2D
var detail: Node2D
var commerce: Node2D
func group(label: String, parent: Node, z: int=0) -> Node2D:
	var node := Node2D.new();node.name=label;node.z_index=z;parent.add_child(node);return node
func art(file: String, point: Vector2, size: Vector2, parent: Node, angle: float=0) -> Sprite2D:
	if file.begins_with("reconstruction/") and file.ends_with(".png"):
		var texture: Texture2D=load("res://assets/"+file)
		var pixels := Vector2(texture.get_size())
		size=pixels*minf(size.x/pixels.x,size.y/pixels.y)
	return b.art(file,point,size,parent,angle)
func shadow(point: Vector2, width: float) -> void:
	art("fx/light.svg",point+Vector2(5,8),Vector2(width,48),detail).modulate=Color(0,0,0,.65)
	art("terrain/market_dirt.png",point,Vector2(width*1.16,75),detail,.12).modulate=Color(.81,.74,.59,.39)
func solid(point: Vector2, size: Vector2, parent: Node) -> void:
	var body := StaticBody2D.new();body.position=point
	var collision := CollisionShape2D.new();var rectangle := RectangleShape2D.new();rectangle.size=size;collision.shape=rectangle
	body.add_child(collision);parent.add_child(body)
func lamp(point: Vector2, parent: Node, cyan: bool=false) -> void:
	art("infrastructure/lantern.png",point-Vector2(0,30),Vector2(25,43),parent)
	var light := PointLight2D.new();light.position=point;light.texture=load("res://assets/fx/light.svg");light.texture_scale=.38;light.energy=.42;light.color=Color("61b5ba" if cyan else "e0a353");district.add_child(light)
func stall(label: String, point: Vector2, file: String, size: Vector2, parent: Node) -> void:
	var node := group(label,parent);node.position=point
	shadow(point,size.x*.83)
	art(file,Vector2(0,-size.y*.42),size,node)
	solid(Vector2(0,-16),Vector2(size.x*.57,37),node)
	art("terrain/metal_repair.png",point+Vector2(-size.x*.2,12),Vector2(65,40),detail,-.09).modulate=Color(.76,.70,.53,.60)
func route(points: PackedVector2Array, width: float, intensity: float) -> void:
	for i in range(points.size()-1):
		var delta := points[i+1]-points[i];var count := ceili(delta.length()/47)
		for j in range(count):
			var point := points[i].lerp(points[i+1],(j+.5)/count)
			art("terrain/market_dirt.png",point,Vector2(78,width),detail,delta.angle()).modulate=Color(.97,.85,.66,intensity)
func shop(point: Vector2, stack: bool) -> void:
	var node := group("LojaDeRua",commerce);node.position=point
	shadow(point,198)
	art("terrain/foundation.png",point-Vector2(0,13),Vector2(194,71),detail).modulate=Color(.59,.57,.46,.65)
	art("generated/structures/house_stack.png" if stack else "generated/structures/house.png",Vector2(0,-130),Vector2(228,266),node)
	solid(Vector2(0,-30),Vector2(146,61),node)
	var frontage: String=["reconstruction/market_salvage_cart.png","reconstruction/cloth_stall.png","generated/props/market_stall.png"][posmod(int(point.y),3)]
	art(frontage,Vector2(-96,-20),Vector2(98,85),node)
	lamp(point+Vector2(103,14),commerce)
func install(builder) -> void:
	b=builder
	district=group("MarketDistrict",b.world)
	detail=group("GroundIntegration",district,-14)
	commerce=group("Commerce",district);commerce.y_sort_enabled=true
	var floor := TileMapLayer.new();floor.name="MarketFloor";floor.z_index=-30;floor.tile_set=load("res://assets/terrain/sucateia_terrain.tres");floor.material=b.world.get_node("Ground/TerraceFloor").material;district.add_child(floor)
	var outline := PackedVector2Array([Vector2(340,440),Vector2(315,60),Vector2(480,-170),Vector2(432,-535),Vector2(640,-1005),Vector2(1060,-1100),Vector2(1450,-1000),Vector2(1660,-730),Vector2(1725,-360),Vector2(1650,-80),Vector2(1740,225),Vector2(1490,440)])
	for y in range(-31,10):
		for x in range(5,38):
			var at := Vector2(x*48+24,y*48+24)
			var outgoing: bool=at.y < -960 and at.x>1030 and at.x<1260
			if Geometry2D.is_point_in_polygon(at,outline) or outgoing:floor.set_cell(Vector2i(x,y),0,Vector2i(posmod(x,16),posmod(y,16)))
	var old_wall: Node=b.world.get_node_or_null("Ground/NorthBoundary")
	if old_wall:old_wall.get_parent().remove_child(old_wall);old_wall.free()
	for sprite in b.world.find_children("*","Sprite2D",true,false):
		if not sprite.texture:continue
		var file: String=sprite.texture.resource_path
		if (file.ends_with("retaining_edge.png") or file.ends_with("coastal_wall.png")) and sprite.global_position.y>275 and sprite.global_position.y<420 and sprite.global_position.x<1700:
			sprite.get_parent().remove_child(sprite);sprite.free()
	# Relocate the distant silhouettes beyond the newly built city instead of placing a horizon across the street.
	var backdrop: Node2D=b.world.get_node_or_null("DistantCity")
	if backdrop:
		for child in backdrop.get_children():
			if child is Sprite2D:child.position.y-=1350;child.modulate=Color(.39,.46,.43,.68)
	var background := Polygon2D.new();background.z_index=-34
	background.polygon=PackedVector2Array([Vector2(-1500,-3200),Vector2(3600,-3200),Vector2(3600,600),Vector2(-1500,600)])
	var material := ShaderMaterial.new();material.shader=load("res://assets/reconstruction/market_fringe.gdshader");material.set_shader_parameter("soil",load("res://assets/terrain/floor_atlas.png"));background.material=material;district.add_child(background)
	load("res://scripts/world/market_urban_layout.gd").new().install(self)
	var camera: Camera2D=b.world.get_node("Structures/Player/Camera");camera.limit_top=-1740
	district.set_meta("new_ground_cells",floor.get_used_cells().size())
	district.set_meta("function","commercial circulation, bargaining, stock and connection to adjacent districts")
	district.set_meta("original_scale_preserved",true)
