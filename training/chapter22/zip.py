#zip 함수 사용

# zip 함수는 List 여러개를 slice 할 때 사용한다.

# 김밥에 여러가지 재료를 묶고 김밥을 자르는 것과 비슷하다.
# 여러가지 List를 김밥말듯이 말아버린다.
# 그 후 iterator 등의 함수로 slice를 한다.

#ex
a = [1,2,3,4,5]
b = ['a','b','c','d','e']

for x,y in zip(a,b):
    print(x,y)


print()

# b의 개수가 3개일 때
a = [1,2,3,4,5]
b = ['a','b','c'] # 3개일 때

for x,y in zip(a,b):
    print(x,y)