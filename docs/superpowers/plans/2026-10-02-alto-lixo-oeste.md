# Alto-Lixo — definição espacial sobre a cidade atual

**Objetivo:** ocupar a lateral oeste/noroeste do Mercado, dando largura à cidade. Construir posteriormente na mesma cena `maps/sucateia/sucateia.tscn`. A etapa atual define a estrutura antes do detalhamento.

**Base:** mapa e screenshot atuais, sem reduzir Mercado, alterar seu piso ou substituir arte aprovada. Coordenadas são pixels de mundo, na escala existente de tiles de 48 px; norte corresponde a Y negativo. Alturas abaixo são intenções visuais, não um sistema de elevação já implementado.

## Fronteira e transição

Entrada principal: Beco das Ferragens → abertura oeste do Mercado, em (456, -504). A rota passa entre as fachadas existentes, pela faixa y=-500. Uma segunda conexão parte da Passagem dos Lotes, contorna o quarteirão noroeste e encontra a parte alta residencial. A conexão de serviço ao sudoeste oferece retorno sem obrigar o jogador a repetir o mesmo trajeto.

A transição ocupa x=240..620, y=-1060..100: comércio junto ao Mercado; casas com pequenos balcões no meio; casas sem barracas mais a oeste. Circulação passa de 130 px no Mercado para 100–112 px na transição e 76–88 px no bairro. Beco não pode ter menos de 56 px livres entre colisões. Pedra urbana vai sendo interrompida por terra, lama e drenagem. Cabos, tubulações e alinhamentos de telhados atravessam a fronteira.

## Território e hierarquia das vias

O contorno preliminar vai aproximadamente de x=-1440 a 620 e y=-1480 a 160, com limites irregulares. Não construir uma borda retangular nem usar esse envelope como muralha. O bairro cresce lateralmente; o caminho norte já existente do Mercado permanece uma possibilidade de continuação externa, não a espinha do Alto-Lixo.

| Via | Função | Traçado |
|---|---|---|
| Subida dos Remendos | Principal, entrada do Mercado ao pátio alto | (744,-504) → (456,-504) → (300,-552) → (120,-610) → (-100,-680) → (-400,-780) → (-600,-900) |
| Travessa dos Andaimes | Ligação noroeste, circuito alternativo | (1032,-944) → (970,-1020) → (840,-1110) → (600,-1140) → (310,-1070) → (100,-1100) → (-220,-1060) → (-600,-900) |
| Rua da Drenagem | Retorno sudoeste e manutenção | (830,160) → (700,100) → (420,100) → (240,80) → (40,-50) → (-100,-230) → (-230,-380) → (-100,-680) |

Três becos conectam o circuito: Beco das Calhas liga a Subida à Travessa; Beco dos Fundos conecta a Subida à Drenagem; Passagem das Amarras liga a Travessa ao pátio alto pelo lado oeste. Seus pontos exatos constam de `tools/alto_lixo_spatial_plan.json`. Não são cul-de-sacs decorativos nem linhas retas em grid.

## Patamares e núcleos residenciais

- **Soleira do Mercado, nível 0:** fronteira permeável; poucos balcões presos às casas, pedra predominante e um pequeno respiro de chegada.
- **Casas dos Remendos, +1,5 m visual:** primeiro conjunto residencial, entre x=-240..300. Degraus largos na entrada; anexos e quintais pequenos delimitam a Subida. Terra entre as pedras, calhas e mais drenagem.
- **Pátio dos Andaimes, +3 m visual:** núcleo central em (-600,-900); casas empilhadas enquadram um pátio assimétrico. Cisterna/telhado coletivo como futuro landmark funcional. Duas escadas e uma passagem de manutenção, sem grande praça vazia.
- **Cume das Calhas, +5 m visual:** arco noroeste, casas mais altas, passarelas entre conjuntos e becos estreitos. Suportes, fundações e paredes de contenção pintadas tornam os desníveis legíveis. Não adicionar barras de debug visíveis.

Passarelas altas servem a conexões locais; as vias principais continuam legíveis no chão. Não criar cruzamentos sobrepostos sem separar colisão/camada e acesso. Na implementação, escadas e patamares precisam ser percorríveis antes dos props.

## Saídas e continuidade regional

- Oeste, (-1400,-650): corredor externo de Ferrugem Baixa, mantendo terra e infraestrutura de drenagem. Destino específico ainda não fixado.
- Noroeste, (-1100,-1400): saída elevada para futuras subáreas externas; telhados/cabos prosseguem ao fundo.
- Sudoeste, (-850,120): continuidade de serviço em direção à região de Fundo-Ferro; conexão futura, sem afirmar que já está construída.
- Leste/nordeste do Mercado, x>=1680 e y<=180: reservar a Forjas Rasas. A extensão do Alto-Lixo não ocupa essa faixa.

As três saídas externas são corredores reservados, não portais de troca de cena. A costa existente permanece preservada. Nenhum piso será estendido sobre água sem cais/fundação coerente.

## Sequência de construção após esta definição

1. Preservar checkpoint e hash de MarketFloor; abrir o terreno lateral na mesma cena.
2. Construir os três trajetos, patamares, acessos e becos; validar ida/volta física.
3. Formar quarteirões assimétricos com os assets aprovados de casas, respeitando a escala original.
4. Preparar módulos adicionais somente onde anexos, landmark e desníveis exigirem arte específica gerada por imagem.
5. Integrar lama/pedra, fundações, cabos e calhas; manter os corredores de gameplay limpos.
6. Capturar vista geral, verificar largura real da cidade e a continuidade para Mercado; corrigir isolamento antes de concluir o bairro.

**Estado:** definição espacial concluída; bairro residencial ainda não construído. A mudança jogável desta etapa é apenas realocar a referência de saída do Mercado para a fronteira oeste correta.
