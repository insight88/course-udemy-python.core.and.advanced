import random
print('guess number game!')

choice = random.randrange(100)

while True:
    user_choice = int(input('100보다 작은 숫자를 입력'))
    if choice == user_choice:
        break
    if choice < user_choice:
        print('값이 큽니다')
    else:
        print('값이 작습니다')

print('정답! 프로그램 종료')
