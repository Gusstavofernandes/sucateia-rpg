# Coroa de Lata — implementação em verificação

Atualização: 04/10/2026. A região continua em andamento; não anunciar como concluída.

## Levantamento e escolha

`tools/audit_coroa_space.gd` remove o builder experimental antes de sondar a cena canônica. `tools/audit_coroa_candidate_sites.gd` compara piso/corpo com a área visual de cada objeto existente. O bolso sem sobreposição junto ao eixo cívico está centrado em `(1560,400)`; candidatos mais ao norte ou leste foram preteridos por afastamento das ruas de serviço e proximidade de contenções.

## Construção atual

- Marco `crown.png` limitado a `144 × 164`, apoiado por base de contato em `(1560,463)`; chegada cívica no piso em `(1560,568)`.
- Registro/arbitragem em casa compacta `(1412,399)`, com fundação; limiar de pedra pequeno, mural de audiências com dois apoios, luz a pavio e wayfinding cívico.
- Defesa pública indicada no mural. O antigo posto triangular de sinalização foi removido porque parecia solto e entrava na faixa de tubulação.
- Preserva as duas casas do inventário e as rotas existentes. Sem comércio, oficina ou rede elétrica/hidráulica inventada. Zeladoria abastece as três lanternas com óleo.

## Testes e limitações

`tests/test_coroa_district.gd` imprimiu os quatro caminhos encontrados para Mercado, Os Cabos, núcleo e Forjas, atravessou cada um nos dois sentidos com o corpo do jogador e registrou os caminhos sobre piso transitável. Os quatro marcadores de rota e aproximação agora terminam no mesmo limiar seguro. Embora o script imprima `COROA_DISTRICT PASS`, não contamos esse resultado como QA completo: essa execução também reportou falhas de alocação/import em texturas do restante do mapa.

Verificação independente posterior: `python tools/audit_coroa_source_assets.py` confirmou assinatura e CRC de todas as 82 PNGs referenciadas pela superfície ativa e pelo builder, total 109,750,588 bytes, sem fonte ausente/corrompida. Isto afasta defeito nos arquivos-fonte verificados, mas não corrige/valida o cache comprimido da execução Godot.

`tests/test_coroa_builder.gd` passou isoladamente (`COROA_BUILDER PASS routes=4 contacts=4 source_textures=5 lines=0`): os marcadores de cada abordagem terminam na chegada pública, contatos estão descritos, função/registros estão presentes, e as cinco texturas usadas diretamente pelo builder carregam. Isso confirma o builder e seus próprios recursos em execução pequena; não substitui a carga/captura da cena ativa completa.

A confirmação final está bloqueada por falha ambiental observada: durante carregamento da cena canônica, Godot não consegue reservar memória ao decodificar algumas texturas importadas (`Parameter mem is null`; o import do editor também reportou limite de paging `0x800705AF`). O checker da captura rejeitou a execução; `maps/sucateia/preview_coroa_study.png` é captura anterior à remoção do posto e não serve de prova final. Não apagar cache nem atestar QA visual com esse arquivo. As mensagens de root certificates/log directory são ruído do ambiente e não explicam a captura recusada.

## Falta antes de avançar

1. Repetir teste e captura da cena canônica após carga estável, sem erros de import de imagem.
2. Revisar a nova captura em contexto com ruas/edificações existentes; corrigir sobreposições de renderização, passos, fundações ou letreiros.
3. Registrar hash/caminho e checklist final; então atualizar ordem/progresso e só depois iniciar Banco de Destroços.

## 04/10/2026 17:59 — diagnóstico de carga

- Inventário de dimensões IHDR das 82 PNGs citadas pela cena ativa e pelo builder: aproximadamente 351,3 MiB apenas para RGBA decodificado, sem contar cópias/import/cache e renderização.
- Snapshot do sistema durante o bloqueio: 302 MiB de memória física disponível (94% em uso) e 664 MiB de limite de pagefile disponível. Isso explica por que a carga da cidade pode falhar apesar das imagens-fonte válidas.
- Nenhuma tentativa de limpar cache ou forçar carga pesada; manter captura integrada pendente até haver recursos suficientes.

## 04/10/2026 18:06 — captura e revisão visual concluídas

- Identificada e encerrada somente a leva de sete processos Godot sem janela que ainda executava o comando exato `--headless --path . --script res://tests/test_coroa_district.gd` desde tentativas anteriores; após isso a memória física disponível subiu para cerca de 1.037 MiB e o limite de commit disponível para 4.301 MiB.
- A cena canônica carregou sem erros de recursos/imagens e gerou `deliveries/coroa_civic_district_verified.png` (1198×749, SHA-256 `D55B30328FAB3CCA6F4DF134E53251B34775DA81CDD467BB37B2BED626E46ABC`), com 206 draw calls e 5.853 nós.
- Revisão visual: marco e casa de registro encaixam no quarteirão existente; a pequena praça e o quadro de avisos permanecem legíveis junto ao pavimento. A linha de serviço preexistente termina antes do limiar cívico e não cruza a chegada.
- Regressão independente da cena: `COROA_DISTRICT PASS grounded_routes=4 bidirectional=4 homes_preserved=2 exposed_utility_lines=0` (exit 0). Builder isolado: `COROA_BUILDER PASS routes=4 contacts=4 source_textures=5 lines=0` (exit 0). Auditoria de 82 PNGs referenciadas: zero ausentes ou corrompidas.
- A captura integrada desta etapa está verificada. A Ferrugem Baixa como região completa permanece em construção; não avançar a Banco antes dos demais critérios de ordem/região.

- Envio concluído: print da área cívica entregue à conversa própria do WhatsApp em 04/10/2026 15:15, com confirmação visual e hash registrados em `deliveries/WHATSAPP_PRINTS.json`. A captura enviada é a mesma revisão final acima; nenhuma captura intermediária foi enviada.



## 04/10/2026 18:06 UTC — checkpoint e inventário reconciliados

- Checkpoint local de evidência/rollback criado: `tools/checkpoints/coroa_civic_verified_2026_10_04.zip`, 18 arquivos; manifesto SHA-256 por arquivo em `tools/checkpoints/coroa_civic_verified_2026_10_04.json`; SHA-256 do arquivo ZIP `de44de1df432c2eaac3d99b817d46aef43525b10d19837abc9cf765b917bec3c`. O ZIP é apenas checkpoint local e não foi enviado.
- `tools/FERRUGEM_REAL_INVENTORY.md` reconciliado para distinguir o `CoroaDistrict` ativo do protótipo histórico e registrar a evidência/testes atuais. O restante de Ferrugem Baixa não foi marcado como concluído.
- Consultoria visual externa da captura atual não foi concluída nesta sessão; o acesso ao painel de anexos do navegador expirou em duas tentativas, e nenhum pedido/captura foi enviado ao consultor. A revisão visual local e os testes acima permanecem a base verificável; não afirmar parecer externo.
- Sequência após Coroa: Banco de Destroços, Estrada dos Rebitadores regional, Grande Ferrugem, Chaminés Velhas, Engrenópolis, auditoria integral e somente então Khemet-Ra. Não iniciar região nova até consolidar a revisão visual/checkpoint e a consulta pendente do ciclo atual.
