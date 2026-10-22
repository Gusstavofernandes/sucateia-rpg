import os
import json

log_dir = r'C:\Users\Usuario\.gemini\antigravity\brain'
for root, dirs, files in os.walk(log_dir):
    for f in files:
        if f == 'transcript.jsonl':
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8', errors='ignore') as jf:
                for line in jf:
                    if any(k in line.lower() for k in ['mapa original', 'lixão', 'lixao', 'alto-lixo']):
                        try:
                            data = json.loads(line)
                            source = data.get('source', '')
                            content = data.get('content', '')
                            if source == 'USER_EXPLICIT' or 'mapa original' in str(content).lower():
                                print(f"=== {source} ===")
                                print(str(content)[:400])
                        except:
                            pass
