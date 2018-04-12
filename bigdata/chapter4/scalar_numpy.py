# numpy : 배열과 스칼라 연산
import numpy as np

arr =np.array([[1.,2.,3.],[4.,5.,6.]])

print(arr)

print(arr * arr) # 배열끼리의 스칼라 연산 곱셈

print(arr - arr) # 배열끼리의 스칼라 연산 뺄셈

print( 1 / arr) # 1을 각 배열의 요소로 나눈 값

print( arr ** 0.5) # 각 요소에 0.5를 제곱

