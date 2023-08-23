from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class HashPassword:
	# 문자열을 해싱한 값을 리턴한다
	def create_hash(self, password: str):
		return pwd_context.hash(password)

	# 일반 텍스트 패스워드와 해싱한 패스워드를 받아 두 값이 일치하는지 비교한다
	# 비교 결과에 따라 boolean을 리턴함
	def verify_hash(self, plain_password: str, hashed_password: str):
		return pwd_context.verify(plain_password, hashed_password)