# 주사위 굴리기

from random import *

count = 0
bonus_number= 0
while True:
    ask = input("주사위 게임을 하시겠습니까? [Yes / No]")
    if ask == "Yes":
        first = randint(1,6)
        print("숫자: {}".format(first))
        count += 1
        print("던진 횟수: {}".format(count))
        if first == 6:
            bonus = input("6이 나왔습니다! 한 번 더 던지시겠습니까? [Yes / No]")
            if bonus == "Yes":
                count += 1
                print("던진 횟수: {}".format(count))
                bonus_number += 1                       # 함수명 겹치지 않게 잘 보자
                print("보너스 횟수: {}".format(bonus_number))
            else:
                print("아쉽군요...")
                print("던진 횟수: {}".format(count))
    elif ask == "No":
        print("주사위 게임을 종료합니다.")
        print("던진 횟수: {}".format(count))
        break
    else: 
        print("잘못된 입력: Yes / No 로 입력해주세요")
        continue                                        # 추가

# true 아니다. True 로 대문자로 써줘야 한다!
# continue: 잘못된 입력을 하더라도 게임 계속 할 수 있게 해준다자
# bonus_number: bonus로 하면 if 함수내에 bonus 와 겹쳐서 오류난다.