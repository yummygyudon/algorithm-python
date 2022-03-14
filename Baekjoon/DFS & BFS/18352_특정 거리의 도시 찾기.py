import sys
input = sys.stdin.readline

Cities, Routes, Target, Start = map(int, input().split())

graph = [[] for _ in range(Cities+1)]
visited = [0]*(Cities+1)
distance = [1e9]*(Cities+1)
for i in range(Routes) :
    s, a = map(int, input().split())
    graph[s].append(a)


from collections import deque
q = deque()
q.append([Start, 0])
visited[Start] = 1
while q :
    s, dis = q.popleft()
    distance[s] = min(distance[s], dis)
    if graph[s] :
        for a in graph[s] :
            if visited[a] == 0 :
                visited[a] = 1
                q.append([a, dis+1])

isin = False
for i in range(len(distance)) :
    if distance[i] == Target :
        isin = True
        print(i)
if not isin :
    print(-1)
