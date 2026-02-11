import os # Biblioteca padrão do Python para acessar variáveis de ambiente
from dotenv import load_dotenv # Função que carrega as variáveis do arquivo .env
from sqlalchemy import create_engine # Cria o "motor" de conexão com o banco de dados
from sqlalchemy.orm import sessionmaker # Cria sessões para interagir com o banco usando ORM

load_dotenv() # Lê o arquivo .env e joga as variáveis no ambiente

DB_HOST = os.getenv("DB_HOST") # Endereço do servidor do banco
DB_PORT = os.getenv("DB_PORT") # Porta do banco de dados
DB_USER = os.getenv("DB_USER") # Usuário do banco
DB_PASSWORD = os.getenv("DB_PASSWORD") # Senha do banco
DB_NAME = os.getenv("DB_NAME") # Nome do banco de dados

DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
) # String de conexão usada pelo SQLAlchemy

engine = create_engine(
    DATABASE_URL,
    echo=False  # desativa logs SQL no terminal
) # Cria o engine que gerencia conexões com o banco

SessionLocal = sessionmaker(bind=engine) # Fábrica de sessões para acessar o banco

def get_connection():
    # Função que tenta abrir uma conexão direta com o banco
    try:
        connection = engine.connect() # Abre uma conexão usando o engine
        print("Conectado ao MySQL com sucesso ✅") # Mensagem de sucesso no terminal
        return connection # Retorna a conexão aberta

    except Exception as e: # Captura qualquer erro de conexão
        print("Erro ao conectar no banco ❌") # Mensagem de erro
        print(e) # Mostra o erro no terminal
        return None # Retorna None se falhar

export = get_connection # Cria um alias da função (estilo export do Node, mas não é necessário em Python)
