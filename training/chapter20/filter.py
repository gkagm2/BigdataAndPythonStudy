# filter(함수, 리스트) 형태로 되어있다.
# 리스트에 들어있는 원소들을 함수에 적용시켜서 결과가 참인 값들로 새로운 리스트를 만들어준다.
print(filter(lambda x: x < 5, range(10))) #python2

print(list(filter(lambda x: x < 5, range(10)))) # python3, python2

# 0부터 9까지의 리스트에서 숫자를 하나씩 꺼낸다. 그 숫자를 x라고 하고, x<5가 '참'이면 살려준다.
# 살아남은 것들은 새로운 리스트에 넣어준다. 끝

# 홀수만 들려주는 filter example
print(list(filter(lambda x: x % 2, range(10)))) #python3, python2
# 숫자 % 2로 나눠서 0이 아니면 참            결과값이 0이 나오면 false로 인식, 나머진 true

