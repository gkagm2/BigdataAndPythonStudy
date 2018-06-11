# from __future__ import division  # python 2에서 3에서 사용될 / 연산자의 사용법을 미리 사용
from numpy.random import randn
import numpy as np
import matplotlib.pyplot as plt
# plt.rc('figure', figsize=(10, 6))
np.random.seed(12345)
from pandas import Series, DataFrame
import pandas as pd
np.set_printoptions(precision=4, threshold=500)
pd.options.display.max_rows = 100


# random.seed(120)

df = pd.read_csv('file.csv', encoding="utf-8")

from datetime import datetime #datetime을 사용하기 위하여

dff = abs(pd.to_datetime(df['교육시작일자'])-pd.to_datetime(df['교육종료일자'])) #시작일자에서 종료일자를 뺀다. 그럼 얼마나 했는지 알 수 있다.
dff2 = dff.value_counts().sort_values().tail(10)

print(dff2)

# print(dff2.plot())