BOARD = []
CHECK = []
H, W = 0, 0
RM_COUNT = 0
D = [[0,1], [1,1], [1,0]]

def solution(m, n, board):
    global BOARD, CHECK, H, W
    for line in board :
        BOARD.append(list(line))
    # CHECK = [[False]*n for _ in range(m)]
    H,W = m,n
    
    while True :
        # possiblePos = []
        removePos = set()
        for i in range(H-1) :
            for k in range(W-1) :
                # -1이 아니면서 2x2 구역이 모두 같을 경우 -> 모든 좌표 추가
                if not BOARD[i][k] == -1 and isPossibleFrom(i,k, BOARD[i][k]) :
                    removePos.add((i,k))
                    for j in range(3) :
                        removePos.add((i+D[j][0], k+D[j][1]))
                    # possiblePos.append([i,k])
        # 삭제할 좌표가 한 개도 없으면 끝내기
        if len(removePos) == 0 :
            break
        # 모든 좌표 삭제 처리
        for y, x in removePos :
            BOARD[y][x] = -1
        refreshBoard()
    countRemoved()
    return RM_COUNT

# 새로운 한 판 시작하면서 2x2영역이 똑같은지 확인
def isPossibleFrom(y,x,block) :
    isPossible = True
    for i in range(3) :
        if BOARD[y+D[i][0]][x+D[i][1]] != block :
            isPossible = False
            break
    return isPossible
  

# 한 판 끝나고 Board 갱신하기
def refreshBoard() :
    global BOARD
    for i in range(H-1,0,-1) :
        for k in range(W) :
            if BOARD[i][k] == -1 :
                idx = i-1
                while idx >= 0 :
                    if not BOARD[idx][k] == -1 :
                        BOARD[idx][k], BOARD[i][k] = BOARD[i][k], BOARD[idx][k]
                        break
                    idx -= 1        
    
def countRemoved() :
    global RM_COUNT
    for line in BOARD :
        for block in line :
            if block == -1 :
                RM_COUNT += 1
        
    
    