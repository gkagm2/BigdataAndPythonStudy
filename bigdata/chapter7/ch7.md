pandas.merge : 하나 이상의 키를 기준으로 DataFrame의 row를 합친다. SQL이나 다른 관계형 데이터베이스의 join연산과 유사

pandas.concat : 하나의 축을 따라 객체를 이어붙임
combine_first : 인스턴스 메서드는 두 객체를 포개서 한 객체에서 누락된 데이터를 다른 객체에 있는 값으로 채울 수 있도록 한다.

~~~~
df1 = DataFrame({'key' : ['b','b','a','c','a','a','b'], 'data1':range(7)})
df2 = DataFrame({'key' : ['a','b','d'], 'data2':range(3)})
df1
~~~~





