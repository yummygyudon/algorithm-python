from collections import deque
import sys
input = sys.stdin.readline
"""
학번은 모두 1부터 N까지
"""
N = int(input()) # 동기 수
M = int(input()) # 리스트 길이

"""
본격 친구 찾기 함수
"""
def findFriend(student_id) :
    global INVITE_COUNT
    # [ 학번, 관계 Depth ]
    q = deque()
    q.append([student_id, 0])
    CHECK_LIST[student_id] = True
    while q :
        id, depth = q.popleft()
        # 친구의 친구 까지만
        if depth < 2 :
            # 친구의 친구 List
            for friend in GRAPH[id] :
                # 아직 초대하지 않은 친구들만
                if not CHECK_LIST[friend] :
                    CHECK_LIST[friend] = True
                    INVITE_COUNT += 1
                    q.append([friend, depth+1])



"""
동기 -> Node
서로간의 관계 추가 
"""
GRAPH = [[] for _ in range(N+1)]

for _ in range(M) :
    a,b = map(int, input().split())
    GRAPH[a].append(b)
    GRAPH[b].append(a)
CHECK_LIST = [False]*(N+1)
INVITE_COUNT = 0
findFriend(1)
print(INVITE_COUNT)
