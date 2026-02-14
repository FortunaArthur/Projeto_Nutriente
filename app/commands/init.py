from fastapi import FastAPI
from app.connections.database import get_connection;

app = FastAPI()

@app.on_event("startup")
def startup():
    print("App iniciou 🚀")
    get_connection()

