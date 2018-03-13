# 함수 사용법

def main():
    print(power(10,2))

def say_hello(name):
    print("안녕 " , name)

say_hello("jang")


#반환 함수

def get_sum(start ,end):
    sum = 0
    for i in range(start ,end+1):
        sum += i
    return sum


sum = get_sum(3, 5)
print(sum)


def power(x, y):
    result = 1
    for i in range(y):
        result = result * x
    return result

main()