from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def inicio():
    return {
        "mensagem": "Chefe de Atendimento Online 🚀"
    }
@app.get("/pacientes")
def pacientes():

    return [
        {
            "nome":"João",
            "idade":30
        },
        {
            "nome":"Maria",
            "idade":25
        }
    ]