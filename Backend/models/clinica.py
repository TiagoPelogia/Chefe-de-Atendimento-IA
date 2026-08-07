from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.database import Base

if TYPE_CHECKING:
    from models.paciente import Paciente
    from models.profissional import Profissional
    from models.usuario import Usuario


class Clinica(Base):
    __tablename__ = "clinicas"

    id: Mapped[int] = mapped_column(primary_key=True)

    nome: Mapped[str] = mapped_column(String(120), nullable=False)
    cnpj: Mapped[str] = mapped_column(String(18), unique=True, nullable=False)
    telefone: Mapped[str] = mapped_column(String(20), nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)

    plano: Mapped[str] = mapped_column(String(30), nullable=False, default="starter")
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="ativo")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    pacientes: Mapped[list["Paciente"]] = relationship(
        back_populates="clinica"
    )
    profissionais: Mapped[list["Profissional"]] = relationship(
        back_populates="clinica"
    )
    usuarios: Mapped[list["Usuario"]] = relationship(
    back_populates="clinica"
)