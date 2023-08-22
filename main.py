from fastapi import FastAPI
from routes.users import user_router
from routes.events import event_router
import uvicorn

app = FastAPI()
# 라우트 등록
app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")

# 지정해두면 python main.py로 간단하게 실행이 가능하다
if __name__ == "__main__":
	uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)