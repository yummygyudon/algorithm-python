import sys
input = sys.stdin.readline
TC = int(input())

for _ in range(TC):
    N = int(input())
    SCORE = [[0]*N]*2
    STICKER = []
    for _ in range(2):
        STICKER.append(list(map(int, input().split())))
    if N > 1 :
        STICKER[0][1] += STICKER[1][0]
        STICKER[1][1] += STICKER[0][0]
        for i in range(2, N) :
            temp = max(STICKER[0][i-2], STICKER[1][i-2])
            STICKER[0][i] = max(STICKER[0][i]+temp, STICKER[0][i]+STICKER[1][i-1])
            STICKER[1][i] = max(STICKER[1][i] + temp, STICKER[1][i] + STICKER[0][i-1])
    print(max(STICKER[0][N-1], STICKER[1][N-1]), end="\n")