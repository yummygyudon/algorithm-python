import sys
input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

count = [0]*(N+1)
route = [list(map(int, input().split())) for _ in range(M)]
for x,y in route :
    graph[y].append(x)

from collections import deque
def bfs(start) :
    cnt = 1
    visited = [0 for _ in range(N+1)]
    visited[start] = 1
    q = deque([start])
    while q :
        computer = q.popleft()
        for c in graph[computer] :
            if visited[c] == 0 :
                q.append(c)
                visited[c] = 1
                cnt += 1
    return cnt

for i in range(1, N+1) :
    connected = bfs(i)
    count[i] = connected

mx = max(count)
for i in range(1, N+1) :
    if count[i] == mx :
        print(i,end = ' ')