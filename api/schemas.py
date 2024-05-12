from pydantic import BaseModel
from typing import List

class FilmCreate(BaseModel):
    name: str
    year: int
    tags: str  
    rating: int

class Film(BaseModel):
    id: int
    name: str
    year: int
    tags: str
    rating: int