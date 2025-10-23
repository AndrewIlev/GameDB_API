from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, database

router = APIRouter(
    prefix="/skills",
    tags=["Skills"]
)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.Skill])
def read_skills(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.skill.get_skills(db, skip=skip, limit=limit)

@router.get("/{skill_id}", response_model=schemas.Skill)
def read_skill(skill_id: int, db: Session = Depends(get_db)):
    db_skill = crud.skill.get_skill(db, skill_id)
    if db_skill is None:
        raise HTTPException(status_code=404, detail="Skill not found")
    return db_skill

@router.post("/", response_model=schemas.Skill)
def create_skill(skill: schemas.SkillCreate, db: Session = Depends(get_db)):
    return crud.skill.create_skill(db, skill)

@router.put("/{skill_id}", response_model=schemas.Skill)
def update_skill(skill_id: int, skill: schemas.SkillCreate, db: Session = Depends(get_db)):
    db_skill = crud.skill.update_skill(db, skill_id, skill)
    if db_skill is None:
        raise HTTPException(status_code=404, detail="Skill not found")
    return db_skill

@router.delete("/{skill_id}", response_model=schemas.Skill)
def delete_skill(skill_id: int, db: Session = Depends(get_db)):
    db_skill = crud.skill.delete_skill(db, skill_id)
    if db_skill is None:
        raise HTTPException(status_code=404, detail="Skill not found")
    return db_skill
