from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Bem-vindo à minha API FastAPI"}
