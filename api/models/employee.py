from pydantic import BaseModel
from typing import List

class Employee(BaseModel):
    name: str
    requirements: List[str]
    salary: float


