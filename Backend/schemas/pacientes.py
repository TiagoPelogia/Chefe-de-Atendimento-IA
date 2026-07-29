from pydantic import BaseModel

class Paciente(BaseModel):

    nome: str
    telefone: str
    idade: int