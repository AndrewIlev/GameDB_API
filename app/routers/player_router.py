from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter(
    prefix="/players",
    tags=["Players"]
)

@router.get("/", response_model=list[schemas.Player])
def read_players(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.player.get_players(db, skip=skip, limit=limit)

@router.get("/{player_id}", response_model=schemas.Player)
def read_player(player_id: int, db: Session = Depends(get_db)):
    db_player = crud.player.get_player(db, player_id)
    if db_player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return db_player

@router.post("/", response_model=schemas.Player)
def create_player(player: schemas.PlayerCreate, db: Session = Depends(get_db)):
    return crud.player.create_player(db, player)

@router.put("/{player_id}", response_model=schemas.Player)
def update_player(player_id: int, player: schemas.PlayerCreate, db: Session = Depends(get_db)):
    db_player = crud.player.update_player(db, player_id, player)
    if db_player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return db_player

@router.delete("/{player_id}", response_model=schemas.Player)
def delete_player(player_id: int, db: Session = Depends(get_db)):
    db_player = crud.player.delete_player(db, player_id)
    if db_player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return db_player
