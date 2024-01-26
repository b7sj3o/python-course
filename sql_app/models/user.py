from typing import Optional, List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import (
    String,
    Integer,
    ForeignKey,
)
from .. import Base

class User(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str]
    password: Mapped[str]
    fullname: Mapped[Optional[str]]

    notifications: Mapped[List['Notification']] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    carts: Mapped[List['Cart']] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )