# os module은 os를 제어할 수 있음. 우리가 Windows로 파일과 폴더를 만들고 복사하는 일들도 os 모듈로 할 수 있음

import os
print(os.getcwd())

print(os.listdir('N:\python(bigdata)'))

os.rename('read2.txt','read.txt') # readme.md파일을 readme2.md파일로  바꾸기


