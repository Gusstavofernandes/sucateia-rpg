shader_type canvas_item;

uniform sampler2D ruido_a : repeat_enable, filter_linear_mipmap;
uniform sampler2D ruido_b : repeat_enable, filter_linear_mipmap;

uniform vec4 cor_fundo : source_color = vec4(0.03, 0.12, 0.09, 0.92);
uniform vec4 cor_raso  : source_color = vec4(0.10, 0.30, 0.22, 0.92);
uniform vec4 cor_brilho: source_color = vec4(0.55, 0.80, 0.45, 1.0);
uniform vec4 cor_espuma: source_color = vec4(0.45, 0.55, 0.35, 1.0);
uniform vec4 cor_luz   : source_color = vec4(1.0, 0.55, 0.20, 1.0);

uniform float tile_px = 256.0;      // tamanho do ruido em pixels do mundo
uniform vec2  direcao = vec2(1.0, 0.0);
uniform float velocidade = 0.03;
uniform float distorcao = 0.04;
uniform float borda_largura = 0.14; // 0..0.5 (fracao da altura do sprite)

uniform vec2 luzes[4];              // posicoes das lanternas no mundo
uniform int  n_luzes = 0;
uniform float raio_luz = 90.0;

varying vec2 world_pos;

void vertex() {
    world_pos = (MODEL_MATRIX * vec4(VERTEX, 0.0, 1.0)).xy;
}

void fragment() {
    vec2 p = world_pos / tile_px;
    vec2 fluxo = direcao * TIME * velocidade;

    float n1 = texture(ruido_a, p + fluxo).r;
    float n2 = texture(ruido_b, p * 1.7 - fluxo * 0.6 + 0.37).r;

    // camada principal deformada pelas outras duas
    vec2 off = (vec2(n1, n2) - 0.5) * distorcao;
    float n = texture(ruido_a, p * 0.8 + fluxo * 1.3 + off).r;
    float ondas = n * 0.6 + n2 * 0.4;

    vec3 col = mix(cor_fundo.rgb, cor_raso.rgb, ondas);

    // brilhos pontuais (cristas das ondas)
    float brilho = smoothstep(0.78, 0.95, ondas);
    col += cor_brilho.rgb * brilho * 0.30;

    // espuma/lodo nas bordas (UV.y = 0 e 1 sao as margens do canal)
    float d = min(UV.y, 1.0 - UV.y);
    float rb = texture(ruido_b, p * 3.0 + fluxo * 2.0).r;
    float espuma = smoothstep(borda_largura, 0.0, d + (rb - 0.5) * 0.08);
    col = mix(col, cor_espuma.rgb, espuma * 0.55);

    // reflexo das lanternas, quebrado pelas ondas
    float glow = 0.0;
    for (int i = 0; i < n_luzes; i++) {
        float dist = distance(world_pos, luzes[i]);
        glow += smoothstep(raio_luz, 0.0, dist);
    }
    col += cor_luz.rgb * glow * (0.25 + ondas * 0.6) * 0.5;

    float alfa = mix(cor_fundo.a, cor_raso.a, ondas) * smoothstep(0.0, 0.02, d);
    COLOR = vec4(col, alfa);
}
