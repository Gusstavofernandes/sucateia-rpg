from pathlib import Path
import os, subprocess, sys
root=Path(__file__).resolve().parents[1]
engine=Path(r'C:\Users\Usuario\Downloads\Godot_v4.7.2-stable_mono_win64\Godot_v4.7.2-stable_mono_win64\Godot_v4.7.2-stable_mono_win64_console.exe')
env=dict(os.environ,APPDATA=str(root/'.runtime'),LOCALAPPDATA=str(root/'.runtime'))
for mode in sys.argv[1:] or ['stitch_overview','stitch_sorting','stitch_service','stitch_urban','stitch_mouths']:
    log=root/'tools'/f'capture_{mode}.log'
    result=subprocess.run([str(engine),'--path',str(root),'--log-file',str(log),'--script','tools/capture_port_stitch.gd','--',f'--capture={mode}'],cwd=root,env=env,capture_output=True,text=True,timeout=180)
    output=log.read_text(encoding='utf-8-sig')
    if result.returncode or 'ERROR:' in output or '.png 0 ' not in output:
        print(output,flush=True);sys.exit(1)
    print(output.splitlines()[-1],flush=True)
