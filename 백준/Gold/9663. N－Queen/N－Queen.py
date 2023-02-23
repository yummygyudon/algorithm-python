import sys
input = sys.stdin.readline

N = int(input())

EACH_ROW = [0]*N
# 매 열 시작마다 필요한 리스트 -> 재귀 돌아올 때 다시 False로 초기화 필요
EACH_COLUMN = [False]*N

CASE = 0
def nQueen(nowRow) :
    global CASE
    """
    N까지 갔다는 것 : N-1을 넘었다는 것 : 마지막 줄까지 잘 도착했다는 것
    """
    # print("지금부터 %d행 시작"%nowRow)
    if nowRow == N :
        CASE += 1
        return
    for column in range(N) :
        # 아직 안간 열이면
        if not EACH_COLUMN[column] :
            # print("지금부터 %d열 시작"%column)
            # 현재 행 내 해당 열에 퀸을 놓는다고 가정
            EACH_ROW[nowRow] = column
            # print("EACH ROW = ",EACH_ROW)
            if checkIsPossible(nowRow) :
                EACH_COLUMN[column] = True
                # print("EACH COLUMN = ", EACH_COLUMN)
                nQueen(nowRow+1)
                EACH_COLUMN[column] = False
    # print()

def checkIsPossible(nowRow) :
    for i in range(nowRow) :
        if EACH_ROW[i] == EACH_ROW[nowRow] or (nowRow-i == abs(EACH_ROW[nowRow]-EACH_ROW[i])) :
            return False
    return True

nQueen(0)
print(CASE)
