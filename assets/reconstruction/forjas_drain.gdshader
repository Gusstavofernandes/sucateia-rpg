shader_type canvas_item;
uniform sampler2D grime : filter_linear, repeat_enable;
varying vec2 world_position;
void vertex(){world_position=(MODEL_MATRIX*vec4(VERTEX,0.,1.)).xy;}
void fragment(){
 vec2 p=world_position;vec3 dirt=texture(grime,p/310.+vec2(TIME*.003,0.)).rgb;
 float ripples=sin(p.x*.028+p.y*.07+TIME*.5)*.018;
 // Cooling return has a localized stained plume and moving surface rings.
 float outfall=exp(-length((p-vec2(2860.,155.))/vec2(115.,36.))*2.);
 float rings=sin(length(p-vec2(2860.,155.))*.17-TIME*1.4)*.5+.5;
 vec3 col=dirt*vec3(.16,.24,.20)+vec3(.008,.014,.012)+ripples;
 col+=outfall*vec3(.047,.033,.016)*(rings*.5+.5);
 COLOR=vec4(col,1.);
}
