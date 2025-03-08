from flask import Flask, render_template, jsonify, request
import json
import os
from prompt import generate_prompt
from script import get_text_from_gpt
from did import create_and_download_video
from studio import edit_video, finalize_video

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat')
def chat():
    return render_template('chat.html')


@app.route('/generate_video', methods=['POST'])
def generate_video():
    user_responses = request.get_json()

    # Salvar respostas no arquivo data.json
    with open('data.json', 'w') as f:
        json.dump(user_responses, f)

    # Extraindo as respostas do usuário
    resposta1 = user_responses.get('resposta1')
    resposta2 = user_responses.get('resposta2')

    # 1. Gerar o prompt usando as respostas do usuário.
    prompt_text = generate_prompt(resposta1, resposta2)

    # 2. Obter o texto da OpenAI usando o prompt.
    generated_text = get_text_from_gpt(prompt_text)

    # 3. Usar o texto gerado para criar um vídeo usando a API do D-ID.
    source_image_url = "https://media.discordapp.net/attachments/1157312771151626284/1159074444854173737/stories.png?ex=651e8fb2&is=651d3e32&hm=0ebd447f381c47b6da7e4d34bd452b59f9bfd9206b4cab2ef903188190126e68&=&width=341&height=606"
    downloaded_file = create_and_download_video(
        source_image_url, generated_text)

    # 4. Editar o vídeo usando o módulo studio
    edited_video = edit_video(downloaded_file)

    # 5. Finalizar o vídeo (adicionar música, logo, etc.)
    finalize_video(edited_video)

    # Verifique se o vídeo foi gerado com sucesso
    video_path = "static/render/comunicado-renova.mp4"

    if os.path.exists(video_path):
        return jsonify({"video_path": video_path})
    else:
        return jsonify({"error": "O vídeo não pôde ser gerado. Por favor, tente novamente."}), 500


if __name__ == "__main__":
    app.run(debug=True)
