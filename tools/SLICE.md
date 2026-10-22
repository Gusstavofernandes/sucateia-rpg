# Sucateia — primeira área
Abra project.godot na Godot 4.7.2 e pressione F6 na cena ou F5 no projeto. Jogar.cmd usa a instalação detectada neste computador.
WASD/setas: mover; Shift: correr; roda: zoom; R: retornar ao início; F1: ocultar informações.
Mapa editável: maps/sucateia/sucateia.tscn. Estruturas reutilizáveis: scenes/props/reclaimed_structure.tscn. Não regenere a cena após edições manuais: tools/build_slice.gd substitui a cena com sua composição original.
Verificação: Godot --headless --path . --script tests/test_slice.gd. Testa oito rotas com geometria física e corpo do jogador, movimento, colisão e retorno.
Assets autorais: tools/generate_assets.py (Python padrão). A geração de partículas usa o ZIP original Kenney em tools/particle-pack.zip; assets prontos não precisam do gerador.
Recorte inicial com verticalidade simulada; sem interiores ou troca de pisos sobrepostos. Expansão deve preservar passarela, rotas e escada.

Sprites principais substituídos por oito assets gerados via image_gen integrado: assets/generated/structures/ e assets/generated/props/. Fontes e alpha originais preservados em assets/generated/source/. Prompts e parâmetros de recorte/âncora: tools/art_manifest.json; preparação proporcional 2x: tools/prepare_generated.py (Pillow). Não reaplica o shader de pátina aos novos sprites pintados. Backups da cena anterior em tools/backups/.

Terreno renovado: assets/terrain/ (atlas contínuo e quatro stamps gerados), scripts/world/terrain_builder.gd (integração ao solo). Instalação não acrescenta colisões. Shaders diferenciam microáreas e desgaste das rotas; base anterior em tools/backups/sucateia_before_terrain.tscn.bak. Prompts em tools/terrain_prompts.json.

Infraestrutura finalizada: scripts/world/infrastructure_builder.gd e assets/infrastructure/. Bordas, muro de desnível, canal com margens irregulares, decks metálicos, escada, portais, guindaste e lanternas substituem geometria provisória. Pilhas de sucata texturizadas; prédios aprovados preservados. Passagem e colisões permanecem iguais; hashes de proteção em tools/approved_art_hashes.json. Prompts: tools/infrastructure_prompts.json.


Refinamento de composição: canal com recuos e colisões poligonais correspondentes, bolsões de manutenção, saídas de tubulação e manchas de vazamento. O deck oriental alterna larguras e encaixes, com reparos e cabos. Quatro pequenos pontos de trabalho ocupam bordas de circulação; seis anexos de serviço diferenciam as casas sem modificar suas imagens. Trilhas secundárias e pisadas de terra conectam mercado, residências e escadas. Assets aprovados preservados; circulação validada por travessia real e amostras nas margens deslocadas.


Cais industrial: scripts/world/coastal_builder.gd adiciona muralha costeira gerada, margem reforçada irregular, três píeres inferiores de serviço, quatro drenos e água industrial animada. Os píeres inferiores são decorativos; a muralha bloqueia o acesso ao mar. Assets existentes preservados. Prompt/fonte: tools/coastal_prompt.json; imagem final: assets/infrastructure/coastal_wall.png. Captura dedicada: preview_coast.png. Limite inferior da câmera ampliado para mostrar a transição costeira.


Ferrugem Baixa regional: o projeto inicia no centro preservado. Aproximar-se de uma passagem de distrito e pressionar E; retorno pela passagem de origem. Configuração: maps/ferrugem_baixa/region.json. Oito cenas adicionais: Alto-Lixo, Forjas Rasas, Os Cabos, Fundo-Ferro, Coroa de Lata, Docas, Grande Ferrugem e Chaminés Velhas. R reinicia no último acesso. Construção: tools/build_region.gd; preparar imagens novas: tools/prepare_region.py. Não executar build_slice sozinho depois da expansão: ele remove as conexões do centro; executar build_region depois para reinstalá-las. Testes adicionais: tests/test_region.gd e tests/test_region_travel.gd. As transições são carregamentos entre mapas; não existe mundo contínuo nem gameplay final. Relatório final: tools/REGION_STATUS.md.
