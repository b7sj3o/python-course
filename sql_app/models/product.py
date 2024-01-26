from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from .. import Base

class Product(Base):
    __tablename__ = "products"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[float]
    
    carts: Mapped[List["Cart"]] = relationship(
        secondary="cart_product_assoc", # MUST HAVE secondary
        back_populates="products",
        )
    cart_assoc: Mapped[List["CartProductAssoc"]] = relationship(back_populates='product')
    
    def __str__(self) -> str:
        return f"{self.name}(${self.price})"