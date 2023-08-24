from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from auth.jwt_handler import create_access_token

from auth.hash_password import HashPassword
from database.connetion import Database

from models.users import User, TokenResponse


user_router = APIRouter(
	tags=["User"],
)
# DB대신 임시로 유저를 저장할 객체
user_database = Database(User)
hash_password = HashPassword()

# 로그인 요청을 post로 받았을때
@user_router.post("/signin", response_model=TokenResponse)
async def sign_user_in(user: OAuth2PasswordRequestForm = Depends()) -> dict:
	user_exist = await User.find_one(User.email == user.username)
	if not user_exist:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="User with email does not exist"
		)
	# if user_exist.password == user.password:
	# 	return {
	# 		"message": "User signed in successfully."
	# 	}
	if hash_password.verify_hash(user.password, user_exist.password):
		access_token = create_access_token(user_exist.email)
		return {
			"access_token": access_token,
			"token_type": "Bearer"
		}
	raise HTTPException(
		status_code=status.HTTP_401_UNAUTHORIZED,
		detail="Invalid details passed"
	)

# 회원가입 요청을 post요청을 받았을 때
@user_router.post("/signup")
async def sign_new_user(user: User) -> dict:
	user_exist = await User.find_one(User.email == user.email)
	if user_exist:
		raise HTTPException(
			status_code=status.HTTP_409_CONFLICT,
			detail="User with email provided exists already"
		)
	hashed_password = hash_password.create_hash(user.password)
	user.password = hashed_password
	await user_database.save(user)
	return {
		"message": "User created successfully."
	}

