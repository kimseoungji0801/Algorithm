import sys
from collections import deque

N = int(sys.stdin.readline())
arr = deque([])

for i in range(N):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "push":
        arr.insert(0, cmd[1])
    
    elif cmd[0] == "pop":
        if len(arr) != 0:
            print(arr.pop())
        else:
            print(-1)
    
    elif cmd[0] == "size":
        print(len(arr))
    
    elif cmd[0] == "empty":
        if len(arr) == 0: 
            print(1)
        else: 
            print(0)
    
    elif cmd[0] == "front":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])
    
    elif cmd[0] == "back":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[0])