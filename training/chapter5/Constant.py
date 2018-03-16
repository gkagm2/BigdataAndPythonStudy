# 대문자로 하면 상수로 되는 것 같다.
PI = 3.14159265358979 # 전역 상수

def main():
    radius = float(input("원의 반지름을 입력하시오 : "))
    print("원의 면적 : ", circleArea(radius))
    print("원의 둘레: ", circleCircumference(radius))

def circleArea(radius):
    return PI * radius * radius

def circleCircumference(radius):
    return 2 * PI * radius



main()