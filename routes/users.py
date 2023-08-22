from fastapi import APIRouter, HTTPException, status

from models.users import User, UserSignIn


user_router = APIRouter(
	tags=["User"],
)
# DB대신 임시로 유저를 저장할 객체
users = {}

# 로그인 요청을 post로 받았을때
@user_router.post("/signin")
async def sign_user_in(user: UserSignIn) -> dict:
	if user.email not in users:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="User does not exist"
		)
	if users[user.email].password != user.password:
		raise HTTPException(
			status_code=status.HTTP_403_FORBIDDEN,
			detail="Wrong credentials passed"
		)
	return {
		"message": "User signed in successfully."
	}

# 회원가입 요청을 post요청을 받았을 때
@user_router.post("/signup")
async def sign_new_user(data: User) -> dict:
	if data.email in users:
		raise HTTPException(
			status_code=status.HTTP_409_CONFLICT,
			detail="User with supplied username exists"
		)
	users[data.email] = data
	return {
		"message": "User successfully registered!"
	}

