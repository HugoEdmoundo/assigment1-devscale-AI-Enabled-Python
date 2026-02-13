from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional
from pydantic import validator, constr

# Base model (shared properties)
class ItemBase(SQLModel):
    name: constr(min_length=3) = Field(..., description="Item name, minimum 3 characters")
    price: int = Field(..., gt=0, description="Item price, must be greater than 0")
    stock: int = Field(..., ge=0, description="Item stock, must be 0 or greater")
    
    @validator('price')
    def validate_price(cls, v):
        if v <= 0:
            raise ValueError('Price must be greater than 0')
        return v
    
    @validator('stock')
    def validate_stock(cls, v):
        if v < 0:
            raise ValueError('Stock cannot be negative')
        return v


class Item(ItemBase, table=True):
    __tablename__ = "items"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)


class ItemCreate(ItemBase):
    pass


class ItemRead(ItemBase):
    id: int
    created_at: datetime