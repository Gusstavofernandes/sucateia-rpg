shader_type canvas_item;

uniform sampler2D ruido : repeat_enable, filter_linear_mipmap;
uniform vec4 cor_umidade : source_color = vec4(0.01, 0.04, 0.03, 0.55);

void fragment() {
	// Gradiente transversal suave (1.0 no centro, 0.0 nas bordas da umidade)
	float centro = abs(UV.y - 0.5) * 2.0;
	float r = texture(ruido, vec2(UV.x * 4.0, UV.y * 2.0)).r;
	
	// Borda porosa absorvida pela pedra
	float limite = 0.95 + (r - 0.5) * 0.25;
	float mascara = smoothstep(limite, 0.0, centro);
	
	// Fades suaves no início e fim do piso
	float fade_x = smoothstep(0.0, 0.08, UV.x) * smoothstep(1.0, 0.92, UV.x);
	
	COLOR = vec4(cor_umidade.rgb, cor_umidade.a * mascara * fade_x);
}
