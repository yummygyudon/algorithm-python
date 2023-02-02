import sys
input = sys.stdin.readline
COINS = [1,2,5,7]

COINS.sort(reverse=True)
N = int(input())
DP = [1e9] * (N+1)
DP[0] = 0


for i in range(1,N+1) :
    for coin in COINS:
        if i - coin >= 0 :
            DP[i] = min(DP[i], DP[i-coin] + 1)
print(DP[N])