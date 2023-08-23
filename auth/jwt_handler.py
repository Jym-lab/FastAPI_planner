import time
from datetime import datetime

from fastapi import HTTPException, status
from jose import jwt, JWTError
from database.connetion import Settings

settings = Settings()

def create_access_token(user: str):
	# 문자열을 받아서 payload 딕셔너리에 저장
	# 해당 딕셔너리는 사용자명과 만료시간(1시간 후)을 저장함
	payload = {
		"user": user,
		"expires": time.time() + 3600
	}

	# encode 메서드는 payload, secret_key, 암호화 알고리즘을 인수로 받아 암호화를 함
	token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
	return token

def verify_access_token(token: str):
	try:
		data = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
		expire = data.get("expiores")

		# 토큰의 만료시간이 존재하는지 검사함
		# 없으면 유효한 토큰이 없다고 판단
		if expire is None:
			raise HTTPException(
				status_code=status.HTTP_400_BAD_REQUEST,
				detail="No access token supplied"
			)

		# 토큰이 유효한지 검사
		# 토큰이 유효하다면 디코딩된 payload를 리턴함
		if datetime.utcnow() > datetime.utcfromtimestamp(expire):
			raise HTTPException(
				status_code=status.HTTP_403_FORBIDDEN,
				detail="Token expired!"
			)
		return data
	# JWT 요청자체가 오류가 있는지 예외처리
	except JWTError:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="Invalid token"
		)