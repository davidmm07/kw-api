from typing import List
from app.dependencies.error_messages import BOUNDARY_ARRAY_ERROR_MESSAGE, EMPTY_ARRAY_ERROR_MESSAGE
from httpx import AsyncClient
import pytest
from app.main import app


@pytest.mark.asyncio
async def test_sequence():
    expected_response = {"result": 1}
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/smallest", json={"array": [-1, -3]})
    assert response.status_code == 200
    assert response.json() == expected_response


@pytest.mark.asyncio
async def test_error_empty():
    expected_response = {"error": EMPTY_ARRAY_ERROR_MESSAGE}
    empty_array = []
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/smallest", json={"array": empty_array})
    assert response.status_code == 401
    assert response.json() == expected_response


@pytest.mark.asyncio
async def test_error_boundary():
    expected_response = {"error": BOUNDARY_ARRAY_ERROR_MESSAGE}
    boundary_array = [7] * 100001
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/smallest", json={"array": boundary_array})
    assert response.status_code == 401
    assert response.json() == expected_response
