import os, re

# Procurar em scratch e em logs menções a 'ponte' e 'trilho'
log_dir = 'C:/Users/Usuario/.gemini/antigravity/brain/24487463-0c7d-44b2-91e8-4982c2631f5b/.system_generated/logs'
for f in os.listdir(log_dir):
    if f.endswith('.jsonl'):
        path = os.path.join(log_dir, f)
        with open(path, 'r', encoding='utf-8', errors='ignore') as log_file:
            for line in log_file:
                if 'ponte' in line.lower() and 'trilho' in line.lower():
                    matches = re.findall(r'([a-zA-Z0-9_\-\.]*ponte[a-zA-Z0-9_\-\.]*|[a-zA-Z0-9_\-\.]*trilho[a-zA-Z0-9_\-\.]*|[a-zA-Z0-9_\-\.]*cavalete[a-zA-Z0-9_\-\.]*)', line, re.IGNORECASE)
                    unique_m = set(m for m in matches if len(m) > 4)
                    if unique_m:
                        print(f"No log {f}: {unique_m}")
                        break
