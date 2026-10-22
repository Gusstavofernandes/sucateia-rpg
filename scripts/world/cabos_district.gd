extends Node2D
var surface_spawn := Vector2(1152,1248)
var occlusion: ShaderMaterial
var surface_avatar: Sprite2D
func _ready() -> void:
	occlusion=ShaderMaterial.new();occlusion.shader=load("res://assets/reconstruction/cabos_occlusion.gdshader")
	for label in ["ElevatedDecks","StructuralSupports","TensionAndMessages"]:
		var node := get_node_or_null(label)
		if node:node.material=occlusion;inherit_material(node)
	install_ground_support_depth()
	# Existing roofs can still cover a street pedestrian after the new deck fades.
	# This is a visual readout of the single player, shown only below new structures.
	var original: Sprite2D=get_parent().get_node("Structures/Player/Sprite")
	surface_avatar=Sprite2D.new();surface_avatar.name="SurfaceAvatarReadout";surface_avatar.texture=original.texture;surface_avatar.scale=original.scale;surface_avatar.z_index=9;surface_avatar.visible=false;add_child(surface_avatar)

func install_ground_support_depth() -> void:
	# The elevated layer draws above roofs, but street pillars must be sorted
	# beside buildings at their masonry feet. Keep the authored receivers and
	# physics in place and render their artwork through ground-level pivots.
	var structures: Node2D = get_parent().get_node("Structures")
	var grounded := Node2D.new()
	grounded.name = "CabosGroundSupports"
	grounded.y_sort_enabled = true
	structures.add_child(grounded)
	for source in get_node("StructuralSupports").get_children():
		if not source is Sprite2D:
			continue
		var foot: Vector2
		if source.has_meta("ground_contact"):
			foot = to_global(source.get_meta("ground_contact"))
		elif String(source.name).begins_with("Mastro"):
			foot = source.to_global(Vector2(0, source.texture.get_height() * .44))
		else:
			continue
		var pivot := Node2D.new()
		pivot.name = source.name
		grounded.add_child(pivot)
		pivot.global_position = foot
		var art := Sprite2D.new()
		art.name = "Art"
		art.texture = source.texture
		art.centered = source.centered
		art.offset = source.offset
		art.modulate = source.modulate
		art.material = occlusion
		pivot.add_child(art)
		art.global_transform = source.global_transform
		source.hide()
		var shadow: Sprite2D = get_node("ContactShadows").get_node_or_null(String(source.name) + "Contact")
		if shadow:
			var contact := Sprite2D.new()
			contact.name = "ContactShadow"
			contact.texture = shadow.texture
			contact.modulate = shadow.modulate
			contact.z_index = -1
			pivot.add_child(contact)
			contact.global_transform = shadow.global_transform
			shadow.hide()

func inherit_material(node: Node) -> void:
	for child in node.get_children():
		if child is CanvasItem:child.use_parent_material=true
		inherit_material(child)
func is_walkable(point: Vector2) -> bool:
	for polygon in get_meta("walk_polygons",[]):
		if Geometry2D.is_point_in_polygon(point,polygon):return true
	return false
func change_layer(access: Node) -> bool:
	if access.get_parent()!=get_node("Accesses"):return false
	var world := get_parent();var player: CharacterBody2D=world.get_node("Structures/Player")
	var up: bool=player.get("navigation_layer")=="surface"
	var origin: Vector2=access.get_meta("surface_arrival" if up else "elevated_arrival")
	var destination: Vector2=access.get_meta("elevated_arrival" if up else "surface_arrival")
	if player.position.distance_to(origin)>42:return false
	if up and not is_walkable(destination):return false
	if not up and not world.is_surface_walkable(destination):return false
	var query := PhysicsShapeQueryParameters2D.new();var shape := CircleShape2D.new();shape.radius=11;query.shape=shape;query.collision_mask=4 if up else 1;query.transform=Transform2D(0,destination)
	if not get_world_2d().direct_space_state.intersect_shape(query,1).is_empty():return false
	if up:surface_spawn=player.spawn_point
	player.navigation_layer="cabos" if up else "surface";player.collision_mask=4 if up else 1;player.z_index=8 if up else 0
	player.position=destination;player.velocity=Vector2.ZERO;player.spawn_point=destination if up else surface_spawn
	player.get_node("Camera").reset_smoothing();return true
func _process(_delta: float) -> void:
	var player: Node2D=get_parent().get_node_or_null("Structures/Player")
	if not player:return
	if occlusion:
		occlusion.set_shader_parameter("player_position",player.global_position)
		occlusion.set_shader_parameter("surface_player",player.get("navigation_layer")=="surface")
	if surface_avatar:
		var original: Sprite2D=player.get_node("Sprite");var under := false
		if player.get("navigation_layer")=="surface":
			for node in get_node("ElevatedDecks").get_children():
				if node is Sprite2D and node.get_rect().has_point(node.to_local(original.global_position)):under=true;break
		surface_avatar.visible=under;surface_avatar.global_position=original.global_position;surface_avatar.flip_h=original.flip_h;surface_avatar.modulate=original.modulate
