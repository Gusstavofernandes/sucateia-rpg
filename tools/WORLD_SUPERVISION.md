# Supervisão do mundo de Aethranis

## Autorização e fontes
O usuário autorizou em 02/10/2026 a supervisão do outro chat, avaliação contra os mapas locais e envio de tarefas sucessivas até completar o mapa inteiro enquanto dorme. Implementador: 01a0face-adf4-7ef0-984c-cb5ad576e7b1, Construir a cidade goblin Sucateia. Pasta compartilhada: C:/Users/Usuario/Documents/jogo.
Fontes: sobre.txt; ispirações/Imagem do ChatGPT 2 de out. de 2026, 00_38_14.png (mapa rotulado); ispirações/Atlas Fantástico de Continentes Místicos.png (arte macro); tools/REGION_PLAN.md; tools/SLICE.md. A referência é cartográfica e conceitual: transformar cada região em áreas exploráveis coerentes, não reproduzir a imagem como um cenário estático.

## Fluxo
1. Consultar estado compacto do implementador. Enquanto ativo, evitar mensagens duplicadas e alterações concorrentes.
2. Quando terminar, consultar resumo e relatório, cenas, capturas e testes. Registrar evidências em WORLD_PROGRESS.md.
3. Verificar identidade visual, geografia e landmarks da referência, escala consistente, chão e infraestrutura acabados, legibilidade dos percursos, colisões, spawns seguros, viagens bidirecionais e execução do projeto. Avaliar capturas visualmente; testes não comprovam acabamento artístico.
4. Enviar correções específicas se houver falhas. Quando aprovado, enviar próxima etapa concreta ao mesmo chat. Cada delegação deve indicar fontes, área, integração, entregáveis e critérios verificáveis. Não solicitar confirmação rotineira: continuidade e mensagens já autorizadas.
5. Repetir até todas as regiões e conexões verificadas. Registrar lacunas de detalhe sem inventar requisitos definitivos para pontos não definidos. Não confundir um pequeno recorte representativo com toda uma região concluída.
6. Desativar acompanhamento somente após conclusão verificada, ou informar bloqueio real. Evitar notificações quando nada mudar.

## Escopo e sequência inicial
Concluir primeiro Ferrugem Baixa, seus distritos e arredores conforme REGION_PLAN; conferir também Engrenópolis e Banco de Destroços do mapa macro. Depois construir conexões terrestres e marítimas e progredir para Vhal-Kor, A Coroa Partida, Rhоinar, Khemet-Ra, Grun-Khaz, Ther’Valen, A Espinha do Mundo, Lunareth, Shen-Pao, Nhal-Zareth e Brumafenda. Ajustar ordem conforme conexões e dependências; a lista cobre as 12 regiões incluindo Ferrugem Baixa.
Usar nomes exatos de sobre.txt e do mapa; Rhоinar acima corresponde a RHOINAR em sobre.txt. Landmarks e posições devem ser consultados na imagem, não inferidos apenas desta lista.
Cada região precisa de extensão e composição próprias, principais locais nomeados contemplados, percursos exploráveis e ligação ao mundo. Carregar cenas separadas pode reduzir custo de nós/luzes; um hub com portais não basta para comprovar todo o território construído.

## Preservação
Não substituir casas, oficina, reator e barracas aprovados. Respeitar tools/approved_art_hashes.json. Não regenerar cena manualmente editada sem identificar mudanças e preservar backup. Não alterar mecânicas de economia, combate ou simulação social fora do necessário à construção e exploração do mapa.
Não editar código de construção enquanto implementador trabalha. Arquivos de supervisão pertencem a este chat.
