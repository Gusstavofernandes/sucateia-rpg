shader_type canvas_item;

uniform sampler2D sand_texture : filter_linear, repeat_enable;

varying vec2 world_position;

float hash(vec2 p) {
	return fract(sin(dot(p, vec2(127.1, 311.7))) * 43758.5453);
}

float noise(vec2 p) {
	vec2 i = floor(p);
	vec2 f = fract(p);
	f = f * f * (3.0 - 2.0 * f);
	return mix(mix(hash(i), hash(i + vec2(1.0, 0.0)), f.x),
	           mix(hash(i + vec2(0.0, 1.0)), hash(i + vec2(1.0, 1.0)), f.x), f.y);
}

float fbm(vec2 p) {
	float val = 0.0;
	float amp = 0.5;
	mat2 rot = mat2(vec2(0.8, -0.6), vec2(0.6, 0.8));
	for (int i = 0; i < 3; i++) {
		val += amp * noise(p);
		p = rot * p * 2.02;
		amp *= 0.5;
	}
	return val;
}

void vertex() {
	world_position = (MODEL_MATRIX * vec4(VERTEX, 0.0, 1.0)).xy;
}

void fragment() {
	vec2 p = world_position;
	vec4 base_tex = texture(sand_texture, p / 720.0);
	
	// 1. MACRO-DUNAS EÓLICAS MONUMENTAIS (Ângulo de vento natural ~ 35 graus)
	vec2 wind_dir = normalize(vec2(-0.82, 0.57));
	float d_wind = dot(p, wind_dir);
	float warp = fbm(p * 0.0009) * 450.0 + sin(p.x * 0.0007 + p.y * 0.0011) * 180.0;
	float dune_phase = (d_wind + warp) * 0.0022;
	float s = sin(dune_phase);
	// Encosta assimétrica (barlavento suave, crista esculpida)
	float macro_dune = (s >= 0.0) ? pow(s, 0.74) : -pow(-s, 0.86);
	
	// 2. MICRO-ONDULAÇÕES DE VENTO (Ripples de areia fina)
	float micro_coord = dot(p, vec2(-0.035, 0.022)) + fbm(p * 0.006) * 3.5;
	float micro_ripple = sin(micro_coord) * 0.5 + 0.5;
	
	// 3. GRADIENTE GEOLÓGICO CONTINENTAL (Sucateia Leste -> Kemet-Ra Oeste)
	vec3 c_red_ore       = vec3(1.22, 0.42, 0.28); // Solo mineral vermelho de Sucateia
	vec3 c_terracotta    = vec3(1.20, 0.56, 0.28); // Terracota de transição
	vec3 c_amber_ochre   = vec3(1.22, 0.80, 0.36); // Âmbar ocre do sopé
	vec3 c_gold_sand     = vec3(1.28, 1.05, 0.62); // Areia dourada ensolarada de Kemet-Ra
	vec3 c_crest_sunlit  = vec3(1.38, 1.20, 0.78); // Crista dourada brilhante
	vec3 c_trough_shade  = vec3(1.10, 0.82, 0.44); // Sombra suave da calha da duna
	vec3 c_north_mesa    = vec3(1.22, 0.98, 0.56); // Platô imperial ao norte
	
	// Transição suave contínua em X
	float t_terra = smoothstep(-1800.0, -2500.0, p.x);
	float t_amber = smoothstep(-2500.0, -3500.0, p.x);
	float t_gold  = smoothstep(-3500.0, -4800.0, p.x);
	
	vec3 base_col = mix(c_red_ore, c_terracotta, t_terra);
	base_col = mix(base_col, c_amber_ochre, t_amber);
	base_col = mix(base_col, c_gold_sand, t_gold);
	
	// Modulação norte (platôs superiores)
	float t_north = smoothstep(-1400.0, -3800.0, p.y);
	base_col = mix(base_col, c_north_mesa, t_north * 0.35);
	
	// 4. RELEVO 2.5D DAS DUNAS (Luz solar incidente do topo-norte/noroeste)
	float dune_light = macro_dune * 0.24 + (micro_ripple - 0.5) * 0.08;
	vec3 lit_sand = (dune_light >= 0.0) ? 
		mix(base_col, c_crest_sunlit, dune_light * 1.4) : 
		mix(base_col, c_trough_shade, -dune_light * 1.3);
	
	// 5. WADIS (Antigos leitos de rios secos de Khemet-Ra)
	float wadi_path = abs(sin(p.x * 0.0006 + cos(p.y * 0.0008) * 1.8) * 450.0 - (p.y + 1600.0));
	float wadi_factor = 1.0 - smoothstep(120.0, 320.0, wadi_path);
	vec3 c_wadi_silt = vec3(1.15, 0.85, 0.48);
	lit_sand = mix(lit_sand, c_wadi_silt, wadi_factor * 0.35);
	
	// 6. GRANULARIDADE MINERAL E TEXTURA
	float grain = mix(0.93, 1.07, noise(p * 0.018));
	vec3 final_rgb = mix(base_tex.rgb * lit_sand, lit_sand, 0.62) * grain;
	
	COLOR = vec4(final_rgb, 1.0);
}
