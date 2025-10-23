from sqlalchemy.orm import Session
from app import models, schemas

def get_player(db: Session, player_id: int):
    return db.query(models.Player).filter(models.Player.player_id == player_id).first()

def get_players(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Player).offset(skip).limit(limit).all()

def create_player(db: Session, player: schemas.PlayerCreate):
    db_player = models.Player(**player.dict())
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player

def update_player(db: Session, player_id: int, player: schemas.PlayerCreate):
    db_player = get_player(db, player_id)
    if db_player:
        for key, value in player.dict().items():
            setattr(db_player, key, value)
        db.commit()
        db.refresh(db_player)
    return db_player

def delete_player(db: Session, player_id: int):
    db_player = get_player(db, player_id)
    if db_player:
        db.delete(db_player)
        db.commit()
    return db_player
