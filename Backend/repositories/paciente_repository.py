from sqlalchemy.orm import Session

from models.paciente import Paciente


class PacienteRepository:

    def __init__(self, db: Session):

        self.db = db


    def criar(self, nome, telefone, idade):

        paciente = Paciente(

            nome=nome,

            telefone=telefone,

            idade=idade

        )

        self.db.add(paciente)

        self.db.commit()

        self.db.refresh(paciente)

        return paciente


    def listar(self):

        return self.db.query(Paciente).all()


    def buscar_por_id(self, paciente_id):

        return (

            self.db

            .query(Paciente)

            .filter(Paciente.id == paciente_id)

            .first()

        )

def atualizar(self, paciente_id, nome, telefone, idade):

    paciente = self.buscar_por_id(paciente_id)

    if not paciente:
        return None

    paciente.nome = nome
    paciente.telefone = telefone
    paciente.idade = idade

    self.db.commit()
    self.db.refresh(paciente)

    return paciente

def deletar(self, paciente_id):

    paciente = self.buscar_por_id(paciente_id)

    if not paciente:
        return False

    self.db.delete(paciente)

    self.db.commit()

    return True