# Forjas Rasas — primeira implantação exterior

## Escopo entregue

Continuação física a leste/nordeste do Mercado na cena `maps/sucateia/sucateia.tscn`. A base é o checkpoint atual depois de Alto-Lixo, não os antigos setores noturnos. Nenhuma área anterior foi reconstruída. Piso industrial com 1590 células novas na escala existente de 48 unidades; 14 oficinas/galpões, duas fundições e três máquinas de reciclagem formam frentes e núcleos de trabalho. O território foi dimensionado por função, sem reduzir o Mercado.

Planta: `docs/forjas-rasas-planta-espacial.svg` e `tools/forjas_spatial_plan.json`. O JSON deriva das coordenadas do builder para evitar divergência. Worldbuilding: `sobre.txt` §§17.7,25–28,30–32 e atlas macro em `ispirações/Atlas Fantástico de Continentes Místicos.png`. Norte industrial para Chaminés Velhas, sucata a leste para Grande Ferrugem, drenagem/manutenção ao sul em direção conceitual a Fundo-Ferro.

## Organização e arte

Duas fronteiras acessíveis com o Mercado: entrada comercial e aproximação de carga. Via dos Rebitadores, Circuito das Fornalhas, Carga do Mercado, Passagem das Caldeiras, dois becos de trabalho, Rota da Triagem e Manutenção da Drenagem formam oito vias conectadas. Cinco pátios marcam reparos, fabricação, fundição, carga e reciclagem. Três saídas futuras são aproximações reservadas, sem destino ou teleporte.

Três sprites produzidos pelo gerador de imagem integrado: oficina modular, prensa recicladora e galpão de caldeiras. Prompts e fontes em `tools/forjas_art_manifest.json` e `tools/forjas_boiler_prompt.json`. Fundição gerada anteriormente reutilizada após inspeção contra o benchmark original; nenhuma cena histórica incorporada. Telhados dominantes, fachadas curtas, cobre/ferrugem/carvão e acentos âmbar/ciano coerentes com a base. Variações de galpão, escala controlada, patina, estoques agrupados, guindastes e plataformas de trabalho reduzem repetição.

O canal tem traçado quebrado, bordas texturizadas, extremidades reforçadas, drenagem e duas pontes. Três polígonos de água fornecem visual e colisão; aberturas das pontes são as mesmas lacunas físicas da água. Fundações, sombra de contato, sujeira, óleo, metal de reparo, canos e cabos integram arquitetura ao piso.

## Avaliação visual

Capturas finais: `preview_forjas_full.png`, `preview_forjas_district.png`, `preview_forjas_frontier.png`, `preview_forjas_foundry.png`, `preview_forjas_recycling.png`, `preview_forjas_drain.png`, todas em `maps/sucateia/`.

O panorama mantém uma cidade contínua com largura residencial a oeste e produção a leste. A fronteira passa de bancas/casas a oficinas; a fundição aberta serve de landmark e a prensa distingue o pátio de triagem. Os respiros são vias e pátios de trabalho, com densidade maior nas frentes e bordas. Não há parede retangular cercando um cenário separado. A costa inferior irregular continua intacta.

## Verificação física e preservação

- `test_forjas_rasas.gd`: dez destinos com ida/volta real, todos os trechos das oito vias, duas pontes, três amostras de água bloqueadas, personagem único.
- `test_forjas_preservation.gd`: todos os nós antigos mantidos, três pisos idênticos, colisões/contorno da costa iguais, sprites/transformações anteriores preservados, 19 bases industriais bloqueadas.
- `test_forjas_render_order.gd`: arquitetura e props de Forjas compartilham o Y-sort existente do jogador em `Structures`; nenhuma mudança na ordenação raiz dos bairros aprovados.
- Regressões finais de Alto-Lixo, acabamento residencial, costa, Mercado e núcleo/spawn/WASD/Shift/R passaram. O runner `tools/run_forjas_checks.py` executa as oito verificações sequencialmente.
- Cinco PNGs aprovados são verificados novamente por SHA-256 no finalizador.

## Revisão e correções

Revisão independente parcial por agente, via skill `requesting-code-review`, encontrou ordenação inadequada entre a arquitetura nova e o jogador. Corrigida somente na cena atual, reparentando arquitetura/estoques de Forjas para o grupo Y-sort já existente. Teste reproduziu a falha antes e passou depois; suíte final 8/8. O agente foi interrompido por limite de uso antes de um relatório final completo; revisão restante de composição e preservação realizada pelo autor.

Uma oficina foi retirada da rota de carga após falha física de um trecho. A execução concorrente de capturas/testes encontrou falta de memória do host; houve repetição sequencial, sem alterar produto por esse erro. Logs finais devem conter apenas execuções bem-sucedidas; os testes não representam benchmark prolongado de FPS.

## Limites declarados

Primeira implantação exterior visual e navegável. Elevação somente visual; interiores, NPCs, produção simulada, economia e combate não foram implementados. Chaminés Velhas, Grande Ferrugem e a extensão de Fundo-Ferro ainda não existem nesta cena como destinos completos. Ferrugem Baixa e o mundo continuam incompletos. Aguardar revisão da supervisão antes de outro setor.

Checkpoint final: `tools/checkpoints/sucateia_forjas_rasas_primeira_etapa.zip`.
