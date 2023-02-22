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

from itertools import combinations
combi = []
for i in range(1,N+1) :
    combi.append(combinations(INGREDIENT, i))
result = 1e9
for case in combi :
    for eachCombi in case :
        tmp_s = 1
        tmp_b = 0
        for ingredient in eachCombi :
            tmp_s *= ingredient[0]
            tmp_b += ingredient[1]
        result = min(result, abs(tmp_s-tmp_b))
print(result)