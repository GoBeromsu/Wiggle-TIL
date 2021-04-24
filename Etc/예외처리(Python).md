# 파이썬에서 예외처리하기

* 파이썬에서는 try-except 구문을 사용해  예외 처리를 한다

```python

try:
	•••
except[발생 오류 1 [as 오류 메시지 변수]]
	•••
except 발생 오류 2
	pass
else:
	•••
finally:
	•••
```

* except는 오류 발생시만 수행한다
* else는 except 구문에 걸리지 않을 때 사용한다
* finally는 무조건 실행된다
	* 사용한 소스를 닫을 때 사용한다
* pass는 오류를 회피한다

## except 사용법

* try-except만 사용하는 방법

```python
try:
	•••
except
	•••
```
* 발상 오류만 포함하는 방법

```python
try:
	•••
except[발생 오류]
	•••
```

* 발생 오류 메시지와 변수까지 포함한 방법

```python
try:
	•••
except[발생 오류 [as 오류 메시지 변수]]
	print(오류 메시지 변수)
```

* print(오류 메시지 변수) 식으로 오류 메시지를 출력한다

## 예외 만들기

```python
class MyError(Exception):
	def __str__(self);
		return "오류 메시지"
		
try:
	•••
except MyError()
	•••
```

* __str__ 은 오류메시지 print문으로 출력하고 싶을 때 사용한다
