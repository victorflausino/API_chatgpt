from senha import API_KEY
import requests
import json

# requisicao = requests.post requisição para MANADR
# requisicao = requests.get requisição para PEGAR

headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type":"application/json"}
link = "https://api.openai.com/v1/chat/completions"
id_modelo = "gpt-3.5-turbo"

body_mensagem = {
    "model" : id_modelo,
    "menssages" : [{"role" : "user", "content": "escreva um e-mail dizendo a previsao do dollar do proximo trimestre"}]
}

body_mensagem = json.dumps(body_mensagem)

requisicao = requests.post(link,headers=headers, data=body_mensagem)

resposta = requisicao.json()
mensagem = resposta["choices"][0]["message"]["content"]

print(mensagem)


