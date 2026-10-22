# Vhal-Kor — primeira integração
Escopo autorizado pela mensagem humana original no chat de supervisão: continuar outras áreas do mapa após cada entrega. Esta etapa executa tools/NORTH_CONNECTION_PLAN.md e entrega recortes, não Vhal-Kor completa.

1. Preservar checkpoint/hashes de Ferrugem Baixa; manter teste de viagens existente.
2. Gerar sprites próprios: habitações góticas, armazém portuário, Torres Gêmeas, subestação arcana, travessia fluvial, margem de pedra e pavimento. Registrar prompts/fontes/licenças.
3. Estender manifest compatível com campos region/floor_texture; adicionar cinco cenas em maps/vhal_kor: expedição norte, rota fluvial, Caelporto, bairros inferiores e Torres Gêmeas.
4. Separar composição dos novos setores em scripts/world/vhal_builder.gd. Reutilizar jogador/viagem, sem duplicar sistemas. Portais de pedra nos mapas humanos. HUD/capturas devem refletir região e pasta reais.
5. Teste explícito requer cenas, região, ativos próprios, destinos locais e ligação a Chaminés. Executar travessia física e todas as conexões por E com retorno; regressão centro/hashes.
6. Capturar panoramas e vistas de jogo sem HUD; inspecionar água/limites, escala, perspectiva, densidade e colisões. Corrigir problemas antes do checkpoint.
7. Relatório tools/VHAL_KOR_STATUS.md com recortes concluídos/parciais, integração em REGION_STATUS.md e ZIP recuperável. WORLD_* ficam sob controle da supervisão.
