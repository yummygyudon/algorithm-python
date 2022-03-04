import sys
from collections import deque
input = sys.stdin.readline
H, W = map(int, input().split())
field = []
for _ in range(H) :
    field.append(list(map(int,input().split())))

visited = [[False]*W for _ in range(H)]

start_lv = field[0][0]
move_x = [0, 1, 0, -1]
move_y = [-1, 0, 1, 0]
print(field)
def bfs() :
    q = deque()
    q.append([0,0,start_lv])
    while q :
        x, y, lv = q.popleft()
        print(f"x: {x}, y: {y}, lv : {lv}")
        if visited[x][y] == True :
            continue
        if x == W-1 and y == H-1 :
            return lv
        for i in range(4) :
            nx = x + move_x[i]
            ny = y + move_y[i]

            if 0 < nx <= W-1 and 0 < ny <= H-1 and visited[nx][ny] == False:
                if field[x][y] < field[nx][ny] :
                    if nx+1 <= W-1 and ny+1 <= H-1 and visited[nx+1][ny+1] == False:
                        if field[nx][ny] < field[nx+1][ny+1] :
                            lv = max(field[x][y],field[nx][ny])
                            visited[x][y] = True
                            q.append([nx, ny, lv])
                            continue
                        else :
                            lv = max(field[x][y],field[nx+1][ny+1])
                            visited[x][y] = True
                            q.append([nx+1, ny+1, lv])
                            continue
                    else :
                        lv = max(field[x][y],field[nx][ny])
                        visited[x][y] = True
                        q.append([nx, ny, lv])
                        continue
                lv = max(field[x][y],field[nx][ny])
                visited[x][y] = True
                q.append([nx, ny, lv])
print(bfs())

