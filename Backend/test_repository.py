from core.database import SessionLocal
from repositories.paciente_repository import PacienteRepository

db = SessionLocal()

repo = PacienteRepository(db)

repo.criar(
    "Tiago",
    "14999999999",
    18
)

print(repo.listar())