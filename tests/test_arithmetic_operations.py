# 테스트 파일을 만들 때는 반드시 test_*.py로 만들어야 한다.

def add(a: int, b: int) -> int:
	return a+b

def subtract(a: int, b: int) -> int:
	return b-a

def multiply(a: int, b: int) -> int:
	return a * b

def divide(a: int, b: int) -> int:
	return b // a

def test_add()->None:
	assert add(1, 1) == 11

def test_subtract()->None:
	assert subtract(2, 5) == 3

def test_multiply()->None:
	assert multiply(10, 10) == 100

def test_divide()->None:
	assert divide(25, 100) == 4