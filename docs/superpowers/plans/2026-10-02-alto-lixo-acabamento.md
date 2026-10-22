# Alto-Lixo — acabamento da base atual

Autorização humana verificada no chat de supervisão: revisar a etapa corrente e delegar próximas áreas até completar o mapa. A costa inferior já foi entregue e revisada. Nesta etapa retomar somente Alto-Lixo; não ampliar território, não modificar pisos nem regenerar a cidade a partir de cenas históricas.

1. Guardar a cena atual com costa aprovada. Testar o estado de acabamento ainda ausente.
2. Acrescentar um módulo pintado de patamar residencial, gerado por imagem e referenciado no original.
3. Aplicar edição incremental sobre a cena salva: quarteirões complementares dentro do piso atual, patamares, apoios, entradas de casas, drenagem e pontos de orientação. Conservar moradias existentes e todas as rotas da planta.
4. Validar fisicamente dez destinos, seis vias/becos, quatro escadas, spawn/controles e regressões de costa e Mercado. Comparar três pisos e contorno/colisões costeiras com a cena anterior.
5. Capturar panorama e pátio/fronteiras; corrigir vazios, repetição e falta de apoios antes de concluir a etapa. Registrar limites de elevação visual e destinos externos ainda reservados. Salvar checkpoint.

Aplicador separado: tools/refine_alto_lixo.gd. Assim, nenhuma regeneração global pode apagar o contorno costeiro aprovado. Não editar os relatórios WORLD_* do supervisor e não importar Vhal-Kor.
