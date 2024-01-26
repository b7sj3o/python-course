from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine("sqlite:///my_db.sqlite")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    @classmethod
    @property
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"
