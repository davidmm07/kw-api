

from app.models.record import Record

record_collection = Record


async def add_record(new_record: Record) -> Record:
    record = await new_record.create()
    return record


async def get_ocurrencies(new_record: Record,number: int) -> int:
    total_ocurrencies = await new_record.find({'expected_response': number, }).count()
    return total_ocurrencies


async def get_total_records(new_record: Record,) -> int:
    total = await new_record.count()
    return total


async def get_ratio(ocurrencies: int, total: int) -> int:
    return ocurrencies/total
