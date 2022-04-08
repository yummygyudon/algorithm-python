import sys
from collections import deque
input = sys.stdin.readline
K = int(input())
W, H = map(int, input().split())
world = [list(map(int, input().split())) for _ in range(H)]

hmove_h = [-1, -2, -2, -1, 1, 2,  2,  1]
hmove_w = [-2, -1,  1,  2, 2, 1, -1, -2]

move_h = [-1, 0, 1, 0]
move_w = [0, 1, 0, -1]

def bfs() :
    k_check = [[[False]*(K+1) for _ in range(W)] for _ in range(H)]
    q = deque()
    q.append([0,0,K,0])
    while q :
        x, y, k, cnt = q.popleft()
        if x == (W-1) and y == (H-1) :
            return cnt

        if k > 0 :
            for i in range(8) :
                hx = x + hmove_w[i]
                hy = y + hmove_h[i]

                if 0 <= hx < W and 0 <= hy < H and k_check[hy][hx][k-1] == False and world[hy][hx] != 1:
                    k_check[hy][hx][k-1] = True
                    q.append([hx, hy, k-1,cnt+1])

        for i in range(4) :
            nx = x+move_w[i]
            ny = y+move_h[i]

            if 0 <= nx < W and 0 <= ny < H and k_check[ny][nx][k] == False and world[ny][nx] != 1:
                k_check[ny][nx][k] = True
                q.append([nx, ny, k, cnt + 1])
    return -1

print(bfs())