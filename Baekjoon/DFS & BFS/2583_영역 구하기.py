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
# 일반 이중 리스트라면 좌표가 상하 반전된 값들이지만
# 사실 영역과 땅의 갯수를 구하는 것이기 때문에 좌표를 정확하게 지키면서 할 필요없음
# 높이와 너비만 벗어나지 않으면된다.
for _ in range(Square) :
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2) :
        for k in range(y1, y2):
            m[k][i] = 1

for i in range(H):
    for k in range(W):
        if m[i][k] == 0 :
            m[i][k] = 1 # 꼭 1로 해주어야 (0,-1)등과 같이 나중에 시작한 곳에 돌아왔을 때 cnt를 한번 더 더하지 않음.
            result.append(bfs(i,k))

                # result.append(cnt)
    # dfs(x1, y1)
result.sort()
print(len(result))

## Unpack 이라는 좋은 방법도 있음
print(*result)
# for c in result :
#     print(c, end = ' ')