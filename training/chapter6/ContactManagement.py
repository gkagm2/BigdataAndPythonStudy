menu = 0


list = []

def MenuExplain():
    print("1. 친구 리스트 출력")
    print("2. 친구추가")
    print("3. 친구삭제")
    print("4. 이름변경")
    print("9. 종료")

def PrintFriendsList(list): # 친구 리스트 출력
    for l in list:
        print(l, end=", ")
    print("")

while menu != 9:
    MenuExplain()
    menu = int(input("메뉴를 선택하시오: "))

    if menu == 1:
        PrintFriendsList(list)
    elif menu == 2:
        name = input("이름을 입력하시오: ")
        list.append(name)
    elif menu == 3:
        deleteName = input("삭제하고 싶은 이름을 입력하시오: ")
        if deleteName in list:
            list.remove(deleteName)
        else :
            print("이름이 발견되지 않았음")
    elif menu == 4:
        old_name = input("변경하고 싶은 이름을 입력하시오: ")
        if old_name in list:
            index = list.index(old_name)
            new_name = input("새로운 이름을 입력하시오: ")
            list[index] = new_name
        else :
            print("이름이 발견되지 않았음")



