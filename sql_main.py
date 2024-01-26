from sql_app import (
    Base, 
    SessionLocal, 
    Notification, 
    User, 
    Product,
    Cart,
    CartProductAssoc,
)
# from sql_app import Base, SessionLocal, Association, Child, Parent 
from sql_app.database import engine

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

with SessionLocal() as session:
    cart = Cart()
    for i in range(3):
        cart.products.append(Product(
            name=f'name{i}',
            description=f'description{i}',
            price=i
        ))
    session.add(cart)
    session.commit()
    
    for prod in cart.products:
        print(prod)
# with SessionLocal() as session:
#     c1 = Child()
#     c1.parents.append(Parent())
#     # p1.children.append(c1)


#     session.add(c1)
#     session.commit()

# with SessionLocal() as session:
#     print("SESSION BEGIN")
#     print("*" * 80)
#     user = User(
#         login="something",
#         password='newdwa',
#         fullname='vitalik fedytnyk'
#     )
    
#     product = Product( #child
#         name="Coca Cola",
#         description='some description',
#         price=29.99
#     )
#     cart = Cart( #parent
#         user=user
#     )
#     cart.products.append(product)
#     cart.child_associations.append(CartProductAssoc(product=product))
#     # p1 = Parent()
#     # c1 = Child()
#     # p1.children.append(c1)

#     # redundant, will cause a duplicate INSERT on Association
#     # p1.child_associations.append(Association(child=c1))
#     # assoc = CartProductAssoc()
#     # assoc.product = product
#     # cart.products.append(product)
#     # cart.products.append(product)
#     # for i in cart.products:
#     #     print(i.product.name)
#     session.add(cart)
#     session.commit()


