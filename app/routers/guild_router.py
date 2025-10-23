from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas, database

router = APIRouter(
    prefix="/guilds",
    tags=["Guilds"]
)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.Guild])
def read_guilds(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.guild.get_guilds(db, skip=skip, limit=limit)

@router.get("/{guild_id}", response_model=schemas.Guild)
def read_guild(guild_id: int, db: Session = Depends(get_db)):
    db_guild = crud.guild.get_guild(db, guild_id)
    if db_guild is None:
        raise HTTPException(status_code=404, detail="Guild not found")
    return db_guild

@router.post("/", response_model=schemas.Guild)
def create_guild(guild: schemas.GuildCreate, db: Session = Depends(get_db)):
    return crud.guild.create_guild(db, guild)

@router.put("/{guild_id}", response_model=schemas.Guild)
def update_guild(guild_id: int, guild: schemas.GuildCreate, db: Session = Depends(get_db)):
    db_guild = crud.guild.update_guild(db, guild_id, guild)
    if db_guild is None:
        raise HTTPException(status_code=404, detail="Guild not found")
    return db_guild

@router.delete("/{guild_id}", response_model=schemas.Guild)
def delete_guild(guild_id: int, db: Session = Depends(get_db)):
    db_guild = crud.guild.delete_guild(db, guild_id)
    if db_guild is None:
        raise HTTPException(status_code=404, detail="Guild not found")
    return db_guild
