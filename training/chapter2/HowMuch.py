#하나의 예로 현재 5000원이 있고 사탕의 가격이 120원이라고 하자. 최대한 사 수 있는 사탕의 개수와 나머지 돈은 얼마인가?

myMoney = 5000
candyPrice = 120

#최대한 살 수 있는 사탕 수
numCandies = myMoney // candyPrice # /은 소수점도 포함된 나눗셈 //는 정수값의 나눗셈
print(numCandies)

#최대한 사탕을 구입하고 남은 돈
change = myMoney % candyPrice
print(change)