import sys
input = sys.stdin.readline
N = int(input())
CASE = [0] * 1001
CASE[1] = 1
CASE[2] = 2
if N > 2 :
    for c in range(3,N+1) :
        CASE[c] = CASE[c-1] + CASE[c-2]
print(CASE[N] % 10_007)