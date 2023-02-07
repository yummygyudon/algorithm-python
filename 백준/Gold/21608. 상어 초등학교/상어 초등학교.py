import sys
input = sys.stdin.readline

N = int(input())
MAP = [[0]*N for _ in range(N)]

LOVE = dict()
for _ in range(N*N) :
    values = list(map(int, input().split()))
    LOVE[values[0]] = values[1:]

d = [[-1,0],[0, 1],[1,0],[0,-1]]

SCORE = dict()
SCORE[0] = 0
SCORE[1] = 1
SCORE[2] = 10
SCORE[3] = 100
SCORE[4] = 1000

def firstMapping(studentNum) :
    friendsPos = []
    for friend in LOVE[studentNum] :
        for i in range(N) :
            for k in range(N) :
                if friend == MAP[i][k] :
                    for ablePos in checkAblePos(i,k) :
                        friendsPos.append(ablePos)
    if not friendsPos :
        return checkBestBlank()
    return findNearFriend(studentNum, friendsPos)
def checkAblePos(y,x) :
    ablePos = []
    for i in range(4) :
        ny = y + d[i][0]
        nx = x + d[i][1]
        if 0<=ny<N and 0<=nx<N and MAP[ny][nx] == 0 :
            ablePos.append([ny,nx])
    return ablePos

def checkBestBlank() :
    blanks = []
    for i in range(N) :
        for k in range(N) :
            if MAP[i][k] == 0 :
                cnt = 0
                for j in range(4) :
                    ny = i+d[j][0]
                    nx = k+d[j][1]
                    if 0<=ny<N and 0<=nx<N and MAP[ny][nx] == 0 :
                        cnt+=1
                blanks.append([cnt,i,k])
    blanks.sort(key=lambda pos : (-pos[0], pos[1], pos[2]))
    return [blanks[0][1], blanks[0][2]]

def findNearFriend(studentNum, ablePositions : list) :
    findResult = []
    for ablePos in ablePositions :
        near_cnt = 0
        blank_cnt = 0
        for i in range(4):
            ny = ablePos[0] + d[i][0]
            nx = ablePos[1] + d[i][1]
            if 0 <= ny < N and 0 <= nx < N and MAP[ny][nx] in LOVE[studentNum]:
                near_cnt += 1
            if 0 <= ny < N and 0 <= nx < N and MAP[ny][nx] == 0:
                blank_cnt += 1
        findResult.append([near_cnt,blank_cnt, ablePos[0], ablePos[1]])
    findResult.sort(key=lambda pos : (-pos[0],-pos[1], pos[2], pos[3]))
    return [findResult[0][2], findResult[0][3]]

for studentNum in list(LOVE.keys()) :
    y, x = firstMapping(studentNum)
    MAP[y][x] = studentNum

SURVEY = 0
for i in range(N) :
    for k in range(N):
        checkStudent = MAP[i][k]
        cnt = 0
        for j in range(4):
            ny = i + d[j][0]
            nx = k + d[j][1]
            if 0 <= ny < N and 0 <= nx < N and MAP[ny][nx] in LOVE[checkStudent]:
                cnt += 1
        SURVEY += SCORE[cnt]
print(SURVEY)