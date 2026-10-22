# Costura Docas → cidade/indústria

Implantação concluída, verificada e aprovada consultivamente com observações não bloqueantes (CONSULTANT_PORT_STITCH_FINAL.md,03/10/2026,20:27). Não declara toda Ferrugem Baixa concluída. Fundo/Coroa ainda não iniciados nesta etapa. Cena contínua existente, mesmo jogador, áreas/arte/costa aprovadas preservadas.

Cinco funções econômicas articuladas: espera de carga com carrinho2415,1528; triagem em bins de cobre/madeira2594,1552 diante do abrigo; almoxarifado/oficina de cordas e óleo2983,832; inspeção/drenagem na margem norte do canal3122,85, conectada ao coletor3020,-45 e à descarga3222,138; guincho de serviço1408,1480 ligado à alvenaria do Poço. As três bocasF existentes mantêm coordenadas e funções aprovadas; não há novo portal/camada.

Única extensão: bolso curto sustentado por pilastras/estacas do PNG workyard_platform existente, centro2983,874, contorno conservador~231x115px. Conectado ao corredor lateral na junta3090,925. Não ocupa a faixa vertical60px, não cria ilha nem massa de terra. Todos os polígonos antigos permanecem intactos; somente um apêndice de piso. Seis shapes antigos preservados são desativados em runtime só na emenda coberta, substituídos por trechos externos/guardas novas de união. Teste físico impede saída para água.

Arte: três novos PNGs do gerador integrados em escala uniforme medida pelo bbox visível, com bases reais/sombra curta e profundidade pelos pés. Carrinho e guincho reaproveitados em escala coerente, abrigo/cabrestante/barcaça/berço/luzes/decks/entrada polida preservados.137 fontes anteriores SHA256 idênticas. Fundo-Ferro byte-idêntico ao checkpoint técnico anterior.

Correções motivadas por evidência: carrinho inicialmente grande e oculto pelo abrigo → escala.08 e frente esquerda; lotes baixos → frente direita. Dreno sobre canal → margem norte seca e ramal com terminais contíguos. Oficina estreitava a faixa vertical apesar de percurso alternativo possível → bolso e shed107px oeste. TestesRED→GREEN preservados no registro. Critério de corredor é largura integral anterior, não mera possibilidade de atravessar por desvio.

Nove testes finais PASS, exit0, semERROR: port_stitch_contacts, port_stitch, docas_contacts, docas_routes, fundo_access, port_approach, docas_preservation, forjas_functional_modules, slice.80 amostras novas de apoio seco/pintado; discos75F/35R e retângulos das17 rotas livres de novos pés.A contagem final de centros portuários é2862 em fundo_test_docas_contacts.log. Ida/volta física de funções/17rotas/3F/6R, F/R efetivos nos regressivos. Comparação preserva todos os nós anteriores e a única adição autorizada à lista de pisos.

Cinco capturas finais, mesma árvore5803 nós; frames80, custo de desenho anotado, não benchmark de FPS:
- maps/sucateia/preview_stitch_overview.png — panorama contínuo,555drawcalls.
- maps/sucateia/preview_stitch_sorting.png — chegada/triagem,152.
- maps/sucateia/preview_stitch_service.png — oficina em bolso apoiado e corredor livre,17.
- maps/sucateia/preview_stitch_urban.png — dreno e transição industrial,103.
- maps/sucateia/preview_stitch_mouths.png — serviço do Poço/acesso inferior,275.

Métricas/hashes: tools/port_stitch_metrics.json. Checkpoint local tools/checkpoints/sucateia_port_stitch_verificada.zip, CRC verificado e dependências da cena incluídas. ZIP não será enviado, conforme preferência humana. Checkpoint Docas aprovado anterior intacto.

Revisão independente em PORT_STITCH_REVIEW.md; parecer em CONSULTANT_PORT_STITCH_FINAL.md. Etapa encerrada; microdesgaste/umidade/VFX opcionais não reabrem escopo. Checkpoint histórico aprovado preservado, sem reempacotamento. Próxima etapa: acabamento visual do Fundo-Ferro existente; levantamento em FUNDO_FINISH_BASELINE.md. Ferrugem inteira e regiões posteriores continuam pendentes. Supervisão coordena consulta e poucas capturas ao WhatsApp conforme autorização humana.
