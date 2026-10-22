shader_type canvas_item;
uniform sampler2D stone : filter_linear, repeat_enable;
varying vec2 world_position;
void vertex(){world_position=(MODEL_MATRIX*vec4(VERTEX,0.,1.)).xy;}
void fragment(){vec3 tex=texture(stone,world_position/650.).rgb;COLOR=vec4(tex*vec3(.16,.23,.22),1.);}
