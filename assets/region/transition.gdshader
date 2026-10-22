shader_type canvas_item;
uniform sampler2D dirt : filter_linear, repeat_enable;
uniform sampler2D stone : filter_linear, repeat_enable;
varying vec2 world_position;
void vertex(){world_position=(MODEL_MATRIX*vec4(VERTEX,0.,1.)).xy;}
void fragment(){vec2 p=world_position;vec3 a=texture(dirt,p/768.).rgb*.83;vec3 c=texture(stone,p/768.).rgb*vec3(.69,.81,.78);float blend=smoothstep(660.,1380.,p.x+sin(p.y*.035)*39.);COLOR=vec4(mix(a,c,blend),1.);}
