# 머리 글자어 만들기
# 머리 글자어는 NATO(North Atlantic Treaty Organization)처럼 각 단어의 첫 글자를 모아서 만든 문자열이다.
# 사용자가 문장을 입력하면 해당되는 머리 글자어를 출력하는 프로그램을 작성해보자.



phrase   = input("문자열을 입력하시오:")

acronym = ""

for word in phrase.upper().split():
    print(word)
    acronym += word[0]

print(acronym)
