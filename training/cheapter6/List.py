scores = [32, 22, 45, 75, 34, 74, 21, 68]

for element in scores:
    print(element)

# list class

list1 = list() # 공백 리스트 생성

list2 = list("Hello") # 문자 H, e, l, l, o를 요소로 가지는 리스트 생성
# list2["H","e","l","l","e"] 와 같다.

list3 = list(range(0,5)) # 0, 1, 2, 3, 4를 요소로 가지는 리스트 생성
# list3[0, 1, 2, 3, 4]

print(list1)
print(list2)
print(list3)

list1 = [12, "dog", 180,14] # 혼합 자료형
list2 = [["Seoul", 10], ["Paris", 12], ["London", 50]] # 내장 리스트
list3 = ["aaa", ["bbb", [ "ccc", ["ddd", "eee", 45]]]] # 내장 리스트

print(list1)
print(list2)
print(list3)





