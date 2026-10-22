# Forjas Rasas — refinamento localizado da cidade atual

Direção humana: somente Forjas Rasas a leste/nordeste do Mercado, na cena existente. Referência cartográfica Downloads/Mapa de Ferrugem Baixa.png inspecionada; benchmark original mantido para escala, materiais e câmera. Nenhum mapa noturno incorporado, nenhum setor novo iniciado, nenhuma expansão territorial necessária nesta etapa.

## Mudanças concretas

Piso industrial passa gradualmente de pedra urbana junto ao Mercado para pedra escurecida, remendos de metal, carvão/cinzas e marcas de calor nos pátios. Nas bordas, mistura de barro escuro e resíduos. Contorno, células, rotas e tamanho do piso permanecem os mesmos; shader e overlays fazem a diferenciação. Mercado/Alto-Lixo/núcleo/costa mantêm seus pisos e arte.

Trechos soltos de cano de chão apenas dentro de GroundIntegration/Drainage de Forjas substituídos por oito redes conectadas: caldeiras→fundição, circuito dos fornos, recuperação→triagem, fabricação, drenagem, entrada→oficinas, reparos e carga. Uma ligação adicional conecta o vaso de serviço à rede principal. Canos presos às fachadas anteriores permanecem. Tubulação baixa pode ser cruzada por placas de manutenção; não cria bloqueios artificiais.

Pátios recebem fundações, metal, fuligem e desgaste por função: carga, forja quente, recuperação, fabricação, triagem e reparos da rua. Luz laranja localizada nos dois fornos e na entrada, ciano restrito aos equipamentos anteriores. Ocupação comunicada por forja aberta com ferramentas, carrinho de minério, áreas de abastecimento e manutenção; não há simulação de trabalhadores/produção.

Cinco módulos distintos da frente paralela integrados uma vez cada: fornalha/chaminé (2050,-275), ferreiro da rua (1850,-8), minério/carrinho (2490,30), guindaste da fundição (2945,-925), vaso de serviço (2840,-1390). Arquivos originais selecionados pelo artista em assets/reconstruction/forjas_parallel/, sem variantes _clean em uso. Bases possuem colisão; chaminé/lanças não bloqueiam o jogador. Modules compartilham Structures/y-sort com personagem. As 19 arquiteturas industriais anteriores não mudam de posição ou escala.

Saídas: Chaminés Velhas ao norte e Grande Ferrugem a leste continuam aproximações reservadas. Corredor de manutenção sudeste aproxima Os Cabos, ainda não reconstruído. Acesso F de manutenção sul leva realmente a Fundo-Ferro e retorna. Nenhum destino externo fictício nem portal E reativado.

## Auditoria visual

Nove capturas finais, todas em maps/sucateia/: preview_forjas_full, district, frontier, market_landmark, cargo, boilers, foundry, recycling, drain .png. Inspeção do autor: Forjas distingue-se do comércio central e do residencial oeste pela pedra escura, áreas de trabalho, máquinas expostas, redes e calor concentrado. A fronteira contém ainda barracas/lojas e ferreiro menor; metal e peso aumentam para leste.

preview_forjas_market_landmark posiciona a câmera na entrada leste do Mercado (1600,-275), zoom .88. A fornalha e a chaminé aparecem completas acima/entre os telhados industriais, com boca quente orientando a travessia. A visibilidade foi verificada dessa parte do Mercado, não de toda a praça ou de qualquer posição do distrito. Capturas média, geral e fronteira complementam a leitura.

Panorama confirma Alto-Lixo a oeste, Mercado central, Forjas a leste/nordeste e núcleo/costa abaixo. Nenhuma ilha ou moldura retangular nova; contorno irregular e ruas continuam entre áreas. Respiros são pátios e circulação. O território existente foi suficiente para as funções novas. Isso não declara a região inteira finalizada.

## Verificação

12 verificações distintas passaram: preservação refinada, cinco módulos, y-sort, circulação Forjas, preservação anterior Forjas, Alto, acabamento Alto, costa inferior, Mercado, núcleo/controles, acessos F e circuito inferior preservado. Logs tools/fundo_test_*.log; ferramentas tools/run_forjas_refinement_checks.py e run_fundo_checks.py.

Todas as oito rotas e duas pontes de Forjas atravessadas fisicamente; quatro aproximações regionais e cinco pátios alcançáveis com retorno. Novas cinco bases bloqueadas e cinco frentes de serviço alcançadas ida/volta desde Mercado. Água continua bloqueada. Seis transições F reais verificam os três retornos, jogador único, spawn seguro e R. Cena inferior igual à baseline antes do acabamento interrompido.

tests/test_forjas_refinement_preservation.gd compara toda a cena anterior, inclusive as 19 construções, ordenação, texturas, colisões e quatro pisos. Única exceção nominal: sprites de pipe.png de chão dos dois grupos de Forjas explicitamente substituídos. Nenhuma exceção para bairros aprovados. Finalizador confere quatro pisos e cinco PNGs aprovados por SHA-256, além do hash da cena inferior.

Revisão independente estática por subagente não encontrou regressões materiais; conferiu código, testes e logs, sem executar Godot. QA visual feita pelo autor. Uma tentativa inicial de integração detectou PNG ainda não importado; integrador ganhou validação prévia e reparou somente o módulo incompleto. Encerramento/finalização limpos confirmados em tools/forjas_parallel_integration.log. Não é falha pendente do jogo.

## Arte / limites

Gerador integrado image_gen, prompts/fontes completos: tools/forjas_parallel_art.md e assets/reconstruction/forjas_parallel/manifest.json. Pasta da arte preservada pelo integrador. Torre alternativa que já estava em geração antes da divisão de frentes ficou em tools/pending_art; não usada. Nenhuma geração duplicada depois da divisão.

Sem NPCs, economia, combate ou produção simulada. Fundo-Ferro mantém navegação, mas o acabamento visual adicional solicitado continua pendente: tools/PENDING_FUNDO_FINISH.md. Seus scripts/assets novos foram preservados sem aplicação quando a prioridade humana mudou. Não avançar para Os Cabos ou outro setor nesta entrega.

Checkpoint revisado: tools/checkpoints/sucateia_forjas_rasas_refinamento.zip; CRC verificado pelo finalizador. Checkpoints anteriores continuam históricos.

## Conferência da consultoria visual

tools/CONSULTANT_FORJAS_REVIEW.md foi lido e comparado às nove capturas finais; a consultoria avaliou uma versão em desenvolvimento e não valida colisões.

- Piso pouco distinto: observação superada no acabamento atual por progressão de fuligem/metal/carvão e bordas de barro; Mercado manteve seu material. Confirmado em frontier, foundry e district.
- Vazios sem função: pátios agora possuem minério/carrinho/guindaste, fabricação, fundição e triagem, com faixas de trabalho separadas das vias. Respiros de circulação continuam; não foram preenchidos aleatoriamente.
- Landmark pouco dominante: uma fornalha/chaminé distinta foi acrescentada na fronteira. Legível na vista do Mercado e no panorama de setor; no panorama de toda a cidade é menor pela escala consistente. Não foi inflada até perder proporção com portas/jogador, nem duplicada com outra torre.
- Conexões industriais: nove redes/ligação com origens/destinos de caldeiras, fornos, oficinas, triagem, fabricação e canal substituem os segmentos soltos. Vaso de serviço efetivamente ligado à alimentação das caldeiras.
- Aba lateral/borda: massa existente e fronteira urbana contínua preservadas; infraestrutura segue o contorno irregular e mantém aproximações de Chaminés/Grande Ferrugem/Os Cabos e acesso real inferior. Esses vizinhos ainda incompletos limitam o acabamento regional definitivo; não há alegação de costa/skyline de todos eles concluídos. Não houve expansão adicional para mascarar a borda.

As sugestões de chaminé/oficina/conectores adicionais não geraram duplicação dos cinco módulos já integrados. A evidência final é a cena atual e suas capturas, não somente o parecer consultivo.

Métricas finais de captura: geral 1802 draw calls, setor 483, detalhes 138–231; 3448 nós. Amostras de frame, não benchmark prolongado de FPS. Dados por captura em tools/forjas_refinement_spatial.json.
