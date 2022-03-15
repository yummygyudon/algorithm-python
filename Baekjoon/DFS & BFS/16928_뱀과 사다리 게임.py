import sys
from collections import deque
input = sys.stdin.readline
visited = [0]*101
L, S = map(int, input().split())
# 풀이 1 graph
graph = [i for i in range(101)]
for _ in range(L) :
    s, a = map(int, input().split())
    graph[s] = a
for _ in range(S) :
    s, a = map(int, input().split())
    graph[s] = a

q = deque()
q.append(1)

while q :
    now = q.popleft()
    if now == 100 :
        break
    for k in range(1, 7) :
        next = now + k
        if next > 100 :
            continue
        # 풀이 1 : 도착한 사다리/뱀의 도착 지점을 graph에 저장해서 조회 후 해당 지점으로 이동
        next = graph[next]
        if visited[next] == 0 :
            q.append(next)
            visited[next] = visited[now]+1



print(visited[100])

''' 처음 풀이 _ 예제까지는 모두 통과 '''
# import sys
# from collections import deque
# input = sys.stdin.readline
#
# visited = [0]*101
#
# L, S = map(int, input().split())
#
# l_start, l_arrived = [], []
# s_start, s_arrived = [], []
# for _ in range(L) :
#     s, a = map(int, input().split())
#     l_start.append(s)
#     l_arrived.append(a)
# for _ in range(S) :
#     s, a = map(int, input().split())
#     s_start.append(s)
#     s_arrived.append(a)
#
# q = deque()
# q.append([1,0])
# visited[1] = 1
#
# while q :
#     now, cnt = q.popleft()
#     if now == 100 :
#         print(cnt)
#         break
#     for  k in range(1, 7) :
#         next = now + k
#         if next > 100 :
#             continue
#         for i in range(L):
#             if next == l_start[i] and visited[l_start[i]] == 0 and visited[l_arrived[i]] == 0:
#                 q.append([l_arrived[i], cnt+1])
#                 visited[l_start[i]] = 1
#                 visited[l_arrived[i]] = 1
#         for i in range(S):
#             if next == s_start[i] and visited[s_start[i]] == 0 and visited[s_arrived[i]] == 0:
#                 q.append([s_arrived[i], cnt + 1])
#                 visited[s_start[i]] = 1
#                 visited[s_arrived[i]] = 1
#         if visited[next] == 0 :
#             q.append([next, cnt+1])
#             visited[next] = 1
