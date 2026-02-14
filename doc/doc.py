"""
===========================================================
DOCUMENTAÇÃO DO PROJETO - CONFIGURAÇÃO DO AMBIENTE PYTHON
===========================================================

Este arquivo documenta a configuração do ambiente do projeto:

- Criação do ambiente virtual (venv)
- Ativação no Windows (CMD e PowerShell)
- Configuração no VSCode
- Instalação das dependências
- Geração do requirements.txt
- Como replicar o ambiente
- Como rodar o servidor FastAPI

-----------------------------------------------------------
1) O QUE É VENV?
-----------------------------------------------------------

venv = ambiente virtual do Python.

Ele cria um ambiente isolado dentro da pasta do projeto,
contendo:

- Um interpretador Python próprio
- Um pip próprio
- Suas próprias bibliotecas

Isso evita conflito de versões entre projetos diferentes.

Sem venv:
    Bibliotecas são instaladas no Python global do Windows.

Com venv:
    Cada projeto possui suas próprias dependências isoladas.

Comparação com Node.js:
    venv ≈ node_modules
    (porém o venv também inclui o próprio interpretador Python)

-----------------------------------------------------------
2) CRIAÇÃO DO VENV
-----------------------------------------------------------

Dentro da pasta do projeto:

    python -m venv venv

Explicação:

    python      -> executa o Python instalado no sistema
    -m venv     -> executa o módulo interno "venv"
    venv        -> nome da pasta criada

Estrutura gerada:

    Projeto_Nutriente/
        venv/
            Scripts/
            Lib/
            pyvenv.cfg

O arquivo "pyvenv.cfg" vincula o ambiente à versão do Python usada.

-----------------------------------------------------------
3) ATIVAÇÃO DO VENV (WINDOWS)
-----------------------------------------------------------

PowerShell:

    .\venv\Scripts\Activate.ps1

CMD:

    venv\Scripts\activate.bat

Se aparecer:

    (venv) D:\Projeto>

O ambiente está ativo.

Ao ativar:
- O comando "python" usa o python do venv
- O comando "pip" instala dentro do venv
- O PATH é temporariamente alterado

IMPORTANTE:
Sempre que abrir um terminal novo, o venv precisa ser ativado.
(O VSCode pode ativar automaticamente se configurado.)

-----------------------------------------------------------
4) CONFIGURAÇÃO NO VSCODE
-----------------------------------------------------------

Selecionar o interpretador:

Ctrl + Shift + P
Python: Select Interpreter
Selecionar:
    venv\Scripts\python.exe

Para ativação automática, criar:

    .vscode/settings.json

Com o conteúdo:

{
    "python.defaultInterpreterPath": "venv\\Scripts\\python.exe",
    "python.terminal.activateEnvironment": true
}

Isso garante que o terminal integrado abra já com (venv).

-----------------------------------------------------------
5) INSTALAÇÃO DAS DEPENDÊNCIAS
-----------------------------------------------------------

Com o venv ativado:

    pip install fastapi uvicorn sqlalchemy pymysql python-dotenv

As bibliotecas são instaladas em:

    venv/Lib/site-packages

-----------------------------------------------------------
6) GERANDO O REQUIREMENTS.TXT
-----------------------------------------------------------

Para salvar todas as dependências:

    pip freeze > requirements.txt

Esse arquivo registra as versões exatas instaladas.

Comparação com Node:
    requirements.txt ≈ lista de dependências do package.json
    (não contém scripts ou metadata do projeto)

-----------------------------------------------------------
7) RECRIANDO O AMBIENTE EM OUTRA MÁQUINA
-----------------------------------------------------------

1) Clonar o projeto
2) Criar o venv:

    python -m venv venv

3) Ativar:

    .\venv\Scripts\Activate.ps1

4) Instalar dependências:

    pip install -r requirements.txt

Ambiente reconstruído com as mesmas versões.

-----------------------------------------------------------
8) EXECUTANDO O SERVIDOR FASTAPI
-----------------------------------------------------------

Forma recomendada:

    uvicorn init:app --reload

Ou via Python:

    python -m uvicorn init:app --reload

Onde:
    init = nome do arquivo
    app  = instância do FastAPI()

-----------------------------------------------------------
9) FLUXO PADRÃO PARA QUALQUER PROJETO PYTHON
-----------------------------------------------------------

1) python -m venv venv
2) Ativar o ambiente
3) pip install dependências
4) pip freeze > requirements.txt
5) Rodar aplicação

Boa prática:
- Nunca commitar a pasta venv
- Sempre commitar o requirements.txt
- Manter .env fora do versionamento

-----------------------------------------------------------
FIM DA DOCUMENTAÇÃO
-----------------------------------------------------------
"""
