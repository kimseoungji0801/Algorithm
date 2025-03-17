import sys

number = int(sys.stdin.readline())  # 반복될 횟수
bigger = list(map(int, sys.stdin.readline().split()))  # N 개의 정수형 리스트로 입력받음

stk = []
res = [-1] * number  # 결과 값을 -1로 number 수만큼 초기화

for i in range(number):
    while stk and bigger[stk[-1]] < bigger[i]:
        # 스택이 비어있지 않고 / 현재 숫자가 맨 위에 값보다 크다면
        res[stk.pop()] = bigger[i]
        # -1에 값을 삭제하고 bigger[i]값으로 변경 시킴
    stk.append(i)
    # i 값을 stk에 추가
print(*res)