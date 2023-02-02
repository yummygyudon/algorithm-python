import sys
input = sys.stdin.readline

N = int(input())
TIME_TABLE = [[0,0] for _ in range(N+1)]
for i in range(1,N+1) :
    TIME_TABLE[i][0] , TIME_TABLE[i][1] = map(int, input().split())

INCOME = [0] * (N+2)

MAX = 0
for i in range(1, N+1) :
    MAX = max(MAX, INCOME[i])
    if i + TIME_TABLE[i][0] <= N+1:
        
        INCOME[i + TIME_TABLE[i][0]] = max(INCOME[i + TIME_TABLE[i][0]], MAX + TIME_TABLE[i][1])
print(max(INCOME))