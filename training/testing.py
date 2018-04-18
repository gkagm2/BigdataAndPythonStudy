
def no_continuous(s):
    # 함수를 완성하세요
    list = []
    listIndex= 0

    list.append(s[0])

    # for i in range(1, len(s)):
    #     print(i)
    for i in range(1, len(s)):
        if s[i] != list[listIndex]:
            list.append(s[i])
            listIndex += 1



    return list

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( no_continuous( "133303" ))
print( no_continuous( "47330" ))
# def alpha_string46(s):
#     # 함수를 완성하세요
#
#     number = (1,2,3,4,5,6,7,8,9,0)
#     count =0
#     for i in s:
#         try:
#             int(i)
#             count += 1
#         except Exception as e:
#             return False
#     if count % 4 == 0 or count % 6 == 0:
#         return True
#     else:
#         return False


# 아래는 테스트로 출력해 보기 위한 코드입니다.
# print(alpha_string46("2s34"))
# print(alpha_string46("a234"))
# print(alpha_string46("24579834"))
# print(alpha_string46("11828"))



# def longest_palindrom3(s):
#     list_s = list(s)
#     if list_s == list_s[::-1]:
#         return len(list_s)
#
#     result = []
#     for idx, item in enumerate(list_s):
#         if item in list_s[idx+1:]:
#             idx2 = idx + list_s[idx+1:].index(item) + 2
#
#             if list_s[idx:idx2] == (list_s[idx:idx2])[::-1]:
#                 result.append(len(list_s[idx:idx2]))
#
#     if len(result) == 0:
#         return 1
#     return max(result)
#
#
#
# def longest_palindrom(s):
#     # 함수를 완성하세요
#     answer = []
#     for j in range(len(s)) :
#         for i in range(len(s)):
#             a = s[j:i+1]
#             r = a[::-1]
#             if a == r :
#                 #print("a is %s r is %s" % (a, r))
#                 answer.append(i+1-j)
#     return max(answer)
#
#
# # 아래는 테스트로 출력해 보기 위한 코드입니다.
# for i in range(100):
#     print("first :", longest_palindrom("토마토맛토마토"))
#     print("two :", longest_palindrom("토마토는맛있어"))
#     print("three :", longest_palindrom("토있냐있냐고가나다라다나가"))
#     print("four :", longest_palindrom("zzbaabcd"))
#     print("five :", longest_palindrom("asdfvefe"))
#     print("six :", longest_palindrom("abbsddfdd"))
#     print("seven :", longest_palindrom("abbsddfddqkqerivjerqjvjklfdjkldjfklasdj;fsklfsdlfsjkfjdwqiopqfwjiopfjweiopfjweiofjiojfoasdjgjklvnerjknovneroakngvoernognowerjgiowernvioevnwiovnfiovenwionvioeniovnioervneiornvioefnkognkvernkovnekovwnerkognkwnerkobnkodfnbnwortnhkownrkbornbkortnkbortnwbkwdfnblwrtnbiodfnbpwinrthbn"))

# for i in range(100):
#     print("first :", longest_palindrom2("토마토맛토마토"))
#     print("two :", longest_palindrom2("토마토는맛있어"))
#     print("three :", longest_palindrom2("토있냐있냐고가나다라다나가"))
#     print("four :", longest_palindrom2("zzbaabcd"))
#     print("five :", longest_palindrom2("asdfvefe"))
#     print("six :", longest_palindrom2("abbsddfdd"))
#     print("seven :", longest_palindrom2("abbsddfddqkqerivjerqjvjklfdjkldjfklasdj;fsklfsdlfsjkfjdwqiopqfwjiopfjweiopfjweiofjiojfoasdjgjklvnerjknovneroakngvoernognowerjgiowernvioevnwiovnfiovenwionvioeniovnioervneiornvioefnkognkvernkovnekovwnerkognkwnerkobnkodfnbnwortnhkownrkbornbkortnkbortnwbkwdfnblwrtnbiodfnbpwinrthbn"))



# def numPY(s):
#     # 함수를 완성하세요
#     # print(s)
#     # y_count = 0
#     # p_count = 0
#     #
#     # for i in s:
#     #     if i.upper() == 'Y':
#     #         y_count += 1
#     #     elif i.upper() == 'P':
#     #         p_count += 1
#     #
#     # if y_count == p_count:
#     #     return True
#     # else:
#     #     return False
#     print(s.lower().count('p'))
#     return s.lower().count('p') == s.lower().count('y')

# 아래는 테스트로 출력해 보기 위한 코드입니다.
# print( numPY("pPoooyY") )
# print( numPY("Pyy") )


# def average(array):
#     # 함수를 완성해서 매개변수 array의 평균값을 return하도록 만들어 보세요.
#     sum = reduce(lambda x, y: x + y, array)
#     return sum / len(array)
#
# # 아래는 테스트로 출력해 보기 위한 코드입니다.
# list = [5,3,4]
# print("평균값 : {}".format(average(list)));



# def number_generator(x, n):
#     # 함수를 완성하세요
#     list = []
#     for i in range(n):
#         list.append(x * (i+1))
#     return list

# 아래는 테스트로 출력해 보기 위한 코드입니다.
# number_generator(3,5)
# print(number_generator(3,5))
# print(number_generator(3,5))


# print(list(map(lambda x: x**2, range(5)))) # python3 or 2 version
# map함수는 리스트에서 원소를 하나씩 꺼내서 함수를 적용시킨 결과를 새로운 리스트에 담아주니까 위의 예제는 0을 제곱하고 1을 제곱하고
# 2,3,4를 제곱한 것을 새로운 리스트에 넣어주는 것이다.

# def hide_numbers(s):
#     #함수를 완성
#
#     numberLength = len(s) - 4
#     encoding_num = "*" * numberLength
#     encoding_num += s[-4:]
#     print(encoding_num)
#     if len(s) != 11:
#         print("error")
#     else:
#         for i in range(7):
#             print(s[i])
#     return s
#
# # 아래는 테스트로 출력해 보기 위한 코드입니다.
# print("결과 : " + hide_numbers('0212345678'));

# fiboList  = {0:0, 1:1}
#
# def fibm(n):
#     if not n in fiboList:
#         fiboList[n] = fibm(n-1) + fibm(n-2)
#         print(fiboList)
#     return fiboList[n]
# n = int(input("정수를 입력하시오:"))
#
# print(fiboList)
# print(n, "번째 피보나치 수는  ", fibm(n))
