import json

with open('C:/Users/Usuario/.gemini/antigravity/brain/24487463-0c7d-44b2-91e8-4982c2631f5b/.system_generated/logs/transcript.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        content = str(data.get('content', '')) + str(data.get('tool_calls', ''))
        if 'estacao_trilho_v2' in content and 'Vector2' in content:
            print(f"Step {data.get('step_index')}:")
            for sub in content.split('\n'):
                if 'EstacaoCarga' in sub or 'estacao_trilho_v2' in sub or 'scale' in sub or 'position' in sub:
                    print('  ', sub[:120])
