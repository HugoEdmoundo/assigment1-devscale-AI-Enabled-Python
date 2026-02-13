from fastapi import APIRouter, Depends, HTTPException, Query, Header
from sqlmodel import Session, select
from typing import List, Optional
from src.models.item_model import Item, ItemCreate, ItemRead
from src.core.db import get_session

router = APIRouter(prefix="/items", tags=["Items"])

@router.post("/", response_model=ItemRead, status_code=201)
async def create_item(
    *,
    session: Session = Depends(get_session),
    item: ItemCreate,
    x_app_version: str = Header(..., alias="X-App-Version")
):

    existing_item = session.exec(
        select(Item).where(Item.name == item.name)
    ).first()
    
    if existing_item:
        raise HTTPException(
            status_code=400,
            detail=f"Item with name '{item.name}' already exists"
        )
    
    if item.price <= 0:
        raise HTTPException(
            status_code=400,
            detail="Price must be greater than 0"
        )
    
    db_item = Item.from_orm(item)
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    
    return db_item

@router.get("/", response_model=List[ItemRead])
async def read_items(
    *,
    session: Session = Depends(get_session),
    search: Optional[str] = Query(None),
    limit: int = Query(10, ge=1, le=100)
):
    
    query = select(Item)
    
    if search:
        query = query.where(Item.name.contains(search))
    
    query = query.limit(limit)
    
    items = session.exec(query).all()
    return items