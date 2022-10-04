from array import array
from typing import List
from app.database.record_repository import add_record, get_ocurrencies, get_ratio, get_total_records
from app.models.sequence import Sequence
from app.routers.stats import get_stats
from beanie import Document, init_beanie
from mongomock_motor import AsyncMongoMockClient
from httpx import AsyncClient
import pytest
from app.app.main import app

class Record(Document):
    array: List[int]
    expected_response: int


@pytest.mark.asyncio
async def test_total_ocurrencies():
    client = AsyncMongoMockClient()
    query_expected_response=5
    sequenceOne = Sequence(array=[1, 3, 6, 4, 1, 2])
    sequenceTwo = Sequence(array=[1, 2, 6, 4, 3, -3])
    sequenceThree = Sequence(array=[1, 2, -1, 4, 5, -3])
    await init_beanie(database=client.beanie_test, document_models=[Record])
    recordOne = Record(array=sequenceOne.array, expected_response=sequenceOne.estimate_smallest_item())
    await add_record(recordOne)
    recordTwo = Record(array=sequenceTwo.array, expected_response=sequenceTwo.estimate_smallest_item())
    await add_record(recordTwo)
    recordThree = Record(array=sequenceThree.array, expected_response=sequenceThree.estimate_smallest_item())
    await add_record(recordThree)
    find_many = Record.find_many(Record.expected_response == query_expected_response)
    assert find_many.motor_cursor
    total_ocurrencies = await get_ocurrencies(Record,query_expected_response)
    assert await find_many.count() == total_ocurrencies
    query_expected_response = 3
    find_many = Record.find_many(Record.expected_response == query_expected_response)
    assert find_many.motor_cursor
    total_ocurrencies = await get_ocurrencies(Record,query_expected_response)
    assert await find_many.count() == total_ocurrencies

@pytest.mark.asyncio
async def test_total_records_with_new_record():
    expected_total = 4
    find_all = Record
    nextSequence = Sequence(array=[1, 2, 3])
    nextRecord = Record(array=nextSequence.array, expected_response=nextSequence.estimate_smallest_item())
    await add_record(nextRecord)
    assert await find_all.count() == await get_total_records(Record) == expected_total

@pytest.mark.asyncio
async def test_ratio_with_new_record():
    query_expected_response = 1
    nextSequence = Sequence(array=[-1,-3])
    nextRecord = Record(array=nextSequence.array, expected_response=nextSequence.estimate_smallest_item())
    await add_record(nextRecord)
    find_many = Record.find_many(Record.expected_response == query_expected_response)
    assert find_many.motor_cursor
    total_ocurrencies = await get_ocurrencies(Record,query_expected_response)
    assert await find_many.count() == total_ocurrencies 
    find_all = Record
    total_records = await find_all.count()
    assert await get_ratio(total_ocurrencies,total_records) == total_ocurrencies/total_records
