# file example4
infile = open("file/file.txt","r", encoding="UTF-8")

for line in infile:

    line = line.rstrip() # The method rstrip() returns a copy of the string in which all chars have been stripped from the end of the string (default whitespace characters)  (Returns a copy of the string with trailing characters removed.)
    print(line)
infile.close()