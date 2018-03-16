fileName = input("파일이름 : " )

file = open(fileName, 'r')

table = dict()

count = 0
for line in file:
    words = line.split() # .split()는 단어별로 나누는 것.
    print(words)

    for word in words:
        if word not in table:
            table[word] = 1
        else :
            table[word] += 1

print(table)
