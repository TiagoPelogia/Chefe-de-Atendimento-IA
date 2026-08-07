from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, DateTime, ForeignKey, String, func, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.database import Base

if TYPE_CHECKING:
    from models.clinica import Clinica


class Profissional(Base):
    __tablename__ = "profissionais"

    id: Mapped[int] = mapped_column(primary_key=True)

    clinica_id: Mapped[int] = mapped_column(
        ForeignKey("clinicas.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )

    nome: Mapped[str] = mapped_column(String(120), nullable=False)
    especialidade: Mapped[str | None] = mapped_column(String(120))
    conselho: Mapped[str | None] = mapped_column(String(30))
    conselho_uf: Mapped[str | None] = mapped_column(String(2))
    telefone: Mapped[str | None] = mapped_column(String(20))
    email: Mapped[str | None] = mapped_column(String(255))

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

    clinica: Mapped["Clinica"] = relationship(back_populates="profissionais")