import sys
from collections import deque
N = int(sys.stdin.readline())
mx = 0
mn = 100
land = []
for i in range(N) :
    heights = list(map(int,sys.stdin.readline().split()))
    mx = max(mx, max(heights))
    mn = min(mn, min(heights))-1
    land.append(heights)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x,y,deep) :
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    while q :
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N :
                if land[nx][ny] > deep and visited[nx][ny]==0 :
                    visited[nx][ny] = 1
                    q.append([nx,ny])

result = 0
for deep in range(mn,mx+1) :
    best = 0
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for k in range(N) :
            if land[i][k] > deep and visited[i][k] == 0 :
                bfs(i,k,deep)
                best+=1
    if best > result :
        result = best
print(result)