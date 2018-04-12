# numpy : boolean inex

# randn 함수를 이용하여 임의의 표준정규분포

import numpy as np

names = np.array(['Bob','Joe','Wil','Bob','Wil','Joe','Joe'])

data =  np.random.randn(7,4) # 7행 4열 짜리 배열을 random으로 만듬

print(names)
print(data)


value = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(value)
print(value[:,:2])