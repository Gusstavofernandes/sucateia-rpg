# Ferrugem Baixa — reconstrução sobre o original

## Direção vigente
Somente o mapa inicial é benchmark visual. O mapa jogável é maps/sucateia/sucateia.tscn, preservando a base em tools/checkpoints/sucateia_before_world_extension.tscn. Os 16 mapas noturnos são rascunhos de função, posição e conexões; não representam distritos finais. A montagem conjunta foi suspensa e isolada em tools/experiments/assembly/.gdignore. O relatório anterior é histórico: tools/checkpoints/REGION_STATUS_before_reconstruction.md.

## Mercado dos Restos — etapa revisada
Extensão comercial diretamente na mesma cena do original, com casas, oficina, reator e barracas aprovados preservados. Rua dos Catadores, Praça das Trocas com pavilhão focal, núcleos de ferragens/tecidos/lotes, atacado coberto, estoque, três becos e fachadas escalonadas organizam a circulação. Fundos irregulares substituem a moldura técnica; cabos e arquitetura continuam além das bordas. Nenhuma cena noturna incorporada; E não troca de cena.

Benchmark: tools/checkpoints/original_visual_benchmark.png. Capturas atuais: maps/sucateia/preview_market_full.png e preview_market_plaza.png. Piso e tamanho do Mercado preservados por hash da baseline anterior à reorganização.

Avaliação visual em tools/MARKET_URBAN_AUDIT.md: distrito comercial conectado ao original, com coração reconhecível, circulação e núcleos de uso. A cidade ainda precisa de largura regional; o próximo bairro ocupará oeste/noroeste. Não há pretensão de que toda Ferrugem Baixa esteja pronta.

## Alto-Lixo — acabamento revisado
Planta histórica: docs/alto-lixo-planta-espacial.svg e tools/alto_lixo_spatial_plan.json. Continuação após revisão da costa e autorização humana de coordenação verificada no chat de supervisão. Acabamento aplicado incrementalmente sobre a cena atual: 27 moradias (22 anteriores preservadas e cinco complementares), cisterna comunitária sobre patamar, quatro plataformas pintadas, apoios, calhas, portas reparadas, lanternas e cabos. Nenhuma expansão de piso/território e nenhuma regeneração do núcleo.

Dez destinos, seis vias/becos e quatro escadas passaram em ida/volta física. tests/test_alto_refinement.gd confirma três pisos idênticos, moradias anteriores e contorno/barreiras da costa preservados. Regressões atuais de costa, Mercado e original/spawn/controles passaram. Capturas: preview_alto_full.png, preview_alto_court.png, preview_alto_frontier.png e preview_alto_northwest.png. Auditoria: tools/ALTO_RESIDENTIAL_AUDIT.md. Checkpoint: tools/checkpoints/sucateia_alto_lixo_acabamento.zip.

Estado: acabamento visual e circulação desta etapa concluídos. Elevação continua visual; interiores, NPCs e destinos externos não foram implementados. A antiga reserva a leste/nordeste recebeu a primeira implantação de Forjas Rasas. Ferrugem Baixa e as demais regiões ainda estão incompletas.

## Forjas Rasas — primeira implantação exterior

Continuação a leste/nordeste na mesma cena atual, a partir do checkpoint posterior ao acabamento de Alto-Lixo. Duas conexões com o Mercado, oito vias/becos, cinco pátios de trabalho, 14 oficinas/galpões, duas fundições e três recicladores. Canal irregular com três trechos de água bloqueados e duas pontes. 1590 células novas em piso próprio, mesma escala do original; nenhum piso ou posição aprovado foi alterado.

Três módulos gerados por imagem com benchmark exclusivo do mapa original: oficina, prensa e galpão de caldeiras. Prompts e proveniência em tools/forjas_art_manifest.json e tools/forjas_boiler_prompt.json. Planta em docs/forjas-rasas-planta-espacial.svg e tools/forjas_spatial_plan.json. Auditoria em tools/FORJAS_RASAS_AUDIT.md.

Validação final sequencial: oito testes passaram, incluindo dez destinos de Forjas com ida/volta, todos os trechos das oito vias, duas pontes, 19 bases industriais, ordenação com o jogador, preservação de todos os nós antigos e regressões de Alto-Lixo, costa, Mercado e spawn/controles. Capturas finais: preview_forjas_full.png, preview_forjas_district.png, preview_forjas_frontier.png, preview_forjas_foundry.png, preview_forjas_recycling.png e preview_forjas_drain.png. Panorama 1773 draw calls; distrito 450; detalhes 144–196; 3238 nós. São amostras de captura, não benchmark prolongado de FPS.

Revisão independente parcial identificou ordenação de arquitetura, corrigida na cena atual sem reconstrução; teste RED→GREEN. O agente encerrou por limite de uso antes do relatório completo; composição final e preservação restantes revisadas pelo autor. Erros transitórios de memória durante execução concorrente foram resolvidos repetindo sequencialmente testes e capturas.

Estado: primeira etapa exterior visual/navegável validada. Elevação visual, interiores/NPCs/simulação industrial pendentes; economia e combate não alterados. Saídas para Chaminés Velhas, Grande Ferrugem e manutenção/Fundo-Ferro são apenas aproximações reservadas. Não avançar para outra área antes da revisão da supervisão. Checkpoint: tools/checkpoints/sucateia_forjas_rasas_primeira_etapa.zip.

## Costa inferior — etapa aprovada e preservada
Retrabalho estrutural concluído somente na massa inferior: canto sudoeste recuado, entradas de água no sul, recuo no cais sudeste, saída industrial aberta e três docas anexadas ao solo com escadas e suportes. Núcleo, faixa de transição, costa de manutenção e estruturas sobre a água possuem leitura distinta. Água, chão e colisão compartilham o novo contorno.

Capturas atuais: maps/sucateia/preview_lower_coast.png e preview_lower_detail.png. Avaliação em tools/LOWER_COAST_AUDIT.md: a silhueta externa deixou de ser um bloco retangular; água entre os ressaltes e docas dá leitura costeira por camadas. Piso do Mercado, piso do Alto-Lixo, terreno original acima de y=1170 e todas as 16 posições arquitetônicas originais preservados. Cinco assets aprovados inalterados por SHA-256.

Validação atual: seis destinos costeiros com ida/volta, cinco amostras de água bloqueadas, nove percursos originais e oito destinos/três becos do Mercado. A conexão com Fundo-Ferro e a passagem da bomba foram corrigidas depois das primeiras falhas. Checkpoint histórico: tools/checkpoints/sucateia_costa_inferior_retrabalhada.zip. tools/rework_lower_coast.gd está protegido contra replay da base antiga depois do acabamento de Alto-Lixo; futuras edições costeiras devem partir da cena atual. Não executar geradores históricos para restaurar o retângulo.

## Ordem / estado
| Ordem | Setor | Estado |
|---|---|---|
| 1 | Mercado dos Restos | Estrutura urbana reorganizada e validada |
| 2 | Alto-Lixo | Acabamento visual e circulação desta etapa concluídos; interiores/NPCs pendentes |
| 3 | Forjas Rasas | Primeira implantação exterior e circulação validadas; interiores/NPCs pendentes |
| 4 | Fundo-Ferro | Navegação validada; acabamento visual adicional solicitado e interrompido pela prioridade Forjas |
| 5 | Os Cabos | Pendente |
| 6 | Docas | Pendente |
| 7 | Coroa de Lata | Pendente |
| 8 | Chaminés Velhas | Pendente |
| 9 | Passagem das Amarras | Pendente |
| 10 | Galerias do Poço Velho | Pendente |
| 11 | A Grande Ferrugem | Pendente |
| 12 | Banco de Destroços | Pendente |
| 13 | Estrada dos Rebitadores | Pendente |
| 14 | Engrenópolis — Pátio das Transmissões | Pendente |
| 15 | Engrenópolis — Vielas dos Artífices | Pendente |
| 16 | Engrenópolis — Corredor das Caldeiras | Pendente |

## Verificação desta etapa
- tests/test_slice.gd: nove percursos do original, travessia física, spawn, colisões, WASD, Shift e R.
- tests/test_original_rebuild.gd: um personagem, nenhuma montagem de mapas noturnos, nenhuma passagem trocando cena, transparência do novo asset.
- tests/test_market_expansion.gd: oito destinos com ida/volta física, incluindo a saída oeste do Alto-Lixo, e todos os trechos dos três becos.
- Capturas anteriores da etapa do Mercado: praça 150 draw calls; geral 932; 1534 nós. Não é benchmark prolongado de FPS.
- Cinco assets aprovados protegidos por SHA-256; MarketFloor idêntico à baseline anterior à reorganização.
- Relatórios e testes das 54 trocas de cena são históricos do rascunho noturno, não validação do mapa atual.

Controles atuais: WASD/setas, Shift, roda, R e F1; F em proximidade nos três acessos físicos superfície/subsolo. A extensão contínua completa ainda está pendente; não há alegação de 16 setores reconstruídos.


## Fundo-Ferro — primeira camada inferior (acabamento adicional pendente)

Sete salas, oito rotas, circuito de retorno, duas pontes e três acessos físicos bidirecionais (F): Poço Velho, Doca Leste e manutenção sul de Forjas. Cena inferior separada por necessidade de camada, mantendo a cidade de superfície completa; nenhum portal E entre bairros reativado. Retorno e R usam chegadas seguras. Baseline: tools/checkpoints/sucateia_before_fundo.tscn.

11 testes passaram: travessia física de todas as salas/trechos/pontes, água e máquinas bloqueadas, seis transições por input real, preservação completa da superfície e regressões. Onze capturas foram inspecionadas, incluindo panorama, sete salas e três acessos. Parede arruinada e motor abandonado gerados no image_gen integrado; prompts e fontes em tools/fundo_art_manifest.json. Auditoria: tools/FUNDO_FERRO_AUDIT.md. Planta: docs/fundo-ferro-planta-espacial.svg. Checkpoint: tools/checkpoints/sucateia_fundo_ferro_primeira_etapa.zip.

Primeira etapa de navegação/ambientação; sem NPCs, criaturas/gangues funcionais, combate ou economia. Próximo setor aguarda revisão. Os demais setores permanecem pendentes; Ferrugem Baixa não está concluída.


## Etapa atual — Forjas Rasas, refinamento localizado

Direção humana restringe a etapa somente a Forjas na cena atual. Piso industrial com progressão gradual, nove redes/ligação de tubos, pátios de trabalho e cinco novos módulos funcionais da frente de arte paralela. Landmark visível da entrada leste do Mercado (captura market_landmark), ferreiro na transição, minério/carrinho em carga, guindaste na fundição e vaso de serviço ligado às caldeiras. Nenhum piso/território ampliado, 19 conjuntos anteriores preservados, quatro pisos idênticos em células/atlas e cinco PNGs aprovados por hash.

12 testes distintos passaram, nove capturas inspecionadas, revisão independente estática sem problemas materiais. Acessos F existentes e cena inferior preservados. Auditoria tools/FORJAS_REFINEMENT_AUDIT.md; prompts tools/forjas_parallel_art.md e assets/reconstruction/forjas_parallel/manifest.json; dados/métricas tools/forjas_refinement_spatial.json. Checkpoint tools/checkpoints/sucateia_forjas_rasas_refinamento.zip com CRC.

Fundo-Ferro: acabamento adicional solicitado ainda não aplicado, registrado em tools/PENDING_FUNDO_FINISH.md. Não declarar aprovação visual daquela etapa. Não avançar a outro setor; Os Cabos/Chaminés/exterior continuam aproximações, não destinos concluídos. Sem NPCs, economia, combate ou produção simulada.


## Correção de direção e contato físico — versão para revisão

Atualização após auditoria final: passe curto de logística concluído, dois pontos de descarga e resíduos localizados;13/13 testes completos sem ERROR,7 capturas atualizadas. Falha de certificados da execução restrita documentada separadamente; assertions passaram e repetição autorizada foi limpa. Último checkpoint: tools/checkpoints/sucateia_forjas_acabamento_local.zip. Pronto para revisão; nenhum outro setor iniciado.

Forjas na cena atual: faixa industrial20%, quatro pátios funcionais adicionais, chaminé anexada à fundição central, portos alinhados, resfriamento/drenagem, sombras e apoios nas bases reais, tubos sustentados e pontes ancoradas. Água/talude de contexto sem ampliar território jogável.13 testes distintos e7 capturas finais; relatório tools/FORJAS_DIRECTION_RESULT.md, antes/depois de fundição/máquina/passarela, manifesto complementar e checkpoint sucateia_forjas_direcao_integracao.zip. Original/Mercado/Alto-Lixo/pisos/colisões antigas e camada inferior preservados. Aprovação visual humana pendente; nenhum novo setor iniciado.
