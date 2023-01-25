from collections import deque
import sys
input = sys.stdin.readline

moving = [[0,1],[0,-1],[1,0],[-1,0]]
N = int(input())
MAP = []

start_x, start_y = 0, 0
start_size = 2
for i in range(N):
    layer = list(map(int, input().split()))
    MAP.append(layer)
    for j in range(N) :
        if (layer[j] == 9) :
            start_y = i
            start_x = j

def findFish(y,x,size) :
    q = deque()
    q.append( [y,x,0] )
    ableToEat = []
    visited = [[False]*N for _ in range(N)]
    visited[y][x] = True
    while q:
        y, x, move = q.popleft()
        for i in range(4) :
            ny = y + moving[i][0]
            nx = x + moving[i][1]
            n_move = move+1
            if (0 <= ny < N and 0 <= nx < N) and not visited[ny][nx]:
                if (MAP[ny][nx] <= size) :
                    q.append([ny,nx,n_move])
                    visited[ny][nx] = True
                    if MAP[ny][nx] < size and MAP[ny][nx] != 0:
                        ableToEat.append([n_move, ny, nx])
    ableToEat.sort()
    return ableToEat


wasteTime = 0
eatenSize = 0
while True :
    MAP[start_y][start_x] = 0
    result = findFish(start_y, start_x, start_size)
    if not result :
        print(wasteTime)
        break
    else :
        move_cnt, n_y, n_x = result[0][0], result[0][1], result[0][2]
        wasteTime += move_cnt
        start_y = n_y
        start_x = n_x
        eatenSize += 1
        if eatenSize == start_size :
            start_size += 1
            eatenSize = 0
