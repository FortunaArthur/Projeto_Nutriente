import requests
import time
import textwrap


def perguntar_ia(texto):
    prompt = f"""
    Você é um assistente médico educado.
    Responda sempre em português do Brasil.
    Seja claro e objetivo.

    Pergunta do usuário:
    {texto}
    """

    print("\n🤖 IA está pensando...\n")

    inicio = time.time()

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "phi3",
            "prompt": prompt,
            "stream": False
        }
    )

    fim = time.time()
    tempo_total = fim - inicio

    resposta = response.json()["response"]

    return resposta, tempo_total


def formatar_texto(texto, largura=80):
    return textwrap.fill(texto.strip(), width=largura)


if __name__ == "__main__":
    resposta, tempo = perguntar_ia(
        "Estou com dor de cabeça, eu ainda não bebi água hoje, o que devo fazer?"
    )

    print("🩺 Resposta da IA:\n")
    print(formatar_texto(resposta))

    print(f"\n⏱ Tempo de resposta: {tempo:.2f} segundos\n")
