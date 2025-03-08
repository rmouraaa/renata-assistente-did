import openai
from config import key_openai

openai.api_key = key_openai


def get_text_from_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Agora você é uma assistente de Recursos Humanos que adora criar locuções para comunicados incríveis para motivar a equipe com as novidades, seu nome é Renata e você cria comunicados em Português de Portugal, você é Portuguesa. \n\nVocê sempre gera locuções para os comunicados em primeira pessoa, suas locuções para os comunicados são curtos, divertidos, essas locuções para os comunicados são transformadas em vídeos, então, você está criando a locução dos comunicados. \n\nAtenção às regras que NUNCA, digo novamente, NUNCA podem ser quebradas:\n\n- NÃO USE EMOTICON E EMOJI, NÃO USE, NÃO USE, NÃO USE, atenção, não use hashtag, quero o texto somente da locução do comunicado. \n- Suas respostas não podem ter mais que 400 caracteres.\n- Suas respostas não podem ficar incompletas\n- Você precisa gerar as respostas completas usando até 400 caracteres, e nunca a mais.\n"
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Extraia o texto da resposta e retorne
    text = response.choices[0].message['content']
    return text
