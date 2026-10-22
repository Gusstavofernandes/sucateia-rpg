from PIL import Image

for f in [
    'assets/reconstruction/red_iron_rocks_cluster.png',
    'assets/reconstruction/red_rock_cliff_edge.png',
    'assets/reconstruction/red_soil_transition_patch.png'
]:
    im = Image.open(f)
    print(f, 'size:', im.size, 'mode:', im.mode)
