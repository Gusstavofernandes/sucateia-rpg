# Fundo-Ferro existente — baseline de acabamento

Levantamento somente de leitura em04/10/2026, antes do novo brief consultivo. Nenhuma cena, runtime, PNG fonte, import ou colisão alterada; Godot não executado. Costura portuária anterior aprovada em CONSULTANT_PORT_STITCH_FINAL.md, encerrada e preservada. Ferrugem Baixa inteira continua incompleta; esta etapa trata apenas a camada subterrânea existente, não outro Fundo.

Fonte real: maps/fundo_ferro/fundo_ferro.tscn, ligada à cidade atual por LayerTravel. SHA2569793456d07a420d3dcc8114dff367b0a301e87df6f8d4fef478f0a3afe10d083, byte-idêntica a tools/checkpoints/fundo_before_functional_finish.tscn. Evidência estática reproduzível: tools/audit_fundo_finish_baseline.py → tools/fundo_finish_baseline_evidence.json (hashes de duas cenas/runtime/texturas/capturas, nós, coordenadas e rotas reais).

## Sete salas existentes e papel regional

| Sala / centro real | Função / continuidade | Constatação nas capturas existentes |
|---|---|---|
| Poço Velho1296,1572 | Chegada do núcleo costeiro, cisterna de recalque; caminho para Bombas e Ruínas. | Landmark cisterna legível e escadaF presente. Canos curtos soltos, encontro cisterna/rede pouco claro. |
| Bombas1750,2000 | Refluxo/hidráulica entre Poço, Descarte e duas bacias. | Bomba tem base reconhecível. Tubos isolados ao redor; bacias retangulares sem leitura forte de entrada/saída e umidade. |
| Descarte2300,2180 | Triagem inferior ligada às Docas; circuito Bombas→Máquinas e travessa para Ruínas. | Recicladora no canto e pequenos montes soltos. Falta organização visual de coleta/triagem e bancada; chão igual ao resto. |
| Máquinas2900,1770 | Motor industrial abandonado, ligação Descarte→Reservatório. | Motor é landmark forte a preservar. Grande apron neutro; terminais não estão ligados a uma rede funcional visível. |
| Reservatório2700,1240 | Reserva/limo entre Máquinas, Ruínas e Galeria das Válvulas. | Duas bacias e ponte definem o lugar; margens muito retas, canos com finais livres e pouca diferença de umidade. |
| Ruínas1750,1050 | Fundação antiga no circuito de retorno ao Poço e travessa dos drenos. | Um motor/fundação parcialmente arruinado, mas pouca camada de colapso estrutural; mesma parede repetida e piso uniforme. |
| Válvulas3000,570 | Manutenção sob Forjas, controle da rede e término da galeria. | Reator arcano oferece landmark; função de válvulas ainda pouco explícita sem manifold/tubos conectados. Grande piso neutro. |

Correção de referência: tools/fundo_spatial_plan.json ainda guarda centros de intenção Reservatório2700,1160 e Válvulas3100,640. **Usar coordenadas da cena acima**; não mover salas para coincidir com a planta histórica. Dimensões da planta são intenções do builder, não polígonos finais certificados.

## Oito rotas a preservar

Circuito principal: PocoBombas → BombasDescarte → DescarteMaquinas → MaquinasReservatorio → ReservatorioRuinas → RuinasPoco. Ligação secundária TravessaDosDrenos: Descarte2300,2180 →2210,1840→2100,1470→1970,1250→Ruínas1750,1050. GaleriaDasValvulas: Reservatório2700,1240→2660,1250→2660,1030→3000,940→3000,570→3000,480. Todos os vértices reais registrados no JSON de evidência; não reconstruir circuito ou compactar salas.

Duas pontes existentes, PNG infrastructure/walkway.png: centro1820,2100, canvas projetado97x139, trecho físico historicamente testado1820,2025↔1820,2170; centro2660,1127, canvas97x148, trecho2660,1030↔2660,1220. Mantêm quatro porções de água bloqueada: x1680–1776 e1864–1960/y2070–2132; x2540–2617 e2703–2818/y1090–1162. Não tratar água como vazio a preencher. Larguras/apoios/pintura útil reais das pontes precisam de auditoria de contato posterior, sem inferir área livre pelo canvas.

## Três acessos F pareados

| ID | Superfície atual | Subsolo / chegada / retorno | Papel |
|---|---|---|---|
| PocoVelho |1296,1572|1296,1572|Cisterna/carga e serviço sob núcleo urbano costeiro.|
| DocaLeste |2210,1668|2250,2200|Docas→triagem/descarte inferior.|
| ForjasManutencao |3000,260|3000,480|Indústria→Válvulas/galeria técnica.|

LayerTravel contém somente os dois caminhos atuais e os três IDs acima, valida proximidade52px, impede uso na camadaCabos e retorna ao mesmo ID. R usa spawn da chegada; um jogador por cena. Os pares não têm igualdade espacial obrigatória entre camadas; não são teletransportes para distritos isolados. Preservar piso opaco, avatar visível, saídas claras e bolsos seguros durante acabamento.

## Capturas disponíveis, validade e seleção para consulta

Inspecionadas as oito imagens em maps/fundo_ferro/preview_fundo_{full,PocoVelho,Bombas,Descarte,Maquinas,Reservatorio,Ruinas,Valvulas}.png. Representam a primeira etapa salva; são **capturas existentes, não renders novos**. A cena inferior é idêntica à baseline, portanto são referência espacial válida; shaders/runtime compartilhados podem influenciar futuros renders. Mtimes/SHA256 de cada arquivo no JSON, sem afirmar atualidade de render não verificada.

Inspecionadas também as três antigas maps/sucateia/preview_fundo_surface_{PocoVelho,DocaLeste,ForjasManutencao}.png. **Contexto superficial histórico**: precedem refinamentos posteriores de Docas/entrada e costura. Não enviar como imagens da cidade atual. Complementos atuais disponíveis: preview_stitch_mouths.png (Poço/guincho), preview_stitch_urban.png (canal/manutenção), preview_stitch_overview.png e preview_port_approach.png. Nenhum substitui nova captura F localizada quando a etapa de execução for autorizada.

Para consulta visual inicial: panorama fundo_full e detalhes Bombas, Descarte, Reservatório, Ruínas, Válvulas; motor e cisterna atuais como referências a preservar. Necessidade de seleção menor depende da interface do consultor. Não enviar captura histórica de superfície como prova atual.

## Assets reaproveitáveis e pendentes

Já usados e a preservar como ponto de partida: fundo_wall.png (módulo de parede), fundo_abandoned_engine.png, alto_cistern.png, region/pump_station.png, generated/structures/reactor.png, forjas_recycler.png, region/ruined_engine.png, infrastructure/{walkway,retaining_edge,channel,stairs,scrap,lantern}.png e terreno/{foundation,metal_repair,market_dirt,oil_hatch}.png. Texturas/fontes SHA registradas.328 sprites do mesmo módulo de parede explicam a repetição observada; variar somente encontros/cantos/reforços com função.

Disponíveis mas **não integrados**: fundo_sorting_bank.png (bancada baixa com três lotes e peneira) e fundo_collapsed_corner.png (alvenaria/girder de colapso com canto aberto). Ambos inspecionados; prompts/fontes em fundo_pending_finish_art.json. Podem distinguir Descarte/Ruínas após aferir escala uniforme, footprint seco, sockets e margens reais. Nenhum anchor/colisão desses arquivos está certificado. Banco apresenta margem de extração muito apertada no lado direito; esquina tem luz própria e volume diferentes a conferir no zoom de gameplay. Não consumir automaticamente os dois só porque existem.

Reuso do catálogo novo da superfície condicionado a câmera/material/escala: utility_fits/copper_elbow.png e generated/props/pipe.png para redes com terminais medidos; forjas_parallel/complement_v1/maintenance_bench_cluster.png para serviço; docas_finish/workyard_platform.png ou stair_fits/deck_timber_stair.png somente onde houver travessia/patamar real; port_stitch/drain_inspection_module.png apenas em parede com descarga/inspeção concreta. Contato úmido dos decals Docas/Amarras pode servir pedra/metal compatíveis com alpha baixo, sem cobrir piso ou inventar bolsões. Estas são opções de catálogo, não placements autorizados.

## Problemas comprováveis e prioridades de acabamento

1. Redes: fragmentos de tubos por todos os corredores sem origem/destino contínuos. Identificar sockets reais de cisterna/bomba/motor/controle e entrada/saída de bacias antes de gerar conectores. Rede deve atravessar fronteiras de salas acompanhando usos de Poço/Docas/Forjas.
2. Piso: mesmos padrões de pedra/emblemas em todas as salas; manchas e remendos espalhados não distinguem trabalho molhado, triagem, manutenção ou ruína. Variação localizada por uso, corredor legível e transições graduais, preservando células/rotas.
3. Contenções: muitas bordas de escavação seguem degraus de tile e repetem o mesmo bloco328 vezes. Precisa mostrar espessura, juntas, escoras e rocha aderida nos encontros; não alargar toda planta nem substituí-la por arena.
4. Água/ponte: quatro retângulos muito escuros e separação seca/úmida pouco clara. Melhorar contenção, grime/limo, descarga e contato da água; bases de ponte e patamares reais a medir. Física existente não é prova de apoio visual certificado.
5. Função: Descarte precisa de triagem reconhecível e Ruínas de colapso estrutural; Válvulas precisa comunicar controle hidráulico, sem duplicar um reator solto. Cisterna/motor/bomba já são landmarks úteis.
6. Entradas: escadasF legíveis, porém encontros superiores/inferiores pouco explicados visualmente. Conservar pares e spawn; aferir pintura/opacidade/contatos antes de pequenos encaixes. Não há defeito físico novo demonstrado nesta leitura.

Escalas e contatos a aferir: a cisterna usa fatores.12947/.15109 e o motor.22786/.23340; há anisotropia herdada, não justificativa automática para substituir arte. Colisões das seis máquinas foram aprovadas por pontos blocked_base, não por perímetro inteiro dos pés PNG nem sockets reais. Auditoria futura deve medir suporte, profundidade dos pés, tubos e F/R completos.

## Evidência técnica e limites

Logs existentes test_fundo_layout/test_fundo_access preservam sete salas/oito rotas/duas pontes/seis bases/água e F/R efetivos. test_fundo_access foi novamente aprovado durante a costura; layout é evidência anterior, não foi reexecutado agora.824 células de piso vêm da auditoria histórica FUNDO_FERRO_AUDIT.md, não contagem recomposta neste levantamento. Sem NPC/combat/economia/interiores novos.

tools/finish_fundo_functions.gd e fundo_functional_ground.gdshader continuam pendentes. A cena NÃO contém FunctionalGroundFinish/FunctionalRoomMargins nem os dois PNGs pendentes. O builder antigo coloca a instância dentro de SceneTree ao salvar, remove fragmentos, usa escalas XY e pontos de rede genéricos sem socket certificado: **não executar por replay**; retomar com novo brief/plano, baseline preservada e builder de empacotamento seguro fora da árvore. Não se afirma erro runtime, pois não foi executado nesta etapa.

Próximo passo é brief consultivo visual sobre acabamento desta camada existente. Implementação, novas imagens, import, testes e capturas aguardam essa sequência da supervisão. Não iniciar outro Fundo/Coroa/Khemet-Ra nem considerar os setores macro externos dispensados.
