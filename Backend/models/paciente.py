from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.database import Base

if TYPE_CHECKING:
    from models.clinica import Clinica


class Paciente(Base):
    __tablename__ = "pacientes"

    id: Mapped[int] = mapped_column(primary_key=True)

    nome: Mapped[str] = mapped_column(String(120), nullable=False)
    telefone: Mapped[str] = mapped_column(String(20), nullable=False)
    idade: Mapped[int] = mapped_column(Integer, nullable=False)

    clinica_id: Mapped[int] = mapped_column(
        ForeignKey("clinicas.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )

    clinica: Mapped["Clinica"] = relationship(back_populates="pacientes")