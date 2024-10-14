from flask import Flask, render_template, request, jsonify
import requests
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente
load_dotenv()

app = Flask(__name__)

# Página inicial com o formulário
@app.route('/')
def index():
    return render_template('index.html')

# Rota para obter as conversas
@app.route('/obter_conversas', methods=['POST'])
def obter_conversas():
    data = request.json
    chatbot_id = data.get('chatbotId')
    start_date = data.get('start_date')
    end_date = data.get('end_date')

    # Configura a URL da API
    url = f"https://www.chatbase.co/api/v1/get-conversations"
    headers = {
        'Authorization': f"Bearer {os.getenv('API_KEY')}",
        'Content-Type': 'application/json'
    }
    params = {
        'chatbotId': chatbot_id,
        'startDate': start_date,
        'endDate': end_date,
        'size': '20'
    }

    # Faz a requisição à API externa
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Erro ao obter as conversas'}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
