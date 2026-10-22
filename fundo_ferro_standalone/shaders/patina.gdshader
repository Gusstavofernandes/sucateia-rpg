shader_type canvas_item;
varying vec2 world_position;
varying vec4 tint;
float hash(vec2 p) {return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453);}
float noise(vec2 p) {vec2 i=floor(p);vec2 f=fract(p);f=f*f*(3.0-2.0*f);return mix(mix(hash(i),hash(i+vec2(1,0)),f.x),mix(hash(i+vec2(0,1)),hash(i+vec2(1,1)),f.x),f.y);}
void vertex(){tint=COLOR;world_position=(MODEL_MATRIX*vec4(VERTEX,0.0,1.0)).xy;}
void fragment(){vec4 tex=texture(TEXTURE,UV);float grain=hash(floor(world_position*1.7));float wear=noise(world_position*.07);float stain=noise(world_position*.013);tex.rgb*=.94+grain*.075+wear*.07;tex.rgb=mix(tex.rgb,tex.rgb*vec3(.79,.86,.77),smoothstep(.47,.82,stain)*.42);COLOR=tex*tint;}

