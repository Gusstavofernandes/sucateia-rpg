from pathlib import Path
import re
import sys
root=Path(__file__).resolve().parents[1]
p=root/'tools/REGION_STATUS.md'
s=p.read_text(encoding='utf-8')
if '## COBERTURA POR LOCALIDADES' in s:
    print('Status already updated')
    sys.exit(0)
s=s.replace('14 mapas jogáveis, 48 conexões direcionadas (24 ligações de ida/volta)','16 mapas jogáveis, 54 conexões direcionadas (27 ligações de ida/volta)')
s=s.replace('oito setores originais e cinco novas cenas','oito setores originais e sete novas cenas')
s=s.replace('e Estrada dos Rebitadores. É uma base','Estrada dos Rebitadores, Vielas dos Artífices e Corredor das Caldeiras. É uma base')
s=s.replace('- Cinco novos assets integrados e fontes originais preservadas.','- Oito novos assets integrados nas ampliações e fontes originais preservadas.\n- Engrenópolis expandida em três cenas conectadas; oficinas, núcleo de moradores e montagem industrial.\n- Banco subdividido em recuperação de cascos, depósito e margem de atracação; Docas com triagem/manutenção e Fundo-Ferro com drenagem exterior.')
s=s.replace('| Fundo-Ferro | Bombas, escotilha do Poço, escadas, contenção, acesso subterrâneo | Drenagem e continuidade entre níveis exteriores |','| Fundo-Ferro | Bombas, escotilha, contenção, galeria e três trechos de drenagem exterior com travessia | Ampliar continuidade hidráulica e usos dos espaços |')
s=s.replace('| Docas | Armazéns, oficina, píeres, cargas, guindastes, barcas | Atividade portuária e pátios mais densos |','| Docas | Armazéns, oficinas, píeres, barcas, áreas de triagem/manutenção e depósito de expedição | Variantes de carga e acabamento de quinas |')
s=s.replace('| Banco de Destroços | Setor próprio, terra/sucata, casco recuperado, berços e guindaste | Destroços específicos e microáreas |','| Banco de Destroços | Casco próprio em desmontagem, berços, depósito, oficina e margem de atracação | Mais famílias de destroços e reforços costeiros |')
s=s.replace('| Engrenópolis | Fábrica de engrenagens, oficinas, habitação e circuito de serviço | É um recorte local; falta cidade completa |','| Engrenópolis | Três cenas: transmissões, 14 construções nas vielas, seis conjuntos no corredor de caldeiras | Cidade completa e variantes domésticas ainda pendentes |')
s=s.replace('Doze assets regionais nesta sessão:','Quinze assets regionais nesta sessão:')
s=s.replace('pump_station e cargo_barge. Todos','pump_station e cargo_barge; refinamento: wreck_cradle, cargo_depot e machine_lane. Todos')
s=s.replace('e tools/region_extension_art.json. Proveniência','tools/region_extension_art.json e tools/region_refinement_art.json. Proveniência')
s=s.replace('14 cenas, 73 destinos locais','16 cenas, 95 destinos locais').replace('as cinco novas cenas','as sete novas cenas').replace('48 conexões','54 conexões').replace('73 destinos','95 destinos').replace('13 panoramas regionais','15 panoramas regionais')
s=s.replace('Pátios superiores de Docas/Engrenópolis permanecem abertos.','Pátios de Docas e Engrenópolis ganharam funções, mas ainda têm circulação ampla; as novas vielas são mais densas.')
s=s.replace('Drenos, vazamentos localizados e continuidade dos níveis exteriores são limitados.','Três trechos de dreno exterior, contenção, passagem e manchas foram adicionados; a ligação hidráulica entre todos os níveis continua limitada.')
s=s.replace('com apoios e sucata; são decorativas.','com apoios e sucata; são decorativas. Casco desmontado e depósito próprios distinguem o Banco das Docas.')
s=s.replace('Fontes em assets/region/source/;','Fontes em assets/region/source/;')
s=s.replace('Anterior preservado: tools/checkpoints/ferrugem_baixa_primeira_base.zip.','Anteriores preservados: tools/checkpoints/ferrugem_baixa_primeira_base.zip e ferrugem_baixa_14_mapas.zip.')
s += '''
## COBERTURA POR LOCALIDADES DO MAPA ROTULADO
| Localidade | Correspondência construída | Pendências |
|---|---|---|
| Sucateia | Mercado, Alto-Lixo, Forjas, Cabos, Fundo/Galeria, Coroa, Docas | Acabamento por distrito e conexões ambientais adicionais |
| Chaminés Velhas | Usina Quebrada, conjuntos de chaminés e entorno industrial | Extensão ao limite norte da região |
| A Grande Ferrugem | Campos de sucata e colosso desmontado | Território externo mais amplo e ruínas locais |
| Engrenópolis | Transmissões, Vielas dos Artífices, Corredor das Caldeiras | Outras localidades urbanas; escala definitiva |
| Banco de Destroços | Recuperação, depósito, manutenção, atracação | Outras famílias de cascos e bancos costeiros |
| Caelporto / Vhal-Kor | Nenhuma cena implementada | Plano separado em tools/NORTH_CONNECTION_PLAN.md |

O Trono Partido aparece a oeste no mapa, perto de Rhoinar; pertencimento e extensão local não estão definidos em sobre.txt. Não foi inventada uma área jogável para esse nome nesta passada. Nenhuma localidade acima deve ser interpretada como região integralmente finalizada.
'''
p.write_text(s,encoding='utf-8')
print('Status updated')
