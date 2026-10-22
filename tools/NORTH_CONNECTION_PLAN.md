# Ligação norte — plano, sem implementação

Fontes verificadas: sobre.txt, seção 17.1 (linhas 276–296), e mapa rotulado ispirações/Imagem do ChatGPT 2 de out. de 2026, 00_38_14.png.

## Leitura geográfica
O mapa situa Vhal-Kor ao norte de Ferrugem Baixa. Caelporto está na borda sul de Vhal-Kor, junto ao curso d'água entre os dois territórios. Chaminés Velhas é a saída temática mais adequada da indústria goblin em direção ao norte. Não há distância local ou estrada exata definida no texto; traçado abaixo é proposta de level design, não geografia confirmada.

## Percurso proposto
1. Chaminés Velhas → limite industrial de Ferrugem Baixa: pátio de expedição, carvão, entulho organizado e estruturas goblins ainda dominantes.
2. Limite industrial → caminho junto ao rio: reduzir sucata e densidade, introduzir pedra de contenção, trilha comercial e infraestrutura de transporte. Manter destino e retorno claros.
3. Caminho do rio → periferia de Caelporto: transição gradual para cais de pedra, armazéns portuários e estruturas mais planejadas. Área pertencente à futura etapa Vhal-Kor.
4. Caelporto → bairros inferiores de Vhal-Kor: trabalhadores, torres góticas, catedrais, cabos, pontes e elevadores arcanos, conforme sobre.txt. Silhuetas verticais devem respeitar a mesma câmera top-down.

## Contrato técnico para próxima etapa
Reutilizar RegionTravel/portais e instância de jogador. Adicionar destino somente quando a cena estiver construída e validada; nenhum portal vazio foi criado agora. Chegada deve ter espaço físico seguro e passagem de retorno. Proibir teleporte para mapa ausente. Criar testes explícitos das localidades e validar input E, rotas locais, capturas de entrada/saída, preservação dos hashes.

## Assets necessários
Módulos de cais de pedra e armazém de Caelporto, contenção fluvial, ponte/guarita de entrada; depois fachadas e telhados góticos dos níveis inferiores. Gerar arte nova com o mesmo ângulo e iluminação, sem transformar Vhal-Kor em cópia de Sucateia. Não expandir NPCs/economia como parte dessa ligação ambiental.

## Estado
Planejamento apenas. Vhal-Kor, Caelporto e o caminho externo não estão implementados. Nenhum arquivo WORLD_* foi alterado.
