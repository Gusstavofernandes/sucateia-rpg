# Os Cabos — entrega para avaliação consultiva

Camada elevada construída na cidade existente, sobre o encontro Mercado/Alto-Lixo/oeste de Forjas. Não criou mapa, chão ou ilha; pátios industriais/Amarras preservados.

Três acessos F bidirecionais com duas escadas visíveis cada: Alto(-400,-780), Mercado(744,-504), Forjas(1900,108). Chegada elevada212px ao norte, patamares amplos e R seguro por camada. Jogador único, máscara4 elevada/1 superfície. F para Fundo-Ferro fica restrito ao chão. Retorno restaura respawn anterior.

Via principal larga E–O, circuito alternativo com ponte estreita, ramal do Mercado em T e varanda da casa.16 trechos de rota física,14 patamares/soleiras,32 módulos de piso+11 patamares pintados,6 escadas, ponte e T.27 apoios com colisão de chão, recepção estrutural/cabos; dois apoios altos sustentam a casa até a rua. Apoios novos desviados das duas passagens antigas que a regressão detectou.

Cinco PNGs gerados selecionados, sem editar fontes: casa0,28, ponte0,26, T0,38, mastro0,16, deck novo0,1411161. Principal72px úteis sobre75,5px pintados; N–S60px, ponte28px, T32/36px. Todos os105 hashes de arte protegida e o terreno/arquitetura anteriores devem ser conferidos pelo finalizer. Fundo-Ferro permanece byte a byte no baseline anterior.

20 testes distintos PASS na execução completa final. Testes de camada/rotas/arte/preservação revalidados após os últimos ajustes visuais.3458 centros elevados seguros auditados contra pisoPNG real; bases físicas27/27. Revisão independente: doisP2 corrigidos, nenhumP1/P2 restante.

Capturas finais em maps/sucateia/preview_cabos_{full,district,market,alto,forjas,junction,underpass}.png. Panorama mostra continuidade regional; três acessos, T/casa/apoios e circulação inferior estão disponíveis para inspeção. Avatar de baixo tem fade localizado e readout visual do mesmo sprite, sem mudar casas antigas.

Checkpoint: tools/checkpoints/sucateia_cabos_integrada.zip, criado/verificado por tools/finalize_cabos.py. Métricas: tools/cabos_metrics.json. Estado: implementação/verificação independente pronta; aguarda parecer visual consultivo. Não iniciar Docas ou outro setor antes desse parecer.
