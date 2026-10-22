# Ferrugem Baixa — contratos de continuidade
Cada cena é um recorte. Posições regionais são esquema de composição, não coordenadas métricas do mundo.

## Mercado dos Restos
Função: comércio e distribuição das rotas de Sucateia.
| Vizinho | Atravessa a fronteira | Referência distante | Transição |
|---|---|---|---|
| Alto-Lixo | rua gasta, cabos, anexos | region/tenement.png | comércio e distribuição das rotas de Sucateia → moradia em camadas e ligação às oficinas |
| Forjas Rasas | tubulação, suportes, desgaste industrial | region/foundry.png | comércio e distribuição das rotas de Sucateia → produção e alimentação industrial |
| Os Cabos — Ponte das Correntes | passarela, cabos, correntes | region/cable_tower.png | comércio e distribuição das rotas de Sucateia → circulação suspensa entre níveis |
| Fundo-Ferro — Poço Velho | tubulação, suportes, desgaste industrial | generated/structures/skyline.png | comércio e distribuição das rotas de Sucateia → drenagem e serviços inferiores |
| Docas — Cais de Sucateia | costa, contenção, amarras | region/dock_warehouse.png | comércio e distribuição das rotas de Sucateia → expedição de carga e costa |

## Alto-Lixo
Função: moradia em camadas e ligação às oficinas.
| Vizinho | Atravessa a fronteira | Referência distante | Transição |
|---|---|---|---|
| Mercado dos Restos | rua gasta, cabos, anexos | generated/structures/skyline.png | moradia em camadas e ligação às oficinas → comércio e distribuição das rotas de Sucateia |
| Coroa de Lata — Torre do Catador-Rei | rua gasta, cabos, anexos | region/crown.png | moradia em camadas e ligação às oficinas → marco de poder e orientação urbana |
| Chaminés Velhas — Usina Quebrada | tubulação, suportes, desgaste industrial | region/chimney_bank.png | moradia em camadas e ligação às oficinas → usina e limite industrial norte |
| Fundo-Ferro — Poço Velho | tubulação, suportes, desgaste industrial | generated/structures/skyline.png | moradia em camadas e ligação às oficinas → drenagem e serviços inferiores |
| Os Cabos — Ponte das Correntes | passarela, cabos, correntes | region/cable_tower.png | moradia em camadas e ligação às oficinas → circulação suspensa entre níveis |

## Forjas Rasas
Função: produção e alimentação industrial.
| Vizinho | Atravessa a fronteira | Referência distante | Transição |
|---|---|---|---|
| Mercado dos Restos | tubulação, suportes, desgaste industrial | generated/structures/skyline.png | produção e alimentação industrial → comércio e distribuição das rotas de Sucateia |
| Chaminés Velhas — Usina Quebrada | tubulação, suportes, desgaste industrial | region/chimney_bank.png | produção e alimentação industrial → usina e limite industrial norte |
| A Grande Ferrugem — Campos de Sucata | tubulação, suportes, desgaste industrial | region/scrap_colossus.png | produção e alimentação industrial → recuperação de máquinas e suprimento de sucata |
| Fundo-Ferro — Poço Velho | tubulação, suportes, desgaste industrial | generated/structures/skyline.png | produção e alimentação industrial → drenagem e serviços inferiores |

## Os Cabos — Ponte das Correntes
Função: circulação suspensa entre níveis.
| Vizinho | Atravessa a fronteira | Referência distante | Transição |
|---|---|---|---|
| Mercado dos Restos | passarela, cabos, correntes | generated/structures/skyline.png | circulação suspensa entre níveis → comércio e distribuição das rotas de Sucateia |
| Alto-Lixo | passarela, cabos, correntes | region/tenement.png | circulação suspensa entre níveis → moradia em camadas e ligação às oficinas |
| Coroa de Lata — Torre do Catador-Rei | passarela, cabos, correntes | region/crown.png | circulação suspensa entre níveis → marco de poder e orientação urbana |
| Docas — Cais de Sucateia | passarela, cabos, correntes | region/dock_warehouse.png | circulação suspensa entre níveis → expedição de carga e costa |

## Fundo-Ferro — Poço Velho
Função: drenagem e serviços inferiores.
| Vizinho | Atravessa a fronteira | Referência distante | Transição |
|---|---|---|---|
| Mercado dos Restos | tubulação, suportes, desgaste industrial | generated/structures/skyline.png | drenagem e serviços inferiores → comércio e distribuição das rotas de Sucateia |
| Alto-Lixo | tubulação, suportes, desgaste industrial | region/tenement.png | drenagem e serviços inferiores → moradia em camadas e ligação às oficinas |
| Forjas Rasas | tubulação, suportes, desgaste industrial | region/foundry.png | drenagem e serviços inferiores → produção e alimentação industrial |
| Docas — Cais de Sucateia | tubulação, suportes, desgaste industrial | region/dock_warehouse.png | drenagem e serviços inferiores → expedição de carga e costa |
| Galerias do Poço Velho | escotilha, tubulações, drenagem | generated/structures/skyline.png | drenagem e serviços inferiores → manutenção das bombas do Poço Velho |

## Coroa de Lata — Torre do Catador-Rei
Função: marco de poder e orientação urbana.
| Vizinho | Atravessa a fronteira | Referência distante | Transição |
|---|---|---|---|
| Alto-Lixo | rua gasta, cabos, anexos | region/tenement.png | marco de poder e orientação urbana → moradia em camadas e ligação às oficinas |
| Os Cabos — Ponte das Correntes | passarela, cabos, correntes | region/cable_tower.png | marco de poder e orientação urbana → circulação suspensa entre níveis |
| A Grande Ferrugem — Campos de Sucata | trilha de carga, placas, remendos | region/scrap_colossus.png | marco de poder e orientação urbana → recuperação de máquinas e suprimento de sucata |

## Docas — Cais de Sucateia
Função: expedição de carga e costa.
| Vizinho | Atravessa a fronteira | Referência distante | Transição |
|---|---|---|---|
| Mercado dos Restos | costa, contenção, amarras | generated/structures/skyline.png | expedição de carga e costa → comércio e distribuição das rotas de Sucateia |
| Os Cabos — Ponte das Correntes | passarela, cabos, correntes | region/cable_tower.png | expedição de carga e costa → circulação suspensa entre níveis |
| Fundo-Ferro — Poço Velho | tubulação, suportes, desgaste industrial | generated/structures/skyline.png | expedição de carga e costa → drenagem e serviços inferiores |
| A Grande Ferrugem — Campos de Sucata | costa, contenção, amarras | region/scrap_colossus.png | expedição de carga e costa → recuperação de máquinas e suprimento de sucata |
| Passagem das Amarras | costa, contenção, amarras | generated/structures/skyline.png | expedição de carga e costa → circulação e amarras junto à água |

## A Grande Ferrugem — Campos de Sucata
Função: recuperação de máquinas e suprimento de sucata.
| Vizinho | Atravessa a fronteira | Referência distante | Transição |
|---|---|---|---|
| Forjas Rasas | tubulação, suportes, desgaste industrial | region/foundry.png | recuperação de máquinas e suprimento de sucata → produção e alimentação industrial |
| Coroa de Lata — Torre do Catador-Rei | trilha de carga, placas, remendos | region/crown.png | recuperação de máquinas e suprimento de sucata → marco de poder e orientação urbana |
| Docas — Cais de Sucateia | costa, contenção, amarras | region/dock_warehouse.png | recuperação de máquinas e suprimento de sucata → expedição de carga e costa |
| Chaminés Velhas — Usina Quebrada | tubulação, suportes, desgaste industrial | region/chimney_bank.png | recuperação de máquinas e suprimento de sucata → usina e limite industrial norte |
| Estrada dos Rebitadores | trilha de carga, placas, remendos | generated/structures/skyline.png | recuperação de máquinas e suprimento de sucata → transporte entre sucata e oficinas |

## Chaminés Velhas — Usina Quebrada
Função: usina e limite industrial norte.
| Vizinho | Atravessa a fronteira | Referência distante | Transição |
|---|---|---|---|
| Alto-Lixo | tubulação, suportes, desgaste industrial | region/tenement.png | usina e limite industrial norte → moradia em camadas e ligação às oficinas |
| Forjas Rasas | tubulação, suportes, desgaste industrial | region/foundry.png | usina e limite industrial norte → produção e alimentação industrial |
| A Grande Ferrugem — Campos de Sucata | tubulação, suportes, desgaste industrial | region/scrap_colossus.png | usina e limite industrial norte → recuperação de máquinas e suprimento de sucata |

## Galerias do Poço Velho
Função: manutenção das bombas do Poço Velho.
| Vizinho | Atravessa a fronteira | Referência distante | Transição |
|---|---|---|---|
| Fundo-Ferro — Poço Velho | escotilha, tubulações, drenagem | generated/structures/skyline.png | manutenção das bombas do Poço Velho → drenagem e serviços inferiores |

## Passagem das Amarras
Função: circulação e amarras junto à água.
| Vizinho | Atravessa a fronteira | Referência distante | Transição |
|---|---|---|---|
| Docas — Cais de Sucateia | costa, contenção, amarras | region/dock_warehouse.png | circulação e amarras junto à água → expedição de carga e costa |
| Banco de Destroços | costa, contenção, amarras | region/wreck_cradle.png | circulação e amarras junto à água → recuperação de cascos e atracação |

## Banco de Destroços
Função: recuperação de cascos e atracação.
| Vizinho | Atravessa a fronteira | Referência distante | Transição |
|---|---|---|---|
| Passagem das Amarras | costa, contenção, amarras | generated/structures/skyline.png | recuperação de cascos e atracação → circulação e amarras junto à água |
| Engrenópolis — Pátio das Transmissões | costa, contenção, amarras | region/gearworks.png | recuperação de cascos e atracação → montagem e distribuição de transmissões |

## Engrenópolis — Pátio das Transmissões
Função: montagem e distribuição de transmissões.
| Vizinho | Atravessa a fronteira | Referência distante | Transição |
|---|---|---|---|
| Estrada dos Rebitadores | trilha de carga, placas, remendos | generated/structures/skyline.png | montagem e distribuição de transmissões → transporte entre sucata e oficinas |
| Banco de Destroços | costa, contenção, amarras | region/wreck_cradle.png | montagem e distribuição de transmissões → recuperação de cascos e atracação |
| Engrenópolis — Vielas dos Artífices | rua gasta, cabos, anexos | generated/structures/skyline.png | montagem e distribuição de transmissões → moradias e oficinas de artífices |
| Engrenópolis — Corredor das Caldeiras | rua gasta, cabos, anexos | generated/structures/skyline.png | montagem e distribuição de transmissões → pressão, montagem e circulação industrial |

## Estrada dos Rebitadores
Função: transporte entre sucata e oficinas.
| Vizinho | Atravessa a fronteira | Referência distante | Transição |
|---|---|---|---|
| A Grande Ferrugem — Campos de Sucata | trilha de carga, placas, remendos | region/scrap_colossus.png | transporte entre sucata e oficinas → recuperação de máquinas e suprimento de sucata |
| Engrenópolis — Pátio das Transmissões | trilha de carga, placas, remendos | region/gearworks.png | transporte entre sucata e oficinas → montagem e distribuição de transmissões |

## Engrenópolis — Vielas dos Artífices
Função: moradias e oficinas de artífices.
| Vizinho | Atravessa a fronteira | Referência distante | Transição |
|---|---|---|---|
| Engrenópolis — Pátio das Transmissões | rua gasta, cabos, anexos | region/gearworks.png | moradias e oficinas de artífices → montagem e distribuição de transmissões |
| Engrenópolis — Corredor das Caldeiras | rua gasta, cabos, anexos | generated/structures/skyline.png | moradias e oficinas de artífices → pressão, montagem e circulação industrial |

## Engrenópolis — Corredor das Caldeiras
Função: pressão, montagem e circulação industrial.
| Vizinho | Atravessa a fronteira | Referência distante | Transição |
|---|---|---|---|
| Engrenópolis — Pátio das Transmissões | rua gasta, cabos, anexos | region/gearworks.png | pressão, montagem e circulação industrial → montagem e distribuição de transmissões |
| Engrenópolis — Vielas dos Artífices | rua gasta, cabos, anexos | generated/structures/skyline.png | pressão, montagem e circulação industrial → moradias e oficinas de artífices |
