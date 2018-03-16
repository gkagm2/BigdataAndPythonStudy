print("숫자 게임에 오신것을 환영합니다")
number = 62
guess = input("1부터 100 사이의 숫자를 추측해보세요 : ")
guess = int(guess)
if guess == 62:
    print("맞았습니다.")
else:
    print("틀렸습니다.")

print("게임이 종료되었습니다.")
