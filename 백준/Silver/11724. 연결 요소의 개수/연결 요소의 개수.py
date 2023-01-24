import sys
from collections import deque
input = sys.stdin.readline

def bfs(node):
    q = deque()
    q.append(node)
    while q:
        n = q.popleft()
        for neighbor in GRAPH[n] :
            if not VISIT[neighbor]:
                q.append(neighbor)
                VISIT[neighbor] = True


N, M = map(int, input().split())

GRAPH = [[] for _ in range(N+1)]

for _ in range(M):
    v1,v2 = map(int, input().split())
    GRAPH[v1].append(v2)
    GRAPH[v2].append(v1)

VISIT = [False] * (N+1)
cnt = 0

for node in range(1, N+1):
    if VISIT[node]:
        continue
    VISIT[node] = True
    bfs(node)
    cnt += 1

print(cnt)
