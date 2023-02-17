import sys
input = sys.stdin.readline

N = int(input())

NUMS = []
USED = [False]*(N)
for _ in range(N) :
    NUMS.append(int(input()))
if N == 1 :
    print(NUMS[0])
    sys.exit()
NUMS.sort()
result = 0
idx = 0
while True :
    if idx >= N :
        break
    if USED[idx] :
        idx+=1
        continue
    if NUMS[idx] < 0 :
        for i in range(idx+1, N):
            if NUMS[i] <= 0 and not USED[i] :
                result += (NUMS[idx]*NUMS[i])
                USED[idx], USED[i] = True, True
                break
            else:
                result += NUMS[idx]
                USED[idx] = True
                break
        idx += 1
    elif NUMS[idx] == 0 :
        result += NUMS[idx]
        USED[idx] = True
        idx += 1
    else :
        if (N-idx) % 2 == 1 :
            result += NUMS[idx]
            USED[idx] = True
            idx += 1
        else :
            result += max(NUMS[idx]*NUMS[idx+1], NUMS[idx]+NUMS[idx+1])
            USED[idx], USED[idx+1] = True, True
            idx += 2
print(result)