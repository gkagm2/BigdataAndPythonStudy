# re module은 (regular expression : 정규 표현식) string module보다 더 전문적으로 문자열을 다룰 수 있다.

# 마침표(.)는 문자 아무거나 한 개를 뜻함
# 별표(*)는 한 개 이상의 문자를 뜻함

import re, glob

# 현재 디렉토리에서 p 다음에 n이 나오는 이름을 갖고 있는 파일들을 모두 찾아주게 되지요
p = re.compile('.*r.*m.*')
for i in glob.glob('*'):
    m = p.match(i)

    if m:
        print(m.group())