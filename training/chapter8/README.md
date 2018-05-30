+ python instance method 와 class method의 차이점

~~~~
method 입력인자로 cls와 self가 들어가는 것을 본적이 있을 것이다.
이 둘을 구분 짓는 것은 "PEP8"에서 정의된 Instance method와 Class method의 차이에 따라 경우를 나누어 쓴다.
Instance Method의 정의는 클래스 내부에 정의되어 있는 함수를 호출할 때, Instance(객체)를 필요로 한다는 조건이 있는 것을 알 수있다.
이때 첫번째 매개변수는 항상 self이며 self이외에 다른 변수를 사용하는 것은 naming convention에 어긋나는 일이다.

~~~~
