# Entrada urbana do porto — correção local, 2026-10-03

Pedido humano: desobstruir a leitura da área antes do porto, que parecia soterrada e sem coerência estrutural.

Causa visual: módulos de grade sobrepostos à casa e à rua, canos verticais isolados, remendos e sombras de peças antigas, além de pavimentos e contenções duplicados na ligação da rua ao cais. A abordagem anterior misturava estruturas de alturas diferentes na mesma faixa.

Correção: retirar visualmente somente essas peças no retângulo (1985,1115)-(2265,1520); manter a margem de pedra como rua plana. A casa passa a ter uma base legível. O acesso aos decks utiliza uma peça única de transição pedra/madeira com base baixa e estacas, mais a faixa superior de patamar pintada com a mesma madeira.

Dois assets novos gerados no ImageGen integrado: `maintained_quay_paving.png` e `stone_timber_threshold.png`, em `assets/reconstruction/port_approach/`. Prompts completos, posição e medidas no manifesto da pasta. Nenhuma imagem antiga foi sobrescrita.

O pavimento é um Polygon2D recortado no chão existente, abaixo das casas. Coordenadas UV ficam dentro da textura para impedir faixas esticadas na borda. A ligação de madeira mantém os mesmos destinos, chegadas, polígonos de circulação e colisões do porto. O antigo pátio de sucata continua fora da faixa de entrada; sua física permanece.

Verificação específica: piso realmente opaco no PNG sob as três faixas do acesso (y=1360,1370,1380), travessia real de ida e volta com o jogador, amostragem do novo chão contra o contorno de terra existente e remoção das peças sobrepostas selecionadas.

Captura final: `maps/sucateia/preview_port_approach.png`. O ambiente restrito emite o diagnóstico de acesso ao repositório de certificados do Windows antes do Godot; as verificações locais de arte, render e física são avaliadas separadamente.

Seis verificações locais passaram: `test_port_approach`, `test_docas_routes`, `test_docas_preservation`, `test_lower_coast`, `test_utility_contacts`, `test_stair_fits`. A regressão do porto percorreu todos os 17 trechos e os três acessos nos dois sentidos, confirmou pontos seguros de R e água bloqueada. Logs em `tools/port_test_*.log`.

Retomada final: 16 testes sequenciais passaram com código 0 (`tools/port_verify_*.log`); nenhum erro de aplicação além do diagnóstico de certificados do ambiente. A captura atual `preview_port_approach.png` terminou com código 0 e foi conferida visualmente após o último ajuste UV/cor. Os dois PNGs têm SHA256 no manifesto. Evidências e checkpoint local listados em `tools/POLISH_PROGRESS.md`.
