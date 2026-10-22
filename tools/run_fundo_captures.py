from pathlib import Path
import os,subprocess,sys
root=Path(__file__).resolve().parents[1]
engine=Path(r'C:\Users\Usuario\Downloads\Godot_v4.7.2-stable_mono_win64\Godot_v4.7.2-stable_mono_win64\Godot_v4.7.2-stable_mono_win64_console.exe')
env=dict(os.environ,APPDATA=str(root/'.runtime'),LOCALAPPDATA=str(root/'.runtime'))
names=['fundo_full']+['fundo_'+r for r in ['PocoVelho','Bombas','Descarte','Maquinas','Reservatorio','Ruinas','Valvulas','Arena']]+['fundo_surface_'+r for r in ['PocoVelho','DocaLeste','ForjasManutencao']]
if len(sys.argv)>1:names=sys.argv[1:]
for name in names:
    log=root/'tools'/f'capture_{name}.log'
    scene='res://maps/sucateia/sucateia.tscn' if name.startswith('fundo_surface') else 'res://maps/fundo_ferro/fundo_ferro.tscn'
    result=subprocess.run([str(engine),'--path',str(root),scene,'--log-file',str(log),'--',f'--capture={name}'],cwd=root,env=env,capture_output=True,text=True,timeout=120)
    text=log.read_text(encoding='utf-8-sig')
    if result.returncode or 'ERROR:' in text or 'CAPTURE' not in text:
        print(text,flush=True);sys.exit(1)
    print(text.splitlines()[-1],flush=True)
print('PASS:',len(names),'Fundo captures saved',flush=True)
