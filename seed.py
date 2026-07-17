from app.database import SessionLocal
from app.models import User
from app.utils import get_password_hash


def seed():
    db = SessionLocal()
    try:
        exists = db.query(User).filter(User.email == "root@loja.com").first()
        if exists:
            print("Usuário root já existe, nenhuma ação necessária.")
            return

        root = User(
            name="root",
            email="root@loja.com",
            password=get_password_hash("psw@loja"),
        )
        db.add(root)
        db.commit()
        print("Usuário root criado com sucesso.")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
