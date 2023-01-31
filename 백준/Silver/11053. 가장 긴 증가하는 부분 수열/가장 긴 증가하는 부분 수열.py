import sys
input = sys.stdin.readline
N = int(input())
NUMS = list(map(int, input().split()))
CHECK = [0] * 1_001

for idx in range(N) :
    for before in range(idx) :
        if NUMS[idx] > NUMS[before] and CHECK[idx] < CHECK[before] :
            CHECK[idx] = CHECK[before]
    CHECK[idx] += 1

print(max(CHECK))