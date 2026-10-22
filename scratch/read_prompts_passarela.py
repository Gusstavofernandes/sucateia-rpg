import os

for f in ['scratch/prompts/passarela_travessia_v1.txt', 'scratch/integrate_passarelas.py', 'scratch/gerar_passarela_final.py']:
    if os.path.exists(f):
        print(f"=== {f} ===")
        with open(f, 'r', encoding='utf-8', errors='ignore') as file:
            print(file.read()[:1500])
