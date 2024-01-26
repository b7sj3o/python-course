from typing import Optional, List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import (
    String,
    Integer,
    ForeignKey,
)
from .. import Base

class Notification(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[Optional[str]]
    description: Mapped[Optional[str]]

    user: Mapped["User"] = relationship(back_populates="notifications")
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))