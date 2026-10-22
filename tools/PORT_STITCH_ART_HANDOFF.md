# Costura portuária — handoff da frente de arte

Aplicados integralmente os papéis/reservas de `tools/CONSULTANT_PORT_STITCH_BRIEF.md`, `tools/PORT_STITCH_ART_REQUESTS.md` e `docs/superpowers/plans/2026-10-03-port-stitch.md`. Somente novos PNGs/manifestos/QA/documentação; nenhuma cena/import/Godot executado ou alterado. Uso de built-in image_gen (skill imagegen), sem edição determinística dos PNGs fonte. Área de trabalho autorizada é a retaguarda existente, não novo distrito ou entrada de Fundo-Ferro.

**Três novos selecionados**, justificados por diferença econômica/material/silhueta: oficina baixa de cordas/óleo, triagem molhada em dois bins baixos, inserto retangular de inspeção/drenagem.17 funções reaproveitáveis registradas. Não foram duplicados decks, escadas, rampas, guindastes, carrinhos, grandes galpões, abrigo/barcaça/cabrestante/berço Docas ou bocas arqueadas aprovadas.

## Caminhos e QA

- `assets/reconstruction/port_stitch/manifest.json`: medidas reais, SHA256, alpha/bbox/margens, escala uniforme, anchors e offsets, footboxes amostrais, inventário reutilizável e prompts/fontes.
- `assets/reconstruction/port_stitch/prompts.json`: prompts finais integrais e caminhos do gerador. Originais gerados permanecem preservados no destino default e copiados ao projeto.
- `assets/reconstruction/port_stitch/qa_gameplay_contacts.png`: objetos em tamanho de mundo1:1 sobre fundo claro, pontos cianos numerados/bases amarelas e régua24px. Não é panorama de cena.
- `assets/reconstruction/port_stitch/protected_hashes.json`: snapshot de137PNG anteriores, todos idênticos na verificação final; inclui artes/polimentos anteriores, sem arquivo de cena.
- `tools/qa_port_stitch_art.py`: reprodutor de metadados/previews, sem importar/executar motor.

| PNG | Canvas | Escala uniforme | Objeto visível mundo | Envelope seco aproximado mundo |
|---|---:|---:|---:|---:|
| rope_oil_service_shed.png |1492×1054|0,104391649|145×87,69px|138,84×19,83px|
| wet_sorting_lot.png |1536×1024|0,055762082|75×48,74px|74,83×24,70px|
| drain_inspection_module.png |1435×1096|0,067945643|85×62,37px|64,55×11,55px|

Envelope não é collider único aprovado: bases podem ser descontínuas e volumes/carga ampliam a ocupação. Footboxes amostrais no manifesto são estimadas visualmente ±10px nativos, não shapes certificados; o integrador verifica contato seco completo e ausência de interseção de rotas. Escala usa **bbox visível**, não largura inteira do canvas. Sprite centralizado sem pais transformados: ponto global = posição + (ponto nativo−canvas/2)×escala. Aplicar transformação completa em caso de pais/flip/rotação. Não esticar anisotropicamente nem espelhar luz para fabricar encaixe.

## Oficina baixa — serviço/almoxarifado

Arquivo `assets/reconstruction/port_stitch/rope_oil_service_shed.png`. Telhado simples de madeira/cobre, armário à esquerda, frente aberta central e bancada de enrolamento à direita; dois recipientes de óleo guardados, sem fornalha/chaminé/fachada residencial. Serviço ativo visível e silhueta145px baixa, menor que abrigo de triagem270px.

Anchors nativos: frente central(695,729), limiar do armário(280,803), carretel da bancada(1130,677). Vão aberto central~270px nativos→28,19px mundo; armário~180→18,79px, é armazenamento e não passagem pública24–28. Não colocar F/respawn dentro do shed. PNG não inclui piso caminhável no vão: alpha transparente deve revelar piso seco real, jamais água.

Quatro pés de pedra nativos94,768–193,821;383,796–486,854;866,850–971,901;1294,889–1419,946. Envelope de base resultou~139×20px, mais largo que meta110px do prompt; aplicar **medida entregue**, não assumir footprint110. O teto pode ocultar avatar, portanto oficina fora da via, com apron externo de trabalho, e bolso seco compatível. Candidatos do plano3280,610 /3090,925 /2840,1280 **não são placement aprovado**: usar somente onde a reserva real permita base+frente e corredor60px separado. Se não existir folga, não espremer o PNG no corredor; registrar bolso curto apoiado ou reter essa peça como alternativa até captura.

## Triagem molhada — carga baixa variada

Arquivo `assets/reconstruction/port_stitch/wet_sorting_lot.png`. Dois recipientes abertos pequenos: conexões de cobre/ferragens e madeira úmida amarrada, com bandeja de recolhimento, skids completos. Sem anel/sling, barril alto ou roda; distingue-se do bundle de carga volumosa110px já entregue. Bins~30–35px mundo, ligeiramente acima da meta24–30 no maior, legíveis ao lado do jogador. Não usar como pilha opaca gigante.

Anchors de função nativos: cobre(480,354), madeira(1120,578), bandeja(780,778). Bases120,560–230,632;516,711–638,779;949,783–1036,844;1168,867–1280,938. Envelope75×25px aproximado, altura da silhouette49px; nenhum chão embutido. Instalação sugerida no pátio2510,1505 somente após aferir folgas; frente abrigo2490,1440 e respawn2500,1575/via1575→1640 livres. Bandeja é objeto funcional, não decal de piso. Combinar com carrinho/bench existentes, evitar repetir o lote inteiro em fila.

## Inspeção/drenagem — encontro com margem existente

Arquivo `assets/reconstruction/port_stitch/drain_inspection_module.png`. Inserto curto de alvenaria com grelha retangular sul, tampa fechada de inspeção superior, volante ligado à caixa, entrada de tubo curva oeste e flange curto leste. Diferencia-se de `service_arch.png`; não cria boca jogável, camada, escada ou quarto acesso subterrâneo.

Sockets nativos: feed_w(125,180), outlet_e(1298,606), grate_s(652,739), parede norte(787,320), tampa(715,472). Flanges **não estão no mesmo y**: diferença426px nativos→28,95px mundo. São pequeno ramal~13–14px de diâmetro projetado, não encaixe direto de tubulação principal26px. Medir o eixo/diâmetro da face e usar conexão/redutor coerente existente ou trecho de cena apropriado, sem ligar centros do canvas. Se não houver tubo correspondente, tampão/fechamento físico ou outra escolha de placement é necessário; não deixar flange com linha terminando no ar. Não gerar mais conexões sem demanda concreta de captura.

Apoios nativos258,832–430,879;440,926–933,993;951,920–1172,1007. Inserir rear edge/jambs sobre retenção existente com overlap de alvenaria, com base seca real. Grelha inferior pode drenar para água/reentrância; não usar o sprite isolado no meio da rua ou pairando sobre a água. Não representa dreno com fluxo animado, fluxo sai da grelha somente se a cena construir destino físico coerente.

Bocas existentes permanecem nos pontosPocoVelho1296,1572 /DocaLeste2210,1668 /ForjasManutencao3000,260. Inspeção deve ficar ao lado no contexto técnico, **fora do raio75px de inputF**, sem cobrir escada/buraco/avatar ou mover marcadores. Carga vertical pode usar chain_winch/crane/guide existentes; esse catálogo não exige um novo guincho idêntico.

## Reuso por subárea

| Papel | Fonte existente/limite |
|---|---|
| Chegada rasa e margem/deck |stone_timber_threshold já aprovado na entrada2240,1370; preservar área x1985–2265/y1115–1520. Workyard_platform irregular e pier_head_deep fazem patamares/pilastras. Sem clone de entrada polida.|
| Triagem/carga |abrigo/barcaça/cabrestante/berço Docas, bundle slung, market_salvage_cart e maintenance_bench_cluster existentes; novo lote baixo traz outro tipo de mercadoria.|
| Serviço/almoxarifado |oficina nova baixa, banco manutenção existente, chain_winch onde tração for real, deck largo/apoios atuais sem torre nova.|
| Borda urbana |coastal_wall/retaining_edge/service_arch, novo inserto de drenagem, copper_elbow medido, limiar pedra/madeira atual. Pedras/pilhas têm reação física na margem, sem contato fictício.|
| Escadas/patamares/rampa |stair_fits/coastal_stone_stair e deck_timber_stair, docas_finish/naval_slipway e workyard_platform, pier_head_deep e main_deck_ew_wide. Não duplicar.|
| Progressão material |wet_wood_saltwear_decal alpha.20–.30 → damp_anchor_runoff_decal_stains alpha.25 → transition_soot_decal restrito no lado industrial. Preservar piso/juntas pintadas; marcas de roda existentes entre eles.|

Caminhos completos dos17 candidatos no manifesto. Respeitar mínimos existentes e reservas do plano:60px vias principais/44px secundárias quando aplicáveis sem reduzir larguras já maiores, raios75F e35R, chegada segura sobre piso opaco. Não considerar a área transparente de nenhum sprite como pintura transitável.

## Verificação e limites

Todos RGBA com alpha0, bboxes visíveis inteiros, margens mínimas50/69/85px. QA composto em fundo claro inspecionado: sem névoa visível; RGB invisível sob alpha0 não é background. Detalhes de uso/apoio/metal/madeira distinguem funções no tamanho de gameplay. Todos os anchors dentro do canvas.137hashes protegidos anteriores conferidos sem alteração. Sem variantes rejeitadas neste lote; fontes mantidas separadas dos assets aprovados.

Entrega pronta para seleção do implementador, **não aprovação da costura ou encaixe em cena**. Contato de margem/tubos, profundidade de apoios, circulação, sombra/occlusion, três acessos, palco econômico e leitura de panorama dependem das próximas capturas/validações da implantação. Só criar variante adicional se ganho visual concreto ou necessidade de encaixe exigir; catálogo não autoriza preenchimento automático de todos os vazios.
