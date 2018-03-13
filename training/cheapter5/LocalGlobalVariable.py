def sub():
    s = "바나나가 좋음!" # 전역변수를 사용하는 것이 아님!
    print(s)

s = "사과가 좋음!"
print(s)
sub()

######
print()
######

def sub2():
    global s # 이것 없으면 ,referenced before assignment error 발생
    print(s)
    s = "바나나가 좋음!!"
    print(s)

s = "사과가 좋음!!"
sub2()
print(s)


######
print()
######

## example

def sub3(x, y):
    global a

    a = 7
    x,y = y,x  # x와 y를 바꾼다.
    b = 3
    print(a,b,x,y)

a,b,x,y = 1,2,3,4
sub3(x,y)
print(a,b,x,y)