# Numpy ndaaray 다차원 배열 객체

import numpy as np
data = [0.9526, -0.246, -0.8856],[0.5639, 0.2379, 0.9104]
data = np.array(data) # 배열 객체를 만듬.
print(type(data)) # type is class 'numpy.ndarray'

print(data)

data2 = data * 10
print(data2) # 각 요소들에게 10씩 곱한다.

data3 = data + data # 각 요소들끼리 같은 값을 더한다.
print(data3)


print(data.shape) # type is tuple

print(data.dtype) # float64 -> 64bit float


data1 = [6, 7.5, 8, 0, 1] #하나라도 float형이 있으면 float형으로 됨
print(data1)
arr1 = np.array(data1)
print(arr1) # array([6, 7.5, 8, 0, 1])

