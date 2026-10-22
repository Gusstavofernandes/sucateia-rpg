shader_type canvas_item;
uniform sampler2D soil : filter_linear, repeat_enable;
varying vec2 world_position;
void vertex(){world_position=(MODEL_MATRIX*vec4(VERTEX,0.,1.)).xy;}
void fragment(){
 vec2 p=world_position;
 vec3 col=texture(soil,p/768.).rgb;
 float ripple=sin(p.y*.007)*.055+sin(p.y*.019+p.x*.003)*.018;
 float side=abs((p.x-1060.)/1650.)+ripple;
 float alpha=(1.-smoothstep(.66,1.0,side))*(1.-smoothstep(120.+sin(p.x*.01)*45.,550.+sin(p.x*.014)*55.,p.y));
 COLOR=vec4(col*mix(.78,.46,clamp(side,0.,1.)),alpha);
}
