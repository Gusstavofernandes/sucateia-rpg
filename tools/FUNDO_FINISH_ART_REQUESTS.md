# Arte — acabamento Fundo-Ferro existente

Brief CONSULTANT_FUNDO_FINISH_BRIEF.md e levantamento FUNDO_FINISH_BASELINE.md. Dono cena/runtime/Godot root, arte somente assets/reconstruction/fundo_finish/*/manifestos e tools/FUNDO_FINISH_ART_HANDOFF.md. Sem Godot/import/mutações das cenas ou fontes anteriores. Não reabrir costura portuária aprovada.

Inventário deve priorizar ativos atuais e medir reutilização antes de gerar. Motor350x239, bomba205x210, cisterna170x181, reator165x172 e recicladora209x149 são landmarks já existentes a instalar visualmente. Fundo_wall usado328 vezes em canvas projetado87x48; lacuna demonstrada em encontros/cantos reforçados ou colapsados com suporte visível, não outro set genérico. Posição/collider serão decididos pelo levantamento físico.

Lacunas concretas:
1. Válvulas: conjunto baixo/manifold de distribuição com instrumentos, raízes/footboxes e conexões nativas explícitas para reaproveitar reator atual como alimentação/controle. Tamanho útil~100–150px, terminações correspondentes a tubo pequeno13–18px ou principal24px, escala uniforme de gameplay24px avatar; não novo reator/landmark grande. Precisa representar entrada→branches→retorno, não tubos soltos.
2. Margem/apoios: verificar se contenções/utility_fits/PNGexistentes resolvem reserva/bacia/descarga; suporte baixo para tubo integrado a pedra com socket/foot real só se não existir compatível. Bacias pequenas96x62/77x72/115x72; não gerar gigantesco reservatório único sobre elas.
3. Paredes: contraste estrutural contextual em manutenção vs abandono; fundo_collapsed_corner e fundo_wall atuais primeiro. Se canto colapsado não couber/não casar câmera, selecionar módulo baixo compactado de degradado/reforçado que realmente possa entrar no perímetro87x48, sem nova sala.
4. Descarte: fundo_sorting_bank já disponível (~280x95 intenção) com margem fonte apertada; medir canvas/bbox/foot antes de aceitar. Não duplicar bancadas/props aleatórios. Alternativa compacta só se encaixe físico/qualidade exigir.

Piso/umidade/desgaste e pontes podem reutilizar PNGs sem geração adicional. Auditoria do motor e sockets ainda pendente: não gerar conexões aleatórias para preencher. Entregar prompts/fontes, hashes protegidos, RGBA intacto, medida bbox/escala/contactos/sockets/QA1:1. Root poderá pedir variante após detectar lacuna real. Câmera consistente elevated orthographic3/4 top-down S→N, luz superior-esquerda, pedra úmida/ferrugem/ferro/cobre/madeira reaproveitada; acentosciano/âmbar discretos. Preservar ativos aprovados da superfície.
