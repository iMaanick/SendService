import pytest
from httpx import ASGITransport, AsyncClient

from app.bootstrap.entrypoints.api import create_app


@pytest.mark.asyncio
async def test_health():
    transport = ASGITransport(app=create_app())
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        res = await ac.get("/healthcheck")
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}
