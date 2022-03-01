import sys

Layer, row, column = map(int,sys.stdin.readline().split())
value = -1 # 0행 0열 값이 0부터 시작이기 때문에 += 1을 했을 때 첫값이 0이 나오게하기 위해


# 각 사분면으로 2x2로 세고 그 상위 단계에서의 다음 2x2배열로 이동
def Z_read(x,y, N) : # 찾는 값 =  x행, y열 값, N = 현재 단계 가로세로 칸수
    global value

    """
    x <= row < x+N or y <= column < y+N 의 경우
    ( 2^1 x 2^1 )판의 경우는 바로 if문에서 적용되고
    ( 2^2 x 2^2 )판 이상부터 하단의  
    """
    if N == 2 :
        # 이중 for문으로 자동으로 Z 모양으로 읽음.
        # 0행 0열 - 0행 1열 - 1행 0열 - 1행 1열
        for i in range(x, x+N) : # (0 ~ 2)행 - 세로 이동
            for j in range(y, y+N) : # (0~2)열 - 가로 이동
                value += 1
                if i == row and j == column :
                    print(value)
                    sys.exit(0)
        return
        # 재귀 끝

    # 위 최소크기(2x2) 단계까지 가기 전에
    # 전체 범위에서 1차적으로 사분면으로 나눴을 때부터
    #
    # 일찍이 사분면을 나누고
    # 만약 찾으려는 행 열이 해당 분면이 없다면
    # 굳이 이중for문 작업 하지말고
    # 그 범위만큼 values 더해주고 다음 분면으로 넘어간다. (다음순서 재귀) _ (세준 셈 치기)
    if not ( x <= row < x+N and y <= column < y+N) :
        value += N*N
        return

    """ 4x4 넘어서부터 for문 시작 """
    # 간격을  //2 -> 반절씩 이동하게 해 행에서 2등분 & 열에서 2등분해서 4등분이 됨.
    for i in range(x, x+N, N//2) : #범위 나누기 :  (1,2 사분면) / (3,4 사분면)
        for j in range(y, y+N, N//2) : # 범위 나누기 : (1사분면)/(2사분면)/(3사분면)/(4사분면)
            Z_read(i, j, N//2)
            # 각 사분면에서 다시 4등분하게 재귀
            # 처음엔 1사분면의 1사분면의 1사분면.... 범위로 들어가게됨.


Z_read(0,0,2**Layer) # 처음 시작은 무조건 0으로 시작해야함 _ for문에서 +N
# 즉 < 0 ~ 2^Layer > -> 전체 칸수로 for문 시작해야하기 때문에