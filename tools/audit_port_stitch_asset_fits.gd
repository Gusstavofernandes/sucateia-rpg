extends "res://tests/test_docas_contacts.gd"
func run() -> void:
	var world: Node2D=load("res://maps/sucateia/sucateia.tscn").instantiate();root.add_child(world);current_scene=world;await physics_frame;await physics_frame
	var dock: Node2D=world.get_node("DocasDistrict");world.get_node("Structures/Player").set_physics_process(false);var paintings: Array=[]
	for sprite in dock.get_node("WorkingDecks").get_children():
		if not sprite is Sprite2D or str(sprite.name)=="RampaNavalLeste":continue
		var img: Image=sprite.texture.get_image();if img.is_compressed():img.decompress()
		paintings.append([sprite,img])
	var manifest: Dictionary=JSON.parse_string(FileAccess.get_file_as_string("res://assets/reconstruction/port_stitch/manifest.json"));var zones := {"Triagem":Rect2(2350,1420,310,160),"Almox":Rect2(2970,820,270,190),"Sul":Rect2(2720,1160,280,200),"Norte":Rect2(3160,510,260,190)};var report := {};var space := world.get_world_2d().direct_space_state;var query := PhysicsShapeQueryParameters2D.new();query.collision_mask=1;var shape := RectangleShape2D.new();query.shape=shape
	for asset in manifest.assets:
		var results := {};var scale: float=asset.scale_uniform;var canvas := Vector2(asset.canvas[0],asset.canvas[1])
		for zone in zones:
			var bounds: Rect2=zones[zone];var centers: Array=[]
			for y in range(int(bounds.position.y),int(bounds.end.y),4):
				for x in range(int(bounds.position.x),int(bounds.end.x),4):
					var center := Vector2(x,y);var valid := true
					for box in asset.footboxes_native_estimated:
						var native := Rect2(box[0],box[1],box[2]-box[0],box[3]-box[1]);var footprint := Rect2(center+(native.position-canvas*.5)*scale,native.size*scale)
						for pt in [footprint.get_center(),footprint.position,footprint.end,Vector2(footprint.end.x,footprint.position.y),Vector2(footprint.position.x,footprint.end.y)]:
							if not dock.is_walkable(pt) or not dock_painted(pt,paintings):valid=false;break
						if not valid:break
						for route in dock.get_node("Routes").get_children():
							var ends: PackedVector2Array=route.get_meta("points");var near := Geometry2D.get_closest_point_to_segment(footprint.get_center(),ends[0],ends[1]);var lateral: float=footprint.size.y*.5 if absf(ends[0].y-ends[1].y)<1 else footprint.size.x*.5
							if near.distance_to(footprint.get_center())<float(route.get_meta("clear_width"))*.5+lateral+2:valid=false;break
						if not valid:break
						for landing in dock.get_node("SafeLandings").get_children():
							if footprint.get_center().distance_to(landing.position)<35+footprint.size.length()*.5:valid=false
						shape.size=footprint.size;query.transform=Transform2D(0,footprint.get_center());query.exclude=dock.water_exclusions(footprint.get_center())
						if not space.intersect_shape(query,1).is_empty():valid=false
					if valid:centers.append([x,y])
			results[zone]=centers;print("STITCH actual PNG fit ",asset.name," ",zone,"=",centers.size())
		report[asset.name]=results
	var out := FileAccess.open("res://tools/port_stitch_asset_fits.json",FileAccess.WRITE);out.store_string(JSON.stringify(report,"\t"));out.close();world.queue_free();await process_frame;quit(0)
