greeting = "Merry Christmas!"
print(greeting)

greeting2 = 'Happy Hliday1'

print(greeting2)

message = "철수가 '안녕'이라고 말했습니다."
print(message)


message = '철수가 "안녕"이라고 말했습니다.'
print(message)


#여러줄의 문자열 입력시.
greeting = '''지난해야
갑사합니다.'''

print(greeting)

#특수 문자열
## 문자 앞에 \가 붙으면 문자의 특수한 의미를 잃어버린다.
message = 'doesn\'t' # \를 사용하여 작은 따옴표를 출력한다.
print(message)

message = "\"yes,\" he said"
print(message)

#문자열의 연결
string = 'Py''thon'
print(string)

string = 'Harry ' + 'Porter'
print(string)

first_name = "길동"
last_name = "홍"
name = last_name + first_name
print(name)

#문자열과 정수 간의 변환

string = "Student" + str(26)
print(string)

price = int("29500")
print(type(price) , " " , price)

height = float("29.054")
print(height)

#문자열의 반복

line = "=" * 50 # 문자열을 50 곱하니까 50개가 됨
print(line)

message = "Congratulations! "
print(message * 3)

#문자열의 출력

price = 10000
print("상품의 가격은 %s원 입니다." %price) #c언어 형식으로 쓰려면 오른쪽 값에도 %를 붙여야 됨.

message = "현재 시간은 %s 입니다."
time = "12:00pm"
print(message % time) # 이게 되네!? 중요하다 모르는거네
