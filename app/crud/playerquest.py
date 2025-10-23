from sqlalchemy.orm import Session
from app import models, schemas

def get_playerquest(db: Session, player_id: int, quest_id: int):
    return db.query(models.PlayerQuest).filter(models.PlayerQuest.player_id==player_id, models.PlayerQuest.quest_id==quest_id).first()

def get_playerquests(db: Session, skip: int=0, limit: int=100):
    return db.query(models.PlayerQuest).offset(skip).limit(limit).all()

def create_playerquest(db: Session, pq: schemas.PlayerQuestCreate):
    db_pq = models.PlayerQuest(**pq.dict())
    db.add(db_pq)
    db.commit()
    db.refresh(db_pq)
    return db_pq

def delete_playerquest(db: Session, player_id: int, quest_id: int):
    db_pq = get_playerquest(db, player_id, quest_id)
    if db_pq:
        db.delete(db_pq)
        db.commit()
    return db_pq
