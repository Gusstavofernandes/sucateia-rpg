import subprocess
import urllib.request
import json

p = subprocess.Popen(['git', 'credential', 'fill'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
out, err = p.communicate(input='protocol=https\nhost=github.com\n\n')

username = ''
token = ''
for line in out.splitlines():
    if line.startswith('username='): username = line.split('=', 1)[1]
    elif line.startswith('password='): token = line.split('=', 1)[1]

req = urllib.request.Request('https://api.github.com/user/repos?per_page=100', headers={
    'Authorization': f'token {token}',
    'User-Agent': 'Antigravity-Agent',
    'Accept': 'application/vnd.github.v3+json'
})

try:
    with urllib.request.urlopen(req) as resp:
        repos = json.loads(resp.read().decode())
        print(f'Usuario autenticado: {username}')
        print(f'Total de repositorios encontrados: {len(repos)}')
        for r in repos:
            priv = 'private' if r['private'] else 'public'
            print(f"- {r['name']} ({priv})")
except Exception as e:
    print('Erro na consulta:', e)
