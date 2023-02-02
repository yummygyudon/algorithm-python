import sys
input = sys.stdin.readline

N = int(input())
NUMS = list(map(int, input().split()))
UP = [1] * N
DOWN = [1] * N
for i in range(1, N) :
    temp = 1
    if NUMS[i] >= NUMS[i-1] :
        UP[i] = UP[i-1]+1
    if NUMS[i] <= NUMS[i-1] :
        DOWN[i] = DOWN[i-1] + 1

print(max(max(UP), max(DOWN)))