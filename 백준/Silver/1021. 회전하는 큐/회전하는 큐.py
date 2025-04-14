import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split()) 

result = list(map(int,input().split()))

q = deque([i for i in range(1,n+1)])

count = 0

for res in result:
    while 1:
        if q[0] == res:
            q.popleft()
            break
        else:
            if q.index(res) <= len(q)//2:
                q.rotate(-1)
                count +=1
            else:
                q.rotate(1)
                count +=1
print(count)