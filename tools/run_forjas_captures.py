from pathlib import Path
import os, subprocess, sys
root=Path(__file__).resolve().parents[1]
engine=Path(r'C:\Users\Usuario\Downloads\Godot_v4.7.2-stable_mono_win64\Godot_v4.7.2-stable_mono_win64\Godot_v4.7.2-stable_mono_win64_console.exe')
env=dict(os.environ,APPDATA=str(root/'.runtime'),LOCALAPPDATA=str(root/'.runtime'))
names=['forjas_district','forjas_full','forjas_frontier','forjas_foundry','forjas_recycling','forjas_drain']
if len(sys.argv)>1:names=sys.argv[1:]
for name in names:
    log=root/'tools'/f'capture_{name}.log'
    result=subprocess.run([str(engine),'--path',str(root),'--log-file',str(log),'--',f'--capture={name}'],cwd=root,env=env,capture_output=True,text=True,timeout=300 if name.endswith('_full') else 180)
    text=log.read_text(encoding='utf-8-sig')
    if result.returncode or 'ERROR:' in text or '.png 0 ' not in text:
        print(text,flush=True);sys.exit(1)
    print(text.splitlines()[-1],flush=True)
print('PASS:',len(names),'Forjas captures saved',flush=True)
