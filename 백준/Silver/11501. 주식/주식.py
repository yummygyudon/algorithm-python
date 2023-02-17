import sys
input = sys.stdin.readline

TC = int(input())
for _ in range(TC) :
    DAY = int(input())-1
    CHART = list(map(int, input().split()))
    benefit = 0
    MAX = 0
    holding = []
    for day in range(DAY, -1, -1) :
        if CHART[day] > MAX :
            MAX = CHART[day]
        else :
            benefit += MAX - CHART[day]
    print(benefit)