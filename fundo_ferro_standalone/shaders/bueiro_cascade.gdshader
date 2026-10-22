shader_type canvas_item;

uniform sampler2D cascade_texture : filter_linear, repeat_enable;
uniform float cascade_speed = 0.38;
uniform float turbulence_freq = 14.0;
uniform float turbulence_amp = 0.018;
uniform vec4 water_tint : source_color = vec4(0.95, 1.15, 1.05, 1.0);
uniform float foam_surge = 1.4;

void fragment() {
	// Downward scrolling UV
	float flow_offset = TIME * cascade_speed;
	vec2 uv = UV;
	
	// Turbulent lateral wobble mimicking rapid water rushing over uneven stone
	float wobble = sin(uv.y * turbulence_freq + TIME * 4.5) * turbulence_amp;
	float wobble_fine = cos(uv.y * (turbulence_freq * 2.2) - TIME * 6.0) * (turbulence_amp * 0.45);
	uv.x += wobble + wobble_fine;
	uv.y = fract(uv.y - flow_offset);
	
	// Sample animated cascade texture
	vec4 col = texture(cascade_texture, uv);
	
	// Sample original non-scrolled texture for stable outer alpha boundary (keeps water within chute)
	vec4 shape_ref = texture(TEXTURE, UV);
	
	// Combine color with original alpha envelope
	float final_alpha = col.a * shape_ref.a;
	
	// Dynamic foam surge pulsing
	float lum = dot(col.rgb, vec3(0.299, 0.587, 0.114));
	float is_foam = smoothstep(0.28, 0.65, lum);
	float surge = 0.85 + 0.3 * sin(TIME * 5.0 + UV.y * 8.0);
	
	vec3 rgb = col.rgb * water_tint.rgb;
	rgb += vec3(0.14, 0.20, 0.15) * (is_foam * surge * foam_surge);
	
	COLOR = vec4(rgb, final_alpha);
}
