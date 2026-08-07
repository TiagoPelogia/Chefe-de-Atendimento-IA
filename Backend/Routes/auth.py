from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from core.database import get_db
from core.security import (
    DUMMY_PASSWORD_HASH,
    create_access_token,
    verify_password,
)
from models import Usuario
from schemas.auth import LoginRequest, TokenResponse

router = APIRouter(prefix="/auth", tags=["Autenticação"])


@router.post("/login", response_model=TokenResponse)
def login(
    credentials: LoginRequest,
    db: Session = Depends(get_db),
) -> TokenResponse:
    usuario = db.scalar(
        select(Usuario).where(
            func.lower(Usuario.email) == credentials.email
        )
    )

    password_hash = (
        usuario.password_hash
        if usuario is not None
        else DUMMY_PASSWORD_HASH
    )
    senha_valida = verify_password(
        credentials.senha,
        password_hash,
    )

    if (
        usuario is None
        or not senha_valida
        or not usuario.is_active
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token = create_access_token(
        user_id=usuario.id,
        clinica_id=usuario.clinica_id,
        papel=usuario.papel,
    )

    return TokenResponse(access_token=token)