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
    """
    Create a new item
    
    - **x_app_version**: Application version header (required)
    """
    # Check if item with same name exists
    existing_item = session.exec(
        select(Item).where(Item.name == item.name)
    ).first()
    
    if existing_item:
        raise HTTPException(
            status_code=400,
            detail=f"Item with name '{item.name}' already exists"
        )
    
    # Validate price
    if item.price <= 0:
        raise HTTPException(
            status_code=400,
            detail="Price must be greater than 0"
        )
    
    # Create new item
    db_item = Item.from_orm(item)
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    
    return db_item

@router.get("/", response_model=List[ItemRead])
async def read_items(
    *,
    session: Session = Depends(get_session),
    search: Optional[str] = Query(None, description="Search items by name"),
    limit: int = Query(10, ge=1, le=100, description="Limit number of results")
):
    """
    Get list of items with optional search and pagination
    """
    query = select(Item)
    
    if search:
        query = query.where(Item.name.contains(search))
    
    query = query.limit(limit)
    
    items = session.exec(query).all()
    return items