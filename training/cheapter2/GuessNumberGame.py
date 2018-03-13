# 사용자에게 단어 3개를 입력받아서 약자(acronym: 몇 개 단어의 머리글자로 된 말)를 만들어 보자.
# 예를 들어서  ‘OST’도 Original Sound Track의 약자이다. 이 예제는 소 스 파일로 작성하여 실행해보자.

firstWord = input("첫 번째 단어를 입력해주세요 : ")
secondWord= input("두 번째 단어를 입력해주세요 : ")
thirdWord= input("세 번째 단어를 입력해주세요 : ")

smallWord = firstWord[0] + secondWord[0] + thirdWord[0]
print(smallWord)

