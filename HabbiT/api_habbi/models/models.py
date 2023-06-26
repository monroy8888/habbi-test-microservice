from pydantic import BaseModel
from typing import Optional


class House(BaseModel):
    name: Optional[str] = None
    city: Optional[str] = None
    year: Optional[int] = None


class HouseInfo(BaseModel):
    address: Optional[str]
    city: Optional[str]
    name: Optional[str]
    description: Optional[str]
    price: Optional[int]
