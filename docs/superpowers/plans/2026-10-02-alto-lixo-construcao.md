# Alto-Lixo oeste/noroeste — execução

**Objetivo:** construir a planta aprovada sobre a lateral do mapa atual, na mesma cena. Preservar MarketFloor, arte protegida e espaço leste/nordeste para Forjas.

**Arquivos:** `scripts/world/alto_lixo_builder.gd` gera a extensão; `assets/reconstruction/alto_ground.gdshader` mistura pedra e terra somente no piso novo; `tools/rebuild_original.gd` mantém a geração reproduzível da cidade atual; `tests/test_alto_lixo.gd` verifica percursos, escadas e acessos físicos.

1. [x] Guardar cena/checkpoint anterior e criar teste que falha quando Alto-Lixo não existe.
2. [x] Gerar e integrar cisterna comunitária com arte própria, referência do original e transparência.
3. [x] Abrir terreno lateral e faixas contínuas para os acessos fora do polígono inicial.
4. [x] Construir três vias, três becos, quatro patamares, escadas, moradias/anexos e galeria de manutenção.
5. [ ] Verificar ida/volta, becos sem desvios distantes, escadas e regressão do original/Mercado.
6. [ ] Avaliar panoramas/fronteiras, corrigir composição e atualizar status/checkpoint.

Alturas são desníveis visuais com degraus percorríveis. Não introduzir teleporte nem declarar implementada uma mecânica de múltiplas alturas sobrepostas. Saídas externas permanecem reservadas, sem destino ou portal inventado.
