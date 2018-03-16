#numbers = {1,2,3}

#if 1 in numbers:
#    print("집합 안에 1이 있습니다.")

numbers = {2,1,3}
for x in numbers:
    print(x, end=" ")
# 1,2,3으로 나오는 이유는? 항목간 순서는 없다. 그래서 내부적으로 그냥 정렬되어서 나오는 것.
print()

# 세트에 요소 추가하기

numbers = {2,1,3}
# numbrs[0] #이렇게 하면 에러가 난다. set는 indexing을 제공하지 않는다


numbers.add(4) # .add로 추가할 수 있다.
print(numbers)

# 부분 집합 연산
A = {1,2,3}
B = {1,2,3}
print (A == B) # True

A = {1,2,3,4,5}
B = {1,2,3}
print( B < A) # B is a subset of A? True

A = {1,2,3,4,5}
B = {1,2,3}
B.issubset(A) # B < A 와 같다. True

# 집합 연산
A = {1,2,3}
B = {3,4,5}
print(A | B)# 합집합 연산
print(A & B)# 교집합 연산
print(A - B)# 차집합 연산

