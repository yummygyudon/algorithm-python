

''' N이 1일 때, sys.exit(0) 이 필요한 bfs '''
import sys
input = sys.stdin.readline
N = int(input())
Block = list(map(int, input().split()))
if N == 1:
    print(0)
    sys.exit()
from collections import deque
counting = [0]*N
q = deque()
q.append([0, Block[0]])
while q :
    now , jump = q.popleft()
    for i in range(1,jump+1):
        if now + i >= N or counting[now+i] != 0: # 이미 값이 있다는 것은 최솟값이 있다는 것
            continue
        counting[now+i] = counting[now] + 1
        q.append([now+i, Block[now+i]])
if counting[-1] :
    print(counting[-1])
else :
    print(-1)


''' 혼자 푼거 실패 '''
# Block = [0] + list(map(int, input().split()))
# # counting = [0]*(N+1)
# from collections import deque
# q = deque()
# q.append([1, Block[1], 0])
#
# isable=False
# while q :
#     now, able_jump, cnt = q.popleft() # 1, 1, 0
#     if now == N :
#         isable=True
#         print(cnt)
#         break
#
#     for i in range(able_jump+1) : # 0,1
#         if i == 0 or now + i > N :
#             # or counting[now + i] == 1
#             continue
#         # print(i)
#         # counting[now+i] = counting[now]+1 # 2 , 0+1
#         q.append([now+i, Block[now+i], cnt+1])
# if not isable :
#     print(-1)



'''  역DP (제일 맘에 드는 풀이)'''
# 역 DP
# 맨뒤부터 해당 칸까지 올 수 있는 점프를 가진 이전 칸들이 있는지 확인
# while문이 0이 될때까지 계속 가장 멀리있는 가능 칸의 idx로 갱신해서
# 마지막에 가장 멀리있는 해당 idx칸으로 이동 → 재귀 함수 호출
# ( 없어서 처음 설정했던 -1이 그대로라면 이동이 불가능 한것 → -1 return )

def find(now, idx, move):
    if now == 0:
        return move
    tmp = -1
    while idx != 0:
        idx -= 1
        if Block[idx] + idx < now:
            continue
        tmp = idx
    if tmp == -1:
        return -1
    move += 1
    return find(tmp, tmp, move)

import sys
input = sys.stdin.readline
N = int(input())
Block = list(map(int, input().split()))

move = 0
print(find(N - 1, N - 1, move))


'''  DP 시도 (실패)'''
# counting = [1e9]*(N+1)
# counting[0] = 0
# for i in range(N) :
#     for k in range(Block[i], N+1) :
#         for j in range(Block[i]) :
#             if
#             if counting[k-Block[i]+j] != 1e9 :
#                 counting[k+j] = min(counting[k+j], counting[k-Block[i]+j]+1)
# print(counting)
# if counting[N] == 1e9 :
#     print(-1)
# else :
#     print(counting[N])