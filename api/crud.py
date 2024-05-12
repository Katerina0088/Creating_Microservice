from sqlalchemy.orm import Session
from . import models, schemas

def create_film(db: Session, film: schemas.FilmCreate):
    db_film = models.Film(name=film.name, year=film.year, tags=film.tags, rating=film.rating)
    db.add(db_film)
    db.commit()
    db.refresh(db_film)
    return db_film

def get_films(db: Session, year: int = None, tag: str = None):
    query = db.query(models.Film)
    if year:
        query = query.filter(models.Film.year == year)
    if tag:
        query = query.filter(models.Film.tags.contains(tag))
    return query.all()

def get_film(db: Session, film_id: int):
    return db.query(models.Film).filter(models.Film.id == film_id).first()

def update_film(db: Session, film_id: int, film: schemas.FilmCreate):
    db_film = db.query(models.Film).filter(models.Film.id == film_id).first()
    db_film.name = film.name
    db_film.year = film.year
    db_film.tags = film.tags
    db_film.rating = film.rating
    db.commit()
    db.refresh(db_film)
    return db_film

def delete_film(db: Session, film_id: int):
    db_film = db.query(models.Film).filter(models.Film.id == film_id).first()
    db.delete(db_film)
    db.commit()
    return {"message": "Film deleted"}