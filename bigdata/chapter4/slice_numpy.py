import numpy as np


arr = np.arange(10) # 0~9 까지의 데이터를 배열에 넣는다.
print(arr)

print(arr[5]) # 해당 index의 데이터 값을 얻는다.

print(arr[5:8]) # slic  e를 이용하여 5 ,6 ,7 의 데이터 값을 얻는다.
arr[5:8] = 12 # 5~7번째 index의 배열에 12를 대입.
print(arr)

arr_slice = arr[5:8] # 부분적으로 떼옴
print(arr_slice)

arr_slice[1] = 12345 # 부분적으로 떼온 곳에 바꿨는데
print(arr_slice) # 복사가 아니라 원본에 그대로 반영하여

print(arr) # arr 배열에도 바꿔어있다.

arr_slice[:] = 64 # 5,6,7index를 64로 바꾸면
print(arr_slice) # 복사가 아니라 원본에 그대로 반영하므로

print(arr) # arr 배열에도 64로 바뀌어있음.


arr2_slice = arr[5:8].copy() #복사하고 싶으면 .copy()를 이용해야 함.
arr2_slice[:] = 999 #slice부분을 999로 바꿈
print(arr2_slice) # 슬라이스부분은 바꿔었지만
print(arr) # .copy()를 사용하여 복사 했기 때문에 원본은 바뀌지 않았다.



