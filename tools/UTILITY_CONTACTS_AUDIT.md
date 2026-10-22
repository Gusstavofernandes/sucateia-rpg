# Encaixes de bueiros, canos e escadas — 2026-10-03

Quatro molduras `service_arch.png` da costa, antes em y=1484, agora são desenhadas em y=1456. O topo pintado passa a y=1421,3 e intercepta a face da contenção centrada em y=1418. A parede e a boca do bueiro se sobrepõem; não há chão separando as duas peças.

As entradas decorativas `To_fundo` e `To_docas` receberam emendas de alvenaria até os segmentos reais de `LowerCoastReworked/shore_points`. Marcadores, pontos F e chegadas não foram deslocados.

A rede central substitui os canos soltos no retângulo (1200,750)-(1750,1000). Percurso contínuo: saída da máquina (1226,928), queda até (1226,941), curva até (1254,968), tronco até (1686,968), curva até (1714,940), subida até o receptor da oficina (1714,810). Os segmentos usam pontos de flange medidos, não centros aproximados de imagens.

Foi gerado somente um asset adicional, `assets/reconstruction/utility_fits/copper_elbow.png`, usando o gerador integrado ImageGen. Os canos retos, molduras e alvenaria existentes foram reaproveitados. Prompt e medidas no manifesto da pasta.

As três escadas novas de Os Cabos passaram da camada elevada de desenho para pivôs de chão dentro de `Structures`, ordenados pela base de chegada. As casas em primeiro plano cobrem a escada. Texturas, encaixes e materiais de visibilidade continuam iguais; navegação por F preservada.

Validação específica: quatro bueiros encostam na parede, flanges consecutivas sem vãos com tolerância de 0,1 px, três escadas compartilhando a profundidade das casas. Capturas: `maps/sucateia/preview_utility_core.png`, `preview_stairs_coast.png`, `preview_cabos_alto.png`.

Oito verificações locais concluídas: `test_utility_contacts`, `test_stair_fits`, `test_cabos_layers`, `test_cabos_art_contacts`, `test_cabos_support_depth`, `test_cabos_preservation`, `test_lower_coast`, `test_fundo_access`. Logs `tools/utility_test_*.log` registram PASS e nenhum erro de scripts, recursos, encaixes ou física; permanece apenas o diagnóstico de certificados descrito abaixo.

O ambiente restrito emite `Failed to read the root certificate store` antes de executar o Godot. Esse diagnóstico de certificados do Windows é separado das verificações locais de arte e física. A execução de captura e testes simultâneos excedeu a memória disponível; as verificações foram repetidas sequencialmente.
