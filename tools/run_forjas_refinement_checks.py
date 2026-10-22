from pathlib import Path
import subprocess,sys
root=Path(__file__).resolve().parents[1]
names=['test_forjas_production','test_forjas_refinement_preservation','test_forjas_functional_modules','test_forjas_render_order','test_forjas_rasas','test_forjas_preservation','test_alto_lixo','test_alto_refinement','test_lower_coast','test_market_expansion','test_slice','test_fundo_access','test_fundo_layout']
sys.exit(subprocess.call([sys.executable,str(root/'tools/run_fundo_checks.py'),*(sys.argv[1:] or names)],cwd=root))
