from getpass import getpass

from sqlalchemy import select

from core.database import SessionLocal
from core.security import hash_password
from models import Clinica, Usuario


def main():
    clinica_id = int(input("ID da clínica: "))
    nome = input("Nome do administrador: ").strip()
    email = input("E-mail: ").strip().lower()

    password = getpass("Senha: ")
    confirmacao = getpass("Confirme a senha: ")

    if password != confirmacao:
        raise ValueError("As senhas não coincidem.")

    if len(password) < 12:
        raise ValueError("A senha deve ter ao menos 12 caracteres.")

    with SessionLocal() as db:
        clinica = db.get(Clinica, clinica_id)
        if clinica is None:
            raise ValueError("Clínica não encontrada.")

        usuario_existente = db.scalar(
            select(Usuario).where(Usuario.email == email)
        )
        if usuario_existente is not None:
            raise ValueError("Já existe um usuário com este e-mail.")

        usuario = Usuario(
            clinica_id=clinica.id,
            nome=nome,
            email=email,
            password_hash=hash_password(password),
            papel="admin",
        )

        db.add(usuario)
        db.commit()

    print("Administrador criado com sucesso.")


if __name__ == "__main__":
    main()