from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import (
    Boolean,
    CheckConstraint,
    DateTime,
    ForeignKey,
    String,
    func,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.database import Base

if TYPE_CHECKING:
    from models.clinica import Clinica


class Usuario(Base):
    __tablename__ = "usuarios"
    __table_args__ = (
        CheckConstraint(
            "papel IN ('admin', 'recepcao', 'profissional')",
            name="ck_usuarios_papel",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)

    clinica_id: Mapped[int] = mapped_column(
        ForeignKey("clinicas.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )

    nome: Mapped[str] = mapped_column(String(120), nullable=False)
    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
        nullable=False,
    )

    # Nunca armazene a senha; apenas o hash será salvo.
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)

    papel: Mapped[str] = mapped_column(String(30), nullable=False)
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        server_default=text("true"),
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    clinica: Mapped["Clinica"] = relationship(back_populates="usuarios")