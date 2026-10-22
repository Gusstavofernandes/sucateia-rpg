# Arte antecipada — Passagem das Amarras

Brief: `tools/CONSULTANT_AMARRAS_ASSETS.md`. Somente assets/QA novos em `assets/reconstruction/amarras_parallel/`; nenhuma cena, script, import ou runtime. Direção: infraestrutura logística leste/sudeste de Forjas rumo a Engrenópolis, não Forjas2 nem doca/residência. Benchmark primário `tools/checkpoints/original_visual_benchmark.png`; mapa conceitual `C:/Users/Usuario/Downloads/Mapa de Ferrugem Baixa.png` para função regional.

## Inventário de reaproveitamento — não regenerar

| Função existente | Caminho aprovado | Uso / restrição |
|---|---|---|
| Ponte estreita E–W | cabos_parallel/suspension_bridge_ew.png | Vão500–580px; circulação estreita. Precisa das novas ancoragens; não é ponte principal larga. |
| Encontro em T | cabos_parallel/walkway_t_junction_clean.png |350–420px; conexão de caminhos; não inventar novos braços sem suporte. |
| Mastro elétrico/mensagens | cabos_parallel/power_messenger_anchor.png |110–150px; energia leve, não suporta tensão pesada. Não duplicar insuladores/bateria no novo hub. |
| Cabrestante/cabeços | docas_parallel/mooring_capstan.png |120–160px; amarração de barcos. Guincho novo só se tração horizontal/sprocket/freio de corrente, sem repetir capstan vertical. |
| Barcaça/abrigo de carga | docas_parallel/cargo_barge.png e cargo_sorting_shelter.png | Apoio à transferência junto à água; sem construir doca nova nesta frente. |
| Guindaste | forjas_parallel/compact_loading_crane.png | Guindaste216×144px no integrador atual; sem novo braço de carga. |
| Minério/carrinho | forjas_parallel/ore_storage_cart.png |227×151px; reutilizar carga/carrinho, sem duplicar. |
| Tubo sustentado | forjas_parallel/complement_v1/supported_pipe_connector.png |100×36px; flanges~24px/corpo14px; conectividade de serviços. |
| Passarela serviço | forjas_parallel/complement_v1/short_service_catwalk.png |220×56px; caminhada~30px, abas com bolt-lugs. |
| Redutor de exaustão | forjas_parallel/complement_v1/exhaust_reducer_connector.png |26→40–44px; usar apenas onde houver diferença real de diâmetro, não decoração. |
| Suporte avulso N–S | forjas_parallel/complement_v1/pipe_saddle_support_single_ns.png |35×35px; não encaixe direto no tubo E–W. |
| Galpões/oficina e luzes | assets/reconstruction/forjas_workshop.png / forjas_boiler_hall.png / iluminação aprovada | Reaproveitar onde função exigir; nenhum grande edifício industrial novo. |
| Fuligem de fronteira | forjas_parallel/complement_v1/transition_soot_decal.png | FamíliaA do brief junto de Forjas, opacidade inicial0,10–0,20 em Amarras. Não regenerar carvão/escória/calor de Forjas. |

Os caminhos da tabela são relativos a `assets/reconstruction/`, exceto os explicitamente completos. Inventário consultou manifestos e `tools/integrate_forjas_art.gd` somente em leitura.

## Lote enxuto escolhido — oito PNGs, sete funções do brief

1. Contraforte/ancoragem de borda com sapata, brace e correntes — primeira estrutura.
2. Decal de tração/carga/corrente — famíliaB, sem piso substituto.
3. Decal de umidade/óleo/depósito/ancoragem — famíliaC, sem água de fundo.
4. Torre média de tensão — função pesada diferente do mastro elétrico.
5. Guincho horizontal de corrente com trava — diferente do capstan marítimo.
6. Plataforma de amarração com centro vazio para cargas existentes.
7. Hub mecânico baixo de roteamento de correntes — não outro mastro elétrico.
8. Quiosque técnico pequeno — sem balcão comercial/forja.

FamíliaA usa decal já aprovado. Entrega de PNGs separados preserva transparência e evita dependência de recorte de sheet. Conexões de correntes usam abertura6px/algema13px como meta comum; escala base compara portas24–28px e módulos existentes. Luz superior esquerda, câmera benchmark, margem alvo10% e contato real; valores entregues serão conferidos por QA, não presumidos pelo prompt.

Estado: oito PNGs selecionados e QA estático concluído; prompts/conexões/footprint/medições no manifesto final. Não declara setor integrado.

## Entrega incremental

- `edge_anchor_buttress.png` já salvo: contraforte de pedra antiga com duas escoras e correntes reais saindo de pinos de carga. Sapata integral e junção traseira visíveis; repetível como contenção de borda, não torre/pórtico. Largura inicial135px. Correntes terminam em algemas curtas; a cena deve continuar essas linhas a partir dos terminais, não inventar correntes suspensas sem destino.
- `chain_winch_station.png`, `cargo_tiedown_platform.png`, `chain_routing_hub.png` recebidos e em QA. Guincho é horizontal com trava; plataforma vazia com lugs; hub é guia baixo com três saídas.
- Decals originais com correntes/parafusos físicos rejeitados. Variantes `_marks` e `_stains` removem hardware e ficam somente com impressões/manchas.
- Quiosque original com cabo cortado rejeitado; `_complete` recupera terminal curto contido. Torre teve ajuste dos terminais e margem para melhorar leitura/extração. Todos os originais/variantes permanecem preservados sem overwrite.


## Seleção final — oito PNGs entregues para integração

Geração integrada `image_gen`, skill imagegen. `assets/reconstruction/amarras_parallel/manifest.json` contém prompt completo com todos os blocos do brief, fonte original, dimensões, SHA256, alpha, margem, escala e conexões. `variants.json` preserva cinco tentativas não selecionadas com motivo; não implantar essas variantes junto das seleções.

| PNG selecionado | Canvas px | Objeto visível gameplay px | Contato de base aproximado px | Escala uniforme | Alpha sugerido |
|---|---|---|---|---|---|
| edge_anchor_buttress.png | 1391×1131 | 135×108 | 104×32 | 0.103926 | 1 |
| chain_drag_wear_decal_marks.png | 1915×821 | 210×70 | decal plano | 0.116927 | 0.3 |
| damp_anchor_runoff_decal_stains.png | 1499×1049 | 150×109 | decal plano | 0.122249 | 0.25 |
| tension_anchor_tower_margin.png | 1024×1536 | 150×217 | 117×62 | 0.177936 | 1 |
| chain_winch_station.png | 1524×1032 | 155×64 | 94×27 | 0.107341 | 1 |
| cargo_tiedown_platform.png | 1699×926 | 220×94 | 164×21 | 0.145503 | 1 |
| chain_routing_hub.png | 1417×1110 | 125×79 | 69×15 | 0.091042 | 1 |
| technical_control_kiosk_complete.png | 1408×1117 | 185×172 | 165×23 | 0.180664 | 1 |

Escala usa bbox com alpha >16, descontando margem do canvas; não deformar para preencher largura/altura independentes. Contato da base é bbox aproximado do apoio visível no chão, não desenho de colisão já aprovado. Meta do prompt:10%; margem mínima visível entregue22–93px, variando por objeto, nem todos atingem10% proporcional. Nenhum objeto selecionado toca a borda ou apresenta cadeia/terminal cortado. Tower `_margin` foi refeito com folga80px e algemas abertas, em vez da variante quase encostada.

## Conexões e pontos de apoio

Origem das coordenadas: topo esquerdo do PNG. Precisão visual estimada±10px de fonte; revisar centros e sobreposição na cena. JSON também fornece posição normalizada e offset de mundo para Sprite2D centrado. Fórmula: ponto em mundo = posição do sprite + (ponto nativo − metade canvas) × escala. Marcações em `qa_footprints_connections.png` são guias de implantação, não conexão certificada de runtime.

### edge_anchor_buttress

Contraforte transfere tensão à retenção; inserir join N contra contenção real com sobreposição8–10px. Dois terminais E têm offsets distintos. Não usar como torre ou cabeço de barco.

- `wall_join_n`: (543,238) px de fonte; offset do centro (-15.85,-34.04) px gameplay.
- `chain_e_upper`: (1285,451) px de fonte; offset do centro (61.26,-11.9) px gameplay.
- `chain_e_lower`: (982,643) px de fonte; offset do centro (29.77,8.05) px gameplay.

### chain_drag_wear_decal_marks

Família B; marcas planas de roda e arraste. Sem correntes/rings físicos. Aplicar0,20–0,40; não substituir piso existente.

### damp_anchor_runoff_decal_stains

Família C; impressões vazias de fixações, mineral/óleo/umidade. Usar0,15–0,30 sob apoios de borda; sem parafusos físicos ou água externa.

- `origin_left`: (340,218) px de fonte; offset do centro (-50.06,-37.47) px gameplay.
- `origin_middle`: (755,200) px de fonte; offset do centro (0.67,-39.67) px gameplay.
- `origin_right`: (1240,180) px de fonte; offset do centro (59.96,-42.11) px gameplay.

### tension_anchor_tower_margin

Torre estrutural média, menor que fornalha. Algemas abertas, base com dois blocos de apoio. Terminais W/E entregues com desnível~23px de mundo; compensar origem das correntes. Não assumir mesma altura só pelo prompt.

- `chain_w`: (140,412) px de fonte; offset do centro (-66.19,-63.35) px gameplay.
- `chain_e`: (899,540) px de fonte; offset do centro (68.86,-40.57) px gameplay.
- `chain_n`: (678,239) px de fonte; offset do centro (29.54,-94.13) px gameplay.

### chain_winch_station

Drum horizontal, catraca/trava e guias, diferente do capstan marítimo vertical. W/E quase nivelados. Pés/step junto ao chão; não criar novo guindaste.

- `chain_in_w`: (97,434) px de fonte; offset do centro (-71.38,-8.8) px gameplay.
- `chain_out_e`: (1425,432) px de fonte; offset do centro (71.17,-9.02) px gameplay.

### cargo_tiedown_platform

Deck estrutural com clamp/rings e centro livre; não é piso global. Cargas existentes pequenas sobre o centro; carrinho/guindaste ficam na lateral. Passarela reutilizada se liga a lugs W/E, não a anéis de carga.

- `dock_w`: (131,391) px de fonte; offset do centro (-104.54,-10.48) px gameplay.
- `dock_e`: (1568,391) px de fonte; offset do centro (104.54,-10.48) px gameplay.
- `tie_nw`: (562,218) px de fonte; offset do centro (-41.83,-35.65) px gameplay.
- `tie_ne`: (1135,218) px de fonte; offset do centro (41.54,-35.65) px gameplay.
- `tie_sw`: (562,489) px de fonte; offset do centro (-41.83,3.78) px gameplay.
- `tie_se`: (1135,489) px de fonte; offset do centro (41.54,3.78) px gameplay.
- `step_s`: (853,651) px de fonte; offset do centro (0.51,27.35) px gameplay.

### chain_routing_hub

Hub baixo com três guias fixados, sem insuladores/bateria/mastro. Linhas partem de terminais e percorrem rodas; não confundir com sinal elétrico.

- `chain_w`: (75,700) px de fonte; offset do centro (-57.67,13.2) px gameplay.
- `chain_e`: (1344,706) px de fonte; offset do centro (57.86,13.75) px gameplay.
- `chain_n`: (710,131) px de fonte; offset do centro (0.14,-38.6) px gameplay.

### technical_control_kiosk_complete

Posto técnico com sinal/controle e porta~24px, sem bancada de loja/forja. Socket W curto completo, sem cabo cortado. Entrada sul deve ficar livre.

- `service_w`: (220,633) px de fonte; offset do centro (-87.44,13.46) px gameplay.
- `door_s`: (750,930) px de fonte; offset do centro (8.31,67.12) px gameplay.

## Encaixe com peças existentes

- Contraforte: encaixar a chapa traseira contra a contenção real da borda; sapata sobre apoio firme. Suas duas algemas apontam a leste em alturas diferentes. A continuação das correntes nasce nesses pontos e termina em torre, plataforma ou ancoragem real, sem segmento solto. Não usar algema como apoio estrutural do piso.
- Torre:217px de altura visível na largura150px, abaixo do landmark de Forjas. Terminais W/E têm diferença aproximada23px de altura na imagem; corrigir origem/sag da corrente na implantação. O nome da variante `_aligned` representava tentativa, não garantia de resultado; usar somente `_margin`.
- Guincho: saída/entrada quase niveladas, corpo horizontal com trava e sprocket. O cabrestante de Docas permanece como amarração de barcos; não misturar essas funções nem gerar outro guindaste.
- Hub:125px de largura após QA, compacto e baixo; usar em bifurcação de tensão, não como poste elétrico. Nó de Cabos permanece para energia/mensagens.
- Plataforma: lugs W/E recebem extremidades de passarela de serviço reutilizada; os quatro anéis internos recebem carga. Centro visual útil aproximadamente90–120×35–40px, mais estreito que a meta130×65px do prompt. Usar pequenas caixas/carga sobre deck; carrinho existente e guindaste ao lado. Não tratar deck como novo chão global ou travessia principal.
- Algemas/aperturas dos prompts tinham meta comum13/6px. Projeção e tamanho entregue variam aproximadamente10–18px nos terminais; não há encaixe físico automático por nome. Ajustar pequeno overlap de pino/algema ou a linha de corrente no placement, mantendo origem/destino e luz; não espelhar/rotacionar câmera arbitrariamente.
- Quiosque: porta~24px, terminal W contido e controle exterior; entrada sul livre. Não é oficina de vendas nem segunda residência. Nenhum cabo cruza a borda do PNG selecionado.
- Decals: usar A reaproveitada de Forjas a0,10–0,20; B a0,20–0,40; C a0,15–0,30. Seleções contêm impressões/manchas, sem correntes/parafusos físicos. Exterior/gaps alpha0; regiões internas podem ter alpha alto, por isso a modulação é necessária. Não substituem a pedra receptora e não geram água/terreno de fundo.

## QA realizada

- `qa_gameplay_contact_sheet.png`: oito seleções em tamanho de mundo1:1, com comparações do capstan, mastro e landmark existentes, mais régua de porta24px. Funções/silhuetas novas são distintas.
- `qa_footprints_connections.png`: seis estruturas com áreas de apoio amarelas e origens de conexão ciano. Sapatas/blocos, pedestais, brace e acesso ficam visíveis; sombras locais e desgaste acompanham bases.
- `qa_decals_existing_stone.png`: original e três famílias sobre recorte intacto do benchmark, usando alpha0,15 /0,30 /0,25; pedra permanece legível. Este arquivo é QA, não piso de produção.
- `qa_metrics.json`: tamanho, alpha, recorte, margem, escala e footprint. Manifesto inclui hash para integrador conferir seleção.

Originais/variantes preservados, nenhum asset aprovado modificado. QA estático confirma sprites isolados, transparência real, recorte sem cortes visíveis e leitura em escala sugerida. Integração junto ao canal/terrain, continuação de correntes, conectividade da travessia e colisões dependem de placement e nova captura pela frente de cena. Não executamos Godot/import/runtime, não construímos mapa, não alteramos scripts ou cenas. Não avançar outras áreas automaticamente.
