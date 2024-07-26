import random

print("동전게임을 시작합니다.\n")
do = True
while do:
    menu = """
    0. 앞
    1. 뒤
    """
    print(menu)


    num = int(input("앞, 뒤를 선택하세요 (0, 1) : "))

    computer = random.randint(0, 1)

    if computer:
        print("컴퓨터는 뒷면입니다.")
    else:
        print("컴퓨터는 앞면입니다.")

    print()

    if num:
        print("당신의 선택은 뒷면입니다.")
    else:
        print("당신의 선택은 앞면입니다.")

    print()

    if computer == num:
        print("당신이 이겼습니다.")
    else:
        print("애석합니다. 당신이 틀렸습니다.")

        print()
    
    stop_go = input("게임을 계속하시겠습니다? (y/n) : ")

    if stop_go == "n":
        do = False
