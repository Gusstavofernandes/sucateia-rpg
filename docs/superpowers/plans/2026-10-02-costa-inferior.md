# Costa inferior — retrabalho estrutural

Preservar a cena atual e tudo acima de y=1170, incluindo Mercado e Alto-Lixo. Trabalhar a massa inferior original, sem reconstrução global nem expansão regional. Fazer recuos no canto sudoeste, duas entradas de água na borda sul e um recuo no cais sudeste. Manter núcleo urbano, escada principal e percursos de Fundo-Ferro.

Quatro faixas: núcleo urbano até a contenção interna; transição com pavimento gasto e drenagem; borda industrial irregular; pequenos decks e píeres sobre estacas. Usar arte gerada já existente para muros, escadas, grades, ponte e sucata, sem placeholders visíveis.

Aplicar sobre a cena salva atual com `tools/rework_lower_coast.gd`; registrar os hashes de MarketFloor, AltoFloor, cinco assets aprovados e do trecho superior de TerraceFloor. Atualizar água e colisão a partir do mesmo contorno; retirar piso e decoração solta nas novas reentrâncias. PNGs de edifícios aprovados não mudam.

Verificar travessia aos pontos de manutenção e decks, impedir entrada nas três reentrâncias de água, preservar nove rotas originais e regressão do Mercado. Capturar a parte inferior e uma vista geral. Não retomar o detalhamento de Alto-Lixo nesta etapa.
