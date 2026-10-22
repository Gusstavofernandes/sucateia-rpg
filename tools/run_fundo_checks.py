from pathlib import Path
import os, subprocess,sys
root=Path(__file__).resolve().parents[1]
engine=Path(r'C:\Users\Usuario\Downloads\Godot_v4.7.2-stable_mono_win64\Godot_v4.7.2-stable_mono_win64\Godot_v4.7.2-stable_mono_win64_console.exe')
env=dict(os.environ,APPDATA=str(root/'.runtime'),LOCALAPPDATA=str(root/'.runtime'))
names=['test_fundo_layout','test_fundo_access','test_fundo_preservation','test_forjas_render_order','test_forjas_rasas','test_forjas_preservation','test_alto_lixo','test_alto_refinement','test_lower_coast','test_market_expansion','test_slice']
if len(sys.argv)>1:names=sys.argv[1:]
failed=[]
for name in names:
    log=root/'tools'/f'fundo_{name}.log'
    try:
        result=subprocess.run([str(engine),'--path',str(root),'--headless','--log-file',str(log),'--script',f'tests/{name}.gd'],cwd=root,env=env,capture_output=True,text=True,timeout=120)
        text=log.read_text(encoding='utf-8-sig');good=result.returncode==0 and 'PASS:' in text and 'ERROR:' not in text
    except subprocess.TimeoutExpired:
        good=False;text=log.read_text(encoding='utf-8-sig') if log.exists() else 'timeout'
    print(name,'PASS' if good else 'FAIL',flush=True);print('\n'.join(text.splitlines()[-10:]),flush=True)
    if not good:failed.append(name)
print('RESULT',len(names)-len(failed),'/',len(names),'passed',flush=True)
sys.exit(bool(failed))
