from collections import deque
import heapq
import sys
input = sys.stdin.readline

"""
(1,1) 출발 ~ (N, M) 도착이지만
(0,0) 출발 ~ (N-1, M-1) 과 동일하기 때문에 상관 없음
"""

# N : 세로 / M : 가로
N, M = map(int, input().split())
MAP = [list(map(int, list(input().rstrip()))) for _ in range(N)]
"""
각 리스트의 0번째 : 안 부수고 이동했을 때 / 1번째 : 부수고 이동했을 때

TypeError: 'bool' object is not subscriptable 에러 때문에 0과 1로 치환
"""
VISITED =[[0] * M for _ in range(N)]
"""index 0층 : 벽을 안부수고 가는 경로 / index 1층 : 벽을 부수고 가는 경로"""
MOVE =[ [[0]*2 for _ in range(M)] for _ in range(N)] # 0과 1을 갖는 crush 값을 통해 indexing까지
# 우, 좌, 히, 싱
d = [[0,1], [0,-1], [1,0], [-1,0]]

def startMove() :
    q = deque()
    """ (0,0)은 항상 0이라는 가정 """
    """
    처음 시작 : 안 부순 상태이기 때문에 0
    """
    # q.append([0,0,0,False]) # [ (y좌표), (x좌표), (부순 횟수) ]
    # heapq.heappush(heap, [0,0,0,0])
    q.append([0,0,0])
    MOVE[0][0][0] = 1
    while q :
        y, x, crush = q.popleft()
        if (y == N-1) and (x == M-1) :
            """
            시작하는 칸과 끝나는 칸도 포함해서 센다는 조건
            """
            return MOVE[y][x][crush]
        for i in range(4) :
            ny = y + d[i][0]
            nx = x + d[i][1]
            if 0 <= ny < N and 0 <= nx < M :
                """벽일 경우"""
                """
                벽은 "한 개"까지 부술 수 있음
                """
                if MAP[ny][nx] == 1 and crush == 0:
                    """한번도 부순적 없는 경우"""
                    MOVE[ny][nx][1] = MOVE[y][x][crush] + 1 # 이동 전에 저장되어 있던 값
                    q.append([ny, nx, 1]) # crush를 1로
                """이동 가능한 칸일 경우 & 해당 crush의 상태로 최초 방문인 경우 : 동일 crush 층 내에서 최단 거리로 도착한 경우"""
                if MAP[ny][nx] == 0 and MOVE[ny][nx][crush] == 0  :
                    MOVE[ny][nx][crush] = MOVE[y][x][crush] + 1
                    q.append([ny, nx, crush]) # crush 유지
    return -1

print(startMove())