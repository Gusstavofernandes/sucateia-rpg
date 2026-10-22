# Complemento de direção — Forjas Rasas

Fonte de requisitos: `tools/FORJAS_DIRECTION_AUDIT.md`, lido integralmente. PNGs novos somente em `assets/reconstruction/forjas_parallel/complement_v1/`. Produção built-in image_gen usando skill imagegen. Não substitui originais, não importa Godot, não edita cenas, scripts ou pisos. Cabos/Docas preservados.

## Escala conferida no integrador existente (somente leitura)

`tools/integrate_forjas_art.gd` aplica escala uniforme pelo menor limite, e não deformação para preencher o retângulo. Canvas efetivo da fornalha: 340×293px (limite340×345); forja aberta189×133; estoque minério/carrinho227×151; guindaste216×144; vaso de serviço189×126. Portas benchmark24–28px. O corpo visível da fornalha tem aproximadamente300px de largura. Valores de módulos novos são do objeto visível; margem alpha deve ser descontada ao escalar.

## Lote complementar produzido e selecionado por QA estático

1. Decals: transição de fuligem, derrame frio de escória, máscara de reflexo/calor sem pedras. Duas variantes de calor rejeitadas por conter terreno/alpha excessivo; seleção exige modulação de opacidade na cena.
2. Clusters: carvão com saída de alimentação, descarte de escória, tanque/canaleta de resfriamento, manutenção. Reutilizar estoque minério/carrinho/guindaste existentes.
3. Torre de exaustão add-on, tubo curto sustentado, passarela curta e braçadeira com suporte.
4. Oficina híbrida comercial de borda, apenas se distinta da forja aberta.

Blocos PRODUCTION CONSTRAINTS e MODULARITY integrais em todos os prompts. Luz difusa superior esquerda, câmera ortográfica elevada sul→norte benchmark; sombra de contato curta sob apoios reais, sem piso de fundo. Meta de margem10%; margem real e encaixes serão medidos no QA.

Este lote não aprova o setor. Identificação do landmark no panorama, transição de15–30% e conexões físicas precisam de avaliação após implantação pela frente de cena. Não são verificadas nesta frente sem runtime.


## Entrega selecionada: 13 módulos/decals

Cada prompt e fonte integral consta em `assets/reconstruction/forjas_parallel/complement_v1/manifest.json`; cada prompt contém PRODUCTION CONSTRAINTS e MODULARITY completos. Geração integrada image_gen, nenhuma CLI/API externa. Variantes não selecionadas em `variants.json` foram preservadas; não usar todas as variantes na cena.

| PNG selecionado | Canvas px | Objeto visível em mundo px | Escala uniforme do canvas | Alpha sugerido |
|---|---|---|---|---|
| transition_soot_decal.png | 1942×809 | 240×66 | 0.137378 | 0.3 |
| slag_spill_decal.png | 1568×1003 | 125×63 | 0.092115 | 1 |
| heat_reflection_mask.png | 1564×1006 | 140×83 | 0.107116 | 0.2 |
| coal_feed_cluster.png | 1547×1016 | 155×88 | 0.123114 | 1 |
| slag_discharge_cluster.png | 1536×1024 | 185×120 | 0.143745 | 1 |
| cooling_trough_cluster_complete.png | 1619×971 | 170×68 | 0.116438 | 1 |
| maintenance_bench_cluster.png | 1536×1024 | 145×79 | 0.105378 | 1 |
| exhaust_tower_addon.png | 1024×1536 | 184×321 | 0.222222 | 1 |
| supported_pipe_connector.png | 1870×841 | 100×36 | 0.072622 | 1 |
| short_service_catwalk.png | 1774×887 | 220×56 | 0.136986 | 1 |
| pipe_saddle_support_single_ns.png | 1102×1427 | 35×35 | 0.057003 | 1 |
| market_forge_transition_shop.png | 1511×1041 | 275×158 | 0.204309 | 1 |
| exhaust_reducer_connector.png | 1415×1111 | 70×47 | 0.056406 | 1 |

A escala usa bbox com alpha >16, não o canvas inteiro. Meta dos prompts: margem10%; resultados têm margem visível mínima de43–196px, nem todos atingem10% proporcional. Todos os recortes visíveis selecionados ficam dentro do canvas; o tanque inicial cortado não foi selecionado. Não recortar pelo primeiro pixel de alpha1/255: existem resíduos quase invisíveis externos, preservados na saída original.

## Encaixes e implantação

Coordenadas nativas aproximadas, top-left do PNG como origem, com estimativa visual±10px de fonte. O JSON também fornece coordenadas normalizadas e deslocamento em mundo a partir do centro do canvas na escala sugerida. `qa_connection_points.png` marca as bocas/lugs; são guias de encaixe, não certificado de runtime. Para Sprite2D centrado: centro de porto = posição + (porto nativo − metade canvas) × escala. Corrigir a posição para sobrepor colares6–8px e conferir diferença de altura, sem espelhar a luz.

### transition_soot_decal

Faixa de poeira/fuligem com roda; concentrar leste, diluir oeste. Opacidade inicial0,25–0,35 para mostrar pedra existente.

### slag_spill_decal

Derrame frio compacto; partículas e contato, sem chapa de terreno. Usar junto ao descarte, não aleatoriamente.

### heat_reflection_mask

Máscara sem pedras; alpha de origem excede meta. Usar opacidade0,15–0,25 (preview0,20), sem blend aditivo obrigatório. Variantes scorch rejeitadas.

### coal_feed_cluster

Carvão separado do minério. Saída E com diâmetro final aproximado22px; acesso sul livre.

- `fuel_out_e`: (1440,517) fonte; offset do centro (82.06,1.11) px de mundo; diâmetro/borda aproximado22px.

### slag_discharge_cluster

Bandejas/escória em fila; flange NW20px na largura185px. Conexão por canaleta/redução, não forçar flange22px sem conferir.

- `slag_in_nw`: (142,177) fonte; offset do centro (-89.98,-48.15) px de mundo; diâmetro/borda aproximado20px.

### cooling_trough_cluster_complete

Ponta E recuperada. Água apenas dentro do tanque/canaleta. Canaleta SW é borda aberta, não flange circular.

- `water_in_e`: (1514,414) fonte; offset do centro (82.03,-8.33) px de mundo; diâmetro/borda aproximado22px.
- `return_trough_sw`: (155,693) fonte; offset do centro (-76.21,24.16) px de mundo; diâmetro/borda aproximado18px.

### maintenance_bench_cluster

Manutenção com peças/óleo/placas; sem bigorna/fogo para não duplicar forja aberta. Trilho é fixação, não porta de fluxo.

- `mount_rail_e`: (1438,675) fonte; offset do centro (70.6,17.18) px de mundo; diâmetro/borda aproximado20px.

### exhaust_tower_addon

Altura visível~320px; largura184px. W aberto; E tampado. Flanges não estão na mesma linha: compensar offsets, nunca espelhar luz.

- `exhaust_in_w`: (171,1156) fonte; offset do centro (-75.78,86.22) px de mundo; diâmetro/borda aproximado40px.
- `capped_return_e`: (891,1230) fonte; offset do centro (84.22,102.67) px de mundo; diâmetro/borda aproximado40px.

### supported_pipe_connector

Tubo horizontal com suportes próprios, corpo14px e flanges~24px. Não girar arbitrariamente; junta deve ocultar colar8px.

- `pipe_w`: (316,404) fonte; offset do centro (-44.95,-1.2) px de mundo; diâmetro/borda aproximado24px.
- `pipe_e`: (1551,404) fonte; offset do centro (44.73,-1.2) px de mundo; diâmetro/borda aproximado24px.

### short_service_catwalk

Largura revista120→220px para superfície caminhável~30px, compatível porta24px. Encaixes retos com pares de furos; não usar escala inicial pequena.

- `dock_w`: (122,456) fonte; offset do centro (-104.79,1.71) px de mundo; diâmetro/borda aproximado32px.
- `dock_e`: (1655,456) fonte; offset do centro (105.21,1.71) px de mundo; diâmetro/borda aproximado32px.

### pipe_saddle_support_single_ns

Resultado visual abre em U para sul/norte, apesar do pedido E–W. Liberado como suporte auxiliar N–S; NÃO snap direto no conector E–W. Este já inclui suportes compatíveis.

- `saddle_bore_ns`: (552,560) fonte; offset do centro (0.06,-8.75) px de mundo; diâmetro/borda aproximado18px.

### market_forge_transition_shop

Largura revista225→275px para porta~24px e balcão legível; cliente sul, serviço E. Não duplicar forja artesanal.

- `shop_service_e`: (1424,542) fonte; offset do centro (136.58,4.39) px de mundo; diâmetro/borda aproximado24px.

### exhaust_reducer_connector

Redução real~26→44px; ajustar largura64–70px para boca maior40–44px. Leve deslocamento vertical3px entre centros, compensar no encaixe.

- `reducer_small_w`: (220,543) fonte; offset do centro (-27.5,-0.71) px de mundo; diâmetro/borda aproximado26px.
- `reducer_large_e`: (1280,598) fonte; offset do centro (32.29,2.4) px de mundo; diâmetro/borda aproximado44px.

## Observações de compatibilidade

- A torre complementa o landmark, não substitui o corpo da fornalha. Altura visível321px supera a chaminé no sprite existente. Colocar atrás/norte-leste do corpo para manter boca de fogo e circulação legíveis; apoio deve tocar o mesmo terreno.
- A fornalha original mostra dutos já fechados/conectados, não oferece uma flange aberta certificada. Encaixe precisa de sobreposição de colar sobre um segmento/junta do duto traseiro, coberto pelo redutor; não tratar arbitrariamente um tubo fechado como boca aberta. O encaixe final depende do placement e deve ser conferido em captura próxima. Nenhum pixel do original foi alterado.
- Redutor entregue tem boca menor~26px e maior40–44px conforme escala64–70px de largura; torre tem entrada~40px. Não ligar o conector24px diretamente à torre40px. O conector24px casa melhor com serviço, carvão, tanque e oficina, admitindo pequeno ajuste de escala e sobreposição de collar.
- Torre possui offsets verticais diferentes entre bocas; saída leste está tampada. Não desenhar linha de fluxo para tampa sem uma substituição visual deliberada.
- Suporte avulso foi pedido E–W, mas entregue com U aberto sul/norte. Nome selecionado descreve a orientação real: `pipe_saddle_support_single_ns.png`. Serve em derivação N–S; não é encaixe direto certificado com o conector E–W. O próprio conector E–W já contém abraçadeiras e apoios corretos.
- Oficina e passarela tiveram largura sugerida revista após QA:275px para porta~24px;220px para passagem~30px. Não aceitar225/120px só por terem aparecido no prompt.
- Máscara de calor saiu com alpha máximo253, acima da meta90 do prompt. É uma máscara de cor sem pedras, utilizável com modulação0,15–0,25; a composição QA usa0,20. Não implantar opacidade1. Variantes anteriores com pedra pintada/calor excessivo foram rejeitadas.
- Fuligem é depósito de pó, não piso substituto; usar0,25–0,35 e preservar a pedra receptora. Cobertura15–30% do setor é decisão de composição do integrador, não preencher área inteira com um único decal.

## QA e limites da entrega

- `qa_gameplay_contact_sheet.png`: sprites em escala gameplay1:1, com a fornalha existente no mesmo tamanho e régua de porta24px. Mostra funções distintas e silhuetas legíveis.
- `qa_connection_points.png`: dez painéis com marcas nativas aproximadas, inclusive redutor.
- `qa_decals_on_existing_stone.png`: composição de teste sobre recorte intacto do benchmark; original, fuligem0,30, escória1, calor0,20. Pedra permanece legível.
- `qa_metrics.json`: dimensões, bbox visível, margem, alpha, transparência, escala. `manifest.json` adiciona hashes SHA256, prompts e fontes.

Só os PNGs e documentação foram produzidos. Não foram executados import/runtime/Godot ou modificados scripts/cenas/pisos. Os originais Forjas e os lotes Cabos/Docas foram preservados. Teste próximo/médio/desde Mercado, pátios ocupados, conexão física e leitura do panorama continuam como critérios de integração da auditoria; este lote não declara o setor aprovado.
