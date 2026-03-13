import random

while True:  # [추가] 전체 게임을 무한 반복합니다.
    print("\n" + "="*30)
    print("🍦 베스킨라빈스 31 게임 시작!")
    print("="*30)
    
    number = 0
    turn = "User"

    while number < 31:
        if turn == "User":
            # 사용자 입력
            try:
                count = int(input("\n몇 개의 숫자를 부르시겠습니까? (1~3개): "))
            except ValueError:
                print("❌ 숫자만 입력해주세요!")
                continue
            
            if count not in [1, 2, 3]:
                print("❌ 1, 2, 3 중에서만 골라주세요!")
                continue
            
            print("당신: ", end="")
            for _ in range(count):
                number += 1
                print(number, end=" ")
                if number == 31: break
            print()
            turn = "Computer"

        else:
            # 컴퓨터 입력
            print("\n컴퓨터의 차례입니다...")
            count = random.randint(1, 3)
            
            print("컴퓨터: ", end="")
            for _ in range(count):
                number += 1
                print(number, end=" ")
                if number == 31: break
            print()
            turn = "User"

    # 결과 판독
    if turn == "User":
        print("\n🎊 축하합니다! 컴퓨터가 31을 불렀습니다. 당신의 승리!")
    else:
        print("\n💀 아쉽네요! 당신이 31을 불렀습니다. 컴퓨터의 승리!")

    # [핵심] 다시 하기 물어보기
    retry = input("\n게임을 다시 하시겠습니까? (y/n): ").lower()
    if retry != 'y':
        print("게임을 종료합니다. 다음에 또 봐요! 👋")
        break  # [추가] 가장 바깥쪽 while문을 빠져나갑니다.