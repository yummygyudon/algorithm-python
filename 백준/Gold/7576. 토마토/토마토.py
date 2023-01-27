from collections import deque
import sys
input = sys.stdin.readline
M, N = map(int, input().split())
BOX = []
TOMATO_POS = []
d = [[0, 1],[0, -1],[-1, 0],[1, 0]]
POSSIBLE = True

for i in range(N) :
    tomatoLine = list(map(int, input().split()))
    BOX.append(tomatoLine)
    for k in range(M) :
        if tomatoLine[k] == 1 :
            TOMATO_POS.append([i,k])
VISITED = [[False]*M for _ in range(N)]
def ripeningTomato(tomatoPostionList:list) :
    global BOX
    q = deque()
    for position in tomatoPostionList :
        q.append([position[0], position[1], 0])
        VISITED[position[0]][position[1]] = True
    while q:
        y, x, move = q.popleft()
        for i in range(4):
            n_y = y + d[i][0]
            n_x = x + d[i][1]
            if (0 <= n_y < N) and (0 <= n_x < M) and not (BOX[n_y][n_x] == -1) and not VISITED[n_y][n_x]:
                VISITED[n_y][n_x] = True
                BOX[n_y][n_x] = move+1
                q.append([n_y, n_x, move + 1])

def calcResult(box) :
    MAX = -1e9
    for line in box:
        for block in line :
            if block == 0 :
                return -1
            if block > MAX :
                MAX = block
    if MAX == 1 :
        return 0
    return MAX

ripeningTomato(TOMATO_POS)
print(calcResult(BOX))