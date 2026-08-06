from datetime import datetime

from sqlalchemy import String, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from core.database import Base


class Clinica(Base):

    __tablename__ = "clinicas"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    nome: Mapped[str] = mapped_column(
        String(120),
        nullable=False
    )

    cnpj: Mapped[str] = mapped_column(
        String(18),
        unique=True,
        nullable=False
    )

    telefone: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(120),
        unique=True,
        nullable=False
    )

    plano: Mapped[str] = mapped_column(
        String(30),
        default="starter"
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="ativo"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )