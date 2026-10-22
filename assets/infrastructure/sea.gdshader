shader_type canvas_item;
uniform sampler2D grime : filter_linear, repeat_enable;
varying vec2 world_position;
float hash(vec2 p){return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453);}
float noise(vec2 p){vec2 i=floor(p);vec2 f=fract(p);f=f*f*(3.-2.*f);return mix(mix(hash(i),hash(i+vec2(1,0)),f.x),mix(hash(i+vec2(0,1)),hash(i+vec2(1,1)),f.x),f.y);}
void vertex(){world_position=(MODEL_MATRIX*vec4(VERTEX,0.,1.)).xy;}
void fragment(){
 vec2 p=world_position;
 float slow=TIME*.8;
 float n=noise(p*.008+vec2(slow*.006,0.));
 vec3 tex=texture(grime,p/610.+vec2(slow*.0009,0.)).rgb;
 float ripple=sin(p.y*.063+sin(p.x*.023)*2.+slow)*.5+.5;
 vec3 water=mix(vec3(.030,.049,.046),vec3(.079,.111,.097),n);
 water+=tex*.105+ripple*.004;
 float shore=min(min(abs(p.x-148.-sin(p.y*.018)*13.),abs(p.x-2250.-sin(p.y*.015)*17.)),abs(p.y-1680.-sin(p.x*.016)*12.));
 float scum=(1.-smoothstep(3.,39.,shore))*smoothstep(.59,.81,noise(p*.036+vec2(0.,slow*.004)));
 water=mix(water,vec3(.24,.25,.17),scum*.24);
 float slick=smoothstep(.71,.86,noise(p*.014));
 water=mix(water,vec3(.039,.058,.062),slick*.35);
 COLOR=vec4(water,1.);
}
