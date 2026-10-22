# Vhal-Kor — etapa preparada, sem integração ativa

## Estado real
Não há mapas de Vhal-Kor implementados ou validados. A etapa foi bloqueada pela revisão automática na importação do Godot. Ferrugem Baixa permanece com 16 mapas/54 conexões; manifest restaurado e teste regional PASS com exit 0.

## Preparado
Sete assets pelo gerador integrado: gothic_block, port_warehouse, twin_towers, arcane_station, river_crossing, stone_quay, stone_ground. Originais e versões preparadas em tools/pending_vhal/assets/vhal/. Prompts/proveniência em tools/vhal_art.json. Nenhum asset aprovado de Sucateia foi substituído.

Manifest pendente para Expedição Norte, Rota Fluvial, Caelporto, Bairros Inferiores e Torres Gêmeas em tools/pending_vhal/region.json. Construtor e teste de escopo preparados, ainda sem validação da implementação. O teste inicial constatou corretamente que as localidades não estavam implementadas.

## Bloqueio
A revisão automática rejeitou importar assets de Vhal-Kor por exceder o escopo confiável da tarefa. Também rejeitou a autorização humana recuperada do chat de supervisão como evidência suficiente nesta conversa. Não houve contorno; diretório de arte pendente tem .gdignore e nenhum portal ausente foi ativado. Necessária autorização direta do usuário nesta conversa antes de retomar a nova região.

## Pendências
Importar/construir somente após autorização; então validar as cinco cenas, travessia sobre água, partidas/retornos, perspectiva, escala, densidade e hashes. Capturas e auditoria visual de gameplay não existem ainda para Vhal-Kor. Não apresentar sprites gerados como prova de uma região construída.

Plano: tools/NORTH_CONNECTION_PLAN.md e docs/superpowers/plans/2026-10-02-vhal-kor-primeira-integracao.md. Checkpoint seguro anterior: tools/checkpoints/ferrugem_baixa_16_mapas.zip. Arquivos WORLD_* não foram alterados.
