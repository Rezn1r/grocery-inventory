from sqlalchemy import select
from models import User
from auth import hash_password, verify_password
from database import get_session


def create_user(username: str, password: str, role: str = "user") -> bool:
    with get_session() as session:
        stmt = select(User).where(User.username == username)
        existing_user = session.scalar(stmt)

        if existing_user:
            return False 

        user = User(
            username=username,
            password_hash=hash_password(password),
            role=role
        )

        session.add(user)
        session.commit()
        return True

def authenticate_user(username: str, password: str) -> User | None:
    with get_session() as session:
        stmt = select(User).where(User.username == username)
        user = session.scalar(stmt)

        if user and verify_password(user.password_hash, password):
            return user

    return None

def is_admin(user: User) -> bool:
    return user.role == "admin"