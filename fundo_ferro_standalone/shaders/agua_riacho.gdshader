shader_type canvas_item;

uniform sampler2D ruido_a : repeat_enable, filter_linear_mipmap;
uniform sampler2D ruido_b : repeat_enable, filter_linear_mipmap;

// Paleta coerente com o canal de esgoto
uniform vec4 cor_fundo : source_color = vec4(0.03, 0.12, 0.09, 0.92);
uniform vec4 cor_raso  : source_color = vec4(0.10, 0.30, 0.22, 0.92);
uniform vec4 cor_nucleo : source_color = vec4(0.58, 0.85, 0.62, 1.0);
uniform vec4 cor_espuma : source_color = vec4(0.68, 0.84, 0.70, 0.95);
uniform vec4 cor_borda : source_color = vec4(0.02, 0.07, 0.05, 0.95);

// Transições entre trechos (em fração 0..1 do comprimento do Line2D)
uniform float fim_parede_topo = 0.210;       // 52px / 248px
uniform float inicio_parede_base = 0.910;    // 226px / 248px
uniform float transicao_largura = 0.035;

// Velocidades de fluxo independentes
uniform float vel_parede = 0.90;             // Fluxo rápido na parede vertical
uniform float vel_chao = 0.22;               // Mais lento e ondulante no chão
uniform float seed_tempo = 0.0;              // Deslocamento de tempo para desincronizar bueiros

// Irregularidade das bordas
uniform float irregularidade_chao = 0.32;
uniform float irregularidade_parede = 0.06;

void fragment() {
	float t = TIME + seed_tempo;
	
	// Máscara do trecho do chão (1.0 = chão, 0.0 = paredes verticais)
	float m_topo = smoothstep(fim_parede_topo - transicao_largura, fim_parede_topo + transicao_largura, UV.x);
	float m_base = smoothstep(inicio_parede_base + transicao_largura, inicio_parede_base - transicao_largura, UV.x);
	float mascara_chao = m_topo * m_base;
	
	// Ondulação dinâmica transversal que quebra o aspecto de fita uniforme
	float onda_transversal = sin(UV.x * 16.0 - t * 2.8) * 0.09 * mascara_chao;
	float centro = abs((UV.y + onda_transversal) - 0.5) * 2.0;

	// =========================================================================
	// 1. CAMPO DE FLUXO DA PAREDE (Rápido, esticado verticalmente)
	// =========================================================================
	vec2 uv_p1 = vec2(UV.x * 5.0 - t * vel_parede, UV.y * 1.6);
	vec2 uv_p2 = vec2(UV.x * 9.0 - t * (vel_parede * 1.4) + 0.35, UV.y * 3.2);
	// Leve distorção lateral para quebrar a linha reta rígida
	float dist_parede = (texture(ruido_b, uv_p1 * 0.5).r - 0.5) * 0.08;
	float n1_p = texture(ruido_a, uv_p1 + vec2(0.0, dist_parede)).r;
	float n2_p = texture(ruido_b, uv_p2).r;
	float fluxo_parede = n1_p * 0.55 + n2_p * 0.45;

	// =========================================================================
	// 2. CAMPO DE FLUXO DO CHÃO (Turbulento, serpentina orgânica)
	// =========================================================================
	vec2 uv_c1 = vec2(UV.x * 3.8 - t * vel_chao, UV.y * 2.5);
	vec2 uv_c2 = vec2(UV.x * 2.5 - t * (vel_chao * 0.8) + 0.42, UV.y * 4.0);
	// Distorção fluida bidimensional cruzada com pulso temporal
	float pulso = sin(UV.x * 8.0 - t * 1.8) * 0.06;
	vec2 dist_chao = (vec2(texture(ruido_b, uv_c1).r + pulso, texture(ruido_a, uv_c2).r) - 0.5) * 0.18;
	float n1_c = texture(ruido_a, uv_c1 + dist_chao).r;
	float n2_c = texture(ruido_b, uv_c2 - dist_chao * 0.7).r;
	float fluxo_chao = n1_c * 0.58 + n2_c * 0.42;

	// Mistura dos dois fluxos conforme a geometria física
	float fluxo = mix(fluxo_parede, fluxo_chao, mascara_chao);

	// =========================================================================
	// 3. CONTORNO E BORDAS IRREGULARES
	// =========================================================================
	float rb_chao = texture(ruido_a, vec2(UV.x * 6.0 - t * (vel_chao * 0.8), 0.25)).r;
	float irreg = mix(irregularidade_parede, irregularidade_chao, mascara_chao);
	float limite_borda = 0.86 + (rb_chao - 0.5) * irreg * 2.2;
	float mascara_borda = smoothstep(limite_borda, limite_borda - 0.18, centro);

	// =========================================================================
	// 4. COLORIZAÇÃO, TURBULÊNCIA E PROFUNDIDADE
	// =========================================================================
	// Gradiente base entre fundo profundo e água rasa iluminada
	vec3 col = mix(cor_fundo.rgb, cor_raso.rgb, fluxo);

	// Turbulência de água quebrada: veios mais claros e dinâmicos
	float veios = smoothstep(0.58, 0.82, fluxo) * (1.0 - centro * 0.6);
	col = mix(col, cor_nucleo.rgb, veios * 0.65);

	// Brilho especular sutil na crista da onda
	float brilho_onda = pow(fluxo, 3.2) * (1.0 - centro);
	col += cor_nucleo.rgb * (brilho_onda * 0.40);

	// No chão: bordas com lodo escurecido
	float escurecer_borda = smoothstep(0.42, 0.95, centro) * mascara_chao;
	col = mix(col, cor_borda.rgb, escurecer_borda * 0.68);

	// Espuminha fina nas bordas laterais do fluxo
	float espuma_borda = smoothstep(0.70, 0.88, centro) * smoothstep(0.50, 0.80, fluxo);
	col = mix(col, cor_espuma.rgb, espuma_borda * 0.45);

	// Na parede: núcleo central mais claro e rápido
	float nucleo_parede = (1.0 - mascara_chao) * smoothstep(0.45, 0.0, centro) * smoothstep(0.52, 0.92, fluxo_parede);
	col = mix(col, cor_nucleo.rgb, nucleo_parede * 0.50);

	// =========================================================================
	// 5. ESPUMA NA QUINA DO VERTEDOURO (Transição chão -> queda no canal)
	// =========================================================================
	float dist_quina = abs(UV.x - inicio_parede_base);
	float mascara_quina = smoothstep(0.035, 0.005, dist_quina);
	float detalhe_quina = texture(ruido_b, vec2(UV.y * 3.0, t * 0.6)).r;
	float espuma_quina = mascara_quina * (0.35 + 0.35 * detalhe_quina);
	col = mix(col, cor_espuma.rgb, espuma_quina * 0.45);

	// Na queda vertical final para o canal, fundir com a cor verde profunda do canal
	float queda_canal = smoothstep(inicio_parede_base, 1.0, UV.x);
	col = mix(col, cor_fundo.rgb, queda_canal * 0.70);

	// =========================================================================
	// 6. TRANSPARÊNCIA E FADES EXTREMOS
	// =========================================================================
	float alfa_base = mix(cor_raso.a, 0.78, mascara_chao);
	float fade_topo = smoothstep(0.0, 0.06, UV.x);   // Fade suave na saída da grade
	float fade_base = smoothstep(1.0, 0.86, UV.x);   // Fade perfeito ao se unir à água do canal

	float alfa_final = alfa_base * mascara_borda * fade_topo * fade_base;

	COLOR = vec4(col, alfa_final);
}
