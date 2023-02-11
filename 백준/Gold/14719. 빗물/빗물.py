import sys
input = sys.stdin.readline

H,W = map(int, input().split())
WALLS = list(map(int, input().split()))
WATER = 0

MAX_HEIGHT = max(WALLS)
MAX_HEIGHT_POS = WALLS.index(MAX_HEIGHT)

leftPointer = 0
rightPointer = W-1

leftMax = WALLS[leftPointer]
rightMax = WALLS[rightPointer]

while (leftPointer <= MAX_HEIGHT_POS) and (rightPointer >= MAX_HEIGHT_POS) :
    leftMax = max(leftMax, WALLS[leftPointer])
    rightMax = max(rightMax, WALLS[rightPointer])
    if leftMax < rightMax :
        WATER += (leftMax - WALLS[leftPointer])
        leftPointer += 1
    else :
        WATER += (rightMax - WALLS[rightPointer])
        rightPointer -= 1

print(WATER)