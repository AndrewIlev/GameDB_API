from sqlalchemy.orm import Session
from app import models, schemas

def get_playerskill(db: Session, player_id: int, skill_id: int):
    return db.query(models.PlayerSkill).filter(models.PlayerSkill.player_id==player_id, models.PlayerSkill.skill_id==skill_id).first()

def get_playerskills(db: Session, skip: int=0, limit: int=100):
    return db.query(models.PlayerSkill).offset(skip).limit(limit).all()

def create_playerskill(db: Session, ps: schemas.PlayerSkillCreate):
    db_ps = models.PlayerSkill(**ps.dict())
    db.add(db_ps)
    db.commit()
    db.refresh(db_ps)
    return db_ps

def delete_playerskill(db: Session, player_id: int, skill_id: int):
    db_ps = get_playerskill(db, player_id, skill_id)
    if db_ps:
        db.delete(db_ps)
        db.commit()
    return db_ps
