import sys
input = sys.stdin.readline
N = int(input())
# Parent = [i for i in range(N+1)]
visited = [0 for _ in range(N+1)]

graph = [[] for _ in range(N+1)]
for _ in range(N-1) :
    p, c = map(int,input().split())
    graph[p].append(c)
    graph[c].append(p)
print(graph)
Parent = [i for i in range(N+1)]
root = 1
from collections import deque
q = deque([root])
visited[root] = 1
while q :
    node = q.popleft()
    # if visited[node] == 1 :
    #     continue
    for v in graph[node] :
        # print(v)
        if visited[v] == 0 :
            q.append(v)
            Parent[v] = node
            visited[v] = 1

for p in Parent[2:]:
    print(p)


# for _ in range(N-1) :
#     p, c = map(int,input().split())
#     if c == 1 :
#         Parent[p] = 1
#         visited[p] = 1
#     else :
#         if visited[p] == 1:
#             Parent[c] = p
#             visited[c] = 1
#         else :
#             Parent[p] = c
#             visited[p] = 1
#
# for p in Parent[2:]:
#     print(p)
#
# print(Parent)
