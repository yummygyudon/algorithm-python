import sys
input = sys.stdin.readline
H, W = map(int, input().split())

graph = []
for _ in range(H) :
    graph.append(list(map(int,input().split())))

visited = [[0]*W for _ in range(H)]

from collections import deque
d = [[0,1], [0, -1], [1, 0], [-1,0]]
def bfs(y, x, size) :
    q = deque()
    visited[y][x] = 1
    q.append([y,x])
    while q:
        y, x = q.popleft()
        for dy,dx in d :
            ny = y + dy
            nx = x + dx
            if 0 <= ny < H and 0<=nx<W :
                if graph[ny][nx] ==1 and visited[ny][nx] == 0 :
                    size += 1
                    visited[ny][nx] = 1
                    q.append([ny,nx])
    return size

result = []
pictures = 0
mx_size = 0
for i in range(H) :
    for k in range(W) :
        if graph[i][k] == 1 and visited[i][k] == 0:
            mx_size = max(mx_size, bfs(i, k, 1))
            pictures += 1



print(pictures)
print(mx_size)

