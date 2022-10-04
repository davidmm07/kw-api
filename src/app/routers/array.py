from array import array
from app.models.record import Record
from ..database.record_repository import add_record
from fastapi import APIRouter
from ..models.sequence import MissingSmallestItemResponse, Sequence
from beanie.exceptions import CollectionWasNotInitialized
router = APIRouter()


@router.post("/smallest", response_model=MissingSmallestItemResponse, response_description="missing smallest item retrieved")
async def check_smallest_item(sequence: Sequence):
    try:
        result = sequence.estimate_smallest_item()
        await add_record(Record(array=sequence.array, expected_response=result))
    except CollectionWasNotInitialized:
        pass
    return {"result": result}
