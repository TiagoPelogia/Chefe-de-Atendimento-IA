from fastapi import FastAPI

from core.database import Base, engine

# Importa o model para que ele seja registrado
from models.paciente import Paciente

app = FastAPI()

Base.metadata.create_all(bind=engine)