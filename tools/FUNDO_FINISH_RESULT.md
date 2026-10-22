# Fundo-Ferro — resultado do acabamento

Data: 2026-10-04 16:20 UTC  
Escopo concluído: acabamento visual aditivo do subsolo existente; esta entrega não declara Ferrugem Baixa inteira concluída.

## Resultado

- As sete salas agora têm detalhes funcionais contextualizados, e oito redes visuais derivam dos oito trajetos existentes com origem, destino e meio identificados.
- O manifold de distribuição em Válvulas usa um asset novo e seus dois sockets coincidem com os ramais; os apoios caem no piso seco. Ruínas recebeu um recorte colapsado discreto, apoiado e fora do corredor.
- As três entradas F, sete salas, oito rotas, duas pontes, pisos e água permanecem conforme o baseline. O script de acabamento não introduz corpos físicos nem muda colisões.
- As chegadas vindas de Fundo-Ferro para o centro tinham dois offsets que pousavam sobre piso inválido/obstruído. Ajustei somente os metadados de chegada em `maps/sucateia/sucateia.tscn`; a auditoria agora percorre 54 conexões dirigidas e retorna por E sem chegada insegura.

## Verificação executada

Executado com Godot 4.7.2 stable:

| Verificação | Resultado |
| --- | --- |
| `tests/test_fundo_finish.gd` | PASS — 7 funções visíveis, redes conectadas, baseline preservado |
| `tests/test_fundo_access.gd` | PASS — três entradas F bidirecionais, retorno R e spawns seguros |
| `tests/test_fundo_layout.gd` | PASS — 8 salas, 9 rotas, 2 pontes bidirecionais, piso e água |
| `tests/test_region_travel.gd` | PASS — 54 conexões dirigidas de ida e volta, chegadas seguras |

O ambiente imprime um aviso de leitura do repositório de certificados durante a inicialização. A captura gráfica também emite avisos de escrita do cache GLES; todas as oito imagens foram gravadas e têm hash SHA-256 no manifesto. Esses avisos não são apresentados como falhas dos testes.

## Capturas, revisão e checkpoint

Oito capturas estáveis (panorama e uma por sala) estão em `tools/fundo_finish_captures/`. Cada tomada aguardou 20 frames e `RenderingServer.frame_post_draw`; `manifest.json` registra versão da engine, dimensões reais e SHA-256. Fiz revisão visual local das oito imagens, conferindo legibilidade funcional, apoios, contato, espaço de circulação e coerência entre as salas. A revisão visual independente do consultor está solicitada; não a declaro até receber parecer.

Checkpoint da cena: `tools/checkpoints/fundo_after_finish_2026_10_04.tscn`  
SHA-256 do checkpoint e da cena ativa: `A1B9DCE39B196BD70781877B4FBFC2CEF79355C93623515680DFB8207B69037C`.

## Limite de escopo

Esta etapa fecha somente o acabamento do Fundo-Ferro e a verificação das chegadas necessárias às transições. Coroa de Lata, setores macro faltantes de Ferrugem Baixa e a auditoria regional completa seguem obrigatórios antes de Khemet-Ra / Império Sepultado.
