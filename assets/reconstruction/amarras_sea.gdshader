shader_type canvas_item;
uniform sampler2D grime : filter_linear, repeat_enable;
uniform vec4 coast_edges[64];
uniform int edge_count=0;
varying vec2 world_position;
float hash(vec2 p){return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453);}
float noise(vec2 p){vec2 i=floor(p);vec2 f=fract(p);f=f*f*(3.-2.*f);return mix(mix(hash(i),hash(i+vec2(1,0)),f.x),mix(hash(i+vec2(0,1)),hash(i+vec2(1,1)),f.x),f.y);}
void vertex(){world_position=(MODEL_MATRIX*vec4(VERTEX,0.,1.)).xy;}
void fragment(){
 vec2 p=world_position;float slow=TIME*.8;
 float n=noise(p*.008+vec2(slow*.006,0.));
 vec3 tex=texture(grime,p/610.+vec2(slow*.0009,0.)).rgb;
 float ripple=sin(p.y*.063+sin(p.x*.023)*2.+slow)*.5+.5;
 vec3 water=mix(vec3(.030,.049,.046),vec3(.079,.111,.097),n)+tex*.105+ripple*.004;
 float shore=10000.;
 for(int i=0;i<64;i++){if(i>=edge_count)break;vec2 a=coast_edges[i].xy;vec2 ab=coast_edges[i].zw-a;shore=min(shore,length(p-a-ab*clamp(dot(p-a,ab)/max(dot(ab,ab),.01),0.,1.)));}
 float scum=(1.-smoothstep(3.,39.,shore))*smoothstep(.59,.81,noise(p*.036+vec2(0.,slow*.004)));
 water=mix(water,vec3(.24,.25,.17),scum*.24);
 water=mix(water,vec3(.039,.058,.062),smoothstep(.71,.86,noise(p*.014))*.35);
 COLOR=vec4(water,smoothstep(3770.,3960.,p.x));
}

