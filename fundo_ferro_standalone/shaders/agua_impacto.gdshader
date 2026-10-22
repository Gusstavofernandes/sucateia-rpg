shader_type canvas_item;

uniform vec4 cor_espuma : source_color = vec4(0.65, 0.80, 0.65, 1.0);
uniform float velocidade = 1.6;

void fragment() {
    vec2 q = (UV - 0.5) * vec2(2.0, 4.0);   // achatado em elipse
    float d = length(q);
    float anel = fract(d * 1.5 - TIME * velocidade);
    anel = smoothstep(0.0, 0.15, anel) * smoothstep(0.55, 0.15, anel);
    float borda = smoothstep(1.0, 0.6, d);
    COLOR = vec4(cor_espuma.rgb, anel * borda * 0.5);
}
