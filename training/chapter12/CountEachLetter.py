# 각 문자 횟수 세기
# 파일 안의 각 문자들이 몇 번이나 나타나는지를 세는 프로그램


filename = open("file/file.txt","r", encoding='utf-8')

freqs = {}

for line in filename:

    for char in line:
        print(char)
        if char in freqs:
            freqs[char] += 1
        else :
            freqs[char] = 1

print(freqs)
filename.close()