# 팬시 색인

import numpy as np

arr = np.empty((8,4))

for i in range(8):
    arr[i] = i

print(arr)

print('--------------')
print(arr[[4,3,0,6]])

print('--------------')
print(arr[[-3,-5,-7]])

print('--------------')
arr = np.arange(32).reshape((8,4)) # 0부터 31까지 배열에 넣는데 8행 4열로 넣는다.
print(arr)

print('--------------')
print(arr[[1,5,7,2],[0,3,1,2]])

print('--------------') # np.ix_ 함수 : 1차원 정수 배열 2개를 사각형 영역에서 index로 변환
print(arr[np.ix_([1,5,7,2],[0,3,1,2])])

print('--------------')







