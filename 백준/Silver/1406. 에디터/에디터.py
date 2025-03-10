import sys
stk_L = list(sys.stdin.readline().strip())  # 입력 받을 때 개행 문자 제거
stk_R = []

number = int(sys.stdin.readline().strip())  # 개행 문자 제거

for i in range(number):
    command = sys.stdin.readline().strip().split()  # 명령어 입력 받기

    if command[0] == 'L' and stk_L:
        stk_R.append(stk_L.pop())
    elif command[0] == 'D' and stk_R:
        stk_L.append(stk_R.pop())
    elif command[0] == 'B' and stk_L:
        stk_L.pop()
    elif command[0] == 'P':
        stk_L.append(command[1])

# stk_R을 역순으로 합쳐야 정확한 결과가 나옴
addter = stk_L + stk_R[::-1]
print(''.join(addter))
