import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_routes_ok():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        for path in ["/", "/mentors", "/privacy"]:
            r = await ac.get(path)
            assert r.status_code == 200
            assert "text/html" in r.headers["content-type"]
