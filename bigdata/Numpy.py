import numpy as np

data = [0.9526,-0.246,0.8856],[0.5639,0.2379,0.9104]
#data = np.array(data)
print(data)

# np.array(data)를 하므로 안에 있는 값이 곱해진다. 이걸 하지 않으면 리스트를 10개를 만들어낸다.
print(data * 10)

# 리스트 안에 있는 리스트들의 요소 값 끼리 더한다. np.array(data)를 하지 않으면 리스트를 이어 붙일 뿐이다.
print(data + data)

