new_list = [(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2 + y**2 == z**2]

print(new_list)


###### 이런식으로 가능

new_list = []
for x in range(1,30):
    for y in range(x, 30):
        for z in range(y, 30):
            if x**2 + y**2 == z**2:
                new_list.append((x,y,z))

print(new_list)



#거꾸로 정렬도 해보기.
new_list.reverse() # .reverse()를 사용하면 리스트들이 반대로 정렬 됨. 
print(new_list)


