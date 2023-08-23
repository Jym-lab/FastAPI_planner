from typing import Any, List, Optional
from beanie import PydanticObjectId, init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel, BaseSettings
from models.events import Event
from models.users import User


class Database:
	def __init__(self, model):
		self.model = model
#	레코드 하나를 데이터베이스에 추가한다.
	async def save(self, document) -> None:
		await document.create()
		return
#	단일 레코드를 불러온다
	async def get(self, id: PydanticObjectId) -> Any:
		doc = await self.model.get(id)
		if doc:
			return doc
		return False
#	전체 레코드를 불러온다
	async def get_all(self) -> List[Any]:
		docs = await self.model.find_all().to_list()
		return docs
#	기존 레코드를 변경한다.
	async def update(self, id: PydanticObjectId, body: BaseModel) -> Any:
		doc_id = id
		des_body = body.dict()
		des_body = {k:v for k,v in des_body.items() if v is not None}
		update_query = {"$set": {
			field: value for field, value in des_body.items()
		}}

		doc = await self.get(doc_id)
		if not doc:
			return False
		await doc.update(update_query)
		return doc
#	데이터베이스에서 레코드를 삭제함
	async def delete(self, id: PydanticObjectId) -> bool:
		doc = await self.get(id)
		if not doc:
			return False
		await doc.delete()
		return True
 

class Settings(BaseSettings):
	SECRET_KEY: Optional[str] = None
	DATABASE_URL: Optional[str] = None

	# 데이터베이스를 초기화 함
	async def initialize_database(self):
		client = AsyncIOMotorClient(self.DATABASE_URL)
		# 데이터베이스 클라이언트를 설정
		await init_beanie(database=client.get_default_database(),
			document_models=[Event, User])
	#데이터베이스 URL은 .env에서 읽어옴
	class Config:
		env_file = ".env"