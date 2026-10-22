shader_type canvas_item;
varying vec2 world_position;
uniform vec2 player_position;
uniform bool surface_player = true;
void vertex() { world_position = (MODEL_MATRIX * vec4(VERTEX,0.,1.)).xy; }
void fragment() {
    vec4 tex = COLOR;
    float reveal = 1. - smoothstep(42.,100.,distance(world_position,player_position));
    if (surface_player) tex.a *= mix(1.,.06,reveal);
    COLOR = tex;
}
