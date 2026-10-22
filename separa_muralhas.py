from PIL import Image
import numpy as np

# Carregar a imagem limpa
im = Image.open(r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\teste_muralha_sul_clean.png').convert("RGBA")
arr = np.array(im)
h, w, _ = arr.shape
y_indices, x_indices = np.indices((h, w))

# Elipse interna da terra:
cx = 688
cy = 300
rx = 525
ry = 155

dist_elipse = ((x_indices - cx) / rx) ** 2 + ((y_indices - cy) / ry) ** 2

# Vamos isolar a regiao do portao frontal:
# X do portao: 460 a 916
# Y do portao: 380 a 745
mask_portao_box = (x_indices >= 460) & (x_indices <= 916) & (y_indices >= 380) & (y_indices <= 745)

# A terra fica dentro da elipse (dist_elipse < 0.98), EXCETO onde o portao e suas colunas estao!
# Para o portao: as barras e a estrutura de ferro sao de cor escura de ferro (R, G, B escuros)
# Enquanto a terra no fundo e marrom-claro/amarelado.
# Mas na verdade, os vaos do portao devem ser transparentes para ver a luta no fosso atraves da grade do portao!
# Vamos analisar as cores da terra:
r = arr[:, :, 0].astype(float)
g = arr[:, :, 1].astype(float)
b = arr[:, :, 2].astype(float)

# A terra tem tom marrom medio/claro: (r > 90, g > 80, b > 65)
# As barras do portao sao ferro escuro: (r < 80, g < 75, b < 70)
# A terra a ser removida:
mask_terra_geral = (dist_elipse < 0.98) & (arr[:, :, 3] > 0)

# Mas dentro da caixa do portao (y >= 380):
# Queremos manter as barras de ferro e remover apenas o fundo de terra entre as barras!
# Ferro do portao:
is_ferro_portao = mask_portao_box & ((r < 85) | (g < 80) | (b < 75)) & (arr[:, :, 3] > 100)
# Vamos preservar o topo e estrutura do portao (moldura do portao y >= 380 a 440 tem a viga horizontal pesada)
is_viga_topo_portao = mask_portao_box & (y_indices >= 380) & (y_indices <= 445) & (arr[:, :, 3] > 100)
# Colunas laterais do portao (x de 460 a 510 e x de 865 a 916)
is_coluna_portao = mask_portao_box & ((x_indices <= 515) | (x_indices >= 865)) & (arr[:, :, 3] > 100)

is_estrutura_portao = is_viga_topo_portao | is_coluna_portao | is_ferro_portao

# Terra real a remover:
mask_remover_terra = mask_terra_geral & (~is_estrutura_portao)

# Agora vamos criar as duas pecas:
# 1. PECA NORTE (Muralha Norte Arredondada do Coliseu):
# Tudo da metade norte da arena: y <= 350
arr_norte = arr.copy()
# Remover tudo que for da metade sul
# Linha de corte norte/sul:
mask_sul_para_norte = (y_indices > 340) | mask_remover_terra
arr_norte[mask_sul_para_norte, 3] = 0

# 2. PECA SUL (Mureta Sul Arredondada do Coliseu com Portao):
# Tudo da metade sul da arena: y >= 290
arr_sul = arr.copy()
# Remover a terra do centro
arr_sul[mask_remover_terra, 3] = 0
# Remover a parede norte de tras
mask_norte_para_sul = (y_indices < 300)
arr_sul[mask_norte_para_sul, 3] = 0

# Salvar ambas
im_norte = Image.fromarray(arr_norte)
im_sul = Image.fromarray(arr_sul)

im_norte.save(r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\arena_muralha_arredondada_norte_v1.png')
im_sul.save(r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\arena_muralha_arredondada_sul_v1.png')

print("Peca Norte salva:", im_norte.size)
print("Peca Sul salva:", im_sul.size)

# Vamos tambem gerar uma montagem composta com o chao de sangue/ferro no meio para inspecionar!
chao_fosso = Image.open(r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets\props\arena_piso_fosso_completo_robusto_v1.png').convert("RGBA")
# Redimensionar chao_fosso para caber dentro da elipse (aproximadamente 1050 x 580)
chao_resized = chao_fosso.resize((1080, 560), Image.Resampling.LANCZOS)

# Criar canvas de composicao
comp = Image.new("RGBA", (w, h), (0, 0, 0, 0))
# 1. Colocar o chao
chao_pos_x = (w - 1080) // 2
chao_pos_y = 120
comp.paste(chao_resized, (chao_pos_x, chao_pos_y), chao_resized)

# 2. Colocar a muralha norte atras (ela fica nas bordas e topo)
comp_com_norte = Image.new("RGBA", (w, h), (0, 0, 0, 0))
comp_com_norte.paste(im_norte, (0, 0), im_norte)
comp_com_norte.paste(comp, (0, 0), comp) # chao por cima da base da muralha norte
comp_com_norte.paste(im_sul, (0, 0), im_sul)   # mureta sul por cima de tudo na frente!

comp_com_norte.save(r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\teste_arena_arredondada_composta.png')
print("Composicao salva!")
