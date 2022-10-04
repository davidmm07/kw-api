from typing import List
from ..dependencies.error_messages import BOUNDARY_ARRAY_ERROR_MESSAGE, EMPTY_ARRAY_ERROR_MESSAGE
from ..dependencies.exceptions import CustomArrayException
from pydantic import BaseModel, validator


class Sequence(BaseModel):
    array: List[int] = []

    @validator('array')
    def check_length(cls, a):
        if len(a) < 1:
            raise CustomArrayException(EMPTY_ARRAY_ERROR_MESSAGE, 401)
        elif len(a) > 100000:
            raise CustomArrayException(BOUNDARY_ARRAY_ERROR_MESSAGE, 401)
        return a

    def estimate_smallest_item(cls):
        a = cls.array.copy()
        n = len(a)
        if 1 not in a:
            return 1
        for i in range(n):
            if a[i] <= 0 or a[i] > n:
                a[i] = 1
        for i in range(n):
            a[((a[i] - 1) % n + n) % n] += n
        for i in range(n):
            if a[i] <= n:
                return i + 1
        return n + 1


class MissingSmallestItemResponse(BaseModel):
    result: int
