import numpy as np

arr = np.array([1,2,3,4,5])

print(arr.dtype) # int32로 나온다.

float_arr = arr.astype(np.float64) # int32를 float64로 변환

print(float_arr)
print(float_arr.dtype) # float64로 나온다.


arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
print(arr)

arr = arr.astype(np.int32) #반내림으로 float64를 int32로 변환
print(arr)

numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_) # string_은 뭐지?
print(numeric_strings)
print(numeric_strings.astype(float))

int_array = np.arange(10) # 0에서부터 9까지 만듬
print(int_array)

calibers = np.array([.22, .270, .357, .380, .44, .50], dtype=np.float64)
print(calibers)
print(int_array.astype(calibers.dtype)) # calibers의 data type으로 int_array의 타입을 바꾸어라

empty_uint32 = np.empty(8, dtype='u4') # 부호가 없는 32비트 정수형: u4 를 8개 생성
print(empty_uint32)



