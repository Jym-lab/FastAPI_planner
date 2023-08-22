from typing import List
from pydantic import BaseModel

# 이벤트 모델
class Event(BaseModel):
	id: int
	title: str
	image: str
	description: str
	tags: List[str]
	location: str
	# 서브 클래스 Config는 API를 문서화할 때 샘플 데이터를 보여주기 위함이다.
	class Config:
		schema_extra = {
			"example": {
				"title": "FastAPI Book Launch",
				"image": "https://linktomyimage.com/image.png",
				"description": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts!",
				"tags": ["python", "fastapi", "book", "launch"],
				"location": "Google Meet"
			}
		}