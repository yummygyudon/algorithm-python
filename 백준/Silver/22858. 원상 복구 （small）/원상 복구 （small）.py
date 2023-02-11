import sys
input = sys.stdin.readline

N, SHUFFLE = map(int, input().split())

RESULT = [0] + list(map(int, input().split()))
D = [0] + list(map(int,input().split()))

for _ in range(SHUFFLE) :
    temp = [0]*(N+1)
    for i in range(1,N+1) :
        temp[D[i]] = RESULT[i]
    RESULT = temp
print(*RESULT[1:])