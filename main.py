from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.connetion import Settings
from routes.users import user_router
from routes.events import event_router
import uvicorn

app = FastAPI()
settings = Settings()
# 라우트 등록
app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")

# 애플리케이션 실행 시 데이터베이스 초기화
@app.on_event("startup")
async def init_db():
	await settings.initialize_database()

origins = ['*']

app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_credentials=True,
	allow_methods=['*'],
	allow_headers=['*'],
)

# 지정해두면 python main.py로 간단하게 실행이 가능하다
if __name__ == "__main__":
	uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)