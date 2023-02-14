N, M, R = map(int, input().split())
MAX_DEPTH = min(N,M)//2

MATRIX = []
for _ in range(N) :
    MATRIX.append(list(map(int, input().split())))

for _ in range(R) :
    for depth in range(MAX_DEPTH) :
        nowY, nowX = depth, depth
        temp = MATRIX[nowY][nowX]
        beforeVal = MATRIX[nowY][nowX]
        """
        한 칸씩 pointer 이동해가기
        
        N-startPos / M-startPos : (위 아래 왼쪽 오른쪽) 모두 한 칸씩 더해져 안쪽으로 들어와야하기 때문
        """
        for i in range(depth + 1, N - depth) : # 왼쪽 변 ( 위 -> 아래 )
            nowY = i
            temp = MATRIX[nowY][nowX]
            MATRIX[nowY][nowX] = beforeVal
            beforeVal = temp
        for i in range(depth + 1, M - depth) : # 아랫 변 ( 왼 -> 오 )
            nowX = i
            temp = MATRIX[nowY][nowX]
            MATRIX[nowY][nowX] = beforeVal
            beforeVal = temp
        for i in range(depth + 1, N - depth):  # 오른쪽 변 ( 아래 -> 위 )
            nowY = (N-1) - i
            temp = MATRIX[nowY][nowX]
            MATRIX[nowY][nowX] = beforeVal
            beforeVal = temp
        for i in range(depth + 1, M - depth) : # 윗 변 ( 오 -> 왼 )
            nowX = (M-1) - i
            temp = MATRIX[nowY][nowX]
            MATRIX[nowY][nowX] = beforeVal
            beforeVal = temp
        # for row in MATRIX:
        #     print(*row)
        # print()

for row in MATRIX :
    print(*row)