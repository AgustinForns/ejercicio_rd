from fastapi import Depends, HTTPException, APIRouter
from config.database import Session
from models.item import Item
from schemas.item import ItemSchema
from auth.auth import authentica_user

router = APIRouter()

@router.post("/input/{my_target_field}")
async def create_item(my_target_field: str, item: ItemSchema, _ = Depends(authentica_user)):
    allowed_fields = ["field_1", "author", "description"]
    
    if my_target_field not in allowed_fields:
        raise HTTPException(status_code=400, detail="Invalid target field")
    
    # Convierte el texto del campo objetivo a mayúsculas
    setattr(item, my_target_field, getattr(item, my_target_field).upper())
    
    db_item = Item(**item.model_dump())
    
    db = Session()
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    db.close()
    
    return {"id": db_item.id}



@router.get("/get_data/{id}", response_model=ItemSchema)
async def get_item(id: int, _ = Depends(authentica_user)):
    db = Session()
    item = db.query(Item).filter(Item.id == id).first()
    db.close()
    
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return item

