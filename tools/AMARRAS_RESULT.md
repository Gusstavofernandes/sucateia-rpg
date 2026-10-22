# Passagem das Amarras — integrada para revisão final

Construída na mesma cena de Sucateia, a leste/sudeste das Forjas. Dois acessos físicos, entrada técnica mais estreita, pátio de transferência e continuação estreita reservada a Engrenópolis. Nenhum setor seguinte construído ou portal inventado.

O contorno preliminar largo foi retrabalhado em32vértices, mantendo os encontros, circuito inferior e canal.611células cobrem integralmente a superfície real; o shader recorta exatamente a borda. Esse número inclui células parciais de margem e não aumenta o polígono. Materiais em transição de fuligem para desgaste de carga/umidade, via principal mais legível, remendos pontuais e circuito de inspeção mais discreto.

Oito PNGs finais de `assets/reconstruction/amarras_parallel/manifest.json` integrados em escala uniforme, hashes conferidos: contraforte, torre, guincho, distribuidor, plataforma, controle e dois decals. Variantes rejeitadas não entram na cena. Perspectiva/iluminação preservadas; bases físicas derivadas dos apoios medidos. Módulos reutilizados tiveram o contato visual alinhado pelo alpha real. Correntes de seis conexões nascem/terminam nos terminais dos sprites, com elos sombreados pequenos; sem barras técnicas. A amarração diagonal foi encurtada para o pátio, evitando cruzar o canal. Carga pequena sobre o deck, carrinho/guindaste ao lado, bancadas de inspeção e reserva de carga sem nova família de prédios.

Sete rotas e quatro pontes percorridas fisicamente; destinos e chegadas atingidos em ida/volta. Água do canal bloqueada, bases das máquinas bloqueadas, acessos do quiosque/plataforma livres, R e três acessos F ao Fundo-Ferro preservados. HUD reconhece Amarras e suas pontes, mantendo prioridade Forjas sobre o piso existente.

16testes distintos PASS, semERROR; dois testes Amarras ampliados também passaram para conferir margens, hashes atuais e materiais anteriores. Seis capturas Amarras e uma Forjas renderizadas semERROR. Revisão independente somente leitura não encontrou P1/P2; aprovou para checkpoint. Parecer consultivo anterior aprovou a base espacial e pediu acabamento de fluxo/carga; passe aplicado. Avaliação final do supervisor/humano permanece distinta dessa verificação técnica.

Preservação: todos os nós anteriores, posições, pisos, contornos, materiais, texturas e colisões comparados ao checkpoint pré-Amarras. Hashes de arte protegida intactos; cena do Fundo-Ferro idêntica em bytes ao baseline. O fundo marítimo novo faz fade antes da costa antiga das Forjas. Limites de câmera ampliados para permitir a nova área; respawn original e jogador único mantidos.

Capturas: `maps/sucateia/preview_amarras_full.png`, `preview_amarras_district.png`, `preview_amarras_transition.png`, `preview_amarras_transfer.png`, `preview_amarras_anchor.png`, `preview_amarras_maintenance.png`; comparação Forjas em `preview_forjas_district.png`. Contagens de draw calls são observações de captura, não benchmark de FPS/hardware mínimo. Áreas abertas do pátio são circulação logística, com detalhes localizados; não houve preenchimento aleatório.

Checkpoint integral: `tools/checkpoints/sucateia_amarras_integrada.zip`, verificado com CRC e dependências da cena. Checkpoint anterior `sucateia_forjas_acabamento_local.zip` preservado. Plano e métricas em `docs/superpowers/plans/2026-10-03-passagem-amarras.md` e `tools/amarras_metrics.json`.

Parecer consultivo final das capturas04:44: AMARRAS APROVADA COM OBSERVAÇÕES NÃO BLOQUEANTES. Função logística, plataforma, retenção curta, apoios, margens, transição e circuito aprovados; microdesgaste/animações apenas opcionais futuros. Referência tools/CONSULTANT_AMARRAS_FINAL.md. Retrabalho visual encerrado; nenhuma outra área iniciada.
