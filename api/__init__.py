from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

api = FastAPI()

from . import endpoints
