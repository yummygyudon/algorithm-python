from itertools import permutations
import sys
N = int(sys.stdin.readline())
all_nums = list(permutations([1,2,3,4,5,6,7,8,9],3))

for i in range(N) :
    num, s, b = map(int, sys.stdin.readline().split())
    num = list(str(num))
    remove = 0
    for j in range(len(all_nums)) :
        strike = ball = 0
        j -= remove
        for k in range(3) :
            if int(num[k]) in all_nums[j] :
                if int(num[k]) == all_nums[j][k] :
                    strike += 1
                    continue
                ball += 1
        if strike != s or  ball != b :
            del all_nums[j]
            remove += 1
print(len(all_nums))
