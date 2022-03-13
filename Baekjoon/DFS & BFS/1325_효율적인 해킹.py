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

# 이게 아래 있는 방법보다 48ms 더 걸림
# mx = 0
# result = []
# for i in range(1, N+1) :
#     connected = bfs(i)
#     if connected > mx :
#         mx = connected
#     result.append([connected, i])
# for cnt, idx in result :
#     if cnt == mx :
#         print(idx,end = ' ')


#  count라는 별개 횟수 저장 리스트값으로 비교해서 같으면 출력되게끔
for i in range(1, N+1) :
    connected = bfs(i)
    count[i] = connected
mx = max(count)
for i in range(1, N+1) :
    if count[i] == mx :
        print(i,end = ' ')




# 몹쓸 재귀함수 역량....
# def count_collect(graph, a) :
#     global cnt
#
#     if graph[a] :
#         cnt += len(graph[a])
#         for i in graph[a] :
#             count_collect(graph, i)
#     return cnt
#
# for i in range(N+1) :
#     cnt = 0
#     count[i] = count_collect(graph, i)

# print(count)




# Parent = [0]*(N+1)
# for i in range(1, N+1) :
#     Parent[i] = i
#
# def find_parent(Parent,x) :
#     if Parent[x] != x:
#         Parent[x] = find_parent(Parent, Parent[x])
#     return Parent[x]
#
# def union_parent(Parent, a, b) :
#     a = find_parent(Parent, a)
#     b = find_parent(Parent, b)
#     if a > b :
#         Parent[a] = b
#     else :
#         Parent[b] = a

# route = [list(map(int, input().split())) for _ in range(M)]
#
# for _ in range(2):
#     for x,y in route :
#         union_parent(Parent, x, y)

# print(Parent)