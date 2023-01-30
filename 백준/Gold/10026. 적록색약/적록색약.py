from collections import deque
import sys
input = sys.stdin.readline


d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
N = int(input())

COMMON_MAP = []
BLIND_MAP = [[] for _ in range(N)]

BLIND_COLOR = ["R", "G"]

for i in range(N) :
    line = list(input().rstrip())
    COMMON_MAP.append(line)
    for k in range(N) :
        if line[k] in BLIND_COLOR :
            BLIND_MAP[i].append("RG")
        else :
            BLIND_MAP[i].append(line[k])

VISITED_COMMON = [[False]*N for _ in range(N)]
VISITED_BLIND = [[False]*N for _ in range(N)]

COMMON_COUNT = 0
BLIND_COUNT = 0

def bfs(y, x, color, visited, map) :
    q = deque()
    q.append([y,x])
    visited[y][x] = True
    while q :
        nowY, nowX = q.popleft()
        for i in range(4) :
            nextY = nowY + d[i][0]
            nextX = nowX + d[i][1]
            if 0 <= nextY < N and 0 <= nextX < N and map[nextY][nextX] == color and not visited[nextY][nextX] :
                visited[nextY][nextX] = True
                q.append([nextY, nextX])
    return map, visited

for i in range(N) :
    for k in range(N) :
        if not VISITED_BLIND[i][k] :
            BLIND_COUNT += 1
            BLIND_MAP, VISITED_BLIND =  bfs(i, k, BLIND_MAP[i][k], VISITED_BLIND, BLIND_MAP)
        if not VISITED_COMMON[i][k] :
            COMMON_COUNT += 1
            COMMON_MAP, VISITED_COMMON = bfs(i, k, COMMON_MAP[i][k], VISITED_COMMON, COMMON_MAP)

print(COMMON_COUNT, BLIND_COUNT, sep=" ")