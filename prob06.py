# 문제6
# 숨겨진 카드의 수를 맞추는 게임입니다. 1-100까지의 임의의 수를 가진 카드를 한 장 숨기고 이 카드의 수를 맞추는 게임입니다.
# 아래의 화면과 같이 카드 속의 수가 57인 경우를 보면 수를 맞추는 사람이 40이라고 입력하면 "더 높게",
# 다시 75이라고 입력하면 "더 낮게" 라는 식으로 범위를 좁혀가며 수를 맞추고 있습니다. 게임을 반복하기 위해 y/n이라고 묻고 n인 경우 종료됩니다.
import random

mins, maxs = 1, 100

while True:
    number = random.randrange(maxs) + mins
    print('수를 결정하였습니다. 맞추어 보세요')
    cnt = 1
    answer = -1
    a_mins, a_maxs = mins, maxs
    while number != answer:
        print(a_mins, '-', a_maxs)
        answer = input(str(cnt)+'>>')

        if answer.isdigit() is False:
            print('숫자를 입력해 주세요')
            continue
        answer = int(answer)

        if answer < number:
            print('더 높게')
            if answer > a_mins:
                a_mins = answer
        elif answer > number:
            print('더 낮게')
            if answer < a_maxs:
                a_maxs = answer
        cnt += 1
    print('맞았습니다.')
    if 'y' != input('다시 하시겠습니까(y/n)>>'):
        break
