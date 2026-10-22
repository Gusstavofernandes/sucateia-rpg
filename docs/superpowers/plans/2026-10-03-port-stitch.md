# Costura Docas/cidade/Forjas — plano de implementação

> Para execução: skill superpowers:executing-plans, etapas em sequência; revisão independente somente leitura ao concluir. Autorização humana de execução autônoma prevalece sobre repetição de gates de confirmação.

**Goal:** transformar a faixa de ligação existente em retaguarda econômica portuária, preservando geografia/arte/circulação aprovadas.

**Architecture:** novos grupos de decoração e funções na cena atual; primeira opção é aproveitar pisos existentes, sem alterar topologia. Bases físicas auditadas pela pintura e triagem intencional por uso; qualquer bolso adicional deve ser curto, apoiado e conectado fisicamente, justificado pela auditoria. Não recriar Docas ou módulos de entrada polida.

**Tech stack:** Godot4.7.2 Compatibility, GDScript, PNG gerado comalpha, builders fora daSceneTree ao salvar, auditoria/headless e capturasGPU sequenciais.

**Spec:** tools/CONSULTANT_PORT_STITCH_BRIEF.md; inventário atual FERRUGEM_REAL_INVENTORY.md e reservas POLISH_PROGRESS.md.

## Planta de estudo

Faixa de trabalho: núcleo costeiro oriental e retaguarda técnica existente, x2100–3350/y260–1740. Água entre costa e decks participa; nenhum alargamento indiscriminado ou preenchimento por residências.

1. Chegada rasa/espera de carga: entrada urbana2240,1370 e eixo2350→3170,1640. A entrada pedra/madeira é reservada ao polimento; trabalhar depois dela, em esperas livres/pátios existentes. Tração/defensas devem servir deslocamento de carga, sem duplicar barcaça/cabrestante aprovados.
2. Triagem molhada: pátio2510,1505, abrigo2490,1440 e via2500,1575→1640. Lotes pequenos distintos secos/molhados, bancada e carrinho junto à borda útil; preservar frente do abrigo eR2500,1575. Nunca empilhar nova carga sobre respawn.
3. Corredor de serviço/almoxarifado: sequência técnicaForjas3280,275→3280,610→3090,925→2840,1280→2700,1640. Pontos de serviço nas juntas existentes (3280,610),(3090,925),(2840,1280), com galpão/oficina baixa apenas se houver base seca e via livre. O corredor continua sendo manutenção costeira, com tubos/ferragens ligados a uso real; não clonar barracas ao longo dele.
4. Borda urbana: margem oriental antiga e junturas deDocas, com apoios, contenção/drenagem e progressão pedra molhada→piso firme/fuligem. Evitar área polida x1985–2265/y1115–1520. Cada elemento novo encosta em margem/peça estrutural, jamais piso técnico flutuante.
5. Bocas técnicas: manter PocoVelho1296,1572, DocaLeste2210,1668 e ForjasManutencao3000,260. Não relocá-las por composição. Usos respectivamente carga vertical/serviço inferior, manutenção cais e inspeção industrial; passos/aprons são superfícies de entrada existentes, sem outra camada nova.

Estas coordenadas definem funções, não autorizam colocar collider em espaço ainda não medido. Levantamento deve identificar folgas e suportes reais antes de definirfootprint. Rotas atuais ida/volta são o contrato. Reservar raio75 em acessosF, raio35 nos seis patamaresR e largura livre mínima44 em eixos secundários/60 nas vias principais, conservando larguras anteriores quando maiores. Objetos nunca reduzem uma rota aprovada abaixo do necessário ao jogadorraio11.

## Propriedade

Root: builders/auditoria/tests/docs novos; grupos novos próprios na cena central. Arte: novo diretório assets/reconstruction/port_stitch/ e respectivos manifestos/QA; sem motor ou cena. Polimento: scripts/world/port_approach_finish.gd, escadas/utilidades/pilares, seus testes/arte e prefixoport_. Não sobrescrever fontes nem guardar runtime apenas no diretório do gerador.

## Etapas e evidências

- [x] Levantar piso/corpos/folgas, capturar a ligação, salvar baseline da cena aprovada em checkpoint próprio e registrar pontos funcionais/ausências reais.
- [x] Receber/auditar reaproveitamento e handoffPNG com escala, contatos secos, sockets/anchors e hashes; pedir complemento específico só com função definida.
- [x] Escrever e executar testeRED: cinco papéis, ligação contínua às três entradas, bolsosF/R, preservação da baseline e floor-paint efetivo. Usar movimento físico e shape query, sem testes que apenas copiam o builder.
- [x] Integrar grupos funcionais novos, colisões só nas bases reais e sombras/apoios/cordas com origem/destino. Floor atual primeiro; se houver bolso adicional, definirunião/guardas e testar limites daágua sem alterar costa antiga.
- [x] TesteGREEN e regressões seletivas significativas; custo de desenho anotado, sem declararbenchmark sustentado.
- [x] Capturar panorama e detalhes das cincofunções/transições, inspecionar visualmente; revisar independentemente e corrigir bloqueantes.
- [x] Métricas/hashes/ZIP comCRC e parecer consultivo. Inventário regional não muda de estado só por esse acabamento. Fundo/Coroa somente na sequência debriefs.
