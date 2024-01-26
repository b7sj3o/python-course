from .. import api
from .. models import Product 

@api.get('/product/{name}/{price}', response_model=Product)
def read_product(name: str, price: float):
    return Product(
        name=name,
        price=round(price, 2)
    )
