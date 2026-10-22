shader_type canvas_item;

uniform float ripple_speed = 0.55;
uniform float pulse_intensity = 0.28;
uniform vec4 foam_tint : source_color = vec4(0.95, 1.15, 1.05, 1.0);

void fragment() {
	vec2 center = vec2(0.5, 0.5);
	vec2 diff = UV - center;
	float dist = length(diff * vec2(1.0, 1.8)); // Elliptical distortion
	
	// Expanding concentric ripple waves
	float wave1 = sin(dist * 28.0 - TIME * (ripple_speed * 12.0));
	float wave2 = cos(dist * 18.0 - TIME * (ripple_speed * 8.0));
	float ripple = (wave1 * 0.6 + wave2 * 0.4);
	
	vec4 base_tex = texture(TEXTURE, UV);
	
	// Dynamic opacity pulse
	float pulse = 1.0 + sin(TIME * 4.0) * pulse_intensity;
	
	// Foam highlighting
	vec3 rgb = base_tex.rgb * foam_tint.rgb + vec3(0.12, 0.18, 0.12) * (ripple * 0.35);
	float alpha = base_tex.a * (0.8 + 0.2 * ripple) * pulse;
	
	COLOR = vec4(rgb, clamp(alpha, 0.0, 1.0));
}
