# ndarray 생성

import numpy as np

data2 = [[1,2,3,4],[5,6,7,8]]
arr2 = np.array(data2)
print(arr2)


print(arr2.ndim , "차원 입니다.") # 배열의 차원을 return

print(arr2.shape) # 차원을 알려주는 튜플 (2, 4)면 2행 4열

print(arr2.dtype)

print(np.empty((2,3,4))) # 2개의 3행 4열짜리 gabage 배열을 생성한다.
print(np.zeros((3,6))) # 3행 6열에 0으로 초기화된 배열 생성
print(np.zeros(10)) # 1행 10열에 0으로 초기화된 배열 생성

