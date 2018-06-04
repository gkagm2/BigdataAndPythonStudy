#join function
# 리스트의 요소들을 문자열로 합쳐준다.
# 리스트(배열) 정의
food = [ "123", "자장면", "짬뽕", "탕수육", "물만두", "팔보채" ]



# 요소들 사이에 공백 넣기 (구분자는 공백)
print(" ".join(food))
# 출력 결과: 123 자장면 짬뽕 탕수육 물만두 팔보채



# 모든 요소들을 하나로 연결하여 출력 (구분자 없음)
print("".join(food))
# 123자장면짬뽕탕수육물만두팔보채



# 슬래쉬(/)기호를 구분자로 넣은 후 연결하여 출력
print("/".join(food))
# 123/자장면/짬뽕/탕수육/물만두/팔보채



# 줄바꿈 문자를 구분자로 하여 출력
print("\n".join(food))