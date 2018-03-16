# 동적으로 2차원 리스트를 생성한다.

rows = 3
cols = 5

s = []

for row in range(rows):
    s += [ [0]*cols] #리스트 요소값은 0 이고 cols만큼 만든다.  그것을 row개수만큼 반복하여 만든다.

print("s = " , s)