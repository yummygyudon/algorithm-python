import sys
input = sys.stdin.readline
N = int(input())
CRANE_LIMIT = list(map(int, input().split()))

BOX_QUANTITY = int(input())
BOX_WEIGHT = list(map(int, input().split()))

CRANE_LIMIT.sort(reverse=True)
BOX_WEIGHT.sort(reverse=True)


if CRANE_LIMIT[0] < BOX_WEIGHT[0] :
    print(-1)
else :
    result = 0
    while BOX_WEIGHT :
        idx = 0
        i = 0
        while i < N :
            if idx == len(BOX_WEIGHT) :
                break
            elif CRANE_LIMIT[i] >= BOX_WEIGHT[idx] :
                BOX_WEIGHT.remove(BOX_WEIGHT[idx])
                i += 1
            else :
                idx += 1
        result += 1
    print(result)