# 자동 판매기를 시뮬레이션하는 프로그램을 작성하여 보자. 사용자는 1000원짜리 지폐와 500원짜리 동전, 100원짜리 동전을 사용할 수 있다.
# 물건값을 입력하고 1000원권, 500원짜리 동전, 100원짜리 동전의 개수를 입력하면 거스름돈을 계산하여서 동전으로 반환한다.


itemPrice = int(input("물건값을 입력하시오 : "))

get1000w = int(input("1000dnjs 지폐개수 : "))
get500w = int(input("500dnjs 지폐개수 : "))
get100w = int(input("100dnjs 지폐개수 : "))

change = get1000w * 1000 + get500w * 500 + get100w * 100 - itemPrice

#거스름돈 1000원
won1000 = change // 1000
change = change % 1000
print("1000원 지폐개수 : " , won1000)

#거스름돈 500원
won500 = change // 500
change = change % 500
print("500원 지폐개수 : " , won500)

#거스름돈 100원
won100 = change // 100
change = change % 100
print("100원 지폐개수 : " , won100)

#거스름돈 50원
won50 = change // 50
change = change % 50
print("50원 지폐개수 : " , won50)

#거스름돈 10원
won10 = change // 10
change = change % 1046
print("10원 지폐개수 : " , won10)
