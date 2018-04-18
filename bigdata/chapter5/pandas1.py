
from pandas import Series, DataFrame
import pandas as pd

from __future__ import division

from numpy.random import randn
import numpy as np
import os
import matplotlib.pyplot as plt

np.random.seed(12345)
plt.rc('figure', figsize=(10, 6))
np.set_printoptions(precision=4)

obj = Series([4, 7, -5, 3])
print(obj)

