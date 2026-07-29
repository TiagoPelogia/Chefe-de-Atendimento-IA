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

    novo_paciente = {
        "id": len(pacientes) + 1,
        "nome": paciente.nome,
        "telefone": paciente.telefone,
        "idade": paciente.idade
    }

    pacientes.append(novo_paciente)

    return novo_paciente


# BUSCAR POR ID
@router.get("/pacientes/{id}")
def buscar_paciente(id: int):

    for paciente in pacientes:
        if paciente["id"] == id:
            return paciente

    return {"erro": "Paciente não encontrado"}


# ATUALIZAR
@router.put("/pacientes/{id}")
def atualizar_paciente(id: int, paciente: Paciente):

    for p in pacientes:

        if p["id"] == id:

            p["nome"] = paciente.nome
            p["telefone"] = paciente.telefone
            p["idade"] = paciente.idade

            return p

    return {"erro": "Paciente não encontrado"}

# DELETAR
@router.delete("/pacientes/{id}")
def deletar_paciente(id: int):

    for paciente in pacientes:

        if paciente["id"] == id:

            pacientes.remove(paciente)

            return {"mensagem": "Paciente removido"}

    return {"erro": "Paciente não encontrado"}
