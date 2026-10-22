# Forjas Rasas — implantação incremental

**Objetivo:** construir o distrito industrial no espaço leste/nordeste do Mercado, na cena atual de Sucateia. Execução direta autorizada pelo usuário por meio da supervisão regional.

**Arquitetura:** adicionar apenas ForjasRasasDistrict à cena congelada depois do acabamento de Alto-Lixo. TileMap próprio sobre a mesma escala de 48 unidades; arquitetura em sprites com câmera elevada, sombras/fundações e colisões nos pés. Rotas físicas, nenhum carregamento de cena ou teleporte. Economia e combate ficam fora desta etapa.

## Planta espacial e continuidade

- Fronteira oeste: saída comercial (1668,132) e pátio de carga do Mercado (1416,-756), conectados a duas entradas industriais. Pedra e comércio passam gradualmente a reparos, metal, fuligem e áreas de trabalho.
- Via dos Rebitadores: eixo oeste–leste sinuoso, acesso ao pátio de carga (2470,-120) e à reciclagem (3200,-150). Largura visual 120–160 unidades.
- Circuito das Fornalhas: ligação norte entre reparos, pátio central e fundição (2700,-850), com rota alternativa sul e dois becos de serviço.
- Núcleos: reparos a oeste, fabricação no centro, fundição ao norte/centro, triagem e reciclagem a leste. Edifícios agrupados em frentes com pátios funcionais, não espalhados sobre vazio.
- Drenagem: canal industrial irregular no sul do setor, com pontes, tubulação e ligação visual a Fundo-Ferro. Água/vala bloqueada fisicamente, travessias abertas.
- Limite aproximado: x=1640..3700, y=-1680..330, contorno com recuos. Tamanho por função, sem alterar pisos ou costa existentes.
- Futuras saídas: norte para Chaminés Velhas, leste para Grande Ferrugem, sul para manutenção/Fundo-Ferro. Apenas aproximações reservadas; destinos ainda não construídos.
- Referência macro: `ispirações/Atlas Fantástico de Continentes Místicos.png`, `sobre.txt` §§17.7,25–28,30–32. Sucata industrial costeira; relações regionais em `tools/FERRUGEM_CONTINUITY.md` são conceituais, os antigos protótipos separados não definem coordenadas físicas.
- Referência de qualidade/escala: `tools/checkpoints/original_visual_benchmark.png`. Preservar os cinco PNGs aprovados, casas, reator, oficina e barracas existentes.

## Execução e validação

- [x] Congelar cena atual em `tools/checkpoints/sucateia_before_forjas.tscn`; escrever teste que falha por distrito ausente.
- [x] Criar arte modular de reparo/fabricação e reciclagem com imagegen integrado; reutilizar fundição gerada apenas se consistente com benchmark. Salvar prompt/proveniência.
- [x] Implementar `scripts/world/forjas_rasas_builder.gd` e `tools/build_forjas_rasas.gd`, carregando exclusivamente o checkpoint desta etapa. Guardar scripts históricos contra replay.
- [x] Verificar acesso ida/volta a fronteiras, núcleos e saídas, todas as seções das rotas e pontes, água bloqueada, spawn, jogador único e preservação dos pisos/arquitetura/costa.
- [x] Capturar panorama, fundição/reciclagem e fronteira. Inspecionar visualmente e corrigir composição antes da entrega.
- [x] Executar regressões de Alto-Lixo, Mercado, costa e núcleo. Auditar, atualizar status próprio e salvar ZIP com CRC verificado.

## Focos de revisão

1. Edifícios grandes precisam de leitura dominante de telhado, mesma escala e luz do núcleo.
2. Footprints não devem bloquear rotas nem permitir atravessar a base das máquinas.
3. Canal deve usar a mesma geometria para visual/colisão; pontes precisam de travessia física.
4. Nenhuma mudança nos pisos e posições aprovadas; câmera pode acompanhar o novo território.
5. Saídas reservadas e limites de gameplay devem ser declarados; entrega não significa região completa.

**Limites desta etapa:** elevação visual, edifícios exteriores, nenhuma simulação industrial/NPC/interior novo.
