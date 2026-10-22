shader_type canvas_item;
varying vec2 position;
float hash(vec2 p){return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453);}
void vertex(){position=(MODEL_MATRIX*vec4(VERTEX,0.,1.)).xy;}
void fragment(){vec4 stone=texture(TEXTURE,UV);float patch=hash(floor(position/133.));float damp=smoothstep(.63,.9,patch);vec3 col=stone.rgb*mix(vec3(.77,.83,.76),vec3(.53,.67,.61),damp);COLOR=vec4(col,stone.a);}
