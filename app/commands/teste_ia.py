import requests
import time
import json

URL = "http://localhost:11434/api/generate"
MODEL = "phi3:latest"


def extrair_sintomas(texto):

    prompt = f"""
Extraia somente os sintomas explicitamente mencionados no texto.

Responda EXCLUSIVAMENTE em JSON no formato:

{{ "sintomas": ["sintoma1", "sintoma2"] }}

Não escreva mais nada além do JSON.

Texto:
{texto}
"""

    inicio = time.time()

    response = requests.post(
        URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.0,
                "top_p": 0.05,
                "repeat_penalty": 1.5,
                "num_predict": 80,
                "num_ctx": 160
            }
        },
        timeout=60
    )

    resposta_bruta = response.json().get("response", "").strip()

    fim = time.time()

    # 🔒 Tenta extrair JSON válido
    try:
        inicio_json = resposta_bruta.find("{")
        fim_json = resposta_bruta.rfind("}") + 1
        json_str = resposta_bruta[inicio_json:fim_json]
        dados = json.loads(json_str)
        sintomas = dados.get("sintomas", [])
    except:
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
