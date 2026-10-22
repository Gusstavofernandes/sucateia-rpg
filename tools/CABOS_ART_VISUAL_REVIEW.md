# Os Cabos — revisão visual da frente de arte

Revisão somente leitura das sete capturas finais, todas1198×749px, e dos relatos `tools/CABOS_RESULT.md` / `tools/CABOS_REVIEW.md`. Coordenadas abaixo são pixels da imagem, origem no canto superior esquerdo. Nenhuma cena, asset, import ou runtime foi alterado/executado; somente este parecer foi escrito. Parecer externo do consultor permanece pendente com o supervisor.

**Resultado: não identifiquei defeito visual bloqueante nem lacuna de asset comprovada nestas capturas.** O deck largo resolve visualmente a via principal, com piso pintado entre corrimãos; ponte/T continuam visivelmente mais estreitos. Dois pontos de leitura/composição seguem como observações não bloqueantes, sem pedir nova geração. Esta revisão não certifica collision, rotas bidirecionais, hashes de arquitetura anterior ou equivalência de todos os apoios em runtime; os testes relatados pelo implementador não foram reexecutados aqui.

## Achados concretos

| Prioridade | Imagem e região aproximada | Observação | Implicação |
|---|---|---|---|
| P3, composição | [district](../maps/sucateia/preview_cabos_district.png), corredor inferior x210–988/y446–561; [full](../maps/sucateia/preview_cabos_full.png), x110–580/y213–374 | Repetição muito regular de módulos com a mesma placa/grade e apoios de torre cria duas linhas retas dominantes. A silhueta construída de Cabos se distingue fortemente do tecido irregular dos bairros. | A função de distribuição/travessia fica clara; a aparência de reparo improvisado é menos forte na escala do panorama. Observar no parecer consultivo antes de qualquer variação/decor. Não é falha de emenda ou necessidade comprovada de novo PNG. |
| P3, contato parcialmente encoberto | [alto](../maps/sucateia/preview_cabos_alto.png), escada esquerda x556–642/y417–584, encontro com telhado x568–631/y525–580 | A ponta inferior da escada fica encoberta pelo telhado da casa existente. É possível acompanhar a escada até essa sobreposição, mas o contato final com a rua não fica integralmente visível nesta imagem. | Menor clareza visual da chegada inferior do acesso Alto. Não concluir que flutua ou que está bloqueado: screenshot não demonstra isso, e o resultado relata testes de chegada. Se o consultor exigir contato mais explícito, resolver placement/enquadramento, preservando a casa aprovada; não gerar outra escada. |

## Evidência por critério

**Emendas/decks.** Em [junction](../maps/sucateia/preview_cabos_junction.png), faixa principal x0–1197/y420–515, as juntas verticais têm bandas rebitadas/overlap, sem fenda de fundo visível separando os módulos. Corrimãos acompanham as bordas norte/sul; não observei barra elevada transversal fechando o centro da via. Passarela N–S da casa encontra a faixa larga em x160–239/y421–508. A sobreposição é densa em ferragens, mas o piso segue reconhecível. Em [forjas](../maps/sucateia/preview_cabos_forjas.png), patamar x318–673/y337–418 e aproximação x357–423/y178–338 mostram as entradas com piso contínuo aparente. Fotografias estáticas não provam a continuidade física/collision.

**Suporte até o chão.** Em [junction](../maps/sucateia/preview_cabos_junction.png), pés de pedra em torno de(409,639),(697,639),(967,640) tornam a transferência de carga da via principal ao chão legível. Travessas superiores/diagonais têm continuidade com os corpos verticais e apoios inferiores. Em [forjas](../maps/sucateia/preview_cabos_forjas.png), apoios do patamar em torno de(475,542) e(459,602) terminam em bases de pedra, não em recorte no ar. Em [district](../maps/sucateia/preview_cabos_district.png), vários apoios ficam sobrepostos a casas, mas a vista próxima junction resolve os exemplos centrais. Não extrapolar essas amostras como inspeção individual de27/27 bases.

**Casa/T e origem/destino dos cabos.** Em [junction](../maps/sucateia/preview_cabos_junction.png), casa x155–331/y134–288 está entre os dois receptores altos x78–155 e x330–433, cuja estrutura desce até bases na região inferior. As correntes superiores do PNG encontram a zona das travessas/receptores, de modo que a casa não aparece suspensa só por cabos sem suporte. T central x365–832/y174–415 tem coluna/apoio abaixo da junção e ligações laterais; não há ponta principal abruptamente isolada no vazio. Cabos diagonais visíveis cruzam entre regiões de travessas/postes e bordas estruturais do deck. Vários pontos exatos ficam ocultos por lugs/casas/rails: a evidência confirma conexão visual aparente, não ajuste milimétrico de cada socket. Não identifiquei cabo principal com final livre claramente exposto no ar nestas vistas.

**Acessos.** [market](../maps/sucateia/preview_cabos_market.png) mostra avatar/prompt no patamar central~(599,365), escada norte chegando ao patamar e T ao sul. [alto](../maps/sucateia/preview_cabos_alto.png) mostra avatar/prompt~(600,357), deck alto apoiado e acesso frontal, com a ressalva do telhado acima. [forjas](../maps/sucateia/preview_cabos_forjas.png) mostra avatar/prompt~(599,358), chegada larga diante de oficinas, escada inferior íntegra até região~(600,532). Os três acessos são visualmente distinguíveis; uso F/retorno/respawn pertence à avaliação física do implementador.

**Escala/função econômica.** O avatar cabe com sobra nos patamares largos de market/alto/forjas; a principal pintada é substancialmente mais larga que os braços do T e a ponte secundária. Casa e mastro não parecem superdimensionados diante das casas antigas nas vistas próximas. Hoists/bobinas, mensageria/energia com pequenos pontos cianos, casa suspensa e ligações sobre comércio/oficinas dão função de transporte/manutenção/habitação, sem introduzir equipamento naval de Docas. A largura física72px relatada não foi inferida só do screenshot: a revisão de arte anterior mediu75,5px pintados no deck à escala indicada.

**Continuidade regional e passagem inferior.** [full](../maps/sucateia/preview_cabos_full.png) situa a rede elevada dentro da massa urbana existente, acima do encontro oeste/centro, e mantém Forjas/Amarras à direita. Não aparece nova ilha/terreno exclusivo de Cabos. [district](../maps/sucateia/preview_cabos_district.png) mantém casas e comércio visíveis nas ruas inferiores e a transição às oficinas à direita; fontes aprovadas não foram comparadas byte a byte nesta etapa. Em [underpass](../maps/sucateia/preview_cabos_underpass.png), avatar~(599,354) e prompt F Subir ficam legíveis através do fade localizado no núcleo da junção; face/silhueta verde distinguem-se do deck e terreno. O fade revela a sobreposição de camadas sem apagar o panorama inteiro. Ausência de bloqueio de movimentação não pode ser certificada por essa imagem.

## Capturas efetivamente inspecionadas — SHA256

- full: `6cc9c4a17a113db312f9afe17b12d6b5f80fc7b77d6f435df961f65d0421d102`
- district: `0b8bb0012ddefd52da352c87692c7b4e994aa473e91148fde9f5f4200d8aaefb`
- market: `896112a13d3dc4bab71338ee67d902c70d44dc19421e4098ed077430c7fd9b3c`
- alto: `91591f6cc8198dc0030ca2ac9eff6a2a18f5cf9b127bcdffef707defe632b606`
- forjas: `a08a49036a3697e73067eab543f4019629d1c599220c81412d9f3958175a18d6`
- junction: `a41754190e9c21cc066c5e10e03c6b7c92f2265814fc1bdd5f527b5f67dedca4`
- underpass: `d4b9d997b21531883b004872dfade3663df34d79fc1c5a702d05be1905157d57`

Estado final desta frente: revisão visual concluída, nenhum novo PNG solicitado/gerado. Seguir ao consultor externo pelo supervisor; este parecer não substitui a aprovação dele.
