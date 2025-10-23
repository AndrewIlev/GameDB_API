from sqlalchemy.orm import Session
from app import models, schemas

def get_playerachievement(db: Session, player_id: int, achievement_id: int):
    return db.query(models.PlayerAchievement).filter(models.PlayerAchievement.player_id==player_id, models.PlayerAchievement.achievement_id==achievement_id).first()

def get_playerachievements(db: Session, skip: int=0, limit: int=100):
    return db.query(models.PlayerAchievement).offset(skip).limit(limit).all()

def create_playerachievement(db: Session, pa: schemas.PlayerAchievementCreate):
    db_pa = models.PlayerAchievement(**pa.dict())
    db.add(db_pa)
    db.commit()
    db.refresh(db_pa)
    return db_pa

def delete_playerachievement(db: Session, player_id: int, achievement_id: int):
    db_pa = get_playerachievement(db, player_id, achievement_id)
    if db_pa:
        db.delete(db_pa)
        db.commit()
    return db_pa
