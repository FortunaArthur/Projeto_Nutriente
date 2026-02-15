import requests
import time
import json

URL = "http://localhost:11434/api/generate"
MODEL = "mistral"

def extrair_sintomas(texto):

    prompt = f"""
Extraia apenas os sintomas mencionados.

Responda SOMENTE com JSON válido no formato:
{{"sintomas":["..."]}}

Texto: {texto}
"""

    inicio = time.time()

    try:
        response = requests.post(
            URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0,
                    "num_predict": 60,
                    "top_p": 0.1,
                    "repeat_penalty": 1.2
                }
            },
            timeout=660  # 🔥 aumenta timeout
        )

        resposta = response.json().get("response", "").strip()

    except requests.exceptions.Timeout:
        print("⚠ Timeout do modelo")
        return [], 0

    fim = time.time()

    # 🔒 Extração segura de JSON
    try:
        inicio_json = resposta.find("{")
        fim_json = resposta.rfind("}") + 1
        json_str = resposta[inicio_json:fim_json]
        dados = json.loads(json_str)
        sintomas = dados.get("sintomas", [])
    except Exception:
        print("⚠ Falha ao converter JSON")
        print("Resposta bruta:", resposta)
        sintomas = []

    return sintomas, fim - inicio


if __name__ == "__main__":

    texto_usuario = (
        "Estou com dor de cabeça, eu ainda não bebi agua nenhuma hoje, "
        "minha cabeça doi na parte de trás e estou fraco sem vontade nenhuma de sair da cama"
    )

    print("\n🤖 IA analisando sintomas...\n")

    print("Texto do usuário:")
    print(texto_usuario)

    sintomas, tempo = extrair_sintomas(texto_usuario)

    print("\nSintomas identificados:\n")

    for s in sintomas:
        print(f"* {s}")

    print(f"\n⏱ Tempo total: {tempo:.2f}s\n")
