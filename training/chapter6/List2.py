marvel_heroes = ["스파이더맨", "헐크" , "아이언맨"]
dc_heroes = ["슈퍼맨", "배트맨", "원더우먼"]
heroes = marvel_heroes + dc_heroes

print(heroes)


value = [1, 2, 3] * 3
print(value)

print(len(value))

# 요소 추가하기

shopping_list = []
shopping_list.append("두부")
shopping_list.append("양배추")
shopping_list.append("딸기")


print(shopping_list)

# 요소 찾기

if "배트맨" in heroes: # in 연산자를 사용하면 된다.
    print("배트맨은 영웅 입니다.")


index = heroes.index("슈퍼맨") # 리스트 안에서의 위치 검색
print(index)

# 요소 삭제하기 pop()

heroes.pop(1) #헐크 삭제 pop은 index로 삭제
print(heroes)

heroes.remove("원더우먼") # remove는 요소 이름으로 삭제
print(heroes)

# 리스트 일치 검사
list1 = [1,2,3]
list2 = [1,2,3]
if list1 == list2:
    print("True")
else :
    print("False")

# 리스트 최소값과 최대값 찾기
values = [1,2,3,4,5,6,7,8,9]
print(min(values)) # min()은 요소들 중 최소값 찾기

print(max(values)) # max()는 요소들 중 최대값 찾기

# 리스트 정렬하기 sort()
a = [3,2,1,5,4]
a.sort() # 속성값으로 sort()를 사용할 수 있다.
print(a)

a = [3,2,1,5,4]
b = sorted(a) # sorted()의 내장 함수를 사용하면 정렬된다.
print(b)

# 리스트 복사하기 (얕은 복사 (Shallow copy)

scores = [10,20,30,40,50]
values = scores # 얕은 복사여서 주소값만 복사하여 똑같은 주소를 가리키는 것임.
print(scores)
print(values)
scores[2] = 90 #따라서 스코어의 값을 바꾸면 values값도 바뀌게 됨

print(scores)
print(values)

# 리스트 복사하기 (깊은 복사 (Deep copy)
scores = [10,20,30,40,50]
values = list(scores) #내장함수 list 사용 혹은 deepcopy() 사용 (이렇게 하면 다른 주소에서도 리스트를 만드는 것 처럼 됨)
print(scores)
print(values)

scores[2] = [99]
print(scores)
print(values)
