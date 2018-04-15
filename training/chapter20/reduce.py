# reduce()의 형식은 reduce(함수, 순서형 자료)
# 순서형 자료(문자열, 리스트, 튜플)의 원소들을 누적적으로 함수에 적용시킨다.
from functools import reduce    # python3 에서는 써야 함
print(reduce(lambda x, y : x + y, [0,1,2,3,4]))

# 0과 1을 더하고 그 결과에 2를 더하고 거기에 3을 ㄱ더하고 또 4를 더한 값을 돌려준다.

# example
print(reduce(lambda x,y : y+x, 'abcde'))
# 결과는 edcba로 나옴  왜이렇게 나오지

print(reduce(lambda x,y : x+y, 'abcde'))
# 결과는 abcde로 나옴