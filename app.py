from flask import Flask, jsonify
import json
import os # Importamos o 'os' para pegar a porta do ambiente

app = Flask(__name__)

# Função para carregar os dados do JSON
def carregar_receitas():
    # O 'with' garante que o arquivo seja fechado corretamente
    with open('receitas.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/receitas')
def get_receitas():
    """Este endpoint lê o arquivo JSON e o retorna."""
    receitas = carregar_receitas()
    return jsonify(receitas)

@app.route('/health')
def health_check():
    """Este endpoint serve para o Cloud Run saber que nossa API está saudável."""
    return jsonify({"status": "ok"}), 200

@app.route('/')
def home():
    """home end point"""
    receitas = carregar_receitas()
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    # Cloud Run define uma variável de ambiente PORT. Usamos ela se existir.
    # O 'host="0.0.0.0"' é crucial para o Docker funcionar corretamente.
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)