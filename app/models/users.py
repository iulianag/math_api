from sqlalchemy import Column, String
from models.base import Base, session


class UsersModel(Base):

    __tablename__ = "users"

    username = Column(String(20), primary_key=True)
    password = Column(String(80), nullable=False)
    session_token = Column(String(80), unique=True)

    @classmethod
    def add_user(cls, username, password):
        new_user = UsersModel(username=username, password=password)
        session.add(new_user)
        session.commit()
        return 0

    @classmethod
    def is_registered_user(cls, username: str) -> bool:
        return bool(session.query(cls).filter(cls.username == username).first())

    @classmethod
    def are_registered_credentials(cls, username: str, password: str) -> bool:
        return bool(session.query(cls).filter(cls.username == username, cls.password == password).first())

    @classmethod
    def is_registered_token(cls, session_token: str) -> bool:
        return bool(session.query(cls).filter(cls.session_token == session_token).first())

    @classmethod
    def delete_session_token(cls, session_token: str):
        if cls.is_registered_token(session_token):
            session.query(cls).filter(cls.session_token == session_token).update({"session_token": None})
            session.commit()

    @classmethod
    def update_session_token(cls, username: str, password: str, session_token: str):
        if cls.are_registered_credentials(username, password):
            session.query(cls).filter(cls.username == username, cls.password == password).\
                update({"session_token": session_token})
            session.commit()

