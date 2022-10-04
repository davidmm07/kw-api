from app.database.record_repository import get_ocurrencies, get_ratio, get_total_records
from fastapi import APIRouter
from ..models.record import Record

record_collection = Record

router = APIRouter()


@router.get("/stats/{number}", response_description="stats retrieved")
async def get_stats(number:int):
    count = await get_ocurrencies(record_collection, number)
    total = await get_total_records(record_collection)
    ratio = await get_ratio(count,total)
    return {"count": count, "total": total, "ratio": ratio}
