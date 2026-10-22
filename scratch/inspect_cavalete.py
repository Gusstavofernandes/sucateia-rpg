from PIL import Image

cavalete = Image.open('fundo_ferro_standalone/assets/rails/cavalete_alto_v1.png')
print("Cavalete size:", cavalete.size)
print("Cavalete mode:", cavalete.mode)

txt_path = 'fundo_ferro_standalone/assets/rails/cavalete_alto_v1.txt'
try:
    with open(txt_path, 'r', encoding='utf-8') as f:
        print("Prompt/Info cavalete:\n", f.read())
except Exception as e:
    print("Erro lendo txt:", e)
