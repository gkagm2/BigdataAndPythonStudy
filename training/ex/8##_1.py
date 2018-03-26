
def isPrime(v):
    if v == 2:
        return True  #소수
    for x in range(2, v):
        if v % x == 0:
            break
        elif x == v - 1:
            return True
    return False

value = int(input("최대값을 입력하시오"))


def getFib(value):
    list = []
    a , b = 0, 1
    while a <= value:
        list.append(a)
        a, b = b, a+b
    print()
    return list

list = []

list = getFib(value)
print(list)
list1 = []
for l in list:
    if isPrime(l) == True:
        list1.append(l)

print(max(list1))
