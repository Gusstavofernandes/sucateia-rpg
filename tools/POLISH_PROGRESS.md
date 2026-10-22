# Polimento físico — frente de arte

Responsável: conversa 01a0ff60-3f7e-7bd1-b8d8-3a8021fdbfe7.

## Reserva de arquivos

- `scripts/world/port_approach_finish.gd`
- `assets/reconstruction/port_approach/*`
- `tests/test_port_approach.gd`
- `tools/PORT_APPROACH_AUDIT.md`
- Este registro e capturas/logs com prefixo `port_`.

Não há reserva de cena central nem solicitação de edição central nesta etapa. As integrações existentes serão preservadas.

## Estado

Entrada do porto: dois assets gerados e integrados; substituição visual localizada das grades, canos isolados e sombras sobrepostas. Captura final conferida: rua e base da casa legíveis; transição pedra/madeira contínua; sem faixas UV esticadas. SHA256 registrado nos dois assets.

Godot: captura `port_approach` e 16 testes sequenciais encerrados com código 0. Livre para outra frente; não há import, teste ou captura desta frente em execução.

## Defeitos comprovados e soluções

- Entrada soterrada por grades, tubos verticais e sombras antigas: ocultação localizada das peças redundantes, conservando fonte/geografia/física.
- Rua sem plano de chão legível sob a casa: pavimento de pedra gerado, recortado ao contorno existente e ordenado abaixo da arquitetura.
- Ligação abrupta da rua ao deck: novo patamar pedra/madeira com fundação baixa e apoios.
- Primeiro acabamento com UV fora da imagem: coordenadas reduzidas para permanecer no tamanho nativo; captura final sem faixas esticadas.
- Ajustes anteriores preservados: 27 pilares com profundidade no pé; quatro escadas com oito encaixes opacos; quatro bueiros em contato com parede; alimentação de canos com junções dentro de 0,1 px.

## Auditoria da retomada

16 logs `tools/port_verify_*.log`: PASS, código 0 e nenhum erro de aplicação. Único diagnóstico comum: acesso ao repositório de certificados do Windows no sandbox. Render final terminou com código 0.

- Docas: 17 rotas de ida/volta; 2.776 centros livres respaldados por piso PNG; pés dos equipamentos em chão seco; cabos da barcaça nos sockets; rampa de lançamento entre plataforma e água; contenção da água e R seguros.
- Cabos: 3.458 centros seguros no piso elevado; 27 apoios sólidos; profundidade e transformações preservadas; acessos, patamares e circuitos de ida/volta.
- Amarras: oito seleções com hashes, bases sólidas, correntes nos terminais, acessos seguros, quatro pontes e circuitos de ida/volta.
- Forjas: cinco bases funcionais sólidas e cinco frentes de serviço acessíveis nos dois sentidos; ordenação com jogador.
- Costa: circulação e águas protegidas; seis trechos avaliados.
- Fundo: três acessos F de ida/volta, spawns e R seguros; um jogador.
- Alto: quatro patamares, casas antigas, piso e costa preservados.

Essas verificações não encontraram novos defeitos no escopo amostrado; não equivalem a auditoria exaustiva de cada pixel de todos os assets. Não foi alterada a cena central nesta retomada. Docas aprovadas preservadas.

Antes: `tools/port_approach_before.png` (print humano). Depois: `maps/sucateia/preview_port_approach.png` (render atual). Checkpoint localizado: `tools/checkpoints/port_approach_polish_2026-10-03.zip`, com manifesto de evidências e hashes; depende do projeto existente.
