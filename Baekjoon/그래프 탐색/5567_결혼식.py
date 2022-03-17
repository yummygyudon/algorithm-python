

import sys
input = sys.stdin.readline
N = int(input())
R = int(input())

graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(R):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

from collections import deque
# able_friend = []
def find_friend() :
    q = deque()
    q.append([1,0])
    visited[1] = 1
    cnt = -1
    while q:
        now, depth = q.popleft()
        if depth > 2:
            continue
        cnt += 1
        for f in graph[now] :
            if graph[f] and visited[f]==0 :
                q.append([f, depth+1])
                visited[f] = 1
    return cnt
print(find_friend())