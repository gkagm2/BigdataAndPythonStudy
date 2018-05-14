char = list('hello')
print(char)


# string => list
words = "python은 프로그래밍을 배우기에 아주 좋은 언어입니다."
words_list = words.split()
print(words_list)

time_str = "10:34:17"
print(time_str.split(':'))


############



def Jaden_Case(s):
    # 함수를 완성하세요
    answer =[]
    for i in range(len(s.split())):
        answer.append(s.split()[i][0].upper() + s.split()[i].lower()[1:])
    return " ".join(answer)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Jaden_Case("3people unFollowed me for the last week"))