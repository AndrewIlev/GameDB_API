from sqlalchemy.orm import Session
from app import models, schemas

def get_skill(db: Session, skill_id: int):
    return db.query(models.Skill).filter(models.Skill.skill_id == skill_id).first()

def get_skills(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Skill).offset(skip).limit(limit).all()

def create_skill(db: Session, skill: schemas.SkillCreate):
    db_skill = models.Skill(**skill.dict())
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill

def update_skill(db: Session, skill_id: int, skill: schemas.SkillCreate):
    db_skill = get_skill(db, skill_id)
    if db_skill:
        for key, value in skill.dict().items():
            setattr(db_skill, key, value)
        db.commit()
        db.refresh(db_skill)
    return db_skill

def delete_skill(db: Session, skill_id: int):
    db_skill = get_skill(db, skill_id)
    if db_skill:
        db.delete(db_skill)
        db.commit()
    return db_skill
