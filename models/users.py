from typing import List, Optional
from pydantic import BaseModel, EmailStr

from models.events import Event

# 사용자 모델
class User(BaseModel):
	email: EmailStr
	password: str
	events: Optional[List[Event]]
	# 서브 클래스 Config는 API를 문서화할 때 샘플 데이터를 보여주기 위함이다.
	class Config:
		schema_extra = {
			"example": {
				"email": "fastapi@packt.com",
				"username": "strong!!!",
				"events": [],
			}
		}

# 사용자 로그인 모델
class UserSignIn(BaseModel):
	email: EmailStr
	password: str

	class Config:
		schema_extra = {
			"example": {
				"email": "fastapi@packt.com",
				"password": "strong!!!",
				"events": [],
			}
		}