# Costa inferior — resultado

Escopo aplicado somente abaixo de y=1170 sobre a cena atual. Núcleo urbano e 16 posições de arquitetura original mantidos. MarketFloor, AltoFloor e TerraceFloor acima desse limite foram comparados célula a célula com a cena anterior.

## Forma e camadas

O canto sudoeste recua em etapas; duas entradas de água interrompem a borda sul; o cais sudeste tem um recuo lateral. A saída do canal industrial permanece aberta. Três docas ligadas ao solo têm comprimentos e suportes diferentes, com escadas, estacas, grades, cabos e pequenas zonas de manutenção.

As quatro faixas são legíveis: núcleo urbano atrás da contenção interna, pavimento gasto de transição, muralha costeira remendada e estruturas sobre a água. O reator inferior conserva sua posição, apoiado em um ressalto com passagem de manutenção. A conexão de Fundo-Ferro mantém sua margem livre.

**Avaliação da screenshot:** a massa inferior deixou de ter uma silhueta de retângulo único. A água entra entre os ressaltes e docas, e a borda varia em profundidade. A contenção interna continua sendo uma estrutura urbana construída; não é mais o limite externo do mapa. A composição lê como um trecho costeiro feito por camadas, preservando o núcleo aprovado.

Capturas: `maps/sucateia/preview_lower_coast.png` e `preview_lower_detail.png`. Arte da etapa usa módulos gerados já existentes; não houve substituição dos PNGs aprovados nem nova expansão regional.

## Verificação atual

- `test_lower_coast.gd`: seis destinos costeiros com ida/volta, cinco amostras de água bloqueadas, terreno superior e arquitetura original preservados.
- `test_slice.gd`: nove percursos originais, canal/costa, colisões, WASD, Shift e R.
- `test_market_expansion.gd`: oito destinos e todos os trechos dos três becos do Mercado.
- Dois acessos corrigidos após falha: margem de manutenção da bomba e margem de chegada a Fundo-Ferro.
- Cinco PNGs aprovados protegidos por SHA-256. Checkpoint com CRC verificado.

Alto-Lixo permanece no estado salvo anterior a este retrabalho: base residencial lateral construída, com refinamento ainda pendente. A solicitação atual interrompeu esse detalhamento e não alterou seu terreno. Os 16 setores históricos não são declarados reconstruídos.
