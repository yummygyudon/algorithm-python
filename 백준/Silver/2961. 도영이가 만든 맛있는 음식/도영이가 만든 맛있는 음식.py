import sys
input = sys.stdin.readline

"""
차이가 가장 작은 음식

"""
N = int(input())
INGREDIENT = []
for _ in range(N):
    s, b = map(int, input().split())
    INGREDIENT.append([s,b])

index = 1
result = 1e9

def multi(nums:list) :
    result = nums[0]
    for i in range(1, len(nums)) :
        result *= nums[i]
    return result

while index < (1 << N) : # 16가지 경우의 수가 다 돌때 까지
    MIN = 1e9
    nowS, nowB = [], []
    for k in range(N) :
        if index & (1 << k) :
            nowS.append(INGREDIENT[k][0])
            nowB.append(INGREDIENT[k][1])
            MIN = min(MIN, abs(multi(nowS)-sum(nowB)))
            result = min(result, MIN)
    index += 1
print(result)