# conftest.py
# 테스트 파일이 필요로 하는 애플리케이션의 인스턴스를 만드는 역할
import asyncio
import httpx
import pytest

from main import app
from database.connetion import Settings
from models.events import Event
from models.users import User

# 픽스처는 재사용 가능 함수로 테스트 함수의 필요한 데이터를 반환하기 위해 정의됨 
@pytest.fixture(scope="session")
def event_loop():
	loop = asyncio.get_event_loop()
	yield loop
	loop.close()

async def init_db():
	test_settings = Settings()
	test_settings.DATABASE_URL = "mongodb://localhost:27017/testdb"

	await test_settings.initialize_database()

@pytest.fixture(scope="session")
async def default_client():
	await init_db()
	async with httpx.AsyncClient(app=app, base_url="http://app") as client:
		yield client
		#리소스 정리
		await Event.find_all().delete()
		await User.find_all().delete()