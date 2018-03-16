# immutable object : int, float, str, tuples etc
# mutable object : list, set, dict
# 파이썬은 argument 타입에 따라 함수변수전달 방법이 결정됨


# 값에의한 호출은
# 변하지 않음.
def modify1(s):
    s += "To you"

msg = "Happy Birthday"
print("msg = ", msg)
modify1(msg)
print("msg = ", msg)

# 참조에 의한 호출
def modify2(li):
    li += [100,200]

list = [1,2,3,4,5]
print(list)
modify2(list)
print(list)

width = 10
height = 20

