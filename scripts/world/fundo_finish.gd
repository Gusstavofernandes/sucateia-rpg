extends Node2D
## Infraestrutura Industrial e Rede de Fluidos do Fundo-Ferro (Subterrâneo Goblin)
## Arquitetado conforme padrões Godot 4.7: tipagem estática, y-sort, sem nós genéricos,
## 100% fiel à lore de Sucateia e à topologia física (8 salas, 9 rotas, 2 pontes, 3 acessos).
## Cada máquina responde: De onde recebe? O que produz? Para onde vai?

# --- Texturas de Máquinas Industriais Nano Banana ---
const TEX_BOMBA: Texture2D = preload("res://assets/machines/maquina_bomba_funcional_v1.png")
const TEX_BOMBA_SOMBRA: Texture2D = preload("res://assets/machines/maquina_bomba_funcional_v1_sombra.png")
const TEX_CALDEIRA: Texture2D = preload("res://assets/machines/maquina_caldeira_vapor_v1.png")
const TEX_CALDEIRA_SOMBRA: Texture2D = preload("res://assets/machines/maquina_caldeira_vapor_v1_sombra.png")
const TEX_GERADOR: Texture2D = preload("res://assets/machines/maquina_gerador_dinamo_v1.png")
const TEX_GERADOR_SOMBRA: Texture2D = preload("res://assets/machines/maquina_gerador_dinamo_v1_sombra.png")
const TEX_MANIFOLD: Texture2D = preload("res://assets/machines/maquina_manifold_valvulas_v1.png")
const TEX_MANIFOLD_SOMBRA: Texture2D = preload("res://assets/machines/maquina_manifold_valvulas_v1_sombra.png")
const TEX_DECANTADOR: Texture2D = preload("res://assets/machines/maquina_tanque_decantador_v1.png")
const TEX_DECANTADOR_SOMBRA: Texture2D = preload("res://assets/machines/maquina_tanque_decantador_v1_sombra.png")
const TEX_MOTOR_RUINA: Texture2D = preload("res://assets/machines/maquina_motor_desmontado_v1.png")
const TEX_MOTOR_RUINA_SOMBRA: Texture2D = preload("res://assets/machines/maquina_motor_desmontado_v1_sombra.png")

# --- Novos Assets da Arena do Coliseu ---
const TEX_ARENA_BOMBA: Texture2D = preload("res://assets/machines/maquina_bomba_recalque_arena_v1.png")
const TEX_ARENA_BOMBA_SOMBRA: Texture2D = preload("res://assets/machines/maquina_bomba_recalque_arena_v1_sombra.png")
const TEX_ARENA_COMPORTA: Texture2D = preload("res://assets/props/comporta_inundacao_arena_v1.png")
const TEX_ARENA_COMPORTA_SOMBRA: Texture2D = preload("res://assets/props/comporta_inundacao_arena_v1_sombra.png")
const TEX_ARENA_PORTAO: Texture2D = preload("res://assets/props/portao_grade_arena_v1.png")
const TEX_ARENA_PORTAO_SOMBRA: Texture2D = preload("res://assets/props/portao_grade_arena_v1_sombra.png")
const TEX_ARENA_REATOR: Texture2D = preload("res://assets/machines/maquina_reator_eletrodo_arena_v1.png")
const TEX_ARENA_REATOR_SOMBRA: Texture2D = preload("res://assets/machines/maquina_reator_eletrodo_arena_v1_sombra.png")
const TEX_CANO_RETO: Texture2D = preload("res://assets/pipes/cano_reto_industrial_v4.png")
const TEX_CANO_RETO_SOMBRA: Texture2D = preload("res://assets/pipes/cano_reto_industrial_v4_sombra.png")

# --- Kit de Tubulação Modular ---
const TEX_TUBO_VERTICAL: Texture2D = preload("res://assets/pipes/tubo_vertical_flange.png")
const TEX_TUBO_VERTICAL_SOMBRA: Texture2D = preload("res://assets/pipes/tubo_vertical_flange_sombra.png")
const TEX_TUBO_COTOVELO: Texture2D = preload("res://assets/pipes/tubo_cotovelo_90.png")
const TEX_TUBO_COTOVELO_SOMBRA: Texture2D = preload("res://assets/pipes/tubo_cotovelo_90_sombra.png")
const TEX_TUBO_T: Texture2D = preload("res://assets/pipes/tubo_t_juncao.png")
const TEX_TUBO_T_SOMBRA: Texture2D = preload("res://assets/pipes/tubo_t_juncao_sombra.png")
const TEX_TUBO_VALVULA: Texture2D = preload("res://assets/pipes/tubo_horizontal_valvula.png")
const TEX_TUBO_VALVULA_SOMBRA: Texture2D = preload("res://assets/pipes/tubo_horizontal_valvula_sombra.png")
const TEX_TUBO_SUPORTE: Texture2D = preload("res://assets/pipes/tubo_suporte_piso.png")
const TEX_TUBO_SUPORTE_SOMBRA: Texture2D = preload("res://assets/pipes/tubo_suporte_piso_sombra.png")

# --- Poças Reativas de Esgoto e Efluentes ---
const TEX_POCA_OLEO: Texture2D = preload("res://assets/puddles/poca_oleo_ambar.png")
const TEX_POCA_LIMO: Texture2D = preload("res://assets/puddles/poca_toxica_limo.png")
const TEX_POCA_ESGOTO: Texture2D = preload("res://assets/puddles/poca_esgoto_detritos.png")
const TEX_POCA_FERRUGEM: Texture2D = preload("res://assets/puddles/poca_ferrugem_lodo.png")

# --- Cenas de Efeitos ---
const CENA_VAZAMENTO_GOTA: PackedScene = preload("res://scenes/props/VazamentoGota.tscn")
const CENA_VAPOR_VALVULA: PackedScene = preload("res://scenes/props/VaporValvula.tscn")

# --- Especificação das 8 Redes Industriais Conectadas (ORIGEM -> ROTA -> DESTINO) ---
const NETWORKS: Array[Dictionary] = [
	{
		"id": "PocoBombas",
		"medium": "recalque_pressurizado",
		"color": Color("#5b7a72"),
		"width": 10.0,
		"core_color": Color("#7ec2b0"),
		"source": "PocoVelho",
		"destination": "Bombas",
		"description": "Linha pesada de recalque: puxa efluente bruto do poço para as bombas centrífugas."
	},
	{
		"id": "BombasDescarte",
		"medium": "agua_residual_turva",
		"color": Color("#63655c"),
		"width": 10.0,
		"core_color": Color("#8c9282"),
		"source": "Bombas",
		"destination": "Descarte",
		"description": "Conduto de efluente turvo para separação gravimétrica e triagem de detritos."
	},
	{
		"id": "DescarteMaquinas",
		"medium": "residuo_filtrado_oleoso",
		"color": Color("#786348"),
		"width": 9.0,
		"core_color": Color("#a68863"),
		"source": "Descarte",
		"destination": "Maquinas",
		"description": "Alimentação de água industrial e combustível de resíduo para a caldeira de vapor."
	},
	{
		"id": "MaquinasReservatorio",
		"medium": "condensado_e_vapor",
		"color": Color("#8c704b"),
		"width": 10.0,
		"core_color": Color("#cca56e"),
		"source": "Maquinas",
		"destination": "Reservatorio",
		"description": "Duto isolado de condensado quente e efluente térmico para decantação química."
	},
	{
		"id": "ReservatorioRuinas",
		"medium": "dreno_gravidade_limo",
		"color": Color("#4d6e64"),
		"width": 9.0,
		"core_color": Color("#689e8f"),
		"source": "Reservatorio",
		"destination": "Ruinas",
		"description": "Dreno de transbordo e lodo decantado escorrendo em direção às fundações antigas."
	},
	{
		"id": "RuinasPoco",
		"medium": "retorno_reciclado",
		"color": Color("#545753"),
		"width": 9.0,
		"core_color": Color("#757a73"),
		"source": "Ruinas",
		"destination": "PocoVelho",
		"description": "Canaleta fechada de retorno de infiltração completando o circuito fechado."
	},
	{
		"id": "TravessaDosDrenos",
		"medium": "alivio_bipartido",
		"color": Color("#5a6b63"),
		"width": 8.0,
		"core_color": Color("#7d968b"),
		"source": "Bombas",
		"destination": "Reservatorio",
		"description": "By-pass emergencial conectando o refluxo das bombas direto ao reservatório."
	},
	{
		"id": "GaleriaDasValvulas",
		"medium": "vapor_alta_pressao",
		"color": Color("#8a693b"),
		"width": 11.0,
		"core_color": Color("#d6a75c"),
		"source": "Maquinas",
		"destination": "Valvulas",
		"description": "Linha mestra de vapor e energia pneumática para o manifold distribuidor."
	},
	{
		"id": "GaleriaArena",
		"medium": "duto_vapor_efluente_eletrico",
		"color": Color("#4a5e55"),
		"width": 10.0,
		"core_color": Color("#6a8a7c"),
		"source": "Valvulas",
		"destination": "Arena",
		"description": "Corredor de serviço e duto de interligação: conecta o manifold da Sala das Válvulas / Galeria à Arena clandestina."
	},
]

# --- Especificação Funcional das 8 Salas Industriais ---
const FUNCTIONS: Array[Dictionary] = [
	{
		"id": "PocoVelho",
		"anchor": Vector2(1420, 1480),
		"landmark": "Structures/CisternaDeRecalque",
		"role": "captacao_vertical_redistribuicao"
	},
	{
		"id": "Bombas",
		"anchor": Vector2(1595, 1975),
		"landmark": "Structures/BombasDeRefluxo",
		"role": "pressurizacao_centrifuga_esgoto"
	},
	{
		"id": "Descarte",
		"anchor": Vector2(2300, 2180),
		"landmark": "Structures/TornoDesativado",
		"role": "triagem_mecanica_e_rejeitos"
	},
	{
		"id": "Maquinas",
		"anchor": Vector2(3050, 1680),
		"landmark": "Structures/MotorAbandonado",
		"role": "geracao_vapor_e_energia_dinamo"
	},
	{
		"id": "Reservatorio",
		"anchor": Vector2(2660, 1127),
		"landmark": "",
		"role": "decantacao_quimica_limo_verde"
	},
	{
		"id": "Ruinas",
		"anchor": Vector2(1580, 1025),
		"landmark": "Structures/RestosDaFundacao",
		"role": "maquina_colapsada_vazamento_ativo"
	},
	{
		"id": "Valvulas",
		"anchor": Vector2(3160, 820),
		"landmark": "Structures/ValvulasAntigas",
		"role": "manifold_mestre_controle_3_vias"
	},
	{
		"id": "Arena",
		"anchor": Vector2(3900, 1100),
		"landmark": "Structures/ArenaColiseu",
		"role": "arena_combate_clandestina_infraestrutura_reaproveitada"
	},
]

func _ready() -> void:
	_clean_placeholder_sprites()
	_build_function_art()
	_build_service_networks()

## Oculta sprites genéricos antigos que colidiam com a coerência visual
func _clean_placeholder_sprites() -> void:
	var world: Node = get_parent()
	if world == null:
		return
	
	# Oculta reator de cristal azul antigo na sala das válvulas (incompatível com a lore)
	var valvulas_node: Node = world.get_node_or_null("Structures/ValvulasAntigas")
	if valvulas_node != null:
		for child: Node in valvulas_node.get_children():
			if child is Sprite2D:
				child.visible = false
				
	# Oculta motor esquemático antigo
	var motor_node: Node = world.get_node_or_null("Structures/MotorAbandonado")
	if motor_node != null:
		for child: Node in motor_node.get_children():
			if child is Sprite2D:
				child.visible = false

	# Oculta restos esquemáticos de fundação antiga
	var fundacao_node: Node = world.get_node_or_null("Structures/RestosDaFundacao")
	if fundacao_node != null:
		for child: Node in fundacao_node.get_children():
			if child is Sprite2D:
				child.visible = false

	# Oculta bomba genérica antiga
	var bombas_node: Node = world.get_node_or_null("Structures/BombasDeRefluxo")
	if bombas_node != null:
		for child: Node in bombas_node.get_children():
			if child is Sprite2D:
				child.visible = false

## Constrói os conjuntos funcionais de cada sala
func _build_function_art() -> void:
	var world: Node = get_parent()
	var functions := Node2D.new()
	functions.name = "Functions"
	functions.y_sort_enabled = true
	add_child(functions)
	
	for spec: Dictionary in FUNCTIONS:
		var group := Node2D.new()
		group.name = str(spec.id)
		group.position = spec.anchor
		group.y_sort_enabled = true
		group.set_meta("environmental_role", spec.role)
		functions.add_child(group)
		
		match str(spec.id):
			"PocoVelho":
				_build_poco_velho(group)
			"Bombas":
				_build_bombas(group)
			"Descarte":
				_build_descarte(group)
			"Maquinas":
				_build_maquinas(group)
			"Reservatorio":
				_build_reservatorio(group)
			"Ruinas":
				_build_ruinas(group)
			"Valvulas":
				_build_valvulas(group)

## Sala 1: Poço Velho (Captação, Cisterna e Bomba Auxiliar)
func _build_poco_velho(group: Node2D) -> void:
	# Poça de efluente bruto sob a cisterna
	_add_puddle(group, "PocaEsgotoPoço", TEX_POCA_ESGOTO, Vector2(-40, 25), Vector2(0.24, 0.24), 0.85)
	
	# Bomba centrífuga auxiliar de recalque
	var bomba := _add_machine(group, "BombaRecalquePoco", TEX_BOMBA, TEX_BOMBA_SOMBRA, Vector2(-55, 10), Vector2(0.18, 0.18), Vector2(0, -70))
	
	# Tubo vertical de sucção entrando no poço
	_add_pipe_prop(group, "TuboSuccaoPoco", TEX_TUBO_VERTICAL, TEX_TUBO_VERTICAL_SOMBRA, Vector2(-95, -15), Vector2(0.12, 0.12), 0.0)
	
	# Cotovelo direcionando para a rota de saída PocoBombas
	_add_pipe_prop(group, "CotoveloSaidaPoco", TEX_TUBO_COTOVELO, TEX_TUBO_COTOVELO_SOMBRA, Vector2(-15, 20), Vector2(0.12, 0.12), 0.25)
	
	# Suporte de fixação ao solo
	_add_pipe_prop(group, "SuportePisoPoco", TEX_TUBO_SUPORTE, TEX_TUBO_SUPORTE_SOMBRA, Vector2(25, 22), Vector2(0.11, 0.11), 0.0)
	
	# Gotejamento na flange
	_add_leak(group, "VazamentoFlangePoco", Vector2(-50, -5))

## Sala 2: Bombas de Refluxo (Pressurização e Divisão de Fluxo)
func _build_bombas(group: Node2D) -> void:
	# Poça de óleo e água de gaxeta
	_add_puddle(group, "PocaGaxetaBomba", TEX_POCA_OLEO, Vector2(10, 30), Vector2(0.26, 0.26), 0.82)
	
	# Bomba centrífuga pesada
	var bomba := _add_machine(group, "BombaPrincipal", TEX_BOMBA, TEX_BOMBA_SOMBRA, Vector2(0, 0), Vector2(0.22, 0.22), Vector2(0, -85))
	
	# Tubo com registro de admissão recebendo de PocoBombas
	_add_pipe_prop(group, "RegistroAdmissao", TEX_TUBO_VALVULA, TEX_TUBO_VALVULA_SOMBRA, Vector2(-75, 15), Vector2(0.12, 0.12), 0.0)
	
	# Junção T de descarga dividindo entre Descarte e Alívio
	_add_pipe_prop(group, "TJuncaoDescarga", TEX_TUBO_T, TEX_TUBO_T_SOMBRA, Vector2(75, 8), Vector2(0.12, 0.12), 0.0)
	
	# Suporte de piso na linha de pressão
	_add_pipe_prop(group, "SuporteLinhaPressao", TEX_TUBO_SUPORTE, TEX_TUBO_SUPORTE_SOMBRA, Vector2(110, 12), Vector2(0.11, 0.11), 0.0)
	
	# Gotejamento no selo mecânico
	_add_leak(group, "VazamentoSeloBomba", Vector2(10, 10))

## Sala 3: Descarte (Triagem de Rejeitos, Sucata e Escória)
func _build_descarte(group: Node2D) -> void:
	# Poça espessa de ferrugem e lama decantada
	_add_puddle(group, "PocaFerrugemDescarte", TEX_POCA_FERRUGEM, Vector2(-30, 25), Vector2(0.30, 0.30), 0.90)
	
	# Duto com registro de descarga vindo de BombasDescarte
	_add_pipe_prop(group, "RegistroRejeito", TEX_TUBO_VALVULA, TEX_TUBO_VALVULA_SOMBRA, Vector2(-80, 20), Vector2(0.12, 0.12), -0.15)
	
	# Cotovelo desviando lama pesada para calha
	_add_pipe_prop(group, "CotoveloCalha", TEX_TUBO_COTOVELO, TEX_TUBO_COTOVELO_SOMBRA, Vector2(45, 18), Vector2(0.12, 0.12), 1.57)
	
	# Suporte de piso na entrada do descarte
	_add_pipe_prop(group, "SuporteDescarte", TEX_TUBO_SUPORTE, TEX_TUBO_SUPORTE_SOMBRA, Vector2(-115, 22), Vector2(0.11, 0.11), 0.0)
	
	# Baias de triagem ferrosa marcadas no solo
	_add_sorting_bay(group, "BaiaFerrosa", Vector2(-70, 36), Color("#776b59"))
	_add_sorting_bay(group, "BaiaRejeitos", Vector2(-20, 42), Color("#8b795d"))
	_add_sorting_bay(group, "BaiaEscoria", Vector2(30, 36), Color("#605e55"))

## Sala 4: Casa das Máquinas (Caldeira de Vapor e Gerador Dínamo Interligados)
func _build_maquinas(group: Node2D) -> void:
	# Poça de óleo lubrificante sob os mancais
	_add_puddle(group, "PocaOleoMaquinas", TEX_POCA_OLEO, Vector2(30, 35), Vector2(0.32, 0.32), 0.88)
	
	# 1. Caldeira de Vapor Industrial
	var caldeira := _add_machine(group, "CaldeiraVapor", TEX_CALDEIRA, TEX_CALDEIRA_SOMBRA, Vector2(-75, -10), Vector2(0.22, 0.22), Vector2(0, -95))
	
	# Brilho quente da fornalha da caldeira
	var luz_fornalha := PointLight2D.new()
	luz_fornalha.name = "LuzFornalha"
	luz_fornalha.position = Vector2(-75, -50)
	luz_fornalha.color = Color(1.0, 0.58, 0.18, 1.0)
	luz_fornalha.energy = 2.4
	luz_fornalha.texture = _create_light_texture()
	luz_fornalha.texture_scale = 5.0
	group.add_child(luz_fornalha)
	
	# Escape contínuo de vapor na válvula de alívio superior
	_add_steam(group, "VaporCaldeira", Vector2(-45, -170))
	
	# 2. Gerador Dínamo com Armadura de Cobre
	var dinamo := _add_machine(group, "GeradorDinamo", TEX_GERADOR, TEX_GERADOR_SOMBRA, Vector2(85, 20), Vector2(0.22, 0.22), Vector2(0, -75))
	
	# 3. Interligação física entre Caldeira e Dínamo:
	# Duto de vapor de alta pressão conectando a caldeira ao rotor do dínamo
	_add_pipe_prop(group, "DutoVaporInterligacao", TEX_TUBO_VALVULA, TEX_TUBO_VALVULA_SOMBRA, Vector2(5, 5), Vector2(0.12, 0.12), 0.0)
	
	# Eixo de transmissão e correia entre as máquinas
	_add_belt(group, "CorreiaForca", Vector2(-40, 35), Vector2(35, 35), Color("#6c5b43"))
	_add_bracket(group, "MancalCentral", Vector2(-2, 35), Color("#72634b"))
	
	# Junção T de saída de vapor para GaleriaDasValvulas
	_add_pipe_prop(group, "TSaidaVapor", TEX_TUBO_T, TEX_TUBO_T_SOMBRA, Vector2(-125, -5), Vector2(0.12, 0.12), -1.57)

## Sala 5: Reservatório do Limo (Tanque Decantador Químico com Visor Luminoso)
func _build_reservatorio(group: Node2D) -> void:
	# Poça bioluminescente de limo tóxico
	_add_puddle(group, "PocaLimoDecantador", TEX_POCA_LIMO, Vector2(0, 30), Vector2(0.30, 0.30), 0.90)
	
	# Tanque Decantador de Limo
	var decantador := _add_machine(group, "TanqueDecantadorLimo", TEX_DECANTADOR, TEX_DECANTADOR_SOMBRA, Vector2(0, -5), Vector2(0.22, 0.22), Vector2(0, -80))
	
	# Luz verde esmeralda emitida pelo visor de nível de limo
	var luz_limo := PointLight2D.new()
	luz_limo.name = "LuzVisorLimo"
	luz_limo.position = Vector2(0, -70)
	luz_limo.color = Color(0.25, 0.95, 0.45, 1.0)
	luz_limo.energy = 1.6
	luz_limo.texture = _create_light_texture()
	luz_limo.texture_scale = 4.0
	group.add_child(luz_limo)
	
	# Tubo vertical de alimentação vindo de MaquinasReservatorio
	_add_pipe_prop(group, "TuboAlimentacaoLimo", TEX_TUBO_VERTICAL, TEX_TUBO_VERTICAL_SOMBRA, Vector2(-80, -25), Vector2(0.12, 0.12), 0.0)
	
	# Registro de drenagem para ReservatorioRuinas
	_add_pipe_prop(group, "RegistroDrenagemLimo", TEX_TUBO_VALVULA, TEX_TUBO_VALVULA_SOMBRA, Vector2(80, 10), Vector2(0.12, 0.12), 0.0)
	
	# Suporte de piso na tubulação de efluente
	_add_pipe_prop(group, "SuporteLimo", TEX_TUBO_SUPORTE, TEX_TUBO_SUPORTE_SOMBRA, Vector2(115, 12), Vector2(0.11, 0.11), 0.0)
	
	# Gotejamento na bica do decantador
	_add_leak(group, "VazamentoLimo", Vector2(0, 15))

## Sala 6: Ruínas da Fundação (Dínamo Antigo Desmontado e Vazamento Ativo)
func _build_ruinas(group: Node2D) -> void:
	# Poça espalhada de esgoto e ferrugem penetrando as frestas
	_add_puddle(group, "PocaInfiltracaoRuinas", TEX_POCA_FERRUGEM, Vector2(-20, 25), Vector2(0.32, 0.32), 0.88)
	
	# Motor desmontado / carcaça partida vazando
	var motor_ruina := _add_machine(group, "MotorRuinaDesmontado", TEX_MOTOR_RUINA, TEX_MOTOR_RUINA_SOMBRA, Vector2(0, 0), Vector2(0.22, 0.22), Vector2(0, -75))
	
	# Cotovelo quebrado e torto
	_add_pipe_prop(group, "CotoveloQuebrado", TEX_TUBO_COTOVELO, TEX_TUBO_COTOVELO_SOMBRA, Vector2(-75, 15), Vector2(0.12, 0.12), 0.45)
	
	# Suporte abandonado tombado
	_add_pipe_prop(group, "SuporteAbandonado", TEX_TUBO_SUPORTE, TEX_TUBO_SUPORTE_SOMBRA, Vector2(70, 20), Vector2(0.11, 0.11), -0.2)
	
	# Vazamento ativo na tubulação fraturada
	_add_leak(group, "VazamentoFraturaRuinas", Vector2(-65, 8))
	_add_leak(group, "VazamentoJuntaRuinas", Vector2(-15, 12))

## Sala 7: Sala das Válvulas (Manifold de Distribuição Master de 3 Vias)
func _build_valvulas(group: Node2D) -> void:
	# Poça de condensado limpo sob os registros
	_add_puddle(group, "PocaCondensadoValvulas", TEX_POCA_OLEO, Vector2(0, 30), Vector2(0.28, 0.28), 0.75)
	
	# Manifold com 3 volantes de bronze e manômetros
	var manifold := _add_machine(group, "ManifoldMaster", TEX_MANIFOLD, TEX_MANIFOLD_SOMBRA, Vector2(0, -10), Vector2(0.22, 0.22), Vector2(0, -70))
	
	# Tubo flangeado de entrada recebendo de GaleriaDasValvulas
	_add_pipe_prop(group, "TuboEntradaManifold", TEX_TUBO_VERTICAL, TEX_TUBO_VERTICAL_SOMBRA, Vector2(-90, -35), Vector2(0.12, 0.12), 0.0)
	
	# Junção T no barramento de distribuição
	_add_pipe_prop(group, "TJuncaoManifold", TEX_TUBO_T, TEX_TUBO_T_SOMBRA, Vector2(85, 10), Vector2(0.12, 0.12), 0.0)
	
	# Registro horizontal no ramal secundário
	_add_pipe_prop(group, "RegistroRamalSecundario", TEX_TUBO_VALVULA, TEX_TUBO_VALVULA_SOMBRA, Vector2(130, 10), Vector2(0.11, 0.11), 0.0)
	
	# Escape suave de vapor em junta sob pressão
	_add_steam(group, "EscapeVaporManifold", Vector2(15, -95))
	
	# Gotejamento leve de condensação
	_add_leak(group, "VazamentoGaxetaValvula", Vector2(0, 5))

## Constrói os condutos físicos de cada uma das 9 rotas sem pontas soltas
func _build_service_networks() -> void:
	var routes: Node = get_parent().get_node_or_null("Routes")
	if routes == null:
		return
		
	var network_root := Node2D.new()
	network_root.name = "Networks"
	network_root.z_index = -15
	network_root.y_sort_enabled = false
	add_child(network_root)
	
	for spec: Dictionary in NETWORKS:
		var route_node: Node = routes.get_node_or_null(str(spec.id))
		if route_node == null or not route_node.has_meta("points"):
			continue
			
		var points: PackedVector2Array = route_node.get_meta("points")
		if points.size() < 2:
			continue
			
		# Camada 1: Blindagem de ferro externa protetora (sleeve de alta resistência)
		var base := _line(network_root, str(spec.id) + "_Sleeve", points, Color("#181b1a", 0.92), spec.width + 4.0)
		base.set_meta("route_id", spec.id)
		base.set_meta("medium", spec.medium)
		base.set_meta("source", spec.source)
		base.set_meta("destination", spec.destination)
		
		# Camada 2: Duto primário oxidado
		var primary := _line(network_root, str(spec.id) + "_Casing", points, spec.color, spec.width)
		
		# Camada 3: Núcleo condutor de fluido / calor (tracer)
		var core := _line(network_root, str(spec.id) + "_Core", points, spec.core_color, 2.6)
		core.set_meta("flow_direction", "defined")
		core.set_meta("flow_is_ambiguous", false)
		core.set_meta("source", spec.source)
		core.set_meta("destination", spec.destination)
		core.set_meta("medium_description", spec.description)
		
		# Instancia suportes de piso a intervalos regulares ao longo da rota
		_populate_route_brackets(network_root, spec.id, points)

## Posiciona suportes de solo ao longo das tubulações das rotas
func _populate_route_brackets(parent: Node2D, route_id: String, points: PackedVector2Array) -> void:
	var total_len := 0.0
	for i in range(points.size() - 1):
		total_len += points[i].distance_to(points[i + 1])
		
	var spacing := 220.0
	var count: int = int(total_len / spacing)
	if count <= 0:
		return
		
	for c in range(1, count + 1):
		var target_dist := float(c) * spacing
		var sample_pos := _sample_path(points, target_dist)
		
		# Suporte de piso físico para manter a integridade da tubulação
		var suporte := Sprite2D.new()
		suporte.name = "%s_SuportePiso_%d" % [route_id, c]
		suporte.texture = TEX_TUBO_SUPORTE
		suporte.scale = Vector2(0.09, 0.09)
		suporte.position = sample_pos + Vector2(0, 3)
		suporte.texture_filter = CanvasItem.TEXTURE_FILTER_LINEAR
		
		var sombra := Sprite2D.new()
		sombra.name = "Sombra"
		sombra.texture = TEX_TUBO_SUPORTE_SOMBRA
		sombra.position = Vector2(0, 15)
		sombra.modulate = Color(0, 0, 0, 0.45)
		suporte.add_child(sombra)
		
		parent.add_child(suporte)

## Amostra um ponto ao longo de uma polyline
func _sample_path(points: PackedVector2Array, distance: float) -> Vector2:
	var accumulated := 0.0
	for i in range(points.size() - 1):
		var seg_len: float = points[i].distance_to(points[i + 1])
		if accumulated + seg_len >= distance:
			var t: float = (distance - accumulated) / seg_len
			return points[i].lerp(points[i + 1], t)
		accumulated += seg_len
	return points[points.size() - 1]

# --- Métodos Utilitários de Instanciação Industrial ---

func _add_machine(parent: Node2D, machine_name: String, tex: Texture2D, tex_shadow: Texture2D, pos: Vector2, scl: Vector2, sprite_offset: Vector2) -> Node2D:
	var m_root := Node2D.new()
	m_root.name = machine_name
	m_root.position = pos
	m_root.y_sort_enabled = true
	
	# Sombra de contato no piso
	if tex_shadow != null:
		var shadow := Sprite2D.new()
		shadow.name = "SombraContato"
		shadow.texture = tex_shadow
		shadow.scale = scl
		shadow.position = Vector2(0, 10)
		shadow.modulate = Color(0, 0, 0, 0.50)
		shadow.texture_filter = CanvasItem.TEXTURE_FILTER_LINEAR
		m_root.add_child(shadow)
		
	# Sprite principal da máquina
	var spr := Sprite2D.new()
	spr.name = "Sprite"
	spr.texture = tex
	spr.scale = scl
	spr.position = sprite_offset
	spr.texture_filter = CanvasItem.TEXTURE_FILTER_LINEAR
	m_root.add_child(spr)
	
	parent.add_child(m_root)
	return m_root

func _add_pipe_prop(parent: Node2D, prop_name: String, tex: Texture2D, tex_shadow: Texture2D, pos: Vector2, scl: Vector2, rot: float) -> Sprite2D:
	var spr := Sprite2D.new()
	spr.name = prop_name
	spr.texture = tex
	spr.scale = scl
	spr.position = pos
	spr.rotation = rot
	spr.texture_filter = CanvasItem.TEXTURE_FILTER_LINEAR
	
	if tex_shadow != null:
		var shadow := Sprite2D.new()
		shadow.name = "Sombra"
		shadow.texture = tex_shadow
		shadow.position = Vector2(0, 18)
		shadow.modulate = Color(0, 0, 0, 0.40)
		spr.add_child(shadow)
		
	parent.add_child(spr)
	return spr

func _add_puddle(parent: Node2D, puddle_name: String, tex: Texture2D, pos: Vector2, scl: Vector2, alpha: float) -> Sprite2D:
	var puddle := Sprite2D.new()
	puddle.name = puddle_name
	puddle.texture = tex
	puddle.position = pos
	puddle.scale = scl
	puddle.modulate = Color(1.0, 1.0, 1.0, alpha)
	puddle.z_index = -1
	puddle.texture_filter = CanvasItem.TEXTURE_FILTER_LINEAR
	parent.add_child(puddle)
	return puddle

func _add_leak(parent: Node2D, leak_name: String, pos: Vector2) -> Node2D:
	var leak: Node2D = CENA_VAZAMENTO_GOTA.instantiate()
	leak.name = leak_name
	leak.position = pos
	parent.add_child(leak)
	return leak

func _add_steam(parent: Node2D, steam_name: String, pos: Vector2) -> Node2D:
	var steam: Node2D = CENA_VAPOR_VALVULA.instantiate()
	steam.name = steam_name
	steam.position = pos
	parent.add_child(steam)
	return steam

func _create_light_texture() -> GradientTexture2D:
	var grad := Gradient.new()
	grad.colors = PackedColorArray([Color(1, 1, 1, 1), Color(0, 0, 0, 0)])
	var tex := GradientTexture2D.new()
	tex.gradient = grad
	tex.fill = GradientTexture2D.FILL_RADIAL
	tex.fill_from = Vector2(0.5, 0.5)
	tex.fill_to = Vector2(1.0, 0.5)
	return tex

func _line(parent: Node, id: String, points: PackedVector2Array, color: Color, width: float) -> Line2D:
	var stroke := Line2D.new()
	stroke.name = id
	stroke.points = points
	stroke.width = width
	stroke.default_color = color
	stroke.begin_cap_mode = Line2D.LINE_CAP_ROUND
	stroke.end_cap_mode = Line2D.LINE_CAP_ROUND
	stroke.joint_mode = Line2D.LINE_JOINT_ROUND
	stroke.antialiased = true
	parent.add_child(stroke)
	return stroke

func _add_stroke(parent: Node2D, id: String, points: Array[Vector2], color: Color, width: float) -> Line2D:
	var packed := PackedVector2Array(points)
	var stroke := _line(parent, id, packed, color, width)
	stroke.z_index = -1
	return stroke

func _add_bracket(parent: Node2D, id: String, center: Vector2, color: Color) -> void:
	_add_stroke(parent, id, [center + Vector2(-9, -7), center + Vector2(-9, 5), center + Vector2(9, 5), center + Vector2(9, -7)], color, 3.0)

func _add_sorting_bay(parent: Node2D, id: String, position: Vector2, color: Color) -> void:
	var bay := Polygon2D.new()
	bay.name = id
	bay.position = position
	bay.polygon = PackedVector2Array([Vector2(-19, -7), Vector2(19, -7), Vector2(14, 8), Vector2(-14, 8)])
	bay.color = Color(color, 0.66)
	bay.z_index = -1
	parent.add_child(bay)
	_add_stroke(parent, id + "Rim", [position + Vector2(-19, -7), position + Vector2(19, -7)], Color("#c0a276", 0.75), 2.0)

func _add_belt(parent: Node2D, id: String, left: Vector2, right: Vector2, color: Color) -> void:
	_add_stroke(parent, id + "Upper", [left + Vector2(0, -7), right + Vector2(0, -7)], color, 3.0)
	_add_stroke(parent, id + "Lower", [left + Vector2(0, 7), right + Vector2(0, 7)], color.darkened(0.3), 3.0)
	_add_stroke(parent, id + "Return", [right, right + Vector2(0, 7), left + Vector2(0, 7), left], color.darkened(0.25), 2.0)
