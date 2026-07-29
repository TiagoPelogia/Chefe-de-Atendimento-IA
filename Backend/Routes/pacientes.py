from fastapi import APIRouter
from schemas.pacientes import Paciente

router = APIRouter()

pacientes = []


# LISTAR TODOS
@router.get("/pacientes")
def listar_pacientes():
    return pacientes


# CRIAR
@router.post("/pacientes")
def criar_paciente(paciente: Paciente):

    pacientes.append(paciente)

    return paciente


# BUSCAR POR ID
@router.get("/pacientes/{id}")
def buscar_paciente(id: int):

    if id < 0 or id >= len(pacientes):
        return {"erro": "Paciente não encontrado"}

    return pacientes[id]


# ATUALIZAR
@router.put("/pacientes/{id}")
def atualizar_paciente(id: int, paciente: Paciente):

    if id < 0 or id >= len(pacientes):
        return {"erro": "Paciente não encontrado"}

    pacientes[id] = paciente

    return paciente


# DELETAR
@router.delete("/pacientes/{id}")
def deletar_paciente(id: int):

    if id < 0 or id >= len(pacientes):
        return {"erro": "Paciente não encontrado"}

    pacientes.pop(id)

    return {"mensagem": "Paciente removido"}