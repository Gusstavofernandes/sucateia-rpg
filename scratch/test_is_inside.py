WEST_COAST_LINE = [
	(94, 284),
	(70, 330),
	(-40, 370),
	(-240, 410),
	(-500, 470),
	(-720, 560),
	(-830, 680),
	(-860, 800),
	(-870, 950),
	(-850, 1100),
	(-790, 1220),
	(-660, 1310),
	(-450, 1380),
	(-220, 1430),
	(0, 1470),
	(180, 1505),
	(395, 1535)
]

def is_inside_land(wx, wy):
	if wy < WEST_COAST_LINE[0][1] or wy > WEST_COAST_LINE[-1][1]:
		return wx >= 100.0

	for i in range(len(WEST_COAST_LINE) - 1):
		p0 = WEST_COAST_LINE[i]
		p1 = WEST_COAST_LINE[i + 1]
		if (wy >= p0[1] and wy <= p1[1]) or (wy >= p1[1] and wy <= p0[1]):
			dy = p1[1] - p0[1]
			if abs(dy) > 0.001:
				t = (wy - p0[1]) / dy
				coast_x = p0[0] + (p1[0] - p0[0]) * t
				return wx >= (coast_x - 30.0)
	return wx >= 100.0

matches = 0
for cx in range(-18, 4):
	for cy in range(7, 31):
		wx = cx * 48 + 24
		wy = cy * 48 + 24
		if is_inside_land(wx, wy):
			matches += 1

print("Matches:", matches)
