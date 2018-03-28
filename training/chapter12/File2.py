# file example2

infile = open("file/file.txt","r", encoding="UTF-8")
s = infile.readline() # read in one line
print(s)
s = infile.readline()
print(s)
s = infile.readline()
print(s)

infile.close()