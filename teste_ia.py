import requests

def perguntar_ia(texto):
    prompt = f"""
    Você é um assistente médico educado.
    Responda sempre em português do Brasil.
    Seja claro e objetivo.

    Pergunta do usuário:
    {texto}
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "phi3",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]


if __name__ == "__main__":
    resposta = perguntar_ia("Estou com dor de cabeça e enjoo.")
    print(resposta)
