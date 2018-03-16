# (와 )로 tuple을 만들 수 있다. 리스트는 [와 ]임

colors = ("red", "green", "blue")
print(colors)


numbers =(1,2,3,4,5)
print(numbers)

# 튜플은 변경될 수 없는 리스트다.

t1 = (1,2,3,4,5)
# t1[0] = 100  # 이것을 사용하면 에러 뜸.


# 튜플끼리 합칠 수 있음
t = numbers + colors
print(t)

# 튜플과 리스트는 합칠 수 없음. 에러 뜸
#list = [1,2,3,4,5]
#t2 = numbers + list

print(6 in numbers)

# 기본적인 튜플 연산들
t1 = (1,2,3,4)
t2 = (1,23,3,4)
# print(cmp(t1, t2)) # cmp()는 2개의 튜플을 비교하는데 . 왜 안되지??
print(len(t1)) # len()은 튜플의 길이를 반환한다.

print("max : ", max(t1))
print("min : ", min(t1))

list = [1,2,3,4,5]
print(list)
listTuple = tuple(list) # 리스트를 튜플로 변환한다.
print(listTuple)

