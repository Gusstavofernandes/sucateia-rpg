shader_type canvas_item;
uniform vec2 outline_points[32];
uniform vec4 route_segments[32];
uniform int route_count=0;
uniform vec4 cargo_segments[8];
uniform int cargo_count=0;
uniform sampler2D grime : filter_linear, repeat_enable;
uniform sampler2D metal : filter_linear;
varying vec2 world_position;
float hash(vec2 p){return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453);}
float noise(vec2 p){vec2 i=floor(p),f=fract(p);f=f*f*(3.-2.*f);return mix(mix(hash(i),hash(i+vec2(1,0)),f.x),mix(hash(i+vec2(0,1)),hash(i+vec2(1,1)),f.x),f.y);}
float distance_to(vec2 p,vec2 a,vec2 b){vec2 v=b-a;return length(p-a-v*clamp(dot(p-a,v)/max(dot(v,v),.01),0.,1.));}
void vertex(){world_position=(MODEL_MATRIX*vec4(VERTEX,0.,1.)).xy;}
void fragment(){
 vec2 p=world_position;vec4 stone=texture(TEXTURE,UV);float edge=10000.;bool inside=false;
 for(int i=0;i<32;i++){
  vec2 a=outline_points[i],b=outline_points[(i+1)%32];
  if((a.y>p.y)!=(b.y>p.y)){if(p.x<(b.x-a.x)*(p.y-a.y)/(b.y-a.y)+a.x)inside=!inside;}
 }
 for(int i=0;i<32;i++)edge=min(edge,distance_to(p,outline_points[i],outline_points[(i+1)%32]));
 float road=10000.;for(int i=0;i<32;i++){if(i>=route_count)break;road=min(road,distance_to(p,route_segments[i].xy,route_segments[i].zw));}
 float cargo=10000.;for(int i=0;i<8;i++){if(i>=cargo_count)break;cargo=min(cargo,distance_to(p,cargo_segments[i].xy,cargo_segments[i].zw));}
 float cargo_use=1.-smoothstep(31.,97.,cargo);
 float use=1.-smoothstep(22.,82.,road);float wet=1.-smoothstep(80.,240.,edge);
 float transition=smoothstep(3970.,4360.,p.x);
 vec3 col=stone.rgb*mix(vec3(.57,.55,.49),vec3(.63,.67,.63),transition);
 col=mix(col,texture(grime,p/840.).rgb*vec3(.50,.56,.49),.15+wet*.17);
 col*=mix(.91,1.06,noise(p*.008));
 vec3 worn=col*vec3(1.34,1.27,1.12);
 worn=mix(worn,texture(grime,p/840.).rgb*vec3(.66,.63,.51),.12);
 col=mix(col,worn,use*.46+cargo_use*.38);
 vec4 plates=texture(metal,fract((p+vec2(13.,41.))/171.));
 float work=1.-smoothstep(110.,310.,length((p-vec2(4700.,420.))*vec2(1.,1.15)));
 col=mix(col,plates.rgb*vec3(.57,.58,.51),plates.a*(work*.27+use*.07));
 COLOR=vec4(col,stone.a*smoothstep(0.,28.,edge)*(inside?1.:0.));
}
