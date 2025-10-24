# routers/inventory.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, database, models

router = APIRouter(
    prefix="/player",
    tags=["Player Inventories"]
)

# Залежність для підключення до БД
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------------------------
# Отримати весь інвентар конкретного гравця
# ---------------------------
@router.get("/{player_id}/inventory", response_model=list[schemas.Inventory])
def read_player_inventories(player_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.inventory.get_inventories_by_player(db, player_id, skip=skip, limit=limit)

# ---------------------------
# Отримати конкретний предмет у інвентарі гравця
# ---------------------------
@router.get("/{player_id}/inventory/item/{item_id}", response_model=schemas.Inventory)
def read_inventory_item(player_id: int, item_id: int, db: Session = Depends(get_db)):
    db_inventory = crud.inventory.get_inventory(db, player_id, item_id)
    if not db_inventory:
        raise HTTPException(status_code=404, detail="Inventory item not found")
    return db_inventory

# ---------------------------
# Створити предмет у інвентарі гравця
# ---------------------------
@router.post("/{player_id}/inventory/item", response_model=schemas.Inventory)
def create_inventory_item(player_id: int, inventory: schemas.InventoryCreate, db: Session = Depends(get_db)):
    db_inventory = models.Inventory(
        player_id=player_id,
        item_id=inventory.item_id,
        quantity=inventory.quantity
    )
    db.add(db_inventory)
    db.commit()
    db.refresh(db_inventory)
    return db_inventory

# ---------------------------
# Оновити предмет у інвентарі гравця
# ---------------------------
@router.put("/{player_id}/inventory/item/{item_id}", response_model=schemas.Inventory)
def update_inventory_item(player_id: int, item_id: int, inventory: schemas.InventoryCreate, db: Session = Depends(get_db)):
    db_inventory = crud.inventory.update_inventory(db, player_id, item_id, inventory)
    if not db_inventory:
        raise HTTPException(status_code=404, detail="Inventory item not found")
    return db_inventory

# ---------------------------
# Видалити предмет у інвентарі гравця
# ---------------------------
@router.delete("/{player_id}/inventory/item/{item_id}", response_model=schemas.Inventory)
def delete_inventory_item(player_id: int, item_id: int, db: Session = Depends(get_db)):
    db_inventory = crud.inventory.delete_inventory(db, player_id, item_id)
    if not db_inventory:
        raise HTTPException(status_code=404, detail="Inventory item not found")
    return db_inventory
