# Arte antecipada — Os Cabos

PNG exclusivos em `assets/reconstruction/cabos_parallel/`. Geração: built-in image_gen, skill imagegen. Arte sem integração; nenhuma cena ou piso alterado, Godot não executado.

Referências inspecionadas: `tools/checkpoints/original_visual_benchmark.png` (câmera/textura/luz), `C:/Users/Usuario/Downloads/Mapa de Ferrugem Baixa.png` (identidade), `maps/ferrugem_baixa/preview_cabos.png` (contexto, não estética noturna), `sobre.txt:611` (distrito suspenso). Materiais reaproveitados com reparos e sinais de uso ativo. Todas as dimensões são do arquivo inteiro, incluindo margem transparente; escala final deve usar o objeto, não o canvas.

## Entrega incremental

### Casa pendurada

- Arquivo: `assets/reconstruction/cabos_parallel/hanging_house.png`.
- Estado: inspecionado visualmente; RGBA isolado, função e câmera coerentes.
- Implantação: 230–270 px incluindo suspensão; corpo doméstico 170–200 px. Ancorar pelo limiar sul; correntes exigem apoios superiores na cena.
- Fonte: Generated images are saved to C:\Users\Usuario\.codex\generated_images\01a0ff61-86fa-7101-a020-10db97b53f44 as C:\Users\Usuario\.codex\generated_images\01a0ff61-86fa-7101-a020-10db97b53f44\exec-2aae73de-964f-424d-aa08-dd0e1d48f66b.png

Prompt:

Use case: stylized-concept. ONE production-ready isolated RGBA 2D game sprite for Os Cabos suspended residential district of Sucateia/Ferrugem Baixa. Reference is primary visual style only: match original_visual_benchmark.png dense hand-painted weathered textures, dull rusted iron, old stone where needed, oxidized copper, reclaimed timber; upper-left diffuse DAYLIGHT, never nocturnal aesthetics. Elevated orthographic THREE-QUARTER TOP-DOWN camera from SOUTH toward NORTH, top surfaces dominate, short south walls, no diagonal isometric view or vanishing points. Functional medieval goblin salvage construction. Entire object centered with generous transparent margins, all attachments complete. TRUE transparent background; no surrounding ground, terrain, floor slab, ground shadow, scenery, water, people, letters, typography, logos. Restrained amber, tiny cyan only when functional, no bright cartoon outlines. Subject: ONE small HANGING HOUSE suspended in a cradle of four thick iron chains attached to two short overhead transverse beams, chains all contained in sprite. Broad irregular patched corrugated rusty copper and dark timber roof occupies 70 percent of house, squat reclaimed-timber walls with riveted braces, one small south door and narrow suspended porch with ladder folded up, bundles and small cargo pulley on side. House with mechanical suspension not ground-supported stilts. Asymmetric domestic silhouette, no chimney factory or industrial furnace. Intended object width 230-270 world pixels; door width 24 pixels. Render roof and suspension clearly readable from above.

### Ponte suspensa E–O

- Arquivo: `assets/reconstruction/cabos_parallel/suspension_bridge_ew.png`.
- Estado: inspecionado visualmente; RGBA isolado, função e câmera coerentes.
- Implantação: 500–580 px de vão inicial para passagem estreita (~45–55 px úteis). O resultado é mais estreito que o briefing; não comprimir para 330 px nem usar como via principal.
- Fonte: Generated images are saved to C:\Users\Usuario\.codex\generated_images\01a0ff61-86fa-7101-a020-10db97b53f44 as C:\Users\Usuario\.codex\generated_images\01a0ff61-86fa-7101-a020-10db97b53f44\exec-cb3ff015-cbed-4f96-925a-fe22303131e7.png

Prompt:

Use case: stylized-concept. ONE production-ready isolated RGBA 2D game sprite for Os Cabos suspended residential district of Sucateia/Ferrugem Baixa. Reference is primary visual style only: match original_visual_benchmark.png dense hand-painted weathered textures, dull rusted iron, old stone where needed, oxidized copper, reclaimed timber; upper-left diffuse DAYLIGHT, never nocturnal aesthetics. Elevated orthographic THREE-QUARTER TOP-DOWN camera from SOUTH toward NORTH, top surfaces dominate, short south walls, no diagonal isometric view or vanishing points. Functional medieval goblin salvage construction. Entire object centered with generous transparent margins, all attachments complete. TRUE transparent background; no surrounding ground, terrain, floor slab, ground shadow, scenery, water, people, letters, typography, logos. Restrained amber, tiny cyan only when functional, no bright cartoon outlines. Subject: ONE modular EAST-WEST SUSPENSION FOOTBRIDGE, long narrow weathered uneven timber walkway seen from high above, straight horizontal screen alignment, not diagonal. Thin rusty cable handrails, two short riveted anchor frames at each end, hanging chains below visible edge, small tensioning hardware; subtle sag but continuous walkable path. Ends fully contained, flat connecting terminals allow attachment to existing platforms. Structural bridge only, no surrounding floor tiles, ground or water. Readable 70-85 world-pixel walking width and 330-400 world-pixel length. No house, factory equipment, lantern tower, machinery or giant supports.

### Encontro em T

- Arquivo: `assets/reconstruction/cabos_parallel/walkway_t_junction.png`.
- Estado: entregue para integração como `walkway_t_junction_clean.png`; original preservado como variante, não usar ambos na mesma composição.
- Implantação: 350–420 px de largura; apenas braços como superfície de circulação. Variante de extração revisada por composição alpha sobre fundo claro.
- Fonte: Generated images are saved to C:\Users\Usuario\.codex\generated_images\01a0ff61-86fa-7101-a020-10db97b53f44 as C:\Users\Usuario\.codex\generated_images\01a0ff61-86fa-7101-a020-10db97b53f44\exec-3da33598-299c-4b10-9680-5fddd9251590.png

Prompt:

Use case: stylized-concept. ONE production-ready isolated RGBA 2D game sprite for Os Cabos suspended residential district of Sucateia/Ferrugem Baixa. Reference is primary visual style only: match original_visual_benchmark.png dense hand-painted weathered textures, dull rusted iron, old stone where needed, oxidized copper, reclaimed timber; upper-left diffuse DAYLIGHT, never nocturnal aesthetics. Elevated orthographic THREE-QUARTER TOP-DOWN camera from SOUTH toward NORTH, top surfaces dominate, short south walls, no diagonal isometric view or vanishing points. Functional medieval goblin salvage construction. Entire object centered with generous transparent margins, all attachments complete. TRUE transparent background; no surrounding ground, terrain, floor slab, ground shadow, scenery, water, people, letters, typography, logos. Restrained amber, tiny cyan only when functional, no bright cartoon outlines. Subject: ONE T-SHAPED SUSPENDED WALKWAY JUNCTION, screen-aligned east-west main span and shorter branch toward north. Thin uneven reclaimed timber planks with rusty metal grating repairs, narrow iron railings and chain stays, three complete attaching terminal brackets. Exposed underside beams read as an elevated structure, no slab, stone plaza or ground. Compact irregular handmade functional silhouette. Empty clear walkable center; small rope pulley at side. Intended span 280-330 world pixels, each walking branch 70-85px wide. High top-down view showing T layout, no diagonal perspective, no buildings or tall towers.

### Âncora de energia/mensagens

- Arquivo: `assets/reconstruction/cabos_parallel/power_messenger_anchor.png`.
- Estado: inspecionado visualmente; RGBA isolado, função e câmera coerentes.
- Implantação: 110–150 px de largura; base estreita, topo alto. Ligar sockets a cabos reais da cena; não bloquear caminhada pela copa.
- Fonte: Generated images are saved to C:\Users\Usuario\.codex\generated_images\01a0ff61-86fa-7101-a020-10db97b53f44 as C:\Users\Usuario\.codex\generated_images\01a0ff61-86fa-7101-a020-10db97b53f44\exec-fa59d43f-5c7b-4f85-81b5-219457196959.png

Prompt:

Use case: stylized-concept. ONE production-ready isolated RGBA 2D game sprite for Os Cabos suspended residential district of Sucateia/Ferrugem Baixa. Reference is primary visual style only: match original_visual_benchmark.png dense hand-painted weathered textures, dull rusted iron, old stone where needed, oxidized copper, reclaimed timber; upper-left diffuse DAYLIGHT, never nocturnal aesthetics. Elevated orthographic THREE-QUARTER TOP-DOWN camera from SOUTH toward NORTH, top surfaces dominate, short south walls, no diagonal isometric view or vanishing points. Functional medieval goblin salvage construction. Entire object centered with generous transparent margins, all attachments complete. TRUE transparent background; no surrounding ground, terrain, floor slab, ground shadow, scenery, water, people, letters, typography, logos. Restrained amber, tiny cyan only when functional, no bright cartoon outlines. Show active maintained use through replaced bolts, rope tensioners and pragmatic patches, not abandonment. Region is continuously inhabited and economically active, constructed from discarded older civilizations. Subject: ONE compact asymmetric POWER-LINE ANCHOR AND MESSENGER PULLEY MAST. Two uneven reclaimed riveted iron beams linked by timber crosspieces, several weathered ceramic/copper insulators, contained coiled wires with clear cable connecting sockets at sides, a small hand-cranked messenger parcel pulley and enclosed tiny cyan arcane accumulator. Top mast tilted parts make distinctive fork silhouette, narrow footprint. No long cables leaving frame; actual interbuilding wires will be drawn by game. No giant tower, furnace, chimney, smokestack, turbine or floor base. Small maintenance ladder and copper repair clamps indicate active use. Intended width 110-150 world pixels, higher than nearby domestic roof.


## QA final do lote

Quatro funções entregues; não significa setor integrado. Ver `assets/reconstruction/cabos_parallel/qa_composite.png` e `qa_metrics.json`. Inspeção por composição RGBA sobre fundo claro confirma ausência de névoa visível. Alguns pixels RGB marrons têm alpha zero; a visualização direta de PNG pode exibir esses RGB invisíveis. Alpha muito baixo nas bordas não significa objeto cortado: todos os bboxes com alpha >16 ficam dentro do canvas. Não recortar pelo bbox de alpha >0 sem considerar resíduos quase invisíveis.

| Arquivo liberado | Canvas px | Bbox visível alpha >16 | Transparência zero |
|---|---|---|---|
| hanging_house.png | 1374×1145 | 30,26–1341,1090 | 56,29% |
| suspension_bridge_ew.png | 2172×724 | 26,182–2146,540 | 69,06% |
| walkway_t_junction_clean.png | 1536×1024 | 20,26–1519,901 | 71,85% |
| power_messenger_anchor.png | 1394×1128 | 315,25–1144,1098 | 78,41% |

Extração via built-in image_gen; fonte: Generated images are saved to C:\Users\Usuario\.codex\generated_images\01a0ff61-86fa-7101-a020-10db97b53f44 as C:\Users\Usuario\.codex\generated_images\01a0ff61-86fa-7101-a020-10db97b53f44\exec-0854d4a9-4fc2-457f-a6bf-cd12d9399e42.png

Prompt de extração:

Edit target: supplied walkway_t_junction.png. Preserve exactly this T-shaped suspended bridge geometry, hand-painted texture, colors, camera, bolts, railings and pulley. Remove ALL brown ambient haze, diffuse glow, cast shadow, vignette and background pixels around and between the structure. Outside physical timber, chains, metal and rope must be alpha=0 truly transparent. Keep natural antialiased object edges and holes transparent. Do not add anything, no floor or ground, no people or text. Full isolated structure with comfortable transparent margins.
