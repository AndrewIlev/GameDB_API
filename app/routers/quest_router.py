from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, database

router = APIRouter(
    prefix="/quests",
    tags=["Quests"]
)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.Quest])
def read_quests(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.quest.get_quests(db, skip=skip, limit=limit)

@router.get("/{quest_id}", response_model=schemas.Quest)
def read_quest(quest_id: int, db: Session = Depends(get_db)):
    db_quest = crud.quest.get_quest(db, quest_id)
    if db_quest is None:
        raise HTTPException(status_code=404, detail="Quest not found")
    return db_quest

@router.post("/", response_model=schemas.Quest)
def create_quest(quest: schemas.QuestCreate, db: Session = Depends(get_db)):
    return crud.quest.create_quest(db, quest)

@router.put("/{quest_id}", response_model=schemas.Quest)
def update_quest(quest_id: int, quest: schemas.QuestCreate, db: Session = Depends(get_db)):
    db_quest = crud.quest.update_quest(db, quest_id, quest)
    if db_quest is None:
        raise HTTPException(status_code=404, detail="Quest not found")
    return db_quest

@router.delete("/{quest_id}", response_model=schemas.Quest)
def delete_quest(quest_id: int, db: Session = Depends(get_db)):
    db_quest = crud.quest.delete_quest(db, quest_id)
    if db_quest is None:
        raise HTTPException(status_code=404, detail="Quest not found")
    return db_quest
