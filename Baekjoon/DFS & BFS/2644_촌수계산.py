import sys
input = sys.stdin.readline
N = int(input())

start, end = map(int, input().split())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

from collections import deque
q = deque()
visited = [0 for _ in range(N+1)]
q.append([start, 0])
visited[start] = 1
found = False
while q :
    now, cnt = q.popleft()
    if now == end :
        print(cnt)
        found = True
        break
    for v in graph[now]:
        if visited[v] == 0 :
            q.append([v, cnt+1])
            visited[v]=1
if found == False :
    print(-1)

# def dfs(graph, node) :
