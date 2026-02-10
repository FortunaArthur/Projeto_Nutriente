from connections.database import engine

try:
    with engine.connect() as connection:
        print("Conectado ao MySQL com sucesso 🚀")
except Exception as e:
    print("Erro ao conectar no banco ❌")
    print(e)
