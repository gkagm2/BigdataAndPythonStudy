# 학생들의 성적을 처리하는 프로그램을 완성시켜보자. 사용자로부터 성적을 입력받아서 리스트에 저장한다.
#  성적의 평균을 구하고 80점 이상 성적을 받은 학생의 숫자를 계산하여 출력해보자.

STUDENTS = 5
scores = []
scoreSum = 0


for i in range(STUDENTS):
    value = int(input("성적을 입력하시오: "))
    scores.append(value)
    scoreSum += value

scoreAvg = scoreSum / len(scores)

highScoreStudents = 0
for i in range(len(scores)):
    if scores[i] >= 80:
        highScoreStudents += 1

print("성적 평균은 " , scoreAvg, "입니다.")
print("80점대 이상 성적을 받은 학생은", highScoreStudents, "명 입니다.")
