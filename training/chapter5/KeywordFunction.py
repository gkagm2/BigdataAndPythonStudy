
def calc(x, y ,z):
    print("x : ", x)
    print("y : ", y)
    print("z : ", z)
    return x + y + z

print(calc(10, 20, 30))


# 키워드 인수. 인수들이 윛가 아니고 키워드에 의하여 함수로 전달되는 방식이다.
print(calc(x =10, y = 20, z = 30))

print(calc(z = 30, x = 10, y = 20))