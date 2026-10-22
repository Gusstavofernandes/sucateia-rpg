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
	float t = clamp((-x - 700.0) / 12300.0, 0.0, 1.0);
	float base_y = 120.0 - t * 950.0;
	float w1 = sin(x * 0.0018) * 85.0;
	float w2 = cos(x * 0.0045) * 40.0;
	float w3 = sin(x * 0.012) * 15.0;
	return base_y + w1 + w2 + w3;
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
	
	// Paleta cromática de profundidade marinha:
	// 1. Águas rasas da praia (arrebentação, transparente e luminosa)
	vec3 c_shallow = vec3(0.28, 0.74, 0.85);
	// 2. Plataforma costeira (turquesa límpido)
	vec3 c_shelf   = vec3(0.16, 0.56, 0.72);
	// 3. Média profundidade (azul royal marítimo)
	vec3 c_slope   = vec3(0.08, 0.32, 0.54);
	// 4. Oceano profundo (azul marinho denso)
	vec3 c_deep    = vec3(0.035, 0.16, 0.35);
	// 5. Alto-mar abissal (azul petróleo profundo no horizonte sul)
	vec3 c_abyss   = vec3(0.018, 0.07, 0.18);
	
	// Curvas suaves de atenuação por profundidade (em pixels):
	float d_shelf = smoothstep(15.0, 95.0, depth);
	float d_slope = smoothstep(95.0, 340.0, depth);
	float d_deep  = smoothstep(340.0, 850.0, depth);
	float d_abyss = smoothstep(850.0, 1800.0, depth);
	
	vec3 depth_water = mix(c_shallow, c_shelf, d_shelf);
	depth_water = mix(depth_water, c_slope, d_slope);
	depth_water = mix(depth_water, c_deep, d_deep);
	depth_water = mix(depth_water, c_abyss, d_abyss);
	
	// Caustics solares sutis na água rasa (depth < 120px)
	float caustics = noise(p * 0.035 + vec2(slow * 0.2, -slow * 0.15)) * noise(p * 0.025 - vec2(slow * 0.15, slow * 0.1));
	float shallow_light = (1.0 - smoothstep(0.0, 110.0, depth)) * smoothstep(0.35, 0.75, caustics);
	depth_water += vec3(0.12, 0.18, 0.22) * shallow_light;
	
	// Ondulações oceânicas e ondulações de vento (swell)
	float ocean_swell = sin(p.y * 0.028 - p.x * 0.014 + slow * 1.3) * 0.5 + 0.5;
	float swell_crest = smoothstep(0.75, 0.96, ocean_swell) * (1.0 - smoothstep(0.96, 1.0, ocean_swell));
	depth_water += vec3(0.12, 0.22, 0.28) * swell_crest * smoothstep(80.0, 300.0, depth) * 0.65;
	
	// Fusão gradual entre a água industrial de Sucateia e o oceano com degradê
	vec3 final_water = mix(water_industrial, depth_water, maritime_factor);
	
	// Espuma marítima branca de quebra na linha costeira (onde depth < 18px)
	float surf_line = (1.0 - smoothstep(0.0, 18.0, depth)) * smoothstep(0.35, 0.75, noise(p * 0.045 + vec2(slow * 0.02, 0.0)));
	vec3 surf_foam = vec3(0.88, 0.95, 1.0);
	final_water = mix(final_water, surf_foam, surf_line * maritime_factor * 0.75);
	
	COLOR = vec4(final_water, 1.0);
}
