import sys
from collections import deque


num = int(sys.stdin.readline())

dq = deque([i for i in range(1,num +1)])


while len(dq) >1:
    dq.popleft()
    move = dq.popleft()
    dq.append(move)

print(dq[0])

    