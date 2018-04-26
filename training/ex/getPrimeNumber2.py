# https://github.com/tkZzang 도움받음
# 클래스의 객체를 이터레이터로 쓰기

class MyPrime(object):
    # 세트는 중복되지 않은 항목들이 모인것이며 항목간에 순서가 없다
    # 순서가 없으므로 인덱싱을 할 수 없다
    primeSet = set()

    # 클래스변수 초기화
    def __init__(self, high):
        self.current = 2
        self.high = high

    # 이터레이터 객체로서 자신을 반환한다.
    def __iter__(self):
        return self

    # 다음 인덱스를 가리키는 객체
    def __next__(self):
        while True:
            if self.current not in self.primeSet:
                # 세트에 들어가는 값들은 소수가 아닌 값이다 (참고 : 13장 에라스토스의 체)
                self.primeSet.update(range(self.current**2, self.high + 1, self.current))
                break
            self.current += 1

        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

# ~ n 범위의 소수를 얻겠다!
c = MyPrime(10)
sum = 0

for i in c:
    sum += i
    print(i,end=" ")
print()

print(f'합계 : {sum}')
print('합계 : {}'.format(sum))
print('합계 :',sum)
print('합계 : %d'%sum)
print('합계 : '+str(sum))
