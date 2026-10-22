shader_type canvas_item;
varying vec2 world_position;
varying vec4 tint;
float hash(vec2 p){return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453);}
float noise(vec2 p){vec2 i=floor(p);vec2 f=fract(p);f=f*f*(3.0-2.0*f);return mix(mix(hash(i),hash(i+vec2(1,0)),f.x),mix(hash(i+vec2(0,1)),hash(i+vec2(1,1)),f.x),f.y);}
float path_distance(vec2 p,vec2 a,vec2 b){vec2 ab=b-a;return length(p-a-ab*clamp(dot(p-a,ab)/dot(ab,ab),0.0,1.0));}
void vertex(){world_position=(MODEL_MATRIX*vec4(VERTEX,0.,1.)).xy;tint=COLOR;}
void fragment(){
 vec2 p=world_position;vec4 tex=texture(TEXTURE,UV);
 float luma=dot(tex.rgb,vec3(.299,.587,.114));
 tex.rgb=mix(tex.rgb,vec3(luma)*vec3(1.04,1.0,.92),.13);
 float macro=noise(p*.006);float fine=noise(p*.021);
 vec3 shade=mix(vec3(.77,.81,.77),vec3(1.03,1.0,.91),macro);
 float market=1.0-smoothstep(180.,390.,length((p-vec2(1140,1100))*vec2(1.,1.4)));
 float forge=1.0-smoothstep(170.,340.,length((p-vec2(1510,900))*vec2(1.,1.3)));
 shade=mix(shade,vec3(1.04,.98,.83),market*.55);
 shade=mix(shade,vec3(.68,.72,.70),forge*.72);
 shade=mix(shade,vec3(.66,.76,.71),smoothstep(1390.,1490.,p.y)*.5);
 float route=path_distance(p,vec2(1152,1320),vec2(1120,1060));
 route=min(route,path_distance(p,vec2(1120,1060),vec2(1740,1060)));
 route=min(route,path_distance(p,vec2(1300,1060),vec2(1320,690)));
 route=min(route,path_distance(p,vec2(1320,690),vec2(1135,460)));
 route=min(route,path_distance(p,vec2(1740,1060),vec2(2160,1060)));
 route=min(route,path_distance(p,vec2(1512,1300),vec2(1512,1610)));
 // Secondary paths join individual door courts; their narrower wear stays subtle.
 float secondary=path_distance(p,vec2(1120,1060),vec2(850,1090));
 secondary=min(secondary,path_distance(p,vec2(850,1090),vec2(565,1097)));
 secondary=min(secondary,path_distance(p,vec2(1120,1120),vec2(1180,1284)));
 secondary=min(secondary,path_distance(p,vec2(1180,1284),vec2(1508,1340)));
 secondary=min(secondary,path_distance(p,vec2(570,710),vec2(920,735)));
 secondary=min(secondary,path_distance(p,vec2(920,735),vec2(1318,742)));
 secondary=min(secondary,path_distance(p,vec2(855,1090),vec2(850,1300)));
 secondary=min(secondary,path_distance(p,vec2(2013,1090),vec2(2040,1460)));
 secondary=min(secondary,path_distance(p,vec2(2013,1040),vec2(2010,704)));
 float secondary_wear=(1.-smoothstep(12.,49.,secondary+fine*11.))*.42;
 float wear=(1.-smoothstep(38.,100.,route+(fine-.5)*23.))* .79;
 tex.rgb*=shade*(.95+fine*.07);
 tex.rgb=mix(tex.rgb,tex.rgb*vec3(1.25,1.16,.98),max(wear,secondary_wear));
 COLOR=tex*tint;
}
