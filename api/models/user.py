from pydantic import BaseModel

class User(BaseModel):
    username: str
    age: int
    weight: float
    is_alive: bool
