from collections import deque
import sys
input = sys.stdin.readline
HISTORY = [0]*100001
LIMIT = 100000
def startGame() :
    q = deque()
    q.append(SUBIN)
    while q :
        nowPosition = q.popleft()
        if (nowPosition == BROTHER) :
            print(HISTORY[nowPosition])
            break
        """
         == 0 논리 연산으로 중복 계산 방지 ( 최초 계산일 경우에만 append )
        """
        positionValue = HISTORY[nowPosition]
        if (0 <= (nowPosition + 1) <= LIMIT) and (HISTORY[nowPosition + 1] == 0) :
            HISTORY[nowPosition + 1] = positionValue+1
            q.append(nowPosition + 1)
        if (0 <= (nowPosition - 1) <= LIMIT) and (HISTORY[nowPosition - 1] == 0) :
            HISTORY[nowPosition - 1] = positionValue + 1
            q.append(nowPosition - 1)
        if (0 <= (nowPosition * 2) <= LIMIT) and (HISTORY[nowPosition * 2] == 0) :
            HISTORY[nowPosition * 2] = positionValue + 1
            q.append(nowPosition * 2)

SUBIN, BROTHER = map(int, input().split())
startGame()