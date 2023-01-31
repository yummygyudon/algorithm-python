import sys
input = sys.stdin.readline
N = int(input())
ROCKS = [[0,0] for _ in range(N)]
for i in range(1, N):
    ROCKS[i][0], ROCKS[i][1] = map(int, input().split())
K = int(input())

NO_HUGE_JUMP = [1e9] * (N+1)
NO_HUGE_JUMP[1] = ROCKS[0][0]
minimalJump = 0

if N >= 2 :
    NO_HUGE_JUMP[2] = ROCKS[1][0]
    for nowPos in range(3, N+1):
        NO_HUGE_JUMP[nowPos] = min(NO_HUGE_JUMP[nowPos-1] + ROCKS[nowPos-1][0], NO_HUGE_JUMP[nowPos-2] + ROCKS[nowPos-2][1])
    minimalJump = NO_HUGE_JUMP[-1]
    for i in range(4,N+1) :
        scenario, case1, case2 = NO_HUGE_JUMP[i-3] + K, 1e9, 1e9
        for k in range(i, N) :
            if i+1 <= N :
                case1 = min(case1, scenario+ROCKS[k][0])
            if i+2 <= N :
                case2 = min(case2, scenario+ROCKS[k][1])
            scenario, case1, case2 = case1, case2, 1e9
        minimalJump = min(minimalJump, scenario)
print(minimalJump)