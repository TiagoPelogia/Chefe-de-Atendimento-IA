from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from repositories.paciente_repository import PacienteRepository
from schemas.pacientes import Paciente

router = APIRouter()


# LISTAR TODOS
@router.get("/pacientes")
def listar_pacientes(
    db: Session = Depends(get_db)
):

    repo = PacienteRepository(db)

    return repo.listar()


# CRIAR
@router.post("/pacientes")
def criar_paciente(
    paciente: Paciente,
    db: Session = Depends(get_db)
):

    repo = PacienteRepository(db)

    return repo.criar(
        nome=paciente.nome,
        telefone=paciente.telefone,
        idade=paciente.idade
    )

# BUSCAR POR ID
@router.get("/pacientes/{id}")
def buscar_paciente(
    id: int,
    db: Session = Depends(get_db)
):

    repo = PacienteRepository(db)

    paciente = repo.buscar_por_id(id)

    if paciente is None:
        return {"erro": "Paciente não encontrado"}

    return paciente


# ATUALIZAR
@router.put("/pacientes/{id}")
def atualizar_paciente(
    id: int,
    paciente: Paciente,
    db: Session = Depends(get_db)
):

    repo = PacienteRepository(db)

    atualizado = repo.atualizar(
        paciente_id=id,
        nome=paciente.nome,
        telefone=paciente.telefone,
        idade=paciente.idade
    )

    if atualizado is None:
        return {"erro": "Paciente não encontrado"}

    return atualizado

# DELETAR
@router.delete("/pacientes/{id}")
def deletar_paciente(
    id: int,
    db: Session = Depends(get_db)
):

    repo = PacienteRepository(db)

    removido = repo.deletar(id)

    if not removido:
        return {"erro": "Paciente não encontrado"}

    return {"mensagem": "Paciente removido"}