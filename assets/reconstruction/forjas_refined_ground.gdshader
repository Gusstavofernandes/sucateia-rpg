shader_type canvas_item;
uniform vec2 outline_points[16];
uniform vec4 segments[48];
uniform int segment_count=0;
uniform sampler2D grime : filter_linear, repeat_enable;
uniform sampler2D metal : filter_linear;
uniform sampler2D dirt : filter_linear;
varying vec2 world_position;
float hash(vec2 p){return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453);}
float noise(vec2 p){vec2 i=floor(p),f=fract(p);f=f*f*(3.-2.*f);return mix(mix(hash(i),hash(i+vec2(1,0)),f.x),mix(hash(i+vec2(0,1)),hash(i+vec2(1,1)),f.x),f.y);}
float coverage(vec2 p){float d=10000.;bool inside=false;for(int i=0;i<16;i++){vec2 a=outline_points[i],b=outline_points[(i+1)%16],v=b-a;d=min(d,length(p-a-v*clamp(dot(p-a,v)/max(dot(v,v),.01),0.,1.)));if((a.y>p.y)!=(b.y>p.y)){if(p.x<(b.x-a.x)*(p.y-a.y)/(b.y-a.y)+a.x)inside=!inside;}}d=inside?d:-d;for(int i=0;i<48;i++){if(i>=segment_count)break;vec2 a=segments[i].xy,v=segments[i].zw-a;d=max(d,86.-length(p-a-v*clamp(dot(p-a,v)/max(dot(v,v),.01),0.,1.)));}return d;}
float zone(vec2 p,vec2 c,vec2 s){vec2 q=abs(p-c)/s;return 1.-smoothstep(.55,1.,max(q.x,q.y));}
void vertex(){world_position=(MODEL_MATRIX*vec4(VERTEX,0.,1.)).xy;}
void fragment(){
 vec2 p=world_position;vec4 stone=texture(TEXTURE,UV);vec3 patina=texture(grime,p/697.).rgb;
 // Transition occupies approximately the first 20% of the industrial width.
 float industrial=smoothstep(1710.,2120.,p.x);float edge=1.-smoothstep(35.,180.,coverage(p));
 float hot=max(zone(p,vec2(2700.,-1000.),vec2(410.,420.)),zone(p,vec2(3170.,-950.),vec2(260.,250.)));
 float works=max(zone(p,vec2(2800.,-500.),vec2(330.,300.)),zone(p,vec2(3400.,-740.),vec2(260.,270.)));
 float cargo=zone(p,vec2(2500.,-20.),vec2(315.,230.));
 float coal=zone(p,vec2(2500.,-1160.),vec2(180.,125.));
 float cooling=zone(p,vec2(2740.,-290.),vec2(230.,145.));
 float maintenance=zone(p,vec2(2780.,-475.),vec2(225.,130.));
 float slag=zone(p,vec2(3520.,-870.),vec2(200.,220.));
 float luminance=dot(stone.rgb,vec3(.299,.587,.114));
 vec3 industrial_stone=mix(stone.rgb*.48,vec3(luminance)*vec3(.58,.56,.53),.72);
 vec3 col=mix(stone.rgb*vec3(.94,.91,.84),industrial_stone,industrial);
 col=mix(col,patina*vec3(.49,.44,.35),industrial*(.12+noise(p*.011)*.22)+edge*.48);
 col*=mix(vec3(1.),vec3(.66,.58,.47),hot*.8);
 // Local material use defines work zones without increasing noisy tile repetition.
 col*=mix(vec3(1.),vec3(.46,.44,.42),coal*.78+maintenance*.22);
 col=mix(col,col*vec3(.65,.79,.81),cooling*.65);
 col=mix(col,col*vec3(1.28,.86,.69),slag*.62);
 vec4 plates=texture(metal,fract((p+vec2(43.,19.))/142.));
 float transition=(1.-smoothstep(2050.,2250.,p.x))*industrial;
 float panel=(hot*.22+works*.48+cargo*.35+transition*.22+maintenance*.22+cooling*.16)*industrial;
 col=mix(col,plates.rgb*vec3(.60,.54,.43),plates.a*panel);
 vec4 residue=texture(dirt,fract(p/211.));
 col=mix(col,residue.rgb*vec3(.44,.38,.28),residue.a*(edge*.55+hot*.19));
 float street=10000.;
 for(int i=0;i<6;i++){vec2 a=segments[i].xy,v=segments[i].zw-a;street=min(street,length(p-a-v*clamp(dot(p-a,v)/max(dot(v,v),.01),0.,1.)));}
 col*=mix(.88,1.07,noise(p*.005));
 col=mix(col,col*vec3(1.25,1.18,1.05),industrial*(1.-smoothstep(26.,64.,street))*.55);
 COLOR=vec4(col,stone.a*smoothstep(2.,45.,coverage(p)));
}
