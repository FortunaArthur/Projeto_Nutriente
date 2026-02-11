"""
===========================================================
DOCUMENTAÇÃO DO PROJETO - CONFIGURAÇÃO DO AMBIENTE PYTHON
===========================================================

Este arquivo documenta tudo que foi feito até aqui:
- Criação do ambiente virtual (venv)
- Ativação no Windows (CMD)
- Instalação das dependências
- Como rodar o projeto
- Como replicar o ambiente em outro projeto

-----------------------------------------------------------
1) O QUE É VENV?
-----------------------------------------------------------

venv = ambiente virtual do Python.

Ele cria um Python isolado dentro do projeto.
Isso evita conflitos de versão entre projetos diferentes.

Sem venv:
    Todas as bibliotecas são instaladas no Python global do Windows.

Com venv:
    Cada projeto tem suas próprias bibliotecas isoladas.

Equivalente no Node:
    venv ≈ node_modules

-----------------------------------------------------------
2) COMO CRIAMOS O VENV
-----------------------------------------------------------

Dentro da pasta do projeto rodamos:

    python -m venv venv

Explicação do comando:

    python        -> usa o Python instalado
    -m venv       -> executa o módulo interno chamado venv
    venv          -> nome da pasta criada

Isso criou a estrutura:

    Projeto_Nutriente/
        venv/
            Scripts/
            Lib/
            ...

Essa pasta contém um Python exclusivo do projeto.

-----------------------------------------------------------
3) COMO ATIVAMOS O VENV (WINDOWS - CMD)
-----------------------------------------------------------

Abrimos o terminal CMD e rodamos:

    venv\Scripts\activate.bat

Quando aparece:

    (venv) D:\Projeto>

Significa que o ambiente está ativo.

O que acontece ao ativar:
- O comando "python" passa a usar o python do venv
- O comando "pip" passa a instalar dentro do venv
- Nada mais é instalado globalmente

IMPORTANTE:
Sempre que abrir o projeto, precisa ativar o venv novamente.

-----------------------------------------------------------
4) INSTALANDO AS DEPENDÊNCIAS
-----------------------------------------------------------

Depois de ativar o venv, instalamos:

    pip install fastapi uvicorn sqlalchemy pymysql python-dotenv

Agora essas bibliotecas estão dentro do:

    venv/Lib/site-packages

-----------------------------------------------------------
5) GERANDO O ARQUIVO DE DEPENDÊNCIAS
-----------------------------------------------------------

Para salvar todas as libs instaladas:

    pip freeze > requirements.txt

Isso cria um arquivo com algo como:

    fastapi==...
    uvicorn==...
    sqlalchemy==...
    ...

Esse arquivo é o equivalente ao "package.json" (dependências).

-----------------------------------------------------------
6) COMO RECRIAR O PROJETO EM OUTRA MÁQUINA
-----------------------------------------------------------

Se alguém clonar o projeto:

1) Criar o venv:

    python -m venv venv

2) Ativar:

    venv\Scripts\activate

3) Instalar dependências:

    pip install -r requirements.txt

Pronto. Ambiente reconstruído.

-----------------------------------------------------------
7) COMO RODAMOS O SERVIDOR
-----------------------------------------------------------

Criamos o arquivo main.py com:

    uvicorn.run("init:app", reload=True)

Então rodamos:

    python main.py

Isso inicia o servidor FastAPI.

-----------------------------------------------------------
8) FLUXO PADRÃO PARA TODO PROJETO PYTHON
-----------------------------------------------------------

Sempre que criar um projeto novo:

1) python -m venv venv
2) venv\Scripts\activate
3) pip install ...
4) pip freeze > requirements.txt
5) python main.py

Essa é a base profissional de qualquer projeto Python.

-----------------------------------------------------------
FIM DA DOCUMENTAÇÃO
-----------------------------------------------------------
"""
