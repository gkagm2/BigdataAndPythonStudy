# 중첩 for문을 이용하여 * 기호르 사각형 모양으로 출력하는 프로그램

for y in range(5):
    for i in range(10):
        print("*", end="")
    print("") # 내부 반복문이 종료될 때마다 실행