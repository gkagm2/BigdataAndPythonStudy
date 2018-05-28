#소수(prime number)를 산출하는 클래스 myPrime를 상속 없이 만들고, 다움 for문에서 활용하여 입력된 최대 범위 내의
#소수 리스트와 합계를 출력하는 프로그램을 완성하라

class MyPrime():

    def getCount(self,n):
        self.__count = n

    def eratosthenes():
        multiples = set()
        for i in range(2, n+1):
            if i not in multiples:
                yield i
                multiples.update(range(i*i, n+1, i))

prime = MyPrime()

sum = 0


n = int(input("enter upper limit:"))

for a in prime.eratosthenes(n):
    print(a,end=" ")
    sum += a

print()
print("sum : ",sum)

