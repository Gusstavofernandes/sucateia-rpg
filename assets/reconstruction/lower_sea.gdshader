shader_type canvas_item;

// =============================================================================
// SHADER DE OCEANO COM DEGRADÊ DE PROFUNDIDADE (BATIMETRIA COSTEIRA)
// Transição contínua desde as águas rasas e translúcidas onde as ondas batem
// na areia até o oceano azul profundo e abissal em alto-mar.
// =============================================================================

uniform sampler2D grime : filter_linear, repeat_enable;
uniform vec4 coast_edges[64];
uniform int edge_count = 0;
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

// Curva exata da linha da maré correspondente à geometria física do terreno
float get_coast_tide_y(float x) {
	if (x > -750.0) {
		float t = clamp((x + 750.0) / 1150.0, 0.0, 1.0);
		return mix(115.0, 1500.0, t);
	}
	float t = clamp((-x - 750.0) / 16750.0, 0.0, 1.0);
	float base_rise = -t * 1350.0;
	float drift = 120.0 + base_rise;
	float var_wave = sin(x * 0.004) * 22.0 + sin(x * 0.009) * 14.0 + sin(x * 0.0015) * 32.0;
	return drift + var_wave;
}

void vertex() {
	world_position = (MODEL_MATRIX * vec4(VERTEX, 0.0, 1.0)).xy;
}

void fragment() {
	vec2 p = world_position;
	float slow = TIME * 0.8;
	float n = noise(p * 0.008 + vec2(slow * 0.006, 0.0));
	vec3 tex = texture(grime, p / 610.0 + vec2(slow * 0.0009, 0.0)).rgb;
	float ripple = sin(p.y * 0.063 + sin(p.x * 0.023) * 2.0 + slow) * 0.5 + 0.5;
	
	// Água turva industrial na bacia portuária de Sucateia (X >= -700)
	vec3 water_industrial = mix(vec3(0.030, 0.049, 0.046), vec3(0.079, 0.111, 0.097), n) + tex * 0.105 + ripple * 0.004;
	
	// Fator de transição horizontal de Sucateia para o mar aberto (X: -700 a -3500)
	float maritime_factor = smoothstep(-700.0, -3500.0, p.x);
	
	// -------------------------------------------------------------------------
	// DEGRADÊ VERTICAL DE PROFUNDIDADE (Da praia rasa ao oceano profundo)
	// -------------------------------------------------------------------------
	float tide_y = get_coast_tide_y(p.x);
	// Distância perpendicular em relação à arrebentação da praia
	float depth = max(0.0, p.y - tide_y);
	
	// Paleta cromática natural e harmoniosa com o arenito terracota de Khemet-Ra:
	// 1. Águas rasas da praia (turquesa esmeralda translúcido, reflexo solar suave)
	vec3 c_shallow = vec3(0.18, 0.46, 0.54);
	// 2. Plataforma costeira (azul petróleo mediterrâneo)
	vec3 c_shelf   = vec3(0.09, 0.28, 0.42);
	// 3. Média profundidade (azul marinho clássico)
	vec3 c_slope   = vec3(0.04, 0.17, 0.32);
	// 4. Oceano profundo (azul noite ultramarino)
	vec3 c_deep    = vec3(0.02, 0.08, 0.19);
	// 5. Alto-mar abissal (azul abissal no horizonte sul)
	vec3 c_abyss   = vec3(0.01, 0.03, 0.10);
	
	// Curvas suaves de atenuação por profundidade (em pixels):
	float d_shelf = smoothstep(18.0, 90.0, depth);
	float d_slope = smoothstep(90.0, 320.0, depth);
	float d_deep  = smoothstep(320.0, 780.0, depth);
	float d_abyss = smoothstep(780.0, 1600.0, depth);
	
	vec3 depth_water = mix(c_shallow, c_shelf, d_shelf);
	depth_water = mix(depth_water, c_slope, d_slope);
	depth_water = mix(depth_water, c_deep, d_deep);
	depth_water = mix(depth_water, c_abyss, d_abyss);
	
	// Caustics solares sutis na água rasa (depth < 100px)
	float caustics = noise(p * 0.035 + vec2(slow * 0.2, -slow * 0.15)) * noise(p * 0.025 - vec2(slow * 0.15, slow * 0.1));
	float shallow_light = (1.0 - smoothstep(0.0, 95.0, depth)) * smoothstep(0.35, 0.75, caustics);
	depth_water += vec3(0.10, 0.16, 0.18) * shallow_light;
	
	// Ondulações oceânicas e ondulações de vento (swell)
	float ocean_swell = sin(p.y * 0.028 - p.x * 0.014 + slow * 1.3) * 0.5 + 0.5;
	float swell_crest = smoothstep(0.75, 0.96, ocean_swell) * (1.0 - smoothstep(0.96, 1.0, ocean_swell));
	depth_water += vec3(0.10, 0.18, 0.24) * swell_crest * smoothstep(70.0, 280.0, depth) * 0.55;
	
	// Fusão gradual entre a água industrial de Sucateia e o oceano com degradê
	vec3 final_water = mix(water_industrial, depth_water, maritime_factor);
	
	// Espuma marítima branca de quebra na linha costeira (onde depth < 16px)
	float surf_line = (1.0 - smoothstep(0.0, 16.0, depth)) * smoothstep(0.32, 0.72, noise(p * 0.045 + vec2(slow * 0.02, 0.0)));
	vec3 surf_foam = vec3(0.90, 0.96, 1.0);
	final_water = mix(final_water, surf_foam, surf_line * maritime_factor * 0.70);
	
	// Suavização do contato com a areia nos primeiros 12 pixels para fusão orgânica
	float edge_fade = smoothstep(0.0, 12.0, depth);
	float alpha_val = mix(1.0, clamp(edge_fade + 0.65, 0.0, 1.0), maritime_factor);
	
	COLOR = vec4(final_water, alpha_val);
}
