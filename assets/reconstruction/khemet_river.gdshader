shader_type canvas_item;

// =============================================================================
// ÁGUA DOCE DE KHEMET-RA: RIO SAGRADO, OÁSIS E CANAIS DE IRRIGAÇÃO
// mode 0 = rio (COLOR.r = posição transversal 0..1, COLOR.g = distância ao longo / 4000)
// mode 1 = lago do oásis (máscara elíptica em coordenadas de mundo)
// mode 2 = canal de irrigação (igual ao rio, mais raso e calmo)
// =============================================================================

uniform int mode = 0;
uniform vec2 lake_center = vec2(0.0);
uniform vec2 lake_radii = vec2(400.0, 220.0);
uniform float flow_speed = 38.0;

varying vec2 world_position;
varying vec4 vcol;

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

void vertex() {
	world_position = (MODEL_MATRIX * vec4(VERTEX, 0.0, 1.0)).xy;
	vcol = COLOR;
}

void fragment() {
	vec2 p = world_position;
	float t = TIME;

	// Paleta de água doce: verde-jade raso nas margens, azul-petróleo no canal central
	vec3 c_edge    = vec3(0.30, 0.50, 0.40);
	vec3 c_shallow = vec3(0.16, 0.44, 0.48);
	vec3 c_deep    = vec3(0.05, 0.22, 0.32);
	vec3 c_foam    = vec3(0.86, 0.92, 0.86);

	float depth;      // 0 na margem, 1 no centro
	float edge_alpha;
	vec2 flow_uv;

	if (mode == 1) {
		vec2 q = (p - lake_center) / lake_radii;
		float wobble = (noise(p * 0.012) - 0.5) * 0.10;
		float d = length(q) + wobble;
		depth = clamp(1.0 - d, 0.0, 1.0);
		edge_alpha = 1.0 - smoothstep(0.93, 1.0, d);
		flow_uv = p * 0.02 + vec2(t * 0.05, t * 0.03);
	} else {
		float across = vcol.r;
		float along = vcol.g * 4000.0;
		depth = 1.0 - abs(across * 2.0 - 1.0);
		edge_alpha = smoothstep(0.0, 0.10, depth);
		float spd = (mode == 2) ? flow_speed * 0.45 : flow_speed;
		flow_uv = vec2(along * 0.018 - t * spd * 0.018, across * 5.0);
	}

	float d_curve = smoothstep(0.0, 0.85, depth);
	vec3 water = mix(c_edge, c_shallow, smoothstep(0.0, 0.25, depth));
	water = mix(water, c_deep, d_curve * (mode == 2 ? 0.35 : 1.0));

	// Correnteza: estrias alongadas que descem o rio
	float streak = noise(flow_uv * vec2(1.0, 1.0)) * noise(flow_uv * vec2(2.3, 1.7) + 3.1);
	water += vec3(0.10, 0.14, 0.13) * smoothstep(0.30, 0.60, streak) * (0.4 + depth * 0.6);

	// Reflexo solar do deserto (cintilação dourada suave)
	float glint = noise(p * 0.09 + vec2(t * 0.6, -t * 0.4));
	water += vec3(0.20, 0.17, 0.08) * smoothstep(0.82, 0.97, glint) * depth;

	// Espuma e areia molhada nas margens
	float edge_band = 1.0 - smoothstep(0.0, 0.16, depth);
	float foam_n = noise(p * 0.07 + vec2(t * 0.3, 0.0));
	water = mix(water, c_foam, edge_band * smoothstep(0.55, 0.80, foam_n) * 0.55);

	COLOR = vec4(water, 0.94 * edge_alpha);
}
