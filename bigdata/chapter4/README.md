## ndarray.py
+ Ndarray
+ 같은 종류의 데이터를 저장하는 포괄적 다차원 배열
+ shape : 차원을 알려주는 튜플
+ dtype : 배열에 저장된 자료형
+ ndim : 배열의 차원

## make_ndarray.py
+ array를 이용한 생성
+ 적절한 자료형을 추정
+ np.zeros(10) : 1x10 0 배열생성
+ np.zeros((3,6)) : 3x6 0 배열생성
+ np.empty((2,3,2)) : 2x3x2 garbage 배열생성
+ np.arrange(15) : range()의 np 버전