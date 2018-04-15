### Pandas

대표적인 자료구조 형식
+ Series
- 1차원 객체 배열 같은 자료 구조
- index 라고 하는 데이터에   연관된 이름 소유 -> 사전 자료형과 유사

+ DataFrame
- 스프레드시트 형식의 자료 구조
- 각 칼럼은 서로 다른 종류의 값 저장기능
- 각각의 로우와 컬럼에 대한 index가 존재
- 고차원의 표 형식으로 데이터를 표현 가능
- 색인의 모양이 같은 Series 객체를 담고있는 사전으로 생각
- 내부처리 : 2차원 배열로 저장

- NumPy 자료형 모두 저장 가능

+ Import
- from pandas import Series, DataFrame
- from pandas as pd
- from numpy as np
