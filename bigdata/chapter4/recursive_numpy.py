# 재귀적 접근

import numpy as np

arr2d = np.array([[11,22,33],[44,55,66],[77,88,99]])
print(arr2d)
print(arr2d[2])
print(arr2d[0][2])
print(arr2d[0,2])

print('------')

arr3d = np.array([[[1,2,3],[4,5,6]] , [[7,8,9],[10,11,12]]])
print(arr3d)
print('------')
print(arr3d[1])

print('------')
print(arr3d[0][0][1]) # 첫번째 배열에서 1행 2열을 찾는다.
print('------')
print(arr3d[1][1][2]) # 두번째 배열에서 2행 3열을 찾는다.

print('------------')

old_values = arr3d[0].copy()

print(old_values)

arr3d[0] = 42

print(arr3d[0])

arr3d[0] = old_values

print(arr3d[0])