# Auditoria das escadas — 2026-10-03

Pedido: corrigir escadas soltas nas referências de Forjas/Os Cabos e Costa/Manutenção, gerando dois assets compatíveis com seus pontos reais de conexão.

## Medições e aplicação

- Inventário físico: 38 sprites antigos. Relatório completo em `stair_physical_audit.json`, com posições das extremidades, chão existente e consultas de colisão para raio de jogador de 11 px.
- Os Cabos: seis sprites de grade empilhados foram substituídos visualmente por três lances contínuos de madeira, um em cada acesso. A madeira, as chapas de reparo e os tubos seguem o deck existente. Superior em `elevated_arrival + (0,32)`, com sobreposição de aproximadamente 6 px na faixa de tábuas frontal; último degrau em `surface_arrival`.
- Costa: abertura física do muro entre x=1440 e x=1584, centro x=1512. O novo lance encaixa o patamar em (1512,1378) e o degrau inferior em (1512,1472). Ombreiras sobrepõem as pontas do muro; circulação real testada em x=1490,1512,1534.
- Ajuste dos sprites por dois pontos medidos no PNG, sem editar a imagem gerada. Transformação com tolerância de 0,01 px nos oito pontos de encaixe. Esta é precisão em coordenadas do jogo, não uma unidade física em milímetros.
- Dois PNGs transparentes criados pelo gerador integrado ImageGen, persistidos em `assets/reconstruction/stair_fits/`. Prompts completos, pontos e escalas no manifesto da mesma pasta.

## Limites e ocorrências adicionais

O acesso elevado mantém a transição existente pela tecla F. A nova escada não cria uma rampa continuamente navegável entre as duas camadas. O teste percorre a costa fisicamente e verifica as chegadas do deck nas respectivas máscaras de colisão.

Três sprites antigos têm colisão de superfície em ao menos uma extremidade pintada: `GoblinIndustrialQuay/@Sprite2D@703`, `MarketDistrict/GroundIntegration/@Sprite2D@505` e `LayerEntrances/@Sprite2D@1253`. São ocorrências para inspeção contextual, não diagnóstico automático de rota bloqueada: peças de ambientação e entradas de outra camada podem terminar junto de uma parede. Não foram reposicionados nesta correção.

## Verificação

`test_stair_fits`: quatro lances, oito encaixes opacos a menos de 0,01 px do destino, chegadas livres nos três acessos e travessia física da costa em três faixas, ida e volta.

Regressões: `test_cabos_layers`, `test_cabos_art_contacts`, `test_cabos_support_depth`, `test_cabos_preservation`, `test_lower_coast`. Todos os seis testes passaram na execução local do Godot.

Capturas revisadas: `preview_cabos_forjas.png`, `preview_stairs_coast.png`, `preview_cabos_market.png`, `preview_cabos_alto.png`, em `maps/sucateia/`.
