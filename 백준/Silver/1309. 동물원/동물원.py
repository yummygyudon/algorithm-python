import sys
input = sys.stdin.readline

N = int(input())
MOD = 9901

DP = [[0]*3 for _ in range(N+1)]

DP[1][0], DP[1][1], DP[1][2] = 1, 1, 1

if N > 1 :
    for i in range(2,N+1) :
        for k in range(3) :
            if k == 0 :
                DP[i][k] = (DP[i - 1][0] + DP[i - 1][1] + DP[i-1][2]) % MOD
            if k == 1 :
                DP[i][k] = (DP[i - 1][0] + DP[i - 1][2]) % MOD
            if k == 2 :
                DP[i][k] = (DP[i - 1][0] + DP[i - 1][1]) % MOD
print(sum(DP[N]) % MOD)