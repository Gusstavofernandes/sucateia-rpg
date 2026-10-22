shader_type canvas_item;
uniform sampler2D rock : filter_linear, repeat_enable;
varying vec2 world_position;
void vertex(){world_position=(MODEL_MATRIX*vec4(VERTEX,0.,1.)).xy;}
void fragment(){vec2 p=world_position;vec3 color=texture(rock,p/947.).rgb;float seams=sin(p.x*.004+p.y*.007)*.009;COLOR=vec4(color*vec3(.19,.23,.21)+vec3(.011,.015,.013)+seams,1.);}
