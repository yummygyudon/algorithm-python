import sys
input = sys.stdin.readline

H, W, Square = map(int,input().split())
m = [[0]*W for _ in range(H)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

from collections import deque
def bfs(y, x) :
    q = deque()
    q.append([y,x])
    cnt = 1
    while q:
        y, x = q.popleft()
        for i in range(4) :
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < H and 0 <= nx < W and m[ny][nx] == 0 :
                m[ny][nx] = 1
                q.append([ny,nx])
                cnt += 1
    return cnt

result = []
for _ in range(Square) :
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2) :
        for k in range(y1, y2):
            m[k][i] = 1

for i in range(H):
    for k in range(W):
        if m[i][k] == 0 :
            m[i][k] = 1 
            result.append(bfs(i,k))

result.sort()
print(len(result))
for c in result :
    print(c, end = ' ')