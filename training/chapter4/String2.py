#문자열을 받아서 모음을 전부 없애는 코드.
s = input("문자열을 입력하시오")

vowels = "aeiouAEIOU"

result = ""
for letter in s:
    if letter not in vowels:
        result += letter

print(result)