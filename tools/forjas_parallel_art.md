# Arte paralela — Forjas Rasas

## Entrega incremental

- `assets/reconstruction/forjas_parallel/great_furnace_chimney.png`: landmark de grande fornalha com chaminé. Gerado via built-in image_gen, inspecionado visualmente; estrutura isolada, sem terreno ou texto. Ciano restrito a um pequeno medidor. Porta de fogo sul e silhueta alta de chaminé. Usar apenas uma instância como orientação visível a partir do Mercado.
- Sugestão de colocação: limite oeste/noroeste do núcleo industrial, fora da rua de passagem; chaminé acima dos telhados baixos, boca da fornalha voltada ao sul. Largura inicial do objeto: 310–360 pixels de mundo. Ancoragem próxima à base sul do corpo principal; colisão só no footprint inferior, nunca na chaminé/catwalk.

## Fontes

- `tools/checkpoints/original_visual_benchmark.png`: referência primária de câmera, textura, portas e luz.
- `C:/Users/Usuario/Downloads/Mapa de Ferrugem Baixa.png`: identidade e função do distrito.
- `maps/sucateia/preview_forjas_district.png`: contexto atual.
- `tools/forjas_art_manifest.json`: assets existentes a não duplicar.

## Prompt do landmark

Use case: stylized-concept. Create ONE production-ready isolated RGBA game sprite, a distinctive goblin industrial GREAT BLAST FURNACE WITH TALL CHIMNEY for Forjas Rasas in Sucateia. Reference images are style/context only, not edit targets: original_visual_benchmark.png is the primary visual benchmark; Mapa de Ferrugem Baixa.png supplies scrap-city identity. Match the benchmark's dense hand-painted weathered charcoal iron, soot-dark old masonry, dull rusty copper rivets, reclaimed timber and upper-left diffuse lighting. Camera: elevated orthographic THREE-QUARTER TOP-DOWN from SOUTH looking NORTH; no diagonal isometric camera, no vanishing point. Top surfaces strongly visible, short southern walls. Industrial landmark for navigation from the adjacent market: one broad squat cylindrical smelting furnace reinforced by uneven riveted bands, a very tall narrow irregular chimney at rear-left with visible soot-black mouth, small maintenance ladder and tight service catwalk, two thick bent exhaust pipes, short southern arched fire door with orange/amber contained fire behind iron grate, enclosed pouring channel ending in a compact metal mould. Emphasize tall chimney silhouette and distinguish it from a workshop, recycler or roofed boiler hall. Functional dark medieval scrap engineering. Entire object centered with generous transparent margins, all pipes contained, no clipped edges. At intended game scale 310-360px object width the fire door should be 24-30px wide. Orange/amber glow restrained and localized, no cyan except at most one pinprick gauge. TRUE transparent background, isolated object only, NO ground, terrain, floor slab, ground shadow, background scenery, people, typography, labels, text, logos, giant flames, smoke cloud, futuristic machinery, bright cartoon outlines.

## Estado da ampliação

Os quatro assets adicionais (armazenamento minério/carrinho, forja artesanal aberta, tubulação/caldeira de serviço, guindaste compacto) já haviam sido despachados quando chegou a orientação de transferir a frente a um chat dedicado. Nenhuma nova geração será iniciada. Resultados serão preservados para o novo chat sem regeneração duplicada. Não foram editadas cenas, scripts, pisos ou assets aprovados; Godot não foi executado.


## Entrega final: cinco sprites de produção

Todos os originais abaixo foram inspecionados visualmente e compostos sobre fundo sólido em `assets/reconstruction/forjas_parallel/qa_composite.png`. RGBA e pixels alpha 0 confirmados. O RGB marrom escondido em pixels transparentes não aparece na composição do jogo. Variantes `_clean.png` foram preservadas como alternativas de extração, mas os originais são a seleção de produção e preservam melhor o desenho.

| Arquivo na pasta assets/reconstruction/forjas_parallel | Dimensões | Transparente | Largura visual no mundo | Colocação sugerida |
|---|---|---|---|---|
| great_furnace_chimney.png | 1351 × 1164 | 57,56% | 310–360 px | Landmark único na transição Mercado/Forjas, base fora da rua |
| ore_storage_cart.png | 1536 × 1024 | 62,97% | 170–220 px | Pátio de abastecimento, a um lado da fornalha, carrinho para o corredor |
| open_smithy.png | 1496 × 1051 | 60,57% | 180–220 px | Borda do núcleo artesanal, frente sul aberta para o acesso |
| service_pipe_boiler.png | 1536 × 1024 | 60,92% | 150–190 px | Lateral técnica entre fornalha e fabricação, sem bloquear portas |
| compact_loading_crane.png | 1536 × 1024 | 66,69% | 180–220 px | Pátio de carga junto ao armazenamento; boom cobre área de operação |

Escalas são estimativas iniciais, não colocação validada em Godot. Para calcular escala, usar largura do recorte opaco, não largura do canvas. Colisão deve acompanhar a base de cada máquina; manter livres espaços vazados da forja, vão da grua e trânsito em frente ao carrinho. O landmark e a forja possuem alguns pixels de antialiasing no limite do canvas; não cortar novamente automaticamente.

Prompts completos, fontes de geração, dimensões e alpha_bbox de cada produção: `assets/reconstruction/forjas_parallel/manifest.json`. Nenhum `.tscn`, script, piso, asset aprovado ou importação foi modificado. Não houve execução de Godot.

## Prompts dos quatro módulos

### ore_storage_cart

Use case: stylized-concept. ONE production-ready isolated transparent RGBA 2D game sprite for Forjas Rasas in Sucateia. Primary style reference original_visual_benchmark.png: dense painterly realistic weathered textures, soot-dark charcoal iron, rust-brown copper, old stone, reclaimed timber, upper-left diffuse light. Elevated orthographic THREE-QUARTER TOP-DOWN from SOUTH toward NORTH, top surfaces occupy 70%, short southern faces, no diagonal isometric angle or perspective vanishing point. True transparency; complete object with 10% clear margins. NO ground, terrain, surrounding floor, ground shadow, scenery, people, text, letters, labels or logos. No bright cartoon outlines, no futuristic machinery. Restrained tiny amber lights, cyan minimal or absent. Functional goblin medieval salvage engineering. This is a modular prop, distinct from existing roofed workshop, scrap press/recycler and boiler hall. Compact outdoor ORE AND SLAG STORAGE MODULE: two low rectangular riveted open bins with visibly different piles of dull raw ore chunks and black cooled slag, narrow short built-in loading grate platform, one small squat mine cart with four functional wheels loaded with ore positioned in front, hand-operated tipping lever and a battered small wooden tool rack. No building roof, no furnace or chimney, no glowing molten pool. Wide low silhouette. Intended sprite object width 170-220 world pixels; cart approximately 55 world pixels wide; coherent scale with 25px-wide building doors.

### open_smithy

Use case: stylized-concept. ONE production-ready isolated transparent RGBA 2D game sprite for Forjas Rasas in Sucateia. Primary style reference original_visual_benchmark.png: dense painterly realistic weathered textures, soot-dark charcoal iron, rust-brown copper, old stone, reclaimed timber, upper-left diffuse light. Elevated orthographic THREE-QUARTER TOP-DOWN from SOUTH toward NORTH, top surfaces occupy 70%, short southern faces, no diagonal isometric angle or perspective vanishing point. True transparency; complete object with 10% clear margins. NO ground, terrain, surrounding floor, ground shadow, scenery, people, text, letters, labels or logos. No bright cartoon outlines, no futuristic machinery. Restrained tiny amber lights, cyan minimal or absent. Functional goblin medieval salvage engineering. This is a modular prop, distinct from existing roofed workshop, scrap press/recycler and boiler hall. Small OPEN ARTISAN SMITHY: irregular shallow rusted metal canopy supported by four reclaimed timber and iron posts, one large usable anvil clearly visible under open south side, short side stone charcoal hearth with dim contained orange fire, leather accordion bellows with mechanical foot lever, tongs hanging on side rack, a compact workbench with hammer. Strong open negative space under canopy, roof only covers rear half so work tools remain readable from overhead. No enclosed workshop, no large hall or industrial chimney. Intended object width 180-220 world pixels, anvil 35px wide.

### service_pipe_boiler

Use case: stylized-concept. ONE production-ready isolated transparent RGBA 2D game sprite for Forjas Rasas in Sucateia. Primary style reference original_visual_benchmark.png: dense painterly realistic weathered textures, soot-dark charcoal iron, rust-brown copper, old stone, reclaimed timber, upper-left diffuse light. Elevated orthographic THREE-QUARTER TOP-DOWN from SOUTH toward NORTH, top surfaces occupy 70%, short southern faces, no diagonal isometric angle or perspective vanishing point. True transparency; complete object with 10% clear margins. NO ground, terrain, surrounding floor, ground shadow, scenery, people, text, letters, labels or logos. No bright cartoon outlines, no futuristic machinery. Restrained tiny amber lights, cyan minimal or absent. Functional goblin medieval salvage engineering. This is a modular prop, distinct from existing roofed workshop, scrap press/recycler and boiler hall. Compact EXPOSED SERVICE PIPEWORK ASSEMBLY with small horizontal cylindrical pressure vessel on four metal legs, three uneven bent iron pipes connecting to tall differently sized upright valve manifolds, large manually operated red-rust handwheel, brass pressure gauge and short grated access step attached directly to vessel. Mechanically connected functional assembly; no building, no roof or factory hall, no furnace, no scrap recycler. Distinct low horizontal tank and branching vertical pipes silhouette. Intended object width 150-190 world pixels, tank 100px long. No luminous cyan boiler dome.

### compact_loading_crane

Use case: stylized-concept. ONE production-ready isolated transparent RGBA 2D game sprite for Forjas Rasas in Sucateia. Primary style reference original_visual_benchmark.png: dense painterly realistic weathered textures, soot-dark charcoal iron, rust-brown copper, old stone, reclaimed timber, upper-left diffuse light. Elevated orthographic THREE-QUARTER TOP-DOWN from SOUTH toward NORTH, top surfaces occupy 70%, short southern faces, no diagonal isometric angle or perspective vanishing point. True transparency; complete object with 10% clear margins. NO ground, terrain, surrounding floor, ground shadow, scenery, people, text, letters, labels or logos. No bright cartoon outlines, no futuristic machinery. Restrained tiny amber lights, cyan minimal or absent. Functional goblin medieval salvage engineering. This is a modular prop, distinct from existing roofed workshop, scrap press/recycler and boiler hall. ONE compact GOBLIN LOADING CRANE for industrial yard: squat four-legged iron-and-timber braced frame, angled cantilever rusty riveted boom with pulley at tip, clearly readable vertical hanging chain and empty hook, manual side winch with gear and hand crank, one battered counterweight at rear. Working medieval cargo lifting mechanism, asymmetrical silhouette, no modern tower crane, no building, no enormous gantry, no added cargo or surrounding terrain. Intended object width 180-220 world pixels; base 90px wide. Whole hook and boom inside canvas.

## Variantes de extração preservadas


- ore_storage_cart_clean.png: Generated images are saved to C:\Users\Usuario\.codex\generated_images\01a0ff5e-6e23-79b1-a73b-18055cf7b339 as C:\Users\Usuario\.codex\generated_images\01a0ff5e-6e23-79b1-a73b-18055cf7b339\exec-a30a1159-f25a-4791-b5d3-5a7a43c1a8a9.png by default.
- Prompt: Edit target ore_storage_cart.png. Precise background extraction only: remove ALL brown ambient halo, haze, backdrop and ground shadow around bins and cart. Keep exactly the same bins, ore, slag, cart, tool rack, metal textures, lighting, scale, camera and arrangement. Preserve object's opaque solid surfaces and internal holes; make solid object opacity 255 and every exterior pixel true alpha 0 except natural one-pixel antialiasing at object contour. Isolated clean production RGBA sprite without any aura or ground/background. Do not add or redesign objects.

- service_pipe_boiler_clean.png: Generated images are saved to C:\Users\Usuario\.codex\generated_images\01a0ff5e-6e23-79b1-a73b-18055cf7b339 as C:\Users\Usuario\.codex\generated_images\01a0ff5e-6e23-79b1-a73b-18055cf7b339\exec-f42e4975-49d8-4b5e-bd70-e33b99217f56.png by default.
- Prompt: Background extraction edit of service_pipe_boiler.png only. Remove all brown halo/haze/ambient background and all ground shadow. Keep the entire machine exactly the same: shape, arrangement, materials, upper-left light, camera, chain/hook or pipes, scale. Solid metal/wood surfaces opaque alpha 255; exterior and open gaps fully transparent alpha 0; natural fine contour antialiasing only. Clean isolated production game sprite on TRUE TRANSPARENT BACKGROUND. No new objects or redesign.

- compact_loading_crane_clean.png: Generated images are saved to C:\Users\Usuario\.codex\generated_images\01a0ff5e-6e23-79b1-a73b-18055cf7b339 as C:\Users\Usuario\.codex\generated_images\01a0ff5e-6e23-79b1-a73b-18055cf7b339\exec-4e4eb90d-2931-4b80-9769-9eb9bb1e0862.png by default.
- Prompt: Background extraction edit of compact_loading_crane.png only. Remove all brown halo/haze/ambient background and all ground shadow. Keep the entire machine exactly the same: shape, arrangement, materials, upper-left light, camera, chain/hook or pipes, scale. Solid metal/wood surfaces opaque alpha 255; exterior and open gaps fully transparent alpha 0; natural fine contour antialiasing only. Clean isolated production game sprite on TRUE TRANSPARENT BACKGROUND. No new objects or redesign.

## QA independente da frente dedicada

Cinco originais recebidos e inspecionados na composição RGBA `qa_composite.png`: funções distintas, objetos isolados, sem pessoas/texto/terreno, calor contido e ciano pontual. Nenhum PNG recebido foi alterado ou regenerado por esta frente. A câmera mostra superfícies superiores; mastros/chaminé naturalmente exibem maior altura. Escala/portas devem ser ajustadas pelo footprint, sem colisão de estruturas aéreas.

O aparente contato com bordas está restrito a alpha 1/255: objeto visível não foi cortado. Bboxes com alpha >16 (x0,y0,x1,y1) conferidos:

| Original | Canvas px | Bbox visível |
|---|---|---|
| great_furnace_chimney.png | 1351×1164 | 95,14,1284,1123 |
| ore_storage_cart.png | 1536×1024 | 129,212,1400,859 |
| open_smithy.png | 1496×1051 | 226,63,1275,981 |
| service_pipe_boiler.png | 1536×1024 | 42,47,1518,911 |
| compact_loading_crane.png | 1536×1024 | 157,16,1470,996 |

Medição feita com Pillow somente para leitura; inspeção da composição alpha sobre fundo claro confirma ausência de névoa visível. RGB colorido sob alpha zero pode aparecer em visualizadores que ignoram alpha; não confundir com fundo opaco. Liberados para avaliação/implantação pelo integrador; setor não declarado pronto.
