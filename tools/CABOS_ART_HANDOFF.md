# Os Cabos — auditoria de arte e medidas para integração

Brief aplicado: `tools/CONSULTANT_CABOS_BRIEF.md`. Propriedade desta frente: metadados, documentação e QA de arte. Nenhuma cena, import, builder ou runtime executado/alterado.

**Decisão inicial: zero novas escadas/torres. Complemento após placement: um deck principal E–O.** As duas lacunas potenciais de acesso/suporte têm equivalentes existentes: `assets/infrastructure/stairs.png` para acesso gradual chão/passarela e `assets/region/cable_tower.png` para suporte/ancoragem intermediária. Não gerar escada/torre duplicada. A adequação final depende da altura e placement escolhidos; a escada curta não cobre sozinha um desnível de torre completa. Pedido posterior `tools/CABOS_ART_REQUESTS.md` identificou uma função distinta sem equivalente: deck compacto largo E–O, entregue abaixo.

## Arquivos prontos para a frente de implantação

- `assets/reconstruction/cabos_parallel/audit_v1/manifest.json`: oito arquivos auditados, hashes SHA256, alpha/bounds, escala uniforme sugerida, terminais nativos e offsets em pixels de mundo, contato de base aproximado, limitações.
- `assets/reconstruction/cabos_parallel/audit_v1/qa_gameplay_connections.png`: escala1:1 de mundo nas escalas propostas, régua24px, terminais cianos e bases amarelas. É composição de QA, não cena/panorama jogável.
- `tools/audit_cabos_art.py`: reprodutor de métricas/preview, apenas lê os PNGs fonte. Não importa no Godot.

As medidas visuais são estimativas ±10px nativos nos sprites grandes e ±3 nos pequenos; não são collision shapes. Fórmula para Sprite2D centralizado sem rotação: ponto global = posição do sprite + (ponto nativo − canvas/2) × escala uniforme. Para transformações de pais/flip/rotação, aplicar a transformação completa. Bbox de alpha não é footprint.

## Quatro PNGs Cabos existentes — correções de escala

| Arquivo | Escala sugerida | Objeto visível em px mundo | Leitura e limite |
|---|---:|---:|---|
| hanging_house.png |0,28|367×298|Porta~22px; as recomendações antigas230–270px totais diminuem a porta excessivamente. Corpo doméstico~280px. Fixar as duas travessas superiores em estruturas reais; corrente não deve terminar no ar. Limiar é o ponto door_s, não a base do canvas.|
| suspension_bridge_ew.png |0,26|551×93|Profundidade livre projetada~27–39px, variável pelo arqueamento. Usar travessia secundária estreita, sem spawn. Não confundir93px de bbox com largura caminhável.|
| walkway_t_junction_clean.png |0,38|570×333|Ramo norte~36–46px livres; E–O~32–40px de profundidade projetada. Na antiga largura350–420px, a circulação é ainda menor. Sem espaço para spawn1,5–2larguras. Precisará apoio sob o centro, além de ancoragem nas três pontas.|
| power_messenger_anchor.png |0,16|133×172|Energia/mensagens; footprint pequeno. Não presumir capacidade de sustentar casa/ponte principal. Sockets oeste e leste ficam em alturas distintas.|

As quatro peças mantêm câmera elevada sul→norte, luz superior esquerda, ferro enferrujado/cobre/madeira remendada e terminais completos. Composição RGBA confirma que a aparente névoa na visualização direta é RGB sob alpha zero. Margens visíveis verificadas. Estado é arte utilizável com limites explícitos; não aprovação do setor ou de circulação.

## Reaproveitamento e suporte

| Existente | Escala inicial | Uso |
|---|---:|---|
| assets/infrastructure/stairs.png |0,65|Escada frontal, topo norte/base sul;49–86px livres aproximados. Gargalo no topo. Pode crescer uniformemente se necessário, verificando altura real.|
| assets/infrastructure/walkway.png |0,60|Trecho mais largo N–S e aproximação de acesso,66–102px livres. Deve receber apoio próprio em placement. Não girar90° para fabricar E–O com iluminação/perspectiva incorretas.|
| assets/region/cable_tower.png |0,40|Torre estrutural existente137×304px visíveis; base~96×36px. Ligações nas travessas/torre para extremos de ponte e reforço do T, fora do corredor inferior. Terminais oeste/leste não têm o mesmo y. Ajustar ligações separadamente, sem esticar o PNG.|
| assets/infrastructure/service_arch.png |0,80|Arco de contato baixo na chegada Forjas. Não resolve sozinho apoio de uma seção muito elevada.|

Amarras: torre de tensão/contraforte podem ser reutilizados na borda Forjas se necessário, mas os terminais de corrente são de outra família; não são encaixe direto certificado com cabos. Forjas: passarela curta/tubo apoiado são manutenção/produção, não substitutos de acesso público alto. Suporte de sela sustenta tubo e não ponte. Docas: preservar os quatro PNGs para etapa futura, sem puxar conteúdo naval para Cabos.

Para a casa, usar torre(s)/viga existente(s) alinhadas às travessas beam_w/beam_e e prolongamento estrutural da cena; o PNG não contém estrutura de chão. Para T, alinhar apoio reforçado na zona support_center e sustentar também terminais. Torres têm escada de manutenção, inadequada como única entrada pública; reutilizar a escada frontal para acessos graduais. Qualquer rota principal/spawn exige trechos/plataformas mais largos da geometria existente; nenhum PNG deste lote garante ida/volta entre Mercado, Alto-Lixo e Forjas. A frente de cena verifica altura, sombra, occlusion, collision, spawns e três acessos em runtime.

## QA e preservação

O script registrou105 PNGs protegidos de Cabos/Docas/Forjas/Amarras e infraestrutura/região. Hashes mantidos em `protected_png_hashes` no manifesto. Todos permaneceram idênticos durante a auditoria. Nenhum novo asset aprovado foi substituído. Inspeção visual realizada no preview de gameplay com alpha composto. A frente de arte encerra sem nova geração até uma lacuna concreta de placement invalidar os equivalentes existentes.

## Complemento solicitado — deck principal E–O

Pedido aplicado: `tools/CABOS_ART_REQUESTS.md`. Inventário adicional revisado: `assets/generated/props/bridge.png` e `short_service_catwalk.png` têm corredor insuficiente ao reduzir para210–230px de extensão; `cargo_tiedown_platform.png` tem centro estreito/ferragens para logística; `bridge_segment.svg` tem estética simples sem extração/perspectiva do benchmark. Walkway N–S não foi girado. Nenhuma nova escada/torre.

**Selecionado:** `assets/reconstruction/cabos_parallel/main_deck_ew_wide.png`. Built-in image_gen com duas revisões de profundidade. Canvas1596×985 RGBA; objeto alpha>16 em19,45–1578,960, margem mínima18px; nenhum objeto visível cortado. Meta de margem8% não foi atingida, mas os limites visíveis estão contidos. Variantes `main_deck_ew_v1.png` e `main_deck_ew_v2.png` preservadas, rejeitadas pela faixa estreita; não integrar.

- Escala uniforme do canvas **0,1411161**; largura visível220px e profundidade total129,12px. Não usar220/canvas para calcular escala, pois existe margem.
- Retângulo conservador central de pintura livre: nativo180,155–1410,690 → **173,57×75,50px de mundo**, sem contar corrimãos, lugs ou apoios. Extensão completa entre bandas terminais~181,33px. Estimativa visual ±10px nativos (~1,4px mundo); mesmo com recuo conservador de20px nativos na profundidade, sobra~72,7px.
- Terminais de caminhada: oeste155,422; leste1440,422. Offsets de Sprite2D centralizado: oeste(-90,738,-9,949), leste(90,597,-9,949). Extremidades abertas sem barra transversal elevada; bandas rebitadas são planas. Não adicionar colisão vertical nas bandas.
- Furos das lugs: Wn84,205 / En1510,205; Ws51,714 / Es1547,714. Pares horizontais na mesma linha. Não confundir lugs com terminal da caminhada.
- Sockets inferiores: W400,935 e E1190,935 → offsets(-56,164,62,444) e(55,318,62,444). Triângulos e viga completos, sem pés de chão. Precisam encontrar vigas/torres existentes com posição e altura coerentes; não flutuar. Bboxes aproximados de sockets no manifesto.
- Passo inicial de repetição **181,334px** entre centros. QA de dois módulos mostra encontro contínuo das bandas, com sobreposição lateral das lugs/rails. É ajuste visual inicial, não solução certificada de collision: conferir costura e possível recuo de~2–5px no placement. Manter y/elevacão iguais. Não rotacionar a câmera embutida nem deformar anisotropicamente.

QA: `assets/reconstruction/cabos_parallel/audit_v1/qa_main_deck_gameplay.png`, escala de mundo1:1, retângulo útil marcado, conexões/apoios e dois módulos repetidos, comparação com ponte estreita existente. Alpha composto confirma ausência de névoa e imagem limpa. Manifesto: `main_deck_manifest.json`; prompts/fontes integrais: `main_deck_prompts.json`; reprodutor: `tools/qa_cabos_main_deck.py`. SHA256 selecionado:615dbf4fbe4f3fd025b6b396f2e46c2955afa150b98a67b6f2131e9b52a85370.

Verificação final:105 PNGs protegidos do inventário inicial permanecem idênticos; quatro Cabos originais, Docas e demais aprovados preservados. Nenhuma cena/import/runtime executado nesta frente. Este deck cobre a lacuna de pintura70–85px, mas aprovação da rede, spawns, acessos bidirecionais e collision/occlusion continua com o implementador.
