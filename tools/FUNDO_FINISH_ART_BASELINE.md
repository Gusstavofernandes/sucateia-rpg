# Fundo-Ferro — baseline da frente de arte,04/10/2026

Inspecionadas as oito capturas existentes `maps/fundo_ferro/preview_fundo_{full,PocoVelho,Bombas,Maquinas,Reservatorio,Valvulas,Descarte,Ruinas}.png`, os dois PNGs de `tools/fundo_pending_finish_art.json` e inventário atual. Capturas são baseline histórica, não renders novos. Brief posterior `tools/CONSULTANT_FUNDO_FINISH_BRIEF.md` recebido; esta nota preserva o levantamento anterior à produção. Sem cenas/scripts/imports/Godot.

Snapshot: `assets/reconstruction/fundo_finish/baseline.json`,165PNG anteriores (reconstruction/infrastructure/region/generated/terrain) e oito hashes de capturas. Não substituir snapshot ao finalizar. Dois pendentes ficam em seus caminhos originais intactos. Registro não certifica preservação de runtime ou topologia: são responsabilidades do implementador.

| Sala | Evidência concreta na captura | Reuso/necessidade |
|---|---|---|
| PocoVelho |Cisterna e acessoF legíveis; tubos curtos soltos sem encontro claro com cisterna. |Preservar cisterna/escada, chain_winch e guias existentes para içamento; medir sockets antes de pedir conectores. Não precisa outro poço/landmark.|
| Bombas |Bomba reconhecível com base; tubos ao redor e bacias escuras com pouca entrada/saída legível. |Pipe/copper_elbow/supports e drain_inspection existentes; rede precisa implantação. Variação mineral/umidade existente pode ser reaproveitada.|
| Maquinas |Motor dominante, largo apron neutro e tubos sem percurso operacional claro. |Preservar motor; bases/bench/óleo existentes. Força/transmissão exige conectar mecanismo, não adicionar motor novo.|
| Reservatorio |Duas bacias escuras e ponte central; sem marcas de nível/grelha de inspeção claramente distinguíveis. |Contenções/escada/passarela existentes; lacuna concreta de leitura de retenção/nível/inspeção, sujeita às reservas do implementador.|
| Valvulas |Reator forte, tubos soltos; não há manifold/grupos de válvulas reconhecíveis. |Reator existente; lacuna demonstrada de manifold pequeno apoiado, sockets medidos para rede.|
| Descarte |Recicladora e pequenos montes, sem bancada de triagem organizada. |fundo_sorting_bank pendente cobre função; não gerar outra bancada sem reprovação do encaixe.|
| Ruinas |Motor arruinado, mas contorno/piso semelhante às salas mantidas. |fundo_collapsed_corner pendente pode contextualizar colapso; não duplicar a mesma ruína. Iluminação mais clara da peça exige composição/placement.|

Em todas: repetição de paredes/piso e canos partidos confirmada visualmente; não prova defeito físico de spawn/ponte. Não refazer sete salas, oito rotas, duas pontes ou três entradas. Gradiente deve ser localizado por função, não filtro único.

Pendentes medidos:

- `assets/reconstruction/fundo_sorting_bank.png`:2038×771 RGBA,alpha0–255,bbox>16=15,6–2027,761, margem mínima6px. Escala uniforme inicial.13916501 →280×105,07px. Materiais e triagem coerentes; margem apertada, extensão da morsa próxima da borda. Não assumir corte pela visualizaçãoRGB: bounds visíveis contidos. Fonte/prompt preservados.
- `assets/reconstruction/fundo_collapsed_corner.png`:1697×927 RGBA,alpha0–255,bbox>16=7,3–1690,923, margem3px. Escala.14260250 →240×131,19px. Colapso coerente, área concava não equivale a piso caminhável; pode encostar na margem fora das rotas. Highlights de pedra mais claros que a captura subterrânea, conferir em composição. Não substituir arte por essa diferença antes de placement.

Reutilizáveis: supports Forjas (selaN–S e tubo sustentadoE–O), pipe/copper_elbow para terminais; service_arch e drain_inspection em parede real; chain_winch/capstan para reação/içamento apropriados; maintenance_bench, óleo/mineral/drag-wear/soot existentes com alpha restrito. Decks/stair_fits somente em travessias reais; naval/port cargo e sheds não pertencem automaticamente ao subsolo. Heat_reflection não convém ao abandono sem fonte de calor real.

Próximo: atender FUNDO_FINISH_ART_REQUESTS do implementador, validar dois pendentes em gameplay, produzir somente lacunas demonstradas de distribuição e inspeção. Nenhum lote produzido nesta baseline.
