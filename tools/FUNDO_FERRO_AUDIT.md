# Fundo-Ferro — primeira etapa subterrânea

Oito salas conectadas por um circuito de retorno, uma travessa secundária, uma galeria industrial e a rota de acesso à Arena. Poço Velho, Câmara das Bombas, Galeria de Descarte, Casa das Máquinas, Reservatório do Limo, Ruínas da Fundação, Sala das Válvulas e Arena têm funções e landmarks diferentes. Nove rotas, seis conjuntos de máquinas com bases bloqueadas, quatro porções de água bloqueada e duas passarelas atravessáveis.

A cena inferior separada é necessária para impedir sobreposição de arte e colisões da superfície. Não é uma nova ilha urbana: três escadas/escotilhas na cidade atual levam à camada inferior e retornam ao acesso correspondente. F funciona somente em proximidade. E antigo continua inativo. Coordenadas ajudam orientação entre camadas; não representam simulação física de altura. R usa a última chegada segura.

## Preservação

Baseline completa: tools/checkpoints/sucateia_before_fundo.tscn. Nenhum prédio aprovado, piso, posição arquitetônica, costa ou estrutura de Forjas foi reconstruído. Acrescentados LayerEntrances/LayerArrivals, identificação dos acessos, metadado de camada e autoload LayerTravel. HUD agora distingue corretamente superfície/acesso de subsolo. A reserva de manutenção de Forjas passa a indicar conexão existente; demais destinos externos continuam pendentes.

tests/test_fundo_preservation.gd compara recursivamente classes, transformações, ordem de desenho, texturas, modulação, colisões e dados dos pisos dos nós anteriores. Finalizador também compara quatro pisos (MarketFloor, AltoFloor, TerraceFloor, ForjasFloor) e os cinco PNGs protegidos por SHA-256.

## Arte e leitura visual

Parede arruinada e motor abandonado foram gerados no image_gen integrado, com referência exclusiva do benchmark original. PNGs e prompts completos em tools/fundo_art_manifest.json; arquivos em assets/reconstruction/fundo_wall.png e fundo_abandoned_engine.png. Reuso de cisterna, estação de bombas, fundação arruinada, reator e recicladora preserva materiais e escala. Nenhuma cena histórica incorporada.

Revisão das onze capturas: panorama completo, sete salas e três acessos de superfície. Paredes antes pouco legíveis foram reforçadas; rocha ao redor dos túneis substitui o vazio preto; cisterna e fundação antiga diferenciam Poço Velho e Ruínas. Reservatório/Bombas têm água escura com contato e travessia; motor focal marca a Casa das Máquinas. Contorno acompanha as salas e corredores, sem moldura de arena. Há espaço para circulação, sem decoração bloqueando o circuito. Esta é uma primeira etapa de ambientação, não acabamento final de toda a região.

Capturas inferiores: maps/fundo_ferro/preview_fundo_{full,PocoVelho,Bombas,Descarte,Maquinas,Reservatorio,Ruinas,Valvulas}.png. Acessos: maps/sucateia/preview_fundo_surface_{PocoVelho,DocaLeste,ForjasManutencao}.png. Planta derivada do builder: docs/fundo-ferro-planta-espacial.svg e tools/fundo_spatial_plan.json.

## Evidência

tools/run_fundo_checks.py: 11/11 testes passaram. Navegação física ida/volta em todas as salas e trechos; duas pontes testadas diretamente; água, bases e rocha exterior bloqueadas. Input F real completou seis mudanças de camada, mantendo um jogador, chegada segura e R correto. E/remoto não mudam camada. Regressões de Forjas (incluindo y-sort), Alto-Lixo, costa, Mercado e original passaram. Logs tools/fundo_test_*.log.

tools/run_fundo_captures.py: 11 capturas, saída 0, sem ERROR. Panorama inferior: 246 draw calls / 1337 nós. Salas: 41–100 draw calls / 1337 nós. Acessos de superfície: 99–342 draw calls / 3256 nós. São amostras de captura, não benchmark prolongado de FPS.

Revisão independente estática por subagente: nenhum problema material identificado; conferiu código de acessos/camadas, spawns e logs existentes. Não executou novamente o motor. Avaliação visual das onze capturas realizada pelo implementador.

## Limites

Sem NPCs, criaturas, gangues funcionais, combate, economia ou interiores de moradias. Nenhum desses sistemas é declarado concluído. Nenhuma expansão de superfície nem integração de Vhal-Kor. Ferrugem Baixa continua incompleta. Próximo setor aguarda revisão. Checkpoint: tools/checkpoints/sucateia_fundo_ferro_primeira_etapa.zip, com CRC verificado pelo finalizador.
