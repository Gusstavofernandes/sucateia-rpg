shader_type canvas_item;
uniform sampler2D metal : filter_linear;
uniform sampler2D dirt : filter_linear;
varying vec2 position;
float hash(vec2 p){return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453);}
float area(vec2 center,vec2 size){vec2 q=abs(position-center)/size;return 1.-smoothstep(.62,1.,max(q.x,q.y));}
void vertex(){position=(MODEL_MATRIX*vec4(VERTEX,0.,1.)).xy;}
void fragment(){
 vec4 stone=texture(TEXTURE,UV);
 float noise=hash(floor(position/83.));
 float wet=area(vec2(1750.,2040.),vec2(270.,175.))+area(vec2(2700.,1125.),vec2(305.,210.));
 float refuse=area(vec2(2300.,2250.),vec2(335.,175.));
 float engine=area(vec2(3040.,1690.),vec2(225.,190.));
 float ruin=area(vec2(1750.,1030.),vec2(270.,250.));
 float valves=area(vec2(3150.,670.),vec2(265.,220.));
 vec3 col=stone.rgb*mix(vec3(.78,.83,.76),vec3(.57,.68,.61),noise*.44);
 col*=mix(vec3(1.),vec3(.53,.76,.67),min(1.,wet)*.76);
 col*=mix(vec3(1.),vec3(1.12,.85,.61),refuse*.77);
 col*=mix(vec3(1.),vec3(.69,.70,.66),engine*.7);
 col*=mix(vec3(1.),vec3(1.13,1.09,.92),ruin*.60);
 col*=mix(vec3(1.),vec3(.73,.81,.85),valves*.6);
 vec4 plates=texture(metal,fract((position+vec2(39.,19.))/112.));
 float apron=max(engine,refuse*.58);
 col=mix(col,plates.rgb*vec3(.63,.64,.57),plates.a*apron*.61);
 vec4 grime=texture(dirt,fract(position/193.));
 col=mix(col,grime.rgb*vec3(.55,.51,.40),grime.a*(ruin*.36+refuse*.25+wet*.20));
 COLOR=vec4(col,stone.a);
}
