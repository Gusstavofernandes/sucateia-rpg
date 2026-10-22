shader_type canvas_item;
uniform sampler2D soil : filter_linear, repeat_enable;
varying vec2 world_position;
void vertex(){world_position=(MODEL_MATRIX*vec4(VERTEX,0.,1.)).xy;}
void fragment(){vec2 p=world_position;vec3 col=texture(soil,p/768.).rgb;float fringe=clamp(length((p-vec2(1000,760))*vec2(.001,.0013)),0.,1.);COLOR=vec4(col*mix(.63,.25,fringe),1.);}
