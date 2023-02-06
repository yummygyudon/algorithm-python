import sys
input = sys.stdin.readline
N = int(input())
""" 20년 + 4년(Index 최대치)꺼지 보장된 DP"""
LIVE = [0] * 21
DEAD = [0] * 25
LIVE[1] = 1
DEAD[4] = 1

for i in range(2, N+1) :
    born = LIVE[i-1]
    LIVE[i] = born*2 - DEAD[i]

    if i % 2 == 1:
        DEAD[i+3] += born
    else :
        DEAD[i+4] += born

print(LIVE[N])