# Forjas Rasas — correção de direção e integração física

Passe aplicado somente às Forjas na cena atual. Referência adotada: FORJAS_DIRECTION_AUDIT.md, complementada pelo pedido humano de corrigir a leitura de elementos flutuantes. Esta entrega é uma versão concreta para revisão visual, não aprovação humana nem conclusão de Ferrugem Baixa.

## Resultado

- Faixa de transição industrial x=1710–2120: aproximadamente20% da largura do setor. Pedra escurecida/desaturada, remendos, fuligem diluída e eixo de circulação gasto. Mercado preservado.
- Funções agrupadas: carvão em2500,-1170; minério existente2490,30; escória3545,-875; resfriamento2730,-290; manutenção2780,-475. Desgaste localizado por processo, incluindo umidade e óleo. Via de carga recebe marcas paralelas de rodas.
- Fundição central original2700,-1000 preservada; addon de exaustão com440px de altura visível, plataforma e duto com redutor no inlet oeste real. Tampa leste permanece fechada. Fumaça e calor locais, sem alteração da iluminação global.
- Carvão, tanque e escória têm conexões alinhadas a portos nativos do PNG, tolerância de teste8px. Alimentação e retorno do tanque separados; retorno segue para drenagem existente. Vapor discreto e pluma localizada no canal. Produção é composição visual; não há simulação econômica.
- Bases médias/grandes recebem pequenas placas de apoio, sujeira e sombras curtas nos pés realmente visíveis do sprite, medidos pelo alpha. Os tubos verticais têm selas N–S; conectores horizontais têm apoios próprios. As duas pontes têm ancoragens nos bancos, preservando o vão de circulação.
- Água industrial leste, pequenas contenções e sucata tornam a margem construída. Talude distante ao norte/nordeste oferece contexto regional. Água/talude são ambientação não jogável: nenhuma célula, saída ou território jogável novo. Aproximações para Chaminés/Grande Ferrugem/Os Cabos continuam reservadas, sem alegação de setores construídos.

## Capturas sem labels

[Panorama do distrito](C:/Users/Usuario/Documents/jogo/maps/sucateia/preview_forjas_district.png), [cidade completa](C:/Users/Usuario/Documents/jogo/maps/sucateia/preview_forjas_full.png), [transição](C:/Users/Usuario/Documents/jogo/maps/sucateia/preview_forjas_frontier.png), [landmark desde Mercado](C:/Users/Usuario/Documents/jogo/maps/sucateia/preview_forjas_market_central_landmark.png).

| Detalhe | Antes do passe de contato | Depois |
|---|---|---|
| Fundição/base/dutos | [Antes](C:/Users/Usuario/Documents/jogo/tools/checkpoints/forjas_foundry_before_grounding.png) | [Depois](C:/Users/Usuario/Documents/jogo/maps/sucateia/preview_forjas_foundry.png) |
| Máquina/tubos/escória | [Antes](C:/Users/Usuario/Documents/jogo/tools/checkpoints/forjas_machine_before_grounding.png) | [Depois](C:/Users/Usuario/Documents/jogo/maps/sucateia/preview_forjas_recycling.png) |
| Passarela/apoios/canal | [Antes](C:/Users/Usuario/Documents/jogo/tools/checkpoints/forjas_walkway_before_grounding.png) | [Depois](C:/Users/Usuario/Documents/jogo/maps/sucateia/preview_forjas_drain.png) |

As capturas de detalhe da fundição mantêm enquadramento para comparação da base; cortam o topo da torre. O panorama do distrito demonstra a silhueta inteira. As versões antes são intermediárias reais de23:15–23:16, não reconstruções artificiais do antes.

## Verificação e limites

Após o último passe localizado, a suite completa passou13/13, com retorno zero e nenhum ERROR. Produção verifica portos reais, bases, frentes navegáveis e contexto não jogável; regressões verificam preservação, ordenação, percursos, pontes e acessos ao subsolo. Logs em tools/fundo_test_*.log. Quatro pisos em células/atlas,19 conjuntos industriais, PNGs protegidos e cena inferior preservados. Três acessos F e circuitos antigos seguem funcionais.

Sete capturas finais atualizadas. Distrito854drawcalls, cidade2095, detalhes282–345;3851nós. São amostras de captura, não benchmark prolongado de FPS. Mais detalhe aumentou custo de desenho; não há medição sustentada de desempenho nesta entrega.

Consultoria sobre capturas intermediárias reconheceu transição, landmark e três funções macro. Revisão independente inicial pediu melhorar a borda contra o vazio; contexto costeiro/talude foi acrescentado depois. Revisão final técnica está registrada separadamente. A continuidade com destinos futuros ainda exige construção desses destinos em fases autorizadas; esta etapa não os antecipou.

## Arte e reprodução

13 arquivos selecionados pela frente de arte em assets/reconstruction/forjas_parallel/complement_v1/manifest.json;12 utilizados neste passe. Oficina híbrida adicional não utilizada: ferreiro/comércio existentes já atendem a transição. Tanque inicial cortado e variantes de calor rejeitadas não utilizadas. Prompts/fontes/alpha/encaixes em tools/forjas_complement_art.md e manifesto. Originais anteriores intactos.

Ferramentas incrementais idempotentes, sem replay histórico: correct_forjas_direction.gd, align_forjas_ports.gd, finish_forjas_border.gd, ground_forjas_structures.gd. Checkpoint anterior: sucateia_before_forjas_direction.tscn; checkpoint novo: sucateia_forjas_direcao_integracao.zip.

## Passe curto após auditoria final

As bases dos módulos médios centro/leste e os efeitos de fuligem/escória já estavam presentes e foram mantidos. Acrescentados apenas dois pontos baixos de parada/descarga: diante do minério existente e junto ao guindaste da fundição, com placas e rastros de transporte; óleo localizado junto à bancada e umidade sob a canaleta do tanque. Sem prédios, colisões ou expansão adicionais. Script idempotente: polish_forjas_logistics.gd. Checkpoint deste passe: sucateia_forjas_acabamento_local.zip; versão anterior preservada.

Consultor reconheceu landmark, três zonas e continuidade na auditoria final recebida, com flutuação largamente resolvida. Esse parecer é consultivo; não altera o escopo para construir outros setores. Passagem das Amarras permanece apenas planejamento futuro.

Verificação atual: suite completa13/13 passou, com retorno zero e nenhum ERROR nos13 logs. A execução restrita anterior imprimiu PASS nas assertions, mas cada inicialização registrou `Failed to read the root certificate store` em `os_windows.cpp:2582`, e o runner corretamente rejeitou os logs. Evidências restritas preservadas em tools/certificate_restricted_evidence/. Repetição com a execução autorizada do engine e o mesmo runner passou sem esse erro; isso distingue a falha de acesso ao ambiente Windows da verificação de gameplay. Nenhum erro foi filtrado, teste relaxado ou configuração de certificados alterada.
