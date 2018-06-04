# random module

import random

print(random.randint(1,6))

print(random.random() * 100)


myList = ["red", "blue", "green"]

print(random.choice(myList))



myList = [ [x] for x in range(10)]
print(random.shuffle(myList)) # 리스트의 값들을 랜덤으로 섞어준다.

print(myList)

for i in range(3):
    print(random.randrange(0, 101, 3)) # 0부터 101 까지 3개의 랜덤 수를 뽑아라