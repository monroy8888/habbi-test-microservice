from fastapi import APIRouter
from typing import List

from ..models.models import House, HouseInfo
from ..queries.queries import filter_query

router = APIRouter()


@router.post("/filter_info/", response_model=List[HouseInfo])
async def filter_info(Items: House) -> List[HouseInfo]:
    data = await filter_query(Items)
    return data
