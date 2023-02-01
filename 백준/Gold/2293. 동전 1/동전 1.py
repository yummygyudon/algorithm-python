import sys
input = sys.stdin.readline

N, TARGET = map(int,input().split())
COINS = []
for _ in range(N) :
    COINS.append(int(input()))
COINS.sort()

DP = [0]*(TARGET+1)

for coin in COINS :
    for idx in range(1,TARGET+1) :
        if idx - coin > 0 :
            DP[idx] = DP[idx] + DP[idx-coin];
        elif idx - coin == 0 :
            DP[idx] += 1

print(DP[TARGET])