shader_type canvas_item;
uniform sampler2D mud : filter_linear, repeat_enable;
uniform vec2 outline_points[16];
uniform vec4 segments[40];
uniform int segment_count=0;
varying vec2 world_position;

float hash(vec2 p){return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453);}
float noise(vec2 p){vec2 i=floor(p);vec2 f=fract(p);f=f*f*(3.-2.*f);return mix(mix(hash(i),hash(i+vec2(1,0)),f.x),mix(hash(i+vec2(0,1)),hash(i+vec2(1,1)),f.x),f.y);}

float edge_distance(vec2 p){
 float nearest=10000.;bool inside=false;
 for(int i=0;i<16;i++){vec2 a=outline_points[i];vec2 b=outline_points[(i+1)%16];vec2 ab=b-a;nearest=min(nearest,length(p-a-ab*clamp(dot(p-a,ab)/max(dot(ab,ab),.01),0.,1.)));if((a.y>p.y)!=(b.y>p.y)){if(p.x<(b.x-a.x)*(p.y-a.y)/(b.y-a.y)+a.x)inside=!inside;}}
 float coverage=inside?nearest:-nearest;
 for(int i=0;i<40;i++){if(i>=segment_count)break;vec2 a=segments[i].xy;vec2 ab=segments[i].zw-a;coverage=max(coverage,108.-length(p-a-ab*clamp(dot(p-a,ab)/max(dot(ab,ab),.01),0.,1.)));}
 return coverage;
}

void vertex(){
	world_position=(MODEL_MATRIX*vec4(VERTEX,0.,1.)).xy;
}

void fragment(){
	vec2 p=world_position;
	vec4 stone=texture(TEXTURE,UV);
	vec3 soil=texture(mud,p/768.).rgb;
	float west=1.-smoothstep(-200.,640.,p.x);
	float patch=noise(p*.009);
	float blend=clamp(west*.78+(patch-.5)*.28,0.,.89);
	
	// Solo original de Sucateia: neutro natural (sem vermelho artificial saturado)
	float red_factor = smoothstep(-150.0, -850.0, p.x);
	vec3 soil_tint = mix(vec3(.85, .78, .66), vec3(1.05, .78, .64), red_factor);
	
	// Transição suave para a areia amarela/ouro do deserto a oeste
	float yellow_factor = smoothstep(-1400.0, -3500.0, p.x);
	vec3 yellow_soil = vec3(1.14, 0.98, 0.58);
	soil_tint = mix(soil_tint, yellow_soil, yellow_factor);
	
	vec3 col=mix(stone.rgb,soil*soil_tint,blend);
	col*=mix(.81,1.04,noise(p*.0037));
	COLOR=vec4(col,stone.a*smoothstep(8.,65.,edge_distance(p)));
}
