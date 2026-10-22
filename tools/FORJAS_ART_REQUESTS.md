# Lacunas verificadas — Forjas Rasas / auditoria de direção adotada

STATUS: lacunas integradas na cena atual; entrega para revisão visual. Frente de arte entregou13 selecionados em assets/reconstruction/forjas_parallel/complement_v1/manifest.json;12 necessários utilizados. Tanque completo usado, variantes rejeitadas e oficina adicional não usados. Portos alinhados; contato físico/apoios aplicados. Resultado em tools/FORJAS_DIRECTION_RESULT.md. Não gerar equivalentes nem ampliar outro setor; aprovação visual humana pendente.

Referências: tools/FORJAS_DIRECTION_AUDIT.md (direção adotada), tools/checkpoints/original_visual_benchmark.png (câmera/escala), captura preview_forjas_foundry.png (encaixe). Integrador vai clarear faixa de transição e organizar pátios antes de novos edifícios. Não gerar oficina híbrida adicional: ferreiro aberto + comércio existente já fazem essa função.

## Entregas necessárias

1. **Addon da fundição central** — chimneystack de exaustão que se fixa atrás da fundição EXISTENTE em (2700,-1000). Uma chaminé principal alta, duas ventilações curtas, plataforma de manutenção, escada/braçadeiras. Parte inferior termina em dois dutos claros, encaixados na traseira/telhado do forno. Sprite 170–220 px de largura e 390–460 px de altura visual; chaminé principal domina, sem outra fornalha completa. Encaixe inferior no mundo aproximadamente (2730,-1240), boca superior perto y=-1660. Não criar grande base que bloqueie via atrás do forno. PNG transparente; sem nuvem de fumaça integrada (exaustão será efeito localizado no jogo). Calor somente no encaixe inferior.
2. **Baia de carvão** — baia baixa reforçada com grande massa de carvão negro, carrinho de alimentação e pá/mesa de pesagem, agrupados como uma instalação funcional. Largura visual 190–225 px, profundidade 95–125 px; base curta sul. Colocação planejada (2500,-1170), ligação física à alimentação da fundição à direita/sudeste. Sem minério laranja ou outro galpão/forno. Entrada do carrinho para sul/leste e encaixe no lado leste para via de carga. Piso de contato/ferrugem/poeira apenas sob a própria base, transparência em volta.
3. **Baia de escória** — contenção irregular de escória escura/vermelho queimado, caçamba inclinada com material resfriado, carrinho/roda de descarga, chapas queimadas. Função descarte, não estoque de minério/carvão nem recycler. Largura 190–230 px, profundidade 100–135 px. Colocação (3545,-875) à margem leste, descarga voltada para a faixa externa. Não embutir paisagem/floor slab retangular; contorno remendado, lugar para conectar canaleta na esquerda.
4. **Resfriamento/manutenção** — tanque aberto baixo de água industrial escura, bandeja/canaleta de peças quentes, registros manuais, ferramentas e passarela curta anexada. Largura 160–195 px, profundidade 105–145 px. Colocação (2730,-290). Dois bocais visíveis: alimentação ao norte e descarga a sudeste, dutos devem sair alinhados horizontal/verticalmente para tubo de 20–28 px. Identidade ciano apenas pontual, laranja residual nas peças. Não fazer caldeira ou repetir o vaso de serviço já entregue.

Entregar PNGs e prompts/status/alpha_bbox em pasta própria da frente de arte; registrar os paths neste arquivo ou em manifesto referido. Construtor inspeciona antes de integrar. Não executar Godot nem tocar sucateia.tscn.

## Bloco obrigatório em TODOS os prompts

PRODUCTION CONSTRAINTS:
- match the exact elevated 3/4 top-down camera of the current game;
- match the scale of the existing Ferrugem Baixa buildings;
- readable at gameplay zoom, not only as concept art;
- no dramatic cinematic perspective;
- lighting from the same general direction as current map assets;
- include believable ground contact and base shadow;
- preserve clean silhouette for sprite extraction;
- avoid oversized roof overhangs that obscure walkable space;
- avoid frontal perspective;
- no isolated decorative pipes without visible connection logic;
- materials must match current Ferrugem Baixa: dark stone, rusted iron, copper, patched wood, soot;
- use cyan arcane light only as a secondary accent;
- orange forge light is primary in Forjas Rasas;
- asset must visually belong beside the current Mercado/Forjas transition;
- output should be usable as an in-game sprite, not only as key art.

MODULARITY:
- provide clear connection points;
- pipe ends, wall joins and platform edges must align cleanly;
- avoid asymmetry that prevents reuse unless the asset is a landmark;
- produce variants that differ in function, not just color;
- every module must imply a believable industrial purpose.
