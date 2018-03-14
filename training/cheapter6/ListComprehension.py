
list1 = [3,4,5]

# 리스트 함축
# 리스트 안에 반복문이 돌아가는 것이라고 보면 될 것 같다...

# 형태
#   출력식              변수의 범위              선택사항(조건이 참이여야 새로운 리스트에 항목이 추가됨)
# [ expression         for i in old_list          if filter(i)]

list2 = [x*2 for x in list1]

print(list2)

M = [ x for x in range(10) if x % 2 == 0]
print(M)