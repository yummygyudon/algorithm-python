N = int(input())

MAP = []
for _ in range(N):
    MAP.append(list(map(str, input())))

maxCount = 0

def checkAllRow():
    global maxCount
    for i in range(N): # 0행, 1행 ,...
        for k in range(N) : # 기준 열
            cnt = 1 # 기본 자기 자신 1
            for j in range(k+1, N): # 기준 열 옆으로 쭉 확인
                if MAP[i][k] == MAP[i][j]:
                    cnt += 1
                    maxCount = max(maxCount, cnt)
                else:
                    """
                    중간에 끊기면 초기화
                    """
                    # cnt = 1
                    break


def checkAllColumn():
    global maxCount
    for i in range(N):  # 0열, 1열, 2열 ,...
        for k in range(N): # 기준 행
            cnt = 1
            for j in range(k + 1, N):
                if MAP[k][i] == MAP[j][i]:
                    cnt += 1
                    maxCount = max(maxCount, cnt)
                else:
                    # cnt = 1
                    break
            # maxCount = max(maxCount, cnt)

"""
맨 처음 상태에서 maxCount 연산
"""
checkAllRow()
checkAllColumn()

for i in range(N):
    for k in range(N - 1):
        """
        좌우로 뒤집을 때
        """
        if MAP[i][k] != MAP[i][k + 1]:
            MAP[i][k], MAP[i][k + 1] = MAP[i][k + 1], MAP[i][k]
            checkAllRow()
            checkAllColumn()
            """
            원상 복구
            """
            MAP[i][k + 1], MAP[i][k] = MAP[i][k], MAP[i][k + 1]

        """
        상하로 뒤집을 때
        """
        if MAP[k][i] != MAP[k + 1][i]:
            MAP[k][i], MAP[k + 1][i] = MAP[k + 1][i], MAP[k][i]
            checkAllRow()
            checkAllColumn()
            MAP[k + 1][i], MAP[k][i] = MAP[k][i], MAP[k + 1][i]

print(maxCount)