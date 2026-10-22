shader_type canvas_item;
uniform sampler2D channel_surface : filter_linear, repeat_enable;
varying vec2 world_position;
float hash(vec2 p){return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453);}
float noise(vec2 p){vec2 i=floor(p);vec2 f=fract(p);f=f*f*(3.-2.*f);return mix(mix(hash(i),hash(i+vec2(1,0)),f.x),mix(hash(i+vec2(0,1)),hash(i+vec2(1,1)),f.x),f.y);}
void vertex(){world_position=(MODEL_MATRIX*vec4(VERTEX,0.,1.)).xy;}
void fragment(){
 vec2 p=world_position;
 vec3 water=texture(channel_surface,p/430.0).rgb;
 float depth=.70+.04*sin(p.y*.013+sin(p.x*.029));
 float ripple=sin(p.y*.052+sin(p.x*.06)+TIME*.27)*.014;
 vec3 runoff=water*vec3(.71,.89,.90)*depth+vec3(ripple*.35,ripple*.7,ripple*.6);
 float slow=TIME*.8;
 float n=noise(p*.008+vec2(slow*.006,0.));
 vec3 sea=mix(vec3(.030,.049,.046),vec3(.079,.111,.097),n);
 sea+=texture(channel_surface,p/610.+vec2(slow*.0009,0.)).rgb*.105;
 sea+=(sin(p.y*.063+sin(p.x*.023)*2.+slow)*.5+.5)*.004;
 sea=mix(sea,vec3(.039,.058,.062),smoothstep(.71,.86,noise(p*.014))*.35);
 COLOR=vec4(mix(runoff,sea,smoothstep(1540.,1668.,p.y)),1.);
}
