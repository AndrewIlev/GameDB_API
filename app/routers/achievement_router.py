from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, database

router = APIRouter(
    prefix="/achievements",
    tags=["Achievements"]
)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.Achievement])
def read_achievements(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.achievement.get_achievements(db, skip=skip, limit=limit)

@router.get("/{achievement_id}", response_model=schemas.Achievement)
def read_achievement(achievement_id: int, db: Session = Depends(get_db)):
    db_achievement = crud.achievement.get_achievement(db, achievement_id)
    if db_achievement is None:
        raise HTTPException(status_code=404, detail="Achievement not found")
    return db_achievement

@router.post("/", response_model=schemas.Achievement)
def create_achievement(achievement: schemas.AchievementCreate, db: Session = Depends(get_db)):
    return crud.achievement.create_achievement(db, achievement)

@router.put("/{achievement_id}", response_model=schemas.Achievement)
def update_achievement(achievement_id: int, achievement: schemas.AchievementCreate, db: Session = Depends(get_db)):
    db_achievement = crud.achievement.update_achievement(db, achievement_id, achievement)
    if db_achievement is None:
        raise HTTPException(status_code=404, detail="Achievement not found")
    return db_achievement

@router.delete("/{achievement_id}", response_model=schemas.Achievement)
def delete_achievement(achievement_id: int, db: Session = Depends(get_db)):
    db_achievement = crud.achievement.delete_achievement(db, achievement_id)
    if db_achievement is None:
        raise HTTPException(status_code=404, detail="Achievement not found")
    return db_achievement
