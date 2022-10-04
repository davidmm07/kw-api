from typing import List
from beanie import Document


class Record(Document):
    array: List[int]
    expected_response: int

    class Collection:
        name = "record"

    class Config:
        schema_extra = {
            "example": {
                "array": [1, 3, 2, 13, 6, 7, 4, 5, 9],
                "expected_response": 8,
            }
        }
