import os
import shutil

src_dir = r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone'
art_dir = r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b'

captures = [
    'captura_setor_sul_arena_geral.png',
    'captura_reciclador_e_mercado_close.png',
    'captura_cambio_e_oficina_coliseu_close.png',
    'captura_arcada_triagem_close.png',
    'captura_motor_cisterna_leste_close.png'
]

for c in captures:
    src_file = os.path.join(src_dir, c)
    art_file = os.path.join(art_dir, c)
    if os.path.exists(src_file):
        shutil.copy2(src_file, art_file)
        size_kb = os.path.getsize(art_file) // 1024
        print(f"Copiado para artefatos: {c} ({size_kb} KB)")
    else:
        print(f"Não encontrado: {src_file}")
