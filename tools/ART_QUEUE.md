# Fila de arte antecipada — Ferrugem Baixa

Esta frente entrega somente novos PNGs e documentação. Não constrói cenas, importa no Godot, altera pisos ou declara setores prontos.

## Direção comum

Referência primária: `tools/checkpoints/original_visual_benchmark.png`. Referência de identidade: `C:/Users/Usuario/Downloads/Mapa de Ferrugem Baixa.png`. Capturas atuais consultadas para função e escala, nunca para estética noturna. Câmera ortográfica elevada 3/4 do sul para norte; topo dominante, fachadas curtas, luz difusa superior esquerda, transparência real, recorte completo. Pedra velha, ferro enferrujado, cobre fosco e madeira reaproveitada; âmbar contido, ciano pontual. Sem pessoas, texto, cenário ou piso externo.

## Forjas Rasas — cinco funções entregues e QA independente concluído

Cinco assets recebidos do subagente anterior, sem geração duplicada: landmark fornalha/chaminé, estoque minério/escória com carrinho, forja artesanal bigorna/fole, tubos/válvulas/caldeira serviço, guindaste compacto. Manifesto: `tools/forjas_parallel_art.md`, dados completos em `assets/reconstruction/forjas_parallel/manifest.json`. QA por composição alpha e bboxes visíveis concluído; PNGs originais preservados. Oficina, reciclador e salão de caldeiras preexistentes não são duplicados. Entrega de arte, sem declaração de integração.

## Os Cabos — quatro funções entregues para integração

Pasta: `assets/reconstruction/cabos_parallel/`. Manifesto próprio: `tools/cabos_parallel_art.md`.

1. Casa pendurada: telhado remendado, berço de correntes, pequeno acesso sul, sem pernas apoiadas no chão.
2. Ponte suspensa leste–oeste: tábuas antigas, corrimãos/cabos tensos, terminais completos; peça estrutural elevada, sem terreno.
3. Passarela elevada de encontro em T: grade/madeira mista e braços com ancoragens, distinto da ponte reta.
4. Nó de linhas de energia: mastro assimétrico com isoladores e roldanas, bateria pequena ciano; sem caldeiras ou chaminés.

Silhuetas domésticas e infraestrutura suspensa, distintas da indústria de Forjas. Implantação e colisões ficam com integrador; larguras sugeridas documentadas por asset.

QA visual e composição alpha em `cabos_parallel/qa_composite.png`; métricas em `cabos_parallel/qa_metrics.json`. Usar `walkway_t_junction_clean.png`. Ponte reta é passagem estreita; consultar escala corrigida no manifesto.

## Docas — quatro funções entregues e QA concluído

Pasta: `assets/reconstruction/docas_parallel/`. Manifesto próprio: `tools/docas_parallel_art.md`.

Entregues: `cargo_barge.png`, `cargo_sorting_shelter.png`, `mooring_capstan.png`, `naval_repair_cradle.png`. QA visual por composição alpha em `docas_parallel/qa_composite.png`, métricas e prompts/fontes completos em `manifest.json` e `tools/docas_parallel_art.md`. Sem água pintada, cais/pisos, pessoas ou novo guindaste equivalente ao de Forjas.

## Recomendações consultivas para implantação de Forjas

Registrar como hipóteses a avaliar após placement, não defeitos comprovados: conferir landmark nas vistas perto/média/desde Mercado; entrada de combustível, exaustão e suportes legíveis; mistura comércio–metal na transição; sinais de descanso/ocupação operária; overlays de fuligem/cinzas/óleo/rodas/escória no chão. Esta frente não gera pisos/overlays nem constrói cena. Usar os cinco originais Forjas, não variantes `_clean`. Lacunas adicionais só após QA concreto da integração.

## Limite

## Prioridade atual — complemento Forjas antes de novos setores

Auditoria obrigatória: `tools/FORJAS_DIRECTION_AUDIT.md`. Entregues13 PNGs selecionados em `assets/reconstruction/forjas_parallel/complement_v1/`, com `manifest.json`, variantes preservadas e três imagens QA. Manifesto de leitura: `tools/forjas_complement_art.md`. Blocos PRODUCTION CONSTRAINTS e MODULARITY integrais em cada prompt, números comparados à escala real do integrador/porta24–28px, luz superior esquerda; margens reais medidas, não assumidas iguais à meta10%. Decals de fuligem/escória/calor, quatro clusters funcionais, torre add-on, redutor26→40–44px, tubo sustentado, passarela, suporte N–S e oficina híbrida. Reutilizar minério/carrinho/guindaste existentes. Calor exige alpha0,15–0,25; suporte N–S não é encaixe direto do tubo E–W. Escalas/pontos/limites detalhados no manifesto. Cabos/Docas preservados; nenhuma nova expansão. Integração/panorama continuam com a frente de cena; setor não aprovado por este lote.

Somente Forjas Rasas → Os Cabos → Docas, dentro de Ferrugem Baixa. Demais regiões não autorizadas. Estado entregue significa PNG revisado e documentado, não setor integrado ou jogável.

## Nova autorização — assets antecipados de Passagem das Amarras
Usuário autorizou produção paralela da próxima área enquanto Forjas termina. Prioridade passa a Passagem das Amarras: inventário/reaproveitamento de Cabos, Docas e Forjas; novos PNGs em amarras_parallel e documentação própria. Consultor solicitado para lote de 6–8 funções/prompts. Sem construção, importação ou mudanças de cenas. Primeira função: ancoragem estrutural com sapata e correntes; demais após brief consultivo. Não avançar a outras áreas automaticamente.

Consultor confirmou Amarras; brief/prompts/QA em tools/CONSULTANT_AMARRAS_ASSETS.md. Lote de sete funções sugeridas encaminhado à arte, sujeito a inventário para evitar duplicação de cabrestante e mastro. Produção autorizada de PNGs, sem implantação.

Amarras — entregue: oito seleções em `assets/reconstruction/amarras_parallel/manifest.json`: contraforte/ancoragem, torre média de tensão, guincho horizontal, plataforma de fixação, hub baixo, quiosque técnico e dois decals(B/C). FamíliaA reaproveita fuligem existente. Inventário e instruções em `tools/amarras_parallel_art.md`; QA em tamanho gameplay, bases/conexões e decals sobre pedra existente na pasta própria. Usar torre `_margin`, quiosque `_complete`, decals `_marks`/`_stains`; variantes originais preservadas/não selecionadas. Sem cena/import/runtime. Confirmar offsets de algemas no placement; torre W/E difere~23px. Novos setores não autorizados automaticamente.
