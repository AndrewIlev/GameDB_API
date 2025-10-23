from sqlalchemy.orm import Session
from app import models, schemas

def get_quest(db: Session, quest_id: int):
    return db.query(models.Quest).filter(models.Quest.quest_id == quest_id).first()

def get_quests(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Quest).offset(skip).limit(limit).all()

def create_quest(db: Session, quest: schemas.QuestCreate):
    db_quest = models.Quest(**quest.dict())
    db.add(db_quest)
    db.commit()
    db.refresh(db_quest)
    return db_quest

def update_quest(db: Session, quest_id: int, quest: schemas.QuestCreate):
    db_quest = get_quest(db, quest_id)
    if db_quest:
        for key, value in quest.dict().items():
            setattr(db_quest, key, value)
        db.commit()
        db.refresh(db_quest)
    return db_quest

def delete_quest(db: Session, quest_id: int):
    db_quest = get_quest(db, quest_id)
    if db_quest:
        db.delete(db_quest)
        db.commit()
    return db_quest
