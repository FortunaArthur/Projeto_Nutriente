import requests
import time
import textwrap


URL = "http://localhost:11434/api/generate"
MODEL = "phi3"


# ---------------------------------------------------
# FUNÇÃO BASE DE CHAMADA DA IA (OTIMIZADA)
# ---------------------------------------------------
def chamar_ia(prompt, temperature=0.2, num_predict=80):

    try:
        response = requests.post(
            URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": temperature,
                    "top_p": 0.8,
                    "repeat_penalty": 1.1,
                    "num_predict": num_predict,
                    "num_ctx": 512
                    }

            },
            timeout=180
        )

        response.raise_for_status()

        return response.json().get("response", "").strip()

    except Exception as e:
        return f"Erro na IA: {e}"


# ---------------------------------------------------
# ETAPA 1 - CORREÇÃO AVANÇADA E CONTROLADA
# ---------------------------------------------------
def corrigir_texto(texto):

    prompt = f"""
        Você é um corretor linguístico especializado em:

        - Ortografia
        - Erros de digitação
        - Escrita fonética
        - Palavras digitadas de forma aproximada

        OBJETIVO:
        Corrigir apenas erros linguísticos mantendo exatamente o mesmo significado.

        REGRAS RÍGIDAS:
        - NÃO reescreva frases.
        - NÃO mude a estrutura.
        - NÃO adicione informações.
        - NÃO remova informações.
        - NÃO explique nada.
        - NÃO interprete sintomas.
        - Preserve o tom informal original.
        - Corrija palavras escritas foneticamente usando contexto.
        - Se uma palavra estiver próxima foneticamente de outra válida em português, corrija.

        Retorne exclusivamente o texto corrigido.

        Texto:
        {texto}
    """

    inicio = time.time()

    texto_corrigido = chamar_ia(
        prompt,
        temperature=0.1,
        num_predict=120
    )

    fim = time.time()

    # limpeza defensiva
    if "Texto:" in texto_corrigido:
        texto_corrigido = texto_corrigido.split("Texto:")[-1].strip()

    texto_corrigido = " ".join(texto_corrigido.split())

    return texto_corrigido, fim - inicio


# ---------------------------------------------------
# ETAPA 2 - EXTRAÇÃO DE SINTOMAS CONTROLADA
# ---------------------------------------------------
def extrair_sintomas(texto_corrigido):

    prompt = f"""
        Você é um extrator clínico objetivo.

        OBJETIVO:
        Extrair apenas sintomas explícitos no texto.

        REGRAS:
        - NÃO invente sintomas.
        - NÃO deduza doenças.
        - NÃO interprete além do texto.
        - NÃO explique.
        - NÃO reformule.
        - Extraia apenas o que está claramente descrito.
        - Se não houver sintomas, escreva: "Nenhum sintoma identificado."

        FORMATO OBRIGATÓRIO:

        Sintomas identificados:
        - sintoma 1
        - sintoma 2

        Texto:
        {texto_corrigido}
    """

    inicio = time.time()

    resposta = chamar_ia(
        prompt,
        temperature=0.0,
        num_predict=100
    )

    fim = time.time()

    return resposta.strip(), fim - inicio


# ---------------------------------------------------
# FORMATADOR
# ---------------------------------------------------
def formatar_texto(texto, largura=80):
    return textwrap.fill(texto, width=largura)


# ---------------------------------------------------
# EXECUÇÃO PRINCIPAL
# ---------------------------------------------------
if __name__ == "__main__":

    texto_usuario = (
        "Estou com dor de cabeça, eu ainda não bebi agua nenhuma hoje, "
        "minha cabeça doi na parte de trás e estou fraco sem vontade nenhuma de sair da cama"
    )

    print("\n🤖 IA está pensando...\n")

    inicio_total = time.time()

    # Correção
    texto_corrigido, tempo_correcao = corrigir_texto(texto_usuario)

    # Extração
    sintomas, tempo_extracao = extrair_sintomas(texto_corrigido)

    fim_total = time.time()

    print("📝 Texto corrigido:\n")
    print(formatar_texto(texto_corrigido))

    print("\n🩺 Sintomas:\n")
    print(formatar_texto(sintomas))

    print("\n⏱ Tempo correção: {:.2f}s".format(tempo_correcao))
    print("⏱ Tempo extração: {:.2f}s".format(tempo_extracao))
    print("⏱ Tempo total: {:.2f}s\n".format(fim_total - inicio_total))
