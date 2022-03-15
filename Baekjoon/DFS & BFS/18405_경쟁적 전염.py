import sys
# input = sys.stdin.readline
''' 와 창의력 무엇... https://bgspro.tistory.com/19 참고 '''
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
from collections import deque
def bfs(s) :
    q = deque(virus)
    cnt = 0
    while q :
        # sort되어 들어오기 때문에 쌓이는 작업 순서도
        # 자연스레 1 시험관에서 전염되는 작업부터 pop됨
        if cnt == s :
            # 처음으로 pop된 cnt값이 조건 초값 이 되었을 때
            break

        for _ in range(len(q)) :
            # 초기 시험관 3개를 중심으로 시작
            # 반복마다 이전 반복에서 퍼졌던 작업들의 갯수만큼 다시  반복
            prev , y, x = q.popleft()
            for dy, dx in d :
                next_x = x + dx
                next_y = y + dy
                if 0 <= next_y < N and 0 <= next_x < N and m[next_y][next_x] == 0 :
                    m[next_y][next_x] = m[y][x]
                    q.append([m[next_y][next_x], next_y, next_x])
        cnt += 1

N, V = map(int, input().split())
# 시험관 위치의 값은 바뀌면 안되기 때문에
# 큐에 시작부터 시험관 좌표와 바이러스 라스트를 삽입하고 시작
m = []
virus = []
for i in range(N):
    ls = list(map(int, input().split()))
    m.append(ls)
    for j in range(N):
        if m[i][j] != 0 :
            #초기 시험관 위치 삽입 ( 위에 split되어 들어간 list 대상 )
            virus.append([m[i][j], i , j])
Second, target_Y, target_X = map(int,input().split())

virus.sort() # 시험관의 균 번호이 첫 값이기 때문에 작은 균 순으로 정렬

print(m)

bfs(Second)
print(m)
print(m[target_Y-1][target_X-1])

''' flag와 for문&while문으로 장난치기... _ 예제 통과 / 실패(시간초과) '''
# N, V = map(int, input().split())
# visited = [[0]*N for _ in range(N)]
#
# m = []
# for _ in range(N):
#     ls = list(input().split(' '))
#     m.append(list(map(int,ls)))
#
# d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#
# def bfs(y,x, v) :
#     visited[y][x] = 1
#     for dy, dx in d :
#         next_y = y + dy
#         next_x = x + dx
#         if 0 <= next_y < N and 0 <= next_x < N and visited[next_y][next_x] == 0 and m[next_y][next_x] == 0 :
#             m[next_y][next_x] = v
#             visited[next_y][next_x] = 1
#
# Second, target_Y, target_X = map(int,input().split())
# for _ in range(Second) :
#     for v in range(1, V + 1):
#         flag = False
#         while True :
#             if flag :
#                 break
#             for i in range(N) :
#                 if flag :
#                     break
#                 for k in range(N):
#                     if m[i][k] == v :
#                         bfs(i,k, v)
#                         flag = True
#                         break
# print(m[target_Y-1][target_X-1])
#
# # [[1, 1, 2], [1, 1, 2], [3, 2, 2]]