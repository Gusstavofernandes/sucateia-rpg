shader_type canvas_item;
uniform sampler2D ground_texture : filter_linear, repeat_enable;
varying vec2 world_position;
void vertex(){world_position=(MODEL_MATRIX*vec4(VERTEX,0.,1.)).xy;}
void fragment(){
 vec2 p=world_position;
 vec3 ground=texture(ground_texture,p/720.).rgb;
 float fade=smoothstep(-2310.,-2060.,p.y)*(1.-smoothstep(3950.,4280.,p.x))*smoothstep(1770.,2090.,p.x);
 COLOR=vec4(ground*vec3(.42,.38,.31),fade*.9);
}
