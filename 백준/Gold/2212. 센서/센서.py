import sys
input = sys.stdin.readline
N = int(input()) # 센서 갯수
K = int(input()) # 집중국 갯수
SENSORS = list(map(int, input().split()))
SENSORS.sort()

DISTANCE = [0] * (N-1)

for i in range(N-1) :
    DISTANCE[i] = SENSORS[i+1]-SENSORS[i]
DISTANCE.sort()
print(sum(DISTANCE[:N-K]))