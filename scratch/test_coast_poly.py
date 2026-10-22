def check_polygon():
    coast_points = []
    coast_points.append((-13100, -1120))
    for x in range(-13000, -750, 160):
        t = max(0.0, min(1.0, (-x - 1200) / 11800.0))
        y_reef = 60.0 - t * 860.0
        coast_points.append((float(x), y_reef))
        
    east_coast = [
        (-735, 115), (-695, 118), (-635, 120),
        (-570, 122), (-505, 122), (-440, 120),
        (-375, 120), (-245, 120),
        (-180, 120), (-125, 120), (-73, 166),
        (-18, 198),  (38, 238),   (94, 284),
        (80, 335),   (-50, 370),  (-250, 410),
        (-520, 470), (-740, 560), (-840, 680),
        (-870, 800), (-880, 950), (-850, 1100),
        (-790, 1220), (-660, 1320), (-450, 1390),
        (-220, 1440), (0, 1480), (180, 1510),
        (395, 1535)
    ]
    for pt in east_coast:
        coast_points.append(pt)
        
    print(f"Total points: {len(coast_points)}")
    print("Start:", coast_points[0])
    print("End:", coast_points[-1])
    
check_polygon()
