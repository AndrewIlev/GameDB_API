from sqlalchemy.orm import Session
from app import models, schemas

def get_achievement(db: Session, achievement_id: int):
    return db.query(models.Achievement).filter(models.Achievement.achievement_id == achievement_id).first()

def get_achievements(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Achievement).offset(skip).limit(limit).all()

def create_achievement(db: Session, achievement: schemas.AchievementCreate):
    db_achievement = models.Achievement(**achievement.dict())
    db.add(db_achievement)
    db.commit()
    db.refresh(db_achievement)
    return db_achievement

def update_achievement(db: Session, achievement_id: int, achievement: schemas.AchievementCreate):
    db_achievement = get_achievement(db, achievement_id)
    if db_achievement:
        for key, value in achievement.dict().items():
            setattr(db_achievement, key, value)
        db.commit()
        db.refresh(db_achievement)
    return db_achievement

def delete_achievement(db: Session, achievement_id: int):
    db_achievement = get_achievement(db, achievement_id)
    if db_achievement:
        db.delete(db_achievement)
        db.commit()
    return db_achievement
