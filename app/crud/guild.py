from sqlalchemy.orm import Session
from app import models, schemas

def get_guild(db: Session, guild_id: int):
    return db.query(models.Guild).filter(models.Guild.guild_id == guild_id).first()

def get_guilds(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Guild).offset(skip).limit(limit).all()

def create_guild(db: Session, guild: schemas.GuildCreate):
    db_guild = models.Guild(**guild.dict())
    db.add(db_guild)
    db.commit()
    db.refresh(db_guild)
    return db_guild

def update_guild(db: Session, guild_id: int, guild: schemas.GuildCreate):
    db_guild = get_guild(db, guild_id)
    if db_guild:
        for key, value in guild.dict().items():
            setattr(db_guild, key, value)
        db.commit()
        db.refresh(db_guild)
    return db_guild

def delete_guild(db: Session, guild_id: int):
    db_guild = get_guild(db, guild_id)
    if db_guild:
        db.delete(db_guild)
        db.commit()
    return db_guild
