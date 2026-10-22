shader_type canvas_item;
uniform vec4 district_tint : source_color = vec4(1.);
varying vec2 world_position;
float hash(vec2 p){return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453);}
float noise(vec2 p){vec2 i=floor(p);vec2 f=fract(p);f=f*f*(3.-2.*f);return mix(mix(hash(i),hash(i+vec2(1,0)),f.x),mix(hash(i+vec2(0,1)),hash(i+vec2(1,1)),f.x),f.y);}
float dist(vec2 p,vec2 a,vec2 b){vec2 ab=b-a;return length(p-a-ab*clamp(dot(p-a,ab)/dot(ab,ab),0.,1.));}
void vertex(){world_position=(MODEL_MATRIX*vec4(VERTEX,0.,1.)).xy;}
void fragment(){
 vec2 p=world_position;vec4 tex=texture(TEXTURE,UV);
 float macro=noise(p*.0045);float grain=noise(p*.023);
 vec3 col=tex.rgb*district_tint.rgb*mix(.84,1.06,macro);
 float path=min(dist(p,vec2(290,1050),vec2(1000,880)),dist(p,vec2(1000,280),vec2(1000,1210)));
 path=min(path,dist(p,vec2(1000,880),vec2(1740,1120)));
 float wear=(1.-smoothstep(28.,90.,path+(grain-.5)*30.))*.53;
 col=mix(col,col*vec3(1.27,1.18,1.06),wear);
 COLOR=vec4(col,tex.a);
}
