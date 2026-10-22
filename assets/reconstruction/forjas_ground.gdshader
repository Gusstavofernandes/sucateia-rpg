shader_type canvas_item;
uniform vec2 outline_points[16];
uniform vec4 segments[48];
uniform int segment_count=0;
uniform sampler2D grime : filter_linear, repeat_enable;
varying vec2 world_position;
float hash(vec2 p){return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453);}
float noise(vec2 p){vec2 i=floor(p),f=fract(p);f=f*f*(3.-2.*f);return mix(mix(hash(i),hash(i+vec2(1,0)),f.x),mix(hash(i+vec2(0,1)),hash(i+vec2(1,1)),f.x),f.y);}
float coverage(vec2 p){float d=10000.;bool inside=false;for(int i=0;i<16;i++){vec2 a=outline_points[i],b=outline_points[(i+1)%16],v=b-a;d=min(d,length(p-a-v*clamp(dot(p-a,v)/max(dot(v,v),.01),0.,1.)));if((a.y>p.y)!=(b.y>p.y)){if(p.x<(b.x-a.x)*(p.y-a.y)/(b.y-a.y)+a.x)inside=!inside;}}d=inside?d:-d;for(int i=0;i<48;i++){if(i>=segment_count)break;vec2 a=segments[i].xy,v=segments[i].zw-a;d=max(d,86.-length(p-a-v*clamp(dot(p-a,v)/max(dot(v,v),.01),0.,1.)));}return d;}
void vertex(){world_position=(MODEL_MATRIX*vec4(VERTEX,0.,1.)).xy;}
void fragment(){vec2 p=world_position;vec4 stone=texture(TEXTURE,UV);vec3 patina=texture(grime,p/817.).rgb;float blend=smoothstep(1690.,2450.,p.x)*(.08+noise(p*.008)*.21);vec3 col=mix(stone.rgb,patina*.70,blend);col*=mix(.80,1.03,noise(p*.004));COLOR=vec4(col,stone.a*smoothstep(2.,45.,coverage(p)));}
