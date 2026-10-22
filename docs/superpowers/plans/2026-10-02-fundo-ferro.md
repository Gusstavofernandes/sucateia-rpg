# Fundo-Ferro — camada subterrânea urbana

**Objetivo:** construir uma primeira área inferior explorável ligada fisicamente a Poço Velho/costa e à manutenção sul de Forjas, mantendo toda a superfície atual.

**Representação escolhida:** cena subterrânea independente por necessidade de camada. Isso impede sobreposição de telhados, chão e colisões com a cidade superior. Compartilha coordenadas locais de orientação, linguagem de materiais e o mesmo jogador/escala. Somente três acessos identificáveis mudam entre superfície/subsolo ao pressionar F em proximidade; nenhum antigo portal E entre bairros é reativado.

## Planta e funções

- Poço Velho: entrada urbana/costeira da superfície (1296,1572), salão inferior de acesso e distribuição no mesmo ponto de referência.
- Câmara das Bombas (1750,2000): esgoto, válvulas, tanque, drenos e passarela sobre água bloqueada.
- Galeria de Descarte (2300,2180): triagem antiga, sucata, depósitos laterais e acesso à escotilha da doca leste (superfície 2210,1668).
- Casa das Máquinas (2900,1770): máquina abandonada focal, reparos interrompidos e circulação em torno do conjunto.
- Reservatório do Limo (2700,1160): água residual e pontes, ligação com serviço industrial.
- Ruínas da Fundação (1750,1050): estruturas antigas sob a cidade e retorno ao Poço Velho.
- Sala das Válvulas (3100,640): aproximação à escada de manutenção de Forjas (superfície 3000,260; chegada inferior 3000,480).
- Circuito principal: Poço → Bombas → Descarte → Máquinas → Reservatório → Ruínas → Poço. Travessa secundária liga Descarte a Ruínas; galeria de manutenção leva do Reservatório a Válvulas. Não é um hub de portais.
- Paredes definem salas e túneis; poças/canais bloqueiam a água e preservam passagens. Pisos e footprint das máquinas mantêm escala do benchmark original.

## Continuidade regional

Materiais, drenos e tubos ligam a costa às bombas; estoques descartados sob as oficinas explicam o circuito; tubulações industriais de Forjas reaparecem na Sala das Válvulas. Poço, escotilha costeira e escada industrial têm retornos correspondentes. Referência: `sobre.txt` §§17.7,25–28 e o atlas macro. Vhal-Kor não é incluída.

## Implementação e verificação

- [x] Congelar superfície atual em `tools/checkpoints/sucateia_before_fundo.tscn`. Escrever testes que falham por camada ausente.
- [x] Gerar módulos de parede/ruína e máquina abandonada no imagegen integrado, coerentes com benchmark original; registrar prompts/fontes.
- [x] Construir `maps/fundo_ferro/fundo_ferro.tscn` com sete salas, circuito, passagens secundárias, arte final, limites físicos e jogador único. Builder novo não reaplica a superfície.
- [x] Adicionar somente acessos de camada e autoload próprio, spawns bidirecionais e retorno/R seguros; identificar F em proximidade, E antigo permanece inativo.
- [x] Testar todas as salas e trechos, água e máquinas bloqueadas, três acessos ida/volta acionados por input real, cena correta, spawn seguro e um jogador.
- [x] Regredir superfície, capturar salas/acessos/panorama, avaliar composição, auditar limites e salvar checkpoint com CRC.

**Limites:** primeira etapa exterior do subsolo, sem interiores de habitações, combate, economia ou simulação de gangues/criaturas. Saídas futuras inferiores apenas reservas. Aguardar revisão antes de outro setor.
