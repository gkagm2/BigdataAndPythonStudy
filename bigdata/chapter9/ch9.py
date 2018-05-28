from __future__ import division
import numpy as np
from pandas import Series, DataFrame
np.set_printoptions(precision=4)

np.random.seed(12345)

df = DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],
                'key2' : ['one', 'two', 'one', 'two', 'one'],
                'data1' : np.random.randn(5),
                'data2' : np.random.randn(5)})
print(df)

grouped = df['data1'].groupby(df['key1'])
print(grouped)


print(grouped.mean)