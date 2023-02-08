import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
SCHEDULES = []
for _ in range(N) :
    SCHEDULES.append(list(map(int, input().split())))

CHECKED = [0] * 366
AREA = 0
width, height = 0, 0
for schedule in SCHEDULES :
    for i in range(schedule[0], schedule[1]+1) :
        CHECKED[i] += 1

for i in range(1, 366) :
    if CHECKED[i] == 0 :
        AREA += (width*height)
        width, height = 0, 0
        continue
    if CHECKED[i] > 0 :
        width += 1
        height = max(height, CHECKED[i])
AREA += (width*height)

print(AREA)