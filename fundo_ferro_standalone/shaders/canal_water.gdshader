shader_type canvas_item;

uniform sampler2D water_texture : filter_linear, repeat_enable;
uniform vec2 flow_direction = vec2(1.0, 0.0);
uniform float flow_speed = 0.09;
uniform float wave_frequency = 0.04;
uniform float wave_amplitude = 0.015;
uniform vec4 water_tint : source_color = vec4(0.92, 1.15, 1.05, 1.0);
uniform float foam_boost = 1.35;
uniform float depth_darkening = 0.45;

varying vec2 world_pos;

void vertex() {
	world_pos = (MODEL_MATRIX * vec4(VERTEX, 0.0, 1.0)).xy;
}

void fragment() {
	// Base world coordinate UVs for continuous flow without tiling seams across 4200px
	vec2 base_uv = world_pos * 0.0022;
	
	// Primary flow layer
	float t1 = TIME * flow_speed;
	vec2 uv1 = base_uv - flow_direction * t1;
	
	// Secondary counter-flow / eddy layer at different scale and angle
	float t2 = TIME * (flow_speed * 0.65);
	vec2 uv2 = base_uv * 1.38 + vec2(-0.85, 0.25) * t2;
	
	// Procedural wave displacement
	float wave_disp1 = sin(world_pos.y * wave_frequency + TIME * 2.2) * wave_amplitude;
	float wave_disp2 = cos(world_pos.x * (wave_frequency * 0.8) + TIME * 1.8) * wave_amplitude;
	uv1 += vec2(wave_disp2, wave_disp1);
	uv2 += vec2(-wave_disp1, wave_disp2);
	
	vec4 col1 = texture(water_texture, uv1);
	vec4 col2 = texture(water_texture, uv2);
	
	// Blend the two fluid layers for organic vortex motion
	vec4 water_color = mix(col1, col2, 0.42);
	
	// Detect and boost foam streaks and oil film
	float lum = dot(water_color.rgb, vec3(0.299, 0.587, 0.114));
	float foam_mask = smoothstep(0.22, 0.55, lum);
	
	// Apply tint and foam
	vec3 final_rgb = water_color.rgb * water_tint.rgb;
	final_rgb += vec3(0.12, 0.18, 0.14) * (foam_mask * foam_boost);
	
	// Edge depth shading: darken near north (Y=485) and south (Y=565) retaining walls
	float canal_center_y = 525.0;
	float dist_from_center = abs(world_pos.y - canal_center_y) / 40.0;
	float edge_shadow = smoothstep(0.35, 1.0, dist_from_center);
	final_rgb = mix(final_rgb, final_rgb * (1.0 - depth_darkening), edge_shadow);
	
	COLOR = vec4(final_rgb, 1.0);
}
