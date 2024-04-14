#가위바위보 게임
#난수 생성
import random

player = input("(가위, 바위, 보) 중에서 하나를 선택하세요: ")

#정수 난수 0,1,2 중에 1개 생성
number = random.randint(0,2)
if number == 0:
    computer = "가위"

elif number == 1:
    computer = "바위"

elif number == 2:
    computer = "보"

print("사용자: ", player, "컴퓨터: ", computer)

if player == computer:
    print("비겼다!")

elif (player == "바위"):
    if(computer == "보"):
        print("컴퓨터가 이겼다!")

    else:
        print("사용자가 이겼다!")

elif (player == "가위"):
    if(computer == "바위"):
        print("컴퓨터가 이겼다!")

    else:
        print("사용자가 이겼다!")

elif (player == "보"):
    if(computer == "가위"):
        print("컴퓨터가 이겼다!")

    else:
        print("사용자가 이겼다!")
