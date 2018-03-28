# file example3
infile = open("file/file.txt","r", encoding="UTF-8")
line = infile.readline() # raad first line

while line != "": ## if not the end of line
    print(line)
    line = infile.readline()
infile.close()

