from sqlalchemy.orm import Session
from app import models, schemas

def get_inventory(db: Session, player_id: int, item_id: int):
    return db.query(models.Inventory).filter(models.Inventory.player_id == player_id, models.Inventory.item_id == item_id).first()

def get_inventories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Inventory).offset(skip).limit(limit).all()

def create_inventory(db: Session, inventory: schemas.InventoryCreate):
    db_inventory = models.Inventory(**inventory.dict())
    db.add(db_inventory)
    db.commit()
    db.refresh(db_inventory)
    return db_inventory

def update_inventory(db: Session, player_id: int, item_id: int, inventory: schemas.InventoryCreate):
    db_inventory = get_inventory(db, player_id, item_id)
    if db_inventory:
        for key, value in inventory.dict().items():
            setattr(db_inventory, key, value)
        db.commit()
        db.refresh(db_inventory)
    return db_inventory

def delete_inventory(db: Session, player_id: int, item_id: int):
    db_inventory = get_inventory(db, player_id, item_id)
    if db_inventory:
        db.delete(db_inventory)
        db.commit()
    return db_inventory
