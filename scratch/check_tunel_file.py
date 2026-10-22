from PIL import Image
import os

p1 = 'fundo_ferro_standalone/assets/rails/boca_tunel_v2.png'
p2 = 'assets/rails/boca_tunel_v2.png'

print("p1 existe?", os.path.exists(p1), Image.open(p1).size if os.path.exists(p1) else "no")
print("p2 existe?", os.path.exists(p2), Image.open(p2).size if os.path.exists(p2) else "no")

# Vamos ver se existe boca_tunel_v2.png.import!
imp1 = p1 + '.import'
if os.path.exists(imp1):
    print("imp1:")
    with open(imp1, 'r', encoding='utf-8') as f:
        print(f.read()[:300])
