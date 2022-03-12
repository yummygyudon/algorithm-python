import sys

''' BFS 풀이 _ '''
from collections import deque
N = int(sys.stdin.readline())
mx = 0
mn = 100
land = []
for i in range(N) :
    heights = list(map(int,sys.stdin.readline().split()))
    mx = max(mx, max(heights))
    mn = min(mn, min(heights))-1 # 가장 낮은 높이에서의 영역도 계산할 수 있도록
    land.append(heights)


# print(land)
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
                    # deep이 가장 낮은 구역 (그냥 min) 으로하게 되면 그 구역에 대해서는 구할 수 없어서
                    # 위에서 min에 -1을 해주는 것
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

''' DFS 풀이 _ 런타임 에러 '''
# N = int(sys.stdin.readline())
# mx = 0
# mn = 100
# land = []
# for i in range(N) :
#     heights = list(map(int,sys.stdin.readline().split()))
#     mx = max(mx, max(heights))
#     mn = min(mn, min(heights))
#     land.append(heights)
#
# nx = [0, 0, 1, -1]
# ny = [1, -1, 0, 0]
#
# def dfs(x, y) :
#     if x < 0 or x >= N or y < 0 or y >= N :
#         return False
#     if land[x][y] > deep and visited[x][y] == 0 :
#         visited[x][y] = 1
#         for i in range(4):
#             dfs(x+nx[i], y+ny[i])
#         return True
#     return False
#
# result = 0
# for deep in range(mn,mx+1) :
#     best = 0
#     visited = [[0]*N for _ in range(N)]
#     for i in range(N):
#         for k in range(N) :
#             if dfs(i,k) :
#                 best+=1
#     if best > result :
#         result = best
# print(result)