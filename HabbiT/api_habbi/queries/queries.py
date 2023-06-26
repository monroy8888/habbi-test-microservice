from ..models.models import House, HouseInfo
from ..config.config import database
from typing import List

SELECT_QUERY = """SELECT p.address, p.city, s.name, p.description, p.price  FROM status_history sh 
INNER JOIN status s  ON sh.status_id = s.id
INNER JOIN property p ON sh.property_id  = p.id
WHERE p.`year` AND  p.city  IS NOT NULL 
"""


async def filter_query(Items: House) -> List[HouseInfo]:
    params = {}
    CONDITION_QUERY = SELECT_QUERY
    if Items.name is not None:
        CONDITION_QUERY += " AND s.name = :name"
        params["name"] = Items.name
    if Items.city is not None:
        CONDITION_QUERY += " AND p.city = :city"
        params["city"] = Items.city
    if Items.year is not None:
        CONDITION_QUERY += " AND p.`year` = :year"
        params["year"] = Items.year

    results = await database.fetch_all(CONDITION_QUERY, values=params)
    return [HouseInfo(**dict(row)) for row in results]
