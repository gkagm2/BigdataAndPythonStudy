

fileName = input("입력 파일 이름: ")




WordCount = 0

def process(w):
    output = ""
    for ch in w:
        if ch.isalpha() :
            output += ch
    return output.lower()

words = set()

#파일을 연다.

file = open(fileName, 'r') # read file\

# 파일의 모든 줄에 대하여 반복한다.
for line in file: ## for line in  -  각 라인을 의미
    lineWords = line.split()
    for word in lineWords:
        words.add(process(word)) # 단어를 세트에 추가한다.

print("사용된 단어의 개수 : ", len(words))
print(words)