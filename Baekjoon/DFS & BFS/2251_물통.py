import sys
input = sys.stdin.readline

from collections import deque

A, B, C = map(int, input().split())
already = [[0]*201 for _ in range(201)]

def isAlready(a, b) :
    if not already[a][b] :
        already[a][b] = 1
        q.append([a, b])

q = deque()
q.append([0, 0])
already[0][0] = 1
able = []

while q :
    now_a, now_b = q.popleft()
    now_c = C - now_a - now_b
    if now_a == 0 :
        able.append(now_c)

    ''' A → B '''
    if now_a+now_b < B : # 현재 a의 물이 b로 "완전히" 갈 수 있는지
        isAlready(0, now_a+now_b)
    else : # 다 옮기진 못하지만 b에 꽉채워 a의 물 옮겨 담기
        isAlready(now_a-(B-now_b), B)

    ''' A → C '''
    if now_a + now_c < C :
        isAlready(0, now_b) # 어차피 pop하면 now_c는 자동으로 두 값의 뺀값으로 됨
    else :
        isAlready(now_a-(C-now_c), now_b)

    ''' B → A '''
    if now_a + now_b < A :
        isAlready(now_a+now_b, 0)
    else :
        isAlready(A, now_b-(A-now_a))

    ''' B → C '''
    if now_b + now_c < C :
        isAlready(now_a, 0)
    else :
        isAlready(now_a, now_b-(C-now_c))

    ''' C → A '''
    if now_a + now_c < A :
        isAlready(now_a+now_c, now_b)
    else :
        isAlready(A, now_b)

    ''' C → B '''
    if now_b + now_c < B :
        isAlready(now_a, now_b+now_c)
    else :
        isAlready(now_a,B)

able.sort()
print(*able)

