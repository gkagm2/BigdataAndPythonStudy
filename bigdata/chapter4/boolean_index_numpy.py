# numpy : boolean inex

# randn 함수를 이용하여 임의의 표준정규분포

import numpy as np

names = np.array(['Bob','Joe','Wil','Bob','Wil','Joe','Joe'])

data =  np.random.randn(7,4) # 7행 4열 짜리 배열을 random으로 만듬

print(names)
print(data)


print(names == 'Bob')

print(data[names == 'Bob',2:]) # 이렇게도 된다.

print(data[names == 'Bob', 3])

print(names != 'Bob') # 'Bob'이 아닌 요소를 선택하려면 != 연산자를 사용하거나 -를 사용해서 조건 절을 부정하면 된다.

print(data[(names == 'Bob')])

data[names != 'Joe'] = 7
print(data)