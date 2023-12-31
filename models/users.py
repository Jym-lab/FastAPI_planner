from typing import List, Optional
from beanie import Document
from pydantic import BaseModel, EmailStr
from models.events import Event

# 사용자 모델
class User(Document):
	email: EmailStr
	password: str
	events: Optional[List[Event]]

	class Settings:
		name = "users"
	# 서브 클래스 Config는 API를 문서화할 때 샘플 데이터를 보여주기 위함이다.
	class Config:
		schema_extra = {
			"example": {
				"email": "fastapi@packt.com",
				"password": "strong!!!",
				"events": [],
			}
		}

# 사용자 로그인 모델
class TokenResponse(BaseModel):
	access_token: str
	token_type: str