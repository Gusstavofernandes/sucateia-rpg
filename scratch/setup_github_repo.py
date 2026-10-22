# -*- coding: utf-8 -*-
import subprocess
import urllib.request
import urllib.error
import json
import os
import sys

# 1. Obter credenciais do Git
print("--- Passo 1: Obtendo credenciais do GitHub ---")
p = subprocess.Popen(['git', 'credential', 'fill'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
out, err = p.communicate(input='protocol=https\nhost=github.com\n\n')

username = ''
token = ''
for line in out.splitlines():
    if line.startswith('username='): username = line.split('=', 1)[1]
    elif line.startswith('password='): token = line.split('=', 1)[1]

if not token:
    print("ERRO: Token do GitHub não encontrado nas credenciais do sistema.")
    sys.exit(1)

print(f"Usuário autenticado: {username}")

# 2. Criar repositório remoto via API do GitHub
repo_name = "sucateia-rpg"
print(f"\n--- Passo 2: Criando repositório privado '{repo_name}' no GitHub ---")
url = "https://api.github.com/user/repos"
payload = json.dumps({
    "name": repo_name,
    "private": True,
    "description": "Sucateia RPG - Dark Fantasy / Steampunk RPG desenvolvido em Godot 4.7"
}).encode('utf-8')

req = urllib.request.Request(url, data=payload, headers={
    'Authorization': f'token {token}',
    'User-Agent': 'Antigravity-Agent',
    'Accept': 'application/vnd.github.v3+json',
    'Content-Type': 'application/json'
})

repo_url = f"https://github.com/{username}/{repo_name}.git"
try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode())
        print(f"Sucesso! Repositório criado: {data.get('html_url')}")
        repo_url = data.get('clone_url', repo_url)
except urllib.error.HTTPError as e:
    err_body = e.read().decode()
    if "name already exists" in err_body:
        print(f"Aviso: O repositório '{repo_name}' já existia no GitHub. Usando o existente.")
    else:
        print(f"Erro ao criar repositório ({e.code}): {err_body}")

# 3. Inicializar repositório Git local se necessário
print("\n--- Passo 3: Inicializando Git local ---")
if not os.path.exists(".git"):
    subprocess.run(["git", "init"], check=True)
    print("git init executado com sucesso.")
else:
    print("Repositório .git já existe.")

# Configurar usuário e branch main
subprocess.run(["git", "config", "user.name", "gustavofernandes"], check=True)
subprocess.run(["git", "config", "user.email", "gustavofoliveira153@gmail.com"], check=True)
subprocess.run(["git", "branch", "-M", "main"], check=True)

# 4. Configurar Remote Origin
print("\n--- Passo 4: Configurando remote origin ---")
# Usar URL com autenticação embutida ou padrão
remote_check = subprocess.run(["git", "remote", "get-url", "origin"], capture_output=True, text=True)
if remote_check.returncode == 0:
    subprocess.run(["git", "remote", "set-url", "origin", repo_url], check=True)
else:
    subprocess.run(["git", "remote", "add", "origin", repo_url], check=True)
print(f"Origin configurado: {repo_url}")

# 5. Git add
print("\n--- Passo 5: Adicionando arquivos do jogo ao Git ---")
subprocess.run(["git", "add", "."], check=True)
print("Arquivos adicionados com sucesso.")

# 6. Git commit
print("\n--- Passo 6: Criando commit inicial ---")
status_res = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
if status_res.stdout.strip():
    subprocess.run(["git", "commit", "-m", "feat: initial commit - Sucateia RPG Godot 4.7"], check=True)
    print("Commit inicial criado com sucesso!")
else:
    print("Nenhuma alteração pendente para commit.")

# 7. Git push
print("\n--- Passo 7: Enviando para o GitHub (git push -u origin main) ---")
# Para garantir que o push use o token autenticado sem abrir prompt interativo
auth_repo_url = f"https://{username}:{token}@github.com/{username}/{repo_name}.git"
push_res = subprocess.run(["git", "push", "-u", auth_repo_url, "main", "--force"], capture_output=True, text=True)
print("STDOUT:", push_res.stdout)
print("STDERR:", push_res.stderr)

if push_res.returncode == 0:
    # Restaurar remote origin para URL limpa sem token exposto
    subprocess.run(["git", "remote", "set-url", "origin", repo_url], check=True)
    print(f"\n=======================================================")
    print(f"REPOSITÓRIO CRIADO E SINCRONIZADO COM SUCESSO!")
    print(f"Link: https://github.com/{username}/{repo_name}")
    print(f"=======================================================")
else:
    print(f"Erro no push: retorno {push_res.returncode}")
    sys.exit(push_res.returncode)
