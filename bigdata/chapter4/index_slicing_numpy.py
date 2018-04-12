# 색인과 슬라이싱 기초
import numpy as np

arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("-----")
print(arr2d)
print("-----")
print(arr2d[:2]) # arr2d[0], arr2d[1]
print("-----")
print(arr2d[:2,1:]) # 0~1 1~2
print("-----")
print(arr2d[2,:1])
print("-----")
print(arr2d[:,0]) # slicing이 없으면 행을 출력해도 가로로 나옴
print("-----")
print(arr2d[:,:1]) # slicing을 해야 세로로 나옴
print("-----")
arr2d[:2,1:] = 0
print(arr2d)