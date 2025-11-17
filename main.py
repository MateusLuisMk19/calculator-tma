import os
import json
import webview

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DADOS_PATH = os.path.join(BASE_DIR, 'dados.json')
HTML_PATH = 'https://mateusluismk19.github.io/apps/tmaC/index.html'

# --- Armazenamento ---
def carregar_dados():
    if not os.path.exists(DADOS_PATH):
        return {}
    try:
        with open(DADOS_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {}

def guardar_dados(dados):
    with open(DADOS_PATH, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

# API exposta ao JavaScript
class API:
    def carregar(self):
        return carregar_dados()

    def guardar(self, dados):
        guardar_dados(dados)
        return True

# --- Criar janela ---
api = API()

window = webview.create_window(
    title='Calculadora de TMA',
    url=HTML_PATH,
    width=600,
    height=650,
    resizable=True,
    min_size=(350, 400),
    js_api=api
)

# --- Iniciar aplicação ---
webview.start()
