shader_type canvas_item;
void fragment(){vec2 p=SCREEN_UV*2.0-1.0;float vignette=smoothstep(.55,1.35,length(p));float mist=sin(SCREEN_UV.x*13.0+SCREEN_UV.y*10.0+TIME*.04)*.5+.5;COLOR=vec4(.13,.20,.20,vignette*.15+mist*.015);}
