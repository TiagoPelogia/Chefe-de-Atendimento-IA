from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from core.database import Base


class Paciente(Base):

    __tablename__ = "pacientes"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    nome: Mapped[str] = mapped_column(
        String(120),
        nullable=False
    )

    telefone: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    idade: Mapped[int] = mapped_column(
        Integer,
        nullable=False

    clinica_id: Mapped[int] = mapped_column(
    ForeignKey("clinicas.id"),
    nullable=False
)
    )

clinica = relationship("Clinica")