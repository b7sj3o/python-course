from typing import Optional, List
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import ForeignKey
from .. import Base


class Cart(Base):
    __tablename__ = "carts"
    id: Mapped[int] = mapped_column(primary_key=True)
    
    user: Mapped[Optional["User"]] = relationship(back_populates="carts")
    user_id: Mapped[Optional[int]] = mapped_column(ForeignKey("users.id"))
    
    products: Mapped[List["Product"]] = relationship(
        secondary="cart_product_assoc",  # MUST HAVE secondary
        back_populates="carts",
        )
    product_assoc: Mapped[List["CartProductAssoc"]] = relationship(back_populates='cart')
