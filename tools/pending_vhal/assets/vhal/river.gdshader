shader_type canvas_item;
varying vec2 p;
void vertex(){p=(MODEL_MATRIX*vec4(VERTEX,0.,1.)).xy;}
void fragment(){float waves=sin(p.y*.047+p.x*.009+TIME*.44)*sin(p.x*.022-TIME*.12);float silt=sin(p.x*.005+p.y*.009)*.5+.5;vec3 c=mix(vec3(.045,.079,.085),vec3(.076,.115,.116),silt);c+=waves*.006;COLOR=vec4(c,1.);}
