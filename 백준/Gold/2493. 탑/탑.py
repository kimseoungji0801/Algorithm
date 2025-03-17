import sys

num = int(sys.stdin.readline())

tower = list(map(int,input().split()))
answer = [0] * num
stk = []

# 가장 먼저 만나는 큰 탑이 수신이 가능해짐

for i in range(len(tower)):
    while stk:
        if tower[stk[-1][0]] < tower[i]:
            stk.pop()
        else:
            answer[i] = stk[-1][0] + 1
            break
    stk.append((i,tower[i]))
print(* answer)

