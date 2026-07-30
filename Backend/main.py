from fastapi import FastAPI

from core.database import Base, engine
from models.paciente import Paciente

from routes import pacientes

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(pacientes.router)