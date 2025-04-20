import sys
from collections import deque

num = int(sys.stdin.readline())
input = sys.stdin.readline

for _ in range(num):
    n,m = list(map(int,input().split()))
    q = deque(map(int,input().split()))
    idx = deque(range(0,n)) # 각 인덱스의 위치를 저장

    cnt = 0 # 몇번째로 인쇄되는지 카운트

    while True:
        if q[0] == max(q): # q의 첫번째 원소가 최대값이면
            cnt += 1
            if idx[0] == m:
                print(cnt)
                break
            else:
                q.popleft() # q의 첫번째 원소를 pop
                idx.popleft() # idx의 첫번째 원소를 pop
        else:

            # 중요도가 낮을 경우 뒤로 보낸다
            q.append(q.popleft())   # q의 첫번째 원소를 맨 뒤로 보냄
            idx.append(idx.popleft()) # idx의 첫번째 원소를 맨 뒤로 보냄
            
