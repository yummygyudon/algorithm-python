import sys
input = sys.stdin.readline

K = int(input())
SEQUENCE = list(map(int, input().split()))

LAYER = [[] for _ in range(K+1)]

depth = 1
def dfs(startIndex, endIndex,depth) :
    midIndex = (startIndex+endIndex)//2
    LAYER[depth].append(SEQUENCE[midIndex])

    if depth >= K :
        return
    dfs(startIndex, midIndex, depth+1)
    dfs(midIndex+1, endIndex, depth+1)

dfs(0, len(SEQUENCE), 1)
for i in range(1, K+1) :
    print(*LAYER[i])