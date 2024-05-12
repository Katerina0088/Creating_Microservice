from pydantic import BaseModel
from typing import List

class FilmCreate(BaseModel):
    name: str
    year: int
    tags: str  # Define the "tags" field as a list of strings
    rating: int

class Film(BaseModel):
    id: int
    name: str
    year: int
    tags: str
    rating: int