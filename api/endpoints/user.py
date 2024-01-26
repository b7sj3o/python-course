from .. import api
from ..models import User, Product


@api.get('/user', response_model=User)
def read_user():
    return User(
        username="Vitalij",
        age=16,
        weight=82.5,
        is_alive=True
    )


