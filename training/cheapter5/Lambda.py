# 무명함수.
# lambda 맨 끝에 \ 를 하면 그 밑에 라인에다가도 쓸 수 있는 듯.
sum = lambda x,y: \
    x + y
# 아래와 같은 소스임.
# sum = lambda x,y: x + y

print("정수의 합 : " , sum(10,20))
print("정수의 합 : " , sum(20,30))


# callback 함수에 많이 사용된다. ( 코드 안에 함수가 포함 수 있는 모든 곳에 사용가능 )
# L이라는 list에 요소값들은 각각의 무명 함수가 들어있다.
L = [lambda x: x**2, lambda x: x**3, lambda x: x**4]

for f in L:
    print(f(3))