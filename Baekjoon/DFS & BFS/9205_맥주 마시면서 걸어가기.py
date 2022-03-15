# 출발 : 상근이 집 & 맥주 1박스(20병)
# 1박스 = 20병 = 1000미터 ( 0~999 칸까지 )
# 50미터 당 1병 _ 출발할 때 이미 맥주 1병
# 편의점에서 새 맥주 구매
# 편의점을 나설 때도 이미 맥주 1병
import sys
input = sys.stdin.readline
TC = int(input())

from collections import deque
def bfs() :
    q = deque()
    q.append([home[0],home[1]])
    while q :
        x, y = q.popleft()
        if abs(x-festa[0]) + abs(y - festa[1]) <= 1000 : # 맥주 1박스 한계 거리 이내로 도착지 festa로 도착했을 경우
        # 집or편의점에서의 시작 좌표 간 차이의 절댓값보다 큰 것 ==> 맥주 1박스의 한계를 벗어난 것
        # 밑에 visited와 편의점 좌표를 기준으로 x,y 값을 갱신해주기 때문에 문제없음
            print("happy")
            return
        for i in range(S) : # 0,1
            if visited[i] == 0:
                store_x, store_y = store[i]
                if abs(x-store_x) + abs(y-store_y) <= 1000 :
                    q.append([store_x, store_y])
                    visited[i] = 1
    print("sad")
    return

for _ in range(TC):
    S = int(input())
    home = list(map(int,input().split()))
    store = []
    for _ in range(S):
        s = list(map(int,input().split()))
        store.append(s)
    festa = list(map(int,input().split()))
    visited = [0]*S # 편의점 &

    # H, W = festa_y-home_y, festa_x-home_x
    # stdY = home_y
    # stdX = home_x
    bfs()