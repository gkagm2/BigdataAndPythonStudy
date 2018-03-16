def C2F(c_temp):
    return 9.0/5.0 * c_temp + 32
def F2C(f_temp):
    return (f_temp - 32.0) * 5.0/9.0

while True:

    print("'c' 섭씨온도에서 화씨온도로 변환")
    print("'f' 화씨온도에서 섭씨온도로 변환")
    print("'q' 종료")

    #입력
    word = input()

    if word == 'q':
        break

    elif word == 'c':
        value = float(input("화씨온도:"))
        print("화씨온도 :", C2F(value))

    elif word == 'f':
        value = float(input("섭씨온도:"))
        print("화씨온도 :", F2C(value))

    else :
        print("메뉴에서 선택하세요")


