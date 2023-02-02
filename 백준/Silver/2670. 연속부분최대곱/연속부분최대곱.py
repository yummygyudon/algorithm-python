import sys
input = sys.stdin.readline

N = int(input())
FLOATS = []
for _ in range(N) :
    FLOATS.append(float(input()))
for i in range(1, N) : # 0
    FLOATS[i] = max(FLOATS[i], FLOATS[i]*FLOATS[i-1])
print("%.3f"%max(FLOATS))