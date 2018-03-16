name = input("이름이 무엇인가요?")

print("만나서 반갑습니다. " + name + "씨!")
print("만나서 반갑습니다. " ,name , "씨!")

age = input("나이는요?")

print("네, 그러면 당신은 이미 " + age + " 살이시군요 " + name + "씨!")



x = input("첫 번째 정수: ")
y = input("두 번째 정수: ")
sum = x + y #문자열로 간주하여 서로 합침!
print("합은 " ,sum)

x = int(input("첫 번째 정수: ")) # 입력받을 때 int()로 형변환하여 x에 저장하여 integer형으로 간주함.
y = int(input("두 번째 정수: "))
sum = x + y
print("합은 " ,sum)
