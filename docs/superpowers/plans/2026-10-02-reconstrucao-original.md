# Ferrugem Baixa — reconstrução sobre o original

Direção substitui a montagem de 16 cenas. Mapas noturnos são somente rascunhos de posição, função e conexões; jamais benchmark visual.

Base preservada: tools/checkpoints/sucateia_before_world_extension.tscn. O mapa jogável continua maps/sucateia/sucateia.tscn; nenhum distrito é ativado como outra cena.

Ordem: Mercado, Alto-Lixo, Forjas, Fundo-Ferro, Cabos, Docas, Coroa, Chaminés, Amarras, Galerias, Grande Ferrugem, Banco, Rebitadores, Transmissões, Vielas, Caldeiras.

Para cada setor: composição localizada -> assets com função -> integração ao piso -> colisões/rotas -> captura -> confronto com screenshot original -> correção. Só avançar se o setor conservar o nível do original. Não afirmar que todos estão prontos por terem colisões ou nomes.

Mercado: manter barracas/casas/oficina/reator aprovados; ampliar variedade comercial com carrinho de peças, carga agrupada e tecido; contato/sombra/sujeira; preservar eixos principais. Retirar passagens de troca de cena e registrar fronteiras futuras como vias do mesmo mapa.

Alto-Lixo: extensão física da viela norte do original; habitações com telhados dominantes, anexos, escadas e passarelas em composição assimétrica; sem copiar o pátio noturno fechado.

As experiências tools/extend_existing_world.gd e tests/test_continuous_world.gd foram suspensas por orientação do usuário. A cena original foi restaurada antes de reconstruir Mercado.
