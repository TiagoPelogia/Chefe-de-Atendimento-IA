from fastapi import FastAPI

from routes import auth, pacientes

app = FastAPI(title="Chefe de Atendimento IA")

app.include_router(auth.router)
app.include_router(pacientes.router)