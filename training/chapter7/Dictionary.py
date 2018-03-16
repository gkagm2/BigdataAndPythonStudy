# 딕셔너리는 key와 value의 쌍을 저장할 수 있는 객체

contact = {"kil" : "01011111111" ,'ja':'22122','dsf':"asdf","efdd":'2222'}

print(contact)

# 항목 접근

contacts = { 'kim':'01012345678', 'park':'010987654321'}

print(contacts['kim'])

print(contacts.get('kim'))

if 'park' in contacts:
    print("키가 딕셔너리에 있음")

# 항목 추가 & 삭제하기

contacts['Choi'] = '01099992222'  # 항목 추가

print(contacts)
contacts.pop("kim") # 항목 삭제

print(contacts)

# 항목 순회하기

scores = { 'Korean':80, 'Math':90, 'English':80}

for item in scores.items(): # .item()을 사용하면 됨.
    print(item)

