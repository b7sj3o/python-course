from typing import Optional, List
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import ForeignKey
from .. import Base


class CartProductAssoc(Base):
    __tablename__ = "cart_product_assoc"
    
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), primary_key=True)
    cart_id: Mapped[int] = mapped_column(ForeignKey("carts.id"), primary_key=True)
    
    product: Mapped["Product"] = relationship(back_populates='cart_assoc')
    cart: Mapped["Cart"] = relationship(back_populates='product_assoc')
