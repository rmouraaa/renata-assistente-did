# Gerador de Vídeos de Comunicados

Este projeto é um gerador automatizado de vídeos de comunicados para a empresa **Renova**. Ele recebe respostas do usuário, gera um texto baseado nessas respostas, cria um vídeo com locução e edita o vídeo final com moldura, trilha sonora e logotipo.

## 🛠 Tecnologias Utilizadas

- **Flask**: Framework para construir a API.
- **OpenAI GPT**: Para gerar o texto do comunicado.
- **D-ID API**: Para criar vídeos a partir do texto.
- **MoviePy**: Para editar e finalizar os vídeos.
- **Requests**: Para realizar chamadas HTTP à API do D-ID.

## 🚀 Como Funciona

1. O usuário responde a algumas perguntas na interface.
2. O sistema gera um **prompt** com base nessas respostas.
3. O **OpenAI GPT** cria um texto curto e divertido para o comunicado.
4. O **D-ID API** gera um vídeo com locução a partir do texto.
5. O **MoviePy** edita o vídeo, adiciona moldura, trilha sonora e logotipo.
6. O vídeo final é salvo e disponibilizado para o usuário.

---

## 📁 Estrutura do Projeto

```
📂 projeto
├── app.py              # Aplicação Flask
├── did.py              # Integração com a API do D-ID
├── prompt.py           # Geração do prompt para OpenAI
├── script.py           # Comunicação com OpenAI GPT
├── studio.py           # Edição de vídeo com MoviePy
├── config.py           # Configurações sensíveis (chaves de API, paths)
├── templates/          # Arquivos HTML para interface Flask
└── static/render/      # Pasta onde os vídeos renderizados são armazenados
```

---

## 📌 Configuração e Uso

### 1️⃣ Instale as Dependências

Certifique-se de ter o Python instalado e execute:

```sh
pip install -r requirements.txt
```

### 2️⃣ Configure as Chaves de API

Crie um arquivo `config.py` e adicione as chaves de API:

```python
D_ID_USERNAME = "seu_usuario_did"
D_ID_PASSWORD = "sua_senha_did"
key_openai = "sua_chave_openai"
frame = "caminho/para/moldura.png"
audiofile = "caminho/para/trilha_sonora.mp3"
logo = "caminho/para/logo.png"
```

### 3️⃣ Execute o Servidor

Inicie a aplicação Flask:

```sh
python app.py
```

Acesse no navegador: `http://127.0.0.1:5000/`

---

## 📝 Funcionalidades Detalhadas

### 🔹 `app.py`
- Define as rotas do Flask para renderizar páginas HTML e processar requisições.
- Recebe as respostas do usuário, salva-as e inicia o processo de geração do vídeo.
- Retorna o caminho do vídeo final gerado.

### 🔹 `prompt.py`
- Cria o **prompt** para o GPT-3.5 baseado nas respostas do usuário.

### 🔹 `script.py`
- Envia o prompt para a **OpenAI API** e recebe o texto do comunicado.

### 🔹 `did.py`
- Envia o texto para a **API D-ID** para gerar um vídeo com locução.
- Faz o download do vídeo gerado.

### 🔹 `studio.py`
- Usa **MoviePy** para editar o vídeo:
  - Ajusta o tamanho e adiciona moldura.
  - Sobrepõe trilha sonora e áudio original.
  - Anexa um **logo final** ao vídeo.
- Exporta o vídeo finalizado.

---

## 🔥 Possíveis Melhorias
- Implementar suporte a múltiplos idiomas.
- Criar um banco de dados para armazenar os vídeos gerados.
- Melhorar a interface gráfica com um design mais moderno.
- Permitir upload de imagens personalizadas para os vídeos.

## 📢 Contribuição
Sinta-se à vontade para contribuir! Envie sugestões, abra issues ou faça um pull request. 😃

---

## 📜 Licença
Este projeto está sob a licença **MIT**. Você pode usá-lo livremente, mas lembre-se de dar os devidos créditos! 😉
