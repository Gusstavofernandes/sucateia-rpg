import os

dirs_to_check = ['assets/rails', 'fundo_ferro_standalone/assets/rails']
for d in dirs_to_check:
    print(f"=== Diretório: {d} ===")
    if os.path.exists(d):
        for f in sorted(os.listdir(d)):
            path = os.path.join(d, f)
            size = os.path.getsize(path)
            print(f"  {f:40s} ({size/1024:.1f} KB)")
    else:
        print("  Não existe")
