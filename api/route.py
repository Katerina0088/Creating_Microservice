from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import schemas, crud, models
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/film/", response_model=schemas.Film)
def create_film(film: schemas.FilmCreate, db: Session = Depends(get_db)):
    return crud.create_film(db=db, film=film)

@router.get("/film/")
def get_films(year: int = None, tag: str = None, db: Session = Depends(get_db)):
    return crud.get_films(db=db, year=year, tag=tag)

@router.get("/film/{film_id}", response_model=schemas.Film)
def get_film(film_id: int, db: Session = Depends(get_db)):
    return crud.get_film(db=db, film_id=film_id)

@router.put("/film/{film_id}", response_model=schemas.Film)
def update_film(film_id: int, film: schemas.FilmCreate, db: Session = Depends(get_db)):
    return crud.update_film(db=db, film_id=film_id, film=film)

@router.delete("/film/{film_id}")
def delete_film(film_id: int, db: Session = Depends(get_db)):
    return crud.delete_film(db=db, film_id=film_id)