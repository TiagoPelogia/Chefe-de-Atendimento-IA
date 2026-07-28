from fastapi import APIRouter

router = APIRouter()

pacientes = []


@router.get("/pacientes")
def listar_pacientes():
    return pacientes


@router.post("/pacientes")
def criar_paciente(nome: str):

    paciente = {
        "id": len(pacientes) + 1,
        "nome": nome
    }

    pacientes.append(paciente)

    return paciente