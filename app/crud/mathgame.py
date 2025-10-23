from sqlalchemy.orm import Session
from app import models, schemas

def get_mathgame(db: Session, match_id: int):
    return db.query(models.MathGame).filter(models.MathGame.match_id == match_id).first()

def get_mathgames(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MathGame).offset(skip).limit(limit).all()

def create_mathgame(db: Session, mathgame: schemas.MathGameCreate):
    db_mathgame = models.MathGame(**mathgame.dict())
    db.add(db_mathgame)
    db.commit()
    db.refresh(db_mathgame)
    return db_mathgame

def update_mathgame(db: Session, match_id: int, mathgame: schemas.MathGameCreate):
    db_mathgame = get_mathgame(db, match_id)
    if db_mathgame:
        for key, value in mathgame.dict().items():
            setattr(db_mathgame, key, value)
        db.commit()
        db.refresh(db_mathgame)
    return db_mathgame

def delete_mathgame(db: Session, match_id: int):
    db_mathgame = get_mathgame(db, match_id)
    if db_mathgame:
        db.delete(db_mathgame)
        db.commit()
    return db_mathgame
