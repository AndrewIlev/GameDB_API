from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, database

router = APIRouter(
    prefix="/inventories",
    tags=["Inventories"]
)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.Inventory])
def read_inventories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.inventory.get_inventories(db, skip=skip, limit=limit)

@router.get("/{player_id}/{item_id}", response_model=schemas.Inventory)
def read_inventory(player_id: int, item_id: int, db: Session = Depends(get_db)):
    db_inventory = crud.inventory.get_inventory(db, player_id, item_id)
    if db_inventory is None:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return db_inventory

@router.post("/", response_model=schemas.Inventory)
def create_inventory(inventory: schemas.InventoryCreate, db: Session = Depends(get_db)):
    return crud.inventory.create_inventory(db, inventory)

@router.put("/{player_id}/{item_id}", response_model=schemas.Inventory)
def update_inventory(player_id: int, item_id: int, inventory: schemas.InventoryCreate, db: Session = Depends(get_db)):
    db_inventory = crud.inventory.update_inventory(db, player_id, item_id, inventory)
    if db_inventory is None:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return db_inventory

@router.delete("/{player_id}/{item_id}", response_model=schemas.Inventory)
def delete_inventory(player_id: int, item_id: int, db: Session = Depends(get_db)):
    db_inventory = crud.inventory.delete_inventory(db, player_id, item_id)
    if db_inventory is None:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return db_inventory
