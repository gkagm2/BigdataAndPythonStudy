new_list = [(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2 + y**2 == z**2]

print(new_list)

#거꾸로 정렬도 해보기.
print (len(new_list))




