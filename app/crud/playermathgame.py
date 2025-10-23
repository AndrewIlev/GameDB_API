from sqlalchemy.orm import Session
from app import models, schemas

def get_playermathgame(db: Session, player_id: int, match_id: int):
    return db.query(models.PlayerMathGame).filter(models.PlayerMathGame.player_id==player_id, models.PlayerMathGame.match_id==match_id).first()

def get_playermathgames(db: Session, skip: int=0, limit: int=100):
    return db.query(models.PlayerMathGame).offset(skip).limit(limit).all()

def create_playermathgame(db: Session, pm: schemas.PlayerMathGameCreate):
    db_pm = models.PlayerMathGame(**pm.dict())
    db.add(db_pm)
    db.commit()
    db.refresh(db_pm)
    return db_pm

def delete_playermathgame(db: Session, player_id: int, match_id: int):
    db_pm = get_playermathgame(db, player_id, match_id)
    if db_pm:
        db.delete(db_pm)
        db.commit()
   
