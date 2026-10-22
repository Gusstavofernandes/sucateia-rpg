# Docas / Cais — arte existente e handoff de integração

Brief: `tools/CONSULTANT_DOCAS_BRIEF.md`. Quatro PNGs originais auditados visualmente e em composição alpha,14 candidatos de reaproveitamento registrados. Não havia ausência funcional comprovada antes do placement. Orientação humana posterior prioriza acabamento profissional e autoriza novos assets por ganho visual concreto: complementos de variedade estrutural/carga/transição costeira em produção, separados dos originais. Fontes aprovadas preservadas, sem edição de cena/import/runtime.

## Entrega e medidas

`assets/reconstruction/docas_parallel/audit_v1/manifest.json` contém SHA256, canvas/bbox alpha>16, escalas uniformes, pontos nativos, offsets de mundo a partir do centro do canvas, caixas aproximadas de contato seco, guia visual da linha d'água e inventário. `qa_gameplay_connections.png` mostra as quatro peças em tamanho de mundo1:1, régua24px, conexões cianas numeradas, bases amarelas e guia d'água azul. O guia não é água/piso incluído no asset. Reprodutor: `tools/audit_docas_art.py`.

| PNG em assets/reconstruction/docas_parallel/ | Escala uniforme | Objeto visível mundo | Observação de escala |
|---|---:|---:|---|
| cargo_barge.png |0,205351587|330×131px|Caixa maior~33px; carga/cordas legíveis. Porão cheio, sem zona livre certificada para andar/spawn.|
| cargo_sorting_shelter.png |0,207852194|270×180px|Armário lateral~27px de largura; não confundir com entrada pública de27px. Frente sul já contém bancada/caixas.|
| mooring_capstan.png |0,105501130|140×70px|Tambor~42px de diâmetro; alavancas aumentam o bbox, não a base. Três bases distintas.|
| naval_repair_cradle.png |0,134886573|220×95px|Casco menor que barcaça, tábuas novas e ferramentas legíveis. Cavaletes reais, sem chão ou água.|

Usar escala derivada da largura VISÍVEL; não dividir largura pretendida pela largura total do canvas. Pontos visuais estimados ±10px nativos (~1–2px mundo nas escalas acima), sem aprovação de collision. Fórmula Sprite2D centralizado, sem rotação/flip: global = posição + (ponto nativo − canvas/2) × escala; aplicar transformação de pais quando existir. Nunca usar bbox de alpha como footprint. Não espelhar/girar sprites para forçar outra costa: altera luz e câmera pintadas.

## Barcaça — água, amarração e carga

Orientação horizontal E–O, proa à esquerda, popa à direita. Sem água, wake ou sombra no PNG. Iluminação superior esquerda e superfície de cima dominante, compatível com benchmark. Cais paralelo pode ficar no lado sul visível para facilitar leitura de fenders/amarração; essa sugestão não fixa geografia.

- Cabeço da proa: nativo(232,420), ponto de corda junto à cintura do poste, não topo do parafuso.
- Região de amarração no bordo reforçado traseiro: (1372,650); bordo médio: (940,618). São guias de contato de corda na borda, **não cleats independentes certificados**. Cordas de defensas já pintadas não devem virar linha de tração pesada. Mostrar volta/apoio no bordo reforçado ou estrutura sólida, sem origem no vazio; observar em close-up após placement.
- Saída visual do pequeno guincho: (1360,547); a corda externa deve sair tangente ao tambor e seguir a carga/guia real. Não ligar ao teto do toldo.
- Alcance de carga ao sul: (820,624), junto ao bordo do porão, não piso de travessia livre. Carga pode ser alcançada pelo guindaste do cais ou passarela existente até uma região realmente desocupada. Não desenhar colisão caminhável atravessando caixas para justificar gangway.
- Guia inferior do casco/água: polilinha nativa(105,435)→(330,640)→(800,730)→(1400,730)→(1630,620). É referência visual aproximada para contato/ripple, não máscara física de submersão. Água atrás do barco, defensas junto à borda; não apagar a metade sul do casco nem flutuar o PNG acima da água sem contato.

Dois pontos de amarração separados devem chegar a cabeços/cabrestante/parede existentes; evitar linhas quase horizontais infinitas ou tangentes sem destino. Manter folga curta entre barco e cais que possa ser vencida pelo equipamento de carga escolhido. Nenhuma nova família de amarração é comprovadamente necessária neste momento.

## Abrigo — acesso terrestre e triagem

Frente de trabalho sul: (690,890); limiar do armário lateral: (1120,938); cabeço/corda à esquerda: (135,772); carretel de corda sobre bancada: (686,712). Carretel é estoque, não âncora estrutural. Roof ligeiramente enviesado em relação ao eixoE–O, sem terminais modulares alinhados; colocar como prédio, não esticar entre módulos.

Contato seco aproximado: envelope nativo110,825–1320,980 (~252×32px mundo); amostras de bases110,835–360,900;955,898–1050,960;1230,900–1320,980 no manifesto. Envelope inclui bens e não equivale a collider único retangular aprovado. As caixas/bancada já ocupam o interior; reservar faixa externa sul~70–90px para manobra/triagem, separada da via principal de carga. Água não deve cruzar os pés. Porta do armário não é um acesso de distrito/spawn.

## Cabrestante — base e tração

Cabeço oeste(299,602), cabeço leste com corda(1297,618); tangentes visuais do tambor(600,580)/(910,590). Pontos de rope na cintura, não eixo superior/handles. O PNG contém corda enrolada no cabeço direito, sem cabo externo; a cena completa a ligação a barco/carga com percurso coerente e, se necessário, guia existente. Não presumir que toda linha deve sair exatamente reta do centro do tambor.

Três bases nativas:133,710–480,790;510,735–1010,832;1080,704–1430,790, cerca37×8/53×10/37×9px mundo. Todas assentadas em pedra/deck robusto **seco**, afastadas da faixa principal; dar espaço à alavanca giratória, cujo alcance supera o footprint. Cais precisa oferecer reação de carga por fundação/contenção, não colocar tambor em píer solto. Contato/colisão/raio de operação são decisões de placement.

## Berço — reparo e ligação à margem

Olhal visual de proa(155,309), de popa(1580,250); apoios inferiores(550,792)/(1268,810); aproximação de serviço sul(900,720), no vazio entre os cavaletes. Olhais são para conexão de movimentação do casco, não superfícies de caminhada.

Pés secos:400,755–725,824 e1120,768–1400,834 (~44×9 e38×9px mundo), além das travessas que compõem envelope360,600–1460,834. Todos em terra/slipway firme. O casco está erguido nos cavaletes: não é barco flutuante nem píer/corredor. Reservar acesso de ferramentas ao sul e ligar a oficina à água por margem/reentrância/rampa ou trajeto de lançamento visível. **Uma escada de pedestres não é rampa de carrinho/navio.** Se placement exigir lançamento por rampa pintada específica e nenhuma geometria/asset existente resolver, registrar essa lacuna com captura antes de produzir arte.

## Reaproveitamento útil

| Caminho | Função/limite |
|---|---|
| assets/infrastructure/coastal_wall.png |Contenção com topo de pedra, estacas, cabeços/corrente e limo existentes. Água junto à parte baixa, terreno ligado ao topo; não ilha de parede solta.|
| assets/infrastructure/retaining_edge.png |Transição curta de contenção urbana; não fornece piso largo por si.|
| assets/reconstruction/cabos_parallel/main_deck_ew_wide.png |DeckE–O reutilizável .1411161,75,5px pintados; precisa apoios/estacas/contato com terra no cais. Consultar CABOS_ART_HANDOFF.md para terminais e passo.|
| assets/infrastructure/walkway.png / stairs.png |AcessoN–S e desnível pedestre. Não girar deck para fabricarE–O e não usar escada como rampa de carga.|
| assets/infrastructure/crane.png / assets/reconstruction/forjas_parallel/compact_loading_crane.png |Escolher guindaste existente por estação; base firme em terra, gancho sobre carga real, sem duplicar funções.|
| assets/region/dock_warehouse.png |Armazenamento pronto, guindaste/carga, patamar e anéis existentes. Escalar pela porta e verificar contato do patamar, não criar outro grande galpão.|
| assets/region/wreck_cradle.png |Casco grande de salvamento/destroço; diferente do pequeno reparo ativo. Opcional, não necessário para cobrir função já entregue.|
| assets/reconstruction/market_salvage_cart.png |Transporte de carga geral reutilizável; evitar lotar o porto com minério apenas.|
| assets/reconstruction/amarras_parallel/chain_winch_station.png |Tração terrestre adicional, somente onde precisar; destino/guia real, sem repetir o cabrestante sem propósito.|
| assets/reconstruction/amarras_parallel/damp_anchor_runoff_decal_stains.png |Umidade/mineral/ferrugem discreta, alpha inicial.25. Não é textura nova de madeira molhada/limo certificada; testar no piso de Docas.|
| assets/reconstruction/amarras_parallel/chain_drag_wear_decal_marks.png |Marcas planas de carga/rodas/correntes, alpha inicial.30.|
| assets/infrastructure/lantern.png |Iluminação funcional reaproveitada nas estações/acessos.|

Cordas/correntes ligando pontos distantes são geometria de cena, não motivo automático para novo PNG. O piso portuário, água e geografia ainda estão em implantação; rampa/margem funcional específica precisa de placement concreto. A orientação humana posterior também autoriza melhorias por acabamento/composição: três complementos descritos abaixo. Manter eixo de carga paralelo à costa, ramais aos píeres e três conexões do brief, spawns em patamares livres afastados da água. Esses requisitos não estão certificados pela presente auditoria de arte.

## QA e limites

Os quatro originais permanecem RGBA, alpha mínimo0, bboxes visíveis contidos; margens mínimas43/44/103/53px. Composição RGBA de gameplay confirma extração sem névoa visível; RGB marrom sob alpha0 é invisível. Padrão de câmera/luz coerente; abrigo tem leve obliquidade estrutural, berço é um casco aberto comprido, não bloco quadrado. Texturas/carga/cordas/tábuas novas demonstram uso ativo.

Snapshot de121 PNGs de reconstruction/infrastructure/region com SHA256 no manifesto; todos idênticos após execução da auditoria. Inclui fontes Docas/Cabos/Forjas/Amarras e outras artes existentes nesse inventário, excluindo previews audit_v1. Não executar este script para substituir o snapshot durante revisão de preservação: comparar aos hashes salvos. Nenhum teste/runtime/import Godot executado; aprovação da costa/contatos/rotas exige capturas da integração e parecer consultivo.

## Complementos de acabamento — orientação humana aplicada

A orientação humana autoriza mais assets para acabamento profissional, não apenas ausência funcional. Foram criados **três complementos selecionados**, sem substituir os quatro originais, por ganhos específicos: apoio costeiro distinto de torres Cabos, carga portuária com sling e materiais mistos, transição de umidade/sal própria da madeira. Built-in image_gen; prompts/fontes completos e hashes em `assets/reconstruction/docas_parallel/complement_v1/manifest.json` e `prompts.json`.

| PNG em complement_v1/ | Escala uniforme | Objeto visível mundo | Seleção/limite |
|---|---:|---:|---|
| pier_head_deep.png |0,185185185|270×174,81px|Patamar com estacas, travessas/joelhos, anel lateral, sal/limo e remendos assimétricos. Área central conservadora208,33×88,89px. Meta95px do prompt não atingida integralmente;88,9px reais são adequados como faixa larga, conferir collider/spawn na implantação.|
| port_cargo_sling_cluster.png |0,093220339|110×89,03px|Madeira/lona/cobre/cordas diferenciados e sling com anel. Caixa maior~50px, maior que meta30px; usar como carga volumosa, não caixa doméstica/prop minúsculo. Sem carrinho, sem repetir minério.|
| wet_wood_saltwear_decal.png |0,108641975|220×42,37px|Marcas planas quebradas de umidade/grão/sal, sem objeto/floor. Profundidade42px menor que meta55–65; indicada para faixa costeira localizada. Opacidade inicial.25, faixa.20–.30.|

**Cabeceira:** retângulo nativo livre200,160–1325,640. Entrada oeste(145,417) e leste(1390,417) na mesma linha; offsets de mundo(-115,37,-17,593)/(115,185,-17,593). Pares de lugs: Wn(82,316)/En(1451,316); Ws(64,549)/Es(1470,549). Faixa entre piles nas laterais aberta, com bandas metálicas planas e sem guarda transversal. O anelSW fica em(245,796), offset(-96,852,52,593), fora do piso, próprio para amarração externa.

Pés frontais das estacasSW(137,938),SE(1394,938), offsets(-116,852,78,889)/(115,926,78,889), com caixas aproximadas88,884–195,975 e1340,884–1456,975. Partes inferiores dos apoios traseiros ficam ocultas pelo deck; os topos e as estacas frontais são legíveis. Não afirmar contato certificado com fundo do mar: placement ajusta profundidade água/estacas, conexão com cais e margem. Não usar como píer isolado. Combina com deckE–O existente por entrada no mesmo y/elevacão; lugs são de outra largura e não há encaixe automático certificado. Ajustar junta/banda com comparação próxima, sem anisotropia.

**Carga:** anel da sling nativo(765,78), offset(-0,280,-40,458). Conectar gancho de guindaste ao anel superior, não a uma lona aleatória. Skids de madeira completos; caixas de contato aproximadas no manifesto. Em repouso, toda base deve assentar em cais/área seca; ao suspender, sling/carga segue uma conexão única real. Não bloquear a faixa principal nem colocar collider caminhável sobre o bundle. Detalhe material fica legível em110px; não repetir várias unidades iguais lado a lado por preenchimento.

**Decal:** não é tile de piso nem apoio; aplicar só por cima de madeira existente, preservando alpha. QA lado a lado mostra original e opacidades.20/.30; ambas mantêm as juntas/plank repairs visíveis. Evitar cobrir todos os módulos com o mesmo carimbo: usar poucos pontos coerentes com embarque/contato d'água. Não aplicar como faixa flutuando na água.

**Alternativa preservada:** `pier_head_v1.png`, rejeitada por área central estreita para patamar compacto; não integrar junto com deep. Nenhum PNG foi editado via Pillow; apenas previews derivados e cálculos. Os três selecionados RGBA têm alpha0 e bboxes visíveis contidos; margem mínima32/22/22px, inferior à meta confortável do prompt em alguns lados, mas sem corte visível.

**QA novo:** `complement_v1/qa_gameplay_connections.png`, peças1:1 em escala de mundo com retângulo central/conexões/bases; `complement_v1/qa_saltwear_on_timber.png`, comparação de opacidade em madeira da cabeceira. Reprodutor `tools/qa_docas_polish.py`. Composição alpha inspecionada: sem névoa visível, materiais e apoios íntegros.121 PNGs protegidos no snapshot original continuam idênticos, incluindo os quatro Docas e arte aprovada dos demais setores. Handoff para implantação: selecionar esses três complementos onde reforcem a estação de carga/transição marítima, conferir ligações e pano geral, sem considerar esta entrega aprovação do setor.
