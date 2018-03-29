# 객체 입출력
# used pickle module

# import pickle 을 통하여 모듈 임포트가 필요하다.
# pickle 모듈을 이용하면 원하는 데이터를 자료형의 변경없이 파일로 저장하여 그대로 로드할 수 있다.
# (open(‘text.txt’, ‘w’) 방식으로 데이터를 입력하면 string 자료형으로 저장된다.)
# pickle로 데이터를 저장하거나 불러올때는 파일을 바이트형식으로 읽거나 써야한다. (wb, rb)
# wb로 데이터를 입력하는 경우는 .bin 확장자를 사용하는게 좋다.
# 모든 파이썬 데이터 객체를 저장하고 읽을 수 있다.
# pickle.load(파일) 을 통해서 파일 내용을 읽어오려면, pickle.dump를 사용해서 데이터를 입력한 파일이어야한다.
import pickle

myMovie = {"Superanem vs Batman" : 9.8, "Ironman":"9.6"}

# 딕셔너리를 피클 파일에 저장
pickle.dump(myMovie, open("file/pickleSave.p", "wb"))

# 피클 파일에 딕셔너리를 로딩
myMovie = pickle.load(open("file/pickleSave.p", "rb"))

print(myMovie)