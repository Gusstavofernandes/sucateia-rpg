shader_type canvas_item;
uniform sampler2D mud : filter_linear, repeat_enable;
uniform vec2 outline_points[16];
varying vec2 world_position;
void vertex(){world_position=(MODEL_MATRIX*vec4(VERTEX,0.,1.)).xy;}
void fragment(){
 vec2 p=world_position;float nearest=10000.;bool inside=false;
 for(int i=0;i<16;i++){vec2 a=outline_points[i];vec2 b=outline_points[(i+1)%16];vec2 ab=b-a;nearest=min(nearest,length(p-a-ab*clamp(dot(p-a,ab)/max(dot(ab,ab),.01),0.,1.)));if((a.y>p.y)!=(b.y>p.y)){if(p.x<(b.x-a.x)*(p.y-a.y)/(b.y-a.y)+a.x)inside=!inside;}}
 float sd=inside?nearest:-nearest;
 float ragged=sin(p.y*.028)*12.+sin(p.x*.022+p.y*.015)*9.;
 float alpha=smoothstep(-115.,65.,sd+ragged);
 COLOR=vec4(texture(mud,p/768.).rgb*vec3(.58,.56,.49),alpha);
}
