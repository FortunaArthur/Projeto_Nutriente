import uvicorn
# Importa o servidor ASGI (é ele que mantém o programa rodando,
# equivalente ao "app.listen" ou "npm start" no Node)

if __name__ == "__main__":
    # Esse bloco só roda quando este arquivo é executado diretamente
    # (ex: python main.py ou Play do VSCode)
    # Se alguém importar esse arquivo, isso NÃO executa

    uvicorn.run(
        "init:app",
        # "init"  -> arquivo init.py
        # "app"   -> variável app = FastAPI()
        # Ou seja: diz ao Uvicorn onde está a aplicação

        reload=True,
        # Fica observando mudanças nos arquivos
        # Se salvar algo, o servidor reinicia automaticamente
        # É o "nodemon" do FastAPI

        log_level="error"
        # Mostra apenas erros reais
        # Remove logs INFO e WARNING do Uvicorn
    )
