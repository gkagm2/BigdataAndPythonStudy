# 제너레이터(generators)는 키워드 yield를 사용하여서 함수로부터 이터레이터를 생성하는 하나의 방법이다.
# 모든 값을 메모리에 담고 있지 않고 그때그때 값을 생성(generator)해서 반환하기 때문에 제너레이터를 사용할 때에는
# 한 번에 한 개의 값만 순환(iterate)할 수 있다.

# yield : 넘겨주다. 양도하다.

def myGenerator():
    yield 'first'
    yield 'second'
    yield 'third'


for word in myGenerator():
    print(word)

