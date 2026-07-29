from fastapi import FastAPI
from routes.pacientes import router as pacientes_router

app = FastAPI()

app.include_router(pacientes_router)

@app.get("/")
def inicio():
    return {"mensagem": "Chefe de Atendimento Online 🚀"}