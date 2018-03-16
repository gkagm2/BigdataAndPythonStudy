sum = 0

#range(10)은 0 부터 9까지의 숫자 범위
#rnage(start, stop)와 같이 호출하면 start부터 시작하여서 (stop-1)까지의 정수가 생성된다. 이때 stop은 포함되지 않는다.
for x in range(10):
    sum = sum + x

print(sum)


for x in range(10):
    print(x, end=" ")
print() # 이걸 안하면 밑에 print(sum)부분도 옆에 붙여짐
sum = 0

for x in range(0,10):
    sum = sum + x
print(sum)

# range() 함수는 start부터 stop-1까지 step의 간격으로 정수들을 생성한다.
# start와 step이 대괄호로 싸여져 있는데 이는 생략할 수 있다는 의미이다.
#  start나 step이 생략되면 start는 0, step은 1로 간주된다.

# range( [start ,] stop [, step])

# 문자열 반복

for c in "abcdef":
    print(c, end=" ")
print()


# 정수들의 합 구하기
# 1부터 사용자가 입력한 수 n까지 더해서 (1+2+3+...+n)을 계산하는 프로그램을 작성
sum = 0
integer = int(input("어디까지 계산할까요:"))

for i in range(1, integer):
    sum = sum + i
print("1부터 ",integer , "까지의 정수의 합 =", sum)
