# Passagem das Amarras — expansão contínua autorizada

Escopo: somente Amarras a leste/sudeste das Forjas. Sem cena separada, sem Engrenópolis ou outros distritos. Benchmark define qualidade e escala, não tamanho. Baseline atual salva em tools/checkpoints/sucateia_before_amarras.tscn; checkpoint integral anterior sucateia_forjas_acabamento_local.zip.

## Planta inicial

Dois encontros com Forjas: via logística3550,0→ponte curta3840,0→margem3990,0; manutenção3280,240→ponte de correntes3645,275→margem3935,275. Forjas conserva seus pisos, redes e prédios. Território assimétrico x≈3910–5570,y≈-180–970; área necessária para circulação, amarração e transferência, sem crescer para norte.

Via de transferência:3990,0→4290,30→4480,260→4820,290→5110,440→5480,565. Circuito inferior:3935,275→4120,360→4240,730→4560,835→4950,900→5230,850→5480,565. Travessa de inspeção conecta via/circuito. Canal de manutenção no sul/leste com duas travessias e retorno, evitando água como simples recorte externo.

Pontos planejados: torre de tensão4470,100 (altura inferior à chaminé de Forjas); plataforma de transferência4700,465; guincho4210,540; hub4520,510; quiosque5130,235. Bases e frentes deixadas livres, posição final será conferida com QA/portos da arte. Saída5520,565 reservada à futura Engrenópolis; não criar destino fictício nem teleporte. Respawn original e retornos F existentes mantidos; dois pontos de chegada seguros dentro de Amarras verificados, sem novo sistema de viagem.

Continuidade: via gasta, placas, cabos de serviço e apoios atravessam os encontros com Forjas; menos calor/fuligem progressivamente, mais óleo/umidade e marcas de tração. Pontes e margens ancoradas, correntes com extremos reais, contexto de água além do enquadramento. Não usar formas debug visíveis. Reaproveitar arte aprovada de passarelas, contenções, escadas, luzes e carga; novos oito PNGs somente após manifesto/QA da frente de arte.

## Execução

- [x] Conferir autorização humana, brief, mapa e instruções locais; preservar checkpoint.
- [x] Teste de preservação da cidade e contrato de circulação Amarras antes de implantação.
- [x] Geografia, materiais, vias, duas ligações com Forjas, canal/duas travessias, bordas orgânicas e cenário contínuo.
- [x] Integrar assets liberados; alinhar conexões e adicionar bases, apoios, sombras e desgaste coerente.
- [x] Travessias reais ida/volta, bases bloqueadas, água bloqueada, saídas/chegadas seguras, R/F e regressões aprovadas.
- [x] Capturas geral, transição e detalhes estruturais; revisão independente e comparação consultiva do supervisor.
- [x] Documentar limites, métricas e checkpoint. Não avançar automaticamente a Engrenópolis.

Resultado integrado e limites: tools/AMARRAS_RESULT.md. Oito seleções finais,611células de cobertura recortadas no polígono,16testesPASS,7capturas; aprovação final visual do supervisor/humano permanece pendente. Nenhum setor seguinte iniciado.
