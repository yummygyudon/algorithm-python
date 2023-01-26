import sys
input = sys.stdin.readline

N, K =  map(int, input().split())

counting = [0]*100001
limit = 100000

from collections import deque
q = deque()
q.append(N)

while q:
    now= q.popleft()
    if now == K :
        print(counting[now])
        break
    if 0 <= now-1 <= limit and counting[now-1] == 0:
        counting[now-1] = counting[now]+1
        q.append(now-1)
    if 0 <= now+1 <= limit and counting[now+1] == 0 :
        counting[now+1] = counting[now]+1
        q.append(now+1)
    if 0 <= now*2 <= limit and counting[now*2] == 0 :
        counting[now*2] = counting[now]+1
        q.append(now*2)