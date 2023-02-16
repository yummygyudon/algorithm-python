import sys
input = sys.stdin.readline

N = int(input())
from queue import PriorityQueue
q = PriorityQueue(maxsize=N)

for _ in range(N) :
    q.put(int(input()))
result = 0
for _ in range(N-1) :
    c1 = q.get()
    c2 = q.get()
    x1 = c1 + c2
    result += x1
    q.put(x1)
print(result)