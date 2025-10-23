from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, database

router = APIRouter(
    prefix="/mathgames",
    tags=["MathGames"]
)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.MathGame])
def read_mathgames(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.mathgame.get_mathgames(db, skip=skip, limit=limit)

@router.get("/{match_id}", response_model=schemas.MathGame)
def read_mathgame(match_id: int, db: Session = Depends(get_db)):
    db_game = crud.mathgame.get_mathgame(db, match_id)
    if db_game is None:
        raise HTTPException(status_code=404, detail="MathGame not found")
    return db_game

@router.post("/", response_model=schemas.MathGame)
def create_mathgame(mathgame: schemas.MathGameCreate, db: Session = Depends(get_db)):
    return crud.mathgame.create_mathgame(db, mathgame)

@router.put("/{match_id}", response_model=schemas.MathGame)
def update_mathgame(match_id: int, mathgame: schemas.MathGameCreate, db: Session = Depends(get_db)):
    db_game = crud.mathgame.update_mathgame(db, match_id, mathgame)
    if db_game is None:
        raise HTTPException(status_code=404, detail="MathGame not found")
    return db_game

@router.delete("/{match_id}", response_model=schemas.MathGame)
def delete_mathgame(match_id: int, db: Session = Depends(get_db)):
    db_game = crud.mathgame.delete_mathgame(db, match_id)
    if db_game is None:
        raise HTTPException(status_code=404, detail="MathGame not found")
    return db_game
