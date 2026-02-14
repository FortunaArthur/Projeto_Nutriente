import requests
import time
import textwrap


URL = "http://localhost:11434/api/generate"


# ---------------------------------------------------
# ETAPA 1 - CORRIGIR SOMENTE ORTOGRAFIA
# ---------------------------------------------------
def corrigir_texto(texto):
    prompt = f"""
Corrija apenas erros ortográficos do texto abaixo.
Não reescreva frases.
Não explique nada.
Não adicione nada.
Não remova nada.
Não mude o significado.
Retorne somente o texto corrigido, em uma única linha.

{texto}
"""

    inicio = time.time()

    response = requests.post(
        URL,
        json={
            "model": "phi3",
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.1,
                "num_predict": 120
            }
        }
    )

    fim = time.time()

    texto_corrigido = response.json()["response"].strip()

    # Limpeza caso o modelo insista em colocar rótulo
    if "Texto corrigido:" in texto_corrigido:
        texto_corrigido = texto_corrigido.split("Texto corrigido:")[-1].strip()

    return texto_corrigido, fim - inicio


# ---------------------------------------------------
# ETAPA 2 - ANALISAR SINTOMAS
# ---------------------------------------------------
def analisar_sintomas(texto_corrigido):
    prompt = f"""
Você é um assistente médico educado.
Responda em português do Brasil.
Seja direto e objetivo.

Use EXATAMENTE o formato abaixo:

Sintomas identificados:
- ...

Possíveis causas:
- ...

Recomendações:
- ...

Não invente sintomas.
Não exagere nas recomendações.
Baseie-se apenas no texto fornecido.

Texto:
{texto_corrigido}
"""

    inicio = time.time()

    response = requests.post(
        URL,
        json={
            "model": "phi3",
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.2,
                "top_p": 0.9,
                "num_predict": 180
            }
        }
    )

    fim = time.time()

    return response.json()["response"].strip(), fim - inicio


# ---------------------------------------------------
# FORMATAR TEXTO BONITO NO TERMINAL
# ---------------------------------------------------
def formatar_texto(texto, largura=80):
    return textwrap.fill(texto, width=largura)


# ---------------------------------------------------
# EXECUÇÃO PRINCIPAL
# ---------------------------------------------------
if __name__ == "__main__":

    texto_usuario = (
        "Estou com dor de cabeça, eu ainda não brebi aqua ninhuma aunda hoji, "
        "a cabeça tá duento muita o tia inteiru.. e eu to frakinho e sem vontadi ninhuma de sai da kama"
    )

    print("\n🤖 IA está pensando...\n")

    inicio_total = time.time()

    # Etapa 1 - Correção
    texto_corrigido, tempo_correcao = corrigir_texto(texto_usuario)

    # Etapa 2 - Análise
    resposta_final, tempo_analise = analisar_sintomas(texto_corrigido)

    fim_total = time.time()

    # -------------------------
    # OUTPUT ORGANIZADO
    # -------------------------

    print("📝 Texto corrigido:\n")
    print(formatar_texto(texto_corrigido))

    print("\n🩺 Análise:\n")
    print(formatar_texto(resposta_final))

    print("\n⏱ Tempo de correção: {:.2f} segundos".format(tempo_correcao))
    print("⏱ Tempo de análise: {:.2f} segundos".format(tempo_analise))
    print("⏱ Tempo total: {:.2f} segundos\n".format(fim_total - inicio_total))
