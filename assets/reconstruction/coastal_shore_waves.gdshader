shader_type canvas_item;

// =============================================================================
// SHADER DE ARREBENTAÇÃO E ONDAS NA PRAIA COM FUSÃO PERFEITA DE MAR
// =============================================================================

uniform sampler2D noise_tex : filter_linear, repeat_enable;
uniform float wave_speed : hint_range(0.1, 2.0) = 0.45;
uniform float wave_reach : hint_range(10.0, 80.0) = 48.0;

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

float get_tide_y(float x) {
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
	float tide_y = get_tide_y(p.x);
	float d = p.y - tide_y;
	float t = TIME * wave_speed;
	
	float x_offset = sin(p.x * 0.0035 + t * 0.4) * 18.0 + cos(p.x * 0.008) * 10.0;
	float micro_noise = noise(p * 0.035 + vec2(t * 0.2, 0.0));
	
	// ONDA PRINCIPAL 1: Avanço e Recuo Cíclico
	float cycle1 = fract(t * 0.35 + sin(p.x * 0.0015) * 0.35);
	float progress1 = sin(cycle1 * 3.14159);
	float reach1 = -wave_reach * progress1 + x_offset * 0.5;
	
	float dist_to_crest1 = abs(d - reach1);
	float foam_crest1 = (1.0 - smoothstep(0.0, 9.0 + micro_noise * 6.0, dist_to_crest1)) * smoothstep(0.05, 0.25, cycle1);
	float water_body1 = (1.0 - smoothstep(reach1, reach1 + 55.0, d)) * smoothstep(reach1 - 2.0, reach1 + 8.0, d) * smoothstep(0.05, 0.30, cycle1);
	
	// ONDA SECUNDÁRIA 2: Contra-maré desfasada
	float cycle2 = fract(t * 0.27 + 0.55 + cos(p.x * 0.0022) * 0.30);
	float progress2 = sin(cycle2 * 3.14159);
	float reach2 = -(wave_reach * 0.75) * progress2 - x_offset * 0.4;
	
	float dist_to_crest2 = abs(d - reach2);
	float foam_crest2 = (1.0 - smoothstep(0.0, 7.0 + micro_noise * 5.0, dist_to_crest2)) * smoothstep(0.05, 0.25, cycle2);
	float water_body2 = (1.0 - smoothstep(reach2, reach2 + 45.0, d)) * smoothstep(reach2 - 2.0, reach2 + 6.0, d) * smoothstep(0.05, 0.30, cycle2);
	
	// AREIA MOLHADA RESIDUAL
	float max_wash = -wave_reach - 8.0;
	float wet_sand_mask = (1.0 - smoothstep(max_wash, max_wash + 45.0, d)) * (1.0 - smoothstep(-6.0, 18.0, d));
	float wet_fade = (1.0 - progress1) * 0.45;
	vec4 wet_sand_col = vec4(0.12, 0.08, 0.04, wet_sand_mask * wet_fade);
	
	// Água translúcida turquesa em harmonia com as águas rasas do oceano
	vec3 water_azure = vec3(0.28, 0.74, 0.85);
	vec3 foam_pure   = vec3(0.92, 0.97, 1.0) + vec3(micro_noise * 0.08);
	
	float total_water = clamp(water_body1 * 0.55 + water_body2 * 0.40, 0.0, 0.70);
	float total_foam  = clamp(foam_crest1 * 0.95 + foam_crest2 * 0.85 + micro_noise * (foam_crest1 + foam_crest2) * 0.3, 0.0, 1.0);
	
	float trail = noise(p * 0.05 + vec2(t * 0.08, 0.0));
	float foam_trail = (1.0 - smoothstep(reach1, reach1 + 35.0, d)) * smoothstep(0.65, 0.85, trail) * (1.0 - progress1) * 0.55;
	total_foam = clamp(total_foam + foam_trail, 0.0, 1.0);
	
	vec3 final_color = mix(water_azure, foam_pure, total_foam);
	
	// Dissolução suave na direção do mar para fusão 100% perfeita sem linhas de corte
	float bottom_fade = 1.0 - smoothstep(12.0, 55.0, d);
	float final_alpha = clamp(total_water + total_foam * 0.90, 0.0, 0.92) * bottom_fade;
	
	if (final_alpha < 0.12 && wet_sand_mask > 0.05) {
		COLOR = wet_sand_col;
	} else {
		COLOR = vec4(final_color, final_alpha);
	}
}
