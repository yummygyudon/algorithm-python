N, Relations = map(int,input().split())

cnt = 1
graph = [[] for _ in range(N+1)]
for _ in range(Relations) :
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

from collections import deque
def bfs(Me, Target) :
    q = deque()
    visited = [[0]*(N+1) for _ in range(N+1)]
    cnt = 0
    q.append([Me,cnt])
    visited[Me][Me] = 1

    while q :
        now, cnt = q.popleft()
        if now == Target :
            break
        for f in graph[now] :
            if visited[now][f] == 0 :
                q.append([f, cnt+1])
                visited[now][f]=1
    return cnt


result = []
for i in range(1, N+1):
    bacon = 0
    for k in range(1,N+1) :
        bacon += bfs(i,k)
    result.append(bacon)

mn = min(result)

for i in range(len(result)) :
    if result[i] == mn :
        print(i+1)
        break


# def find_friend(Me, target) : # 1번 친구가 3번 친구로
#     global cnt
#     for f in graph[Me] :
#         if f == target:
#             return  1
#         else :
#             return find_friend(f,target)

