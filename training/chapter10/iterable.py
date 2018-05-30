# iterable object
# 파이썬에서는 for 루프와 함께 사용할 수 있는 여러 종류의 객체가 있으며 이들 객체는 이터러블 객체(iterable object)이라고 불린다.

# __iter__() 은 이터러블 객체 자신을 반환한다.
# __next__() 은 다음 반복을 위한 값을 반환한다. 만약 더 이상의 값이 없으면 StopIteration 예외를 발생하면 된다.

class MyCounter(object):
    #생성자 메소드를 정의한다.
    def __init__(self, low, high):
        self.current = low
        self.high = high

    # 이터레이터 객체로서 자신을 반환한다.
    def __iter__(self):
        return self

    def __next__(self): # 다음
        #current가 high보다 크면 StopIteration 예외를 발생한다.
        #current가 high보다 작으면 다음 값을 반환한다.
        if self.current > self.high:
            raise StopIteration # stopIteration이라는 예외임
        else:
            self.current += 1
            return self.current -1

c = MyCounter(1,10)
for i in c:
    print(i, end=' ')