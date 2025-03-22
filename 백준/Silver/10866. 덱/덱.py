import sys
from collections import deque

dq = deque()
N = int(sys.stdin.readline())


for _ in range(N):
    command = list(map(str, sys.stdin.readline().split()))  # map -> list 변환

    if command[0] == 'push_front':
        dq.appendleft(command[1])
    elif command[0] == 'push_back':
        dq.append(command[1])
    elif command[0] == 'pop_front':
        if dq:
            print(dq.popleft())
        else:
            print('-1')
    elif command[0] == 'pop_back':
        if dq:
            print(dq.pop())
        else:
            print('-1')
    elif command[0] == 'size':
        print(len(dq))
    elif command[0] == 'empty':
        print(0 if dq else 1)
    elif command[0] == 'front':
        if dq:
            print(dq[0])
        else:
            print('-1')
    elif command[0] == 'back':
        if dq:
            print(dq[-1])
        else:
            print('-1')
