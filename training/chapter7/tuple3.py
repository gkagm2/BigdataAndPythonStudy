# 마구 찍은 함수

def magu_print(x, y ,*rest):
    print (x, y, rest)


# 3이상의 값을 넣으면 rest부분에 튜플로 묶인다.
magu_print(1,2,3,4,5,5,6)

# 원소 하나만 가진 튜플을 만들 땐 원소 뒤에 콤마(,)를 써줘야 한다.

one = 5
print(one)

two = 2,
print(two)

# 튜플은 리스트와 달리 원소값을 직접 바꿀 수 없기 때문에, 오려붙이는 방법을 사용해야 함

p = (1,2,3)
print(p)
q = p[:1] + (5,) + p[2:]
print(q)

r = p[:1], 5, p[2:]
print(r)

# 튜플은 리스트로 리스트는 튜플로 바꾸기
p = (1,2,3)
q = list(p) #튜플을 리스트로 만듬
print(q)

r = tuple(q) # 리스트를 튜플로 만듬
print(r)