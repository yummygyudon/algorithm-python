from sys import stdin
input = stdin.readline

N,M = map(int, input().split())
MAP = [list(input().rstrip()) for _ in range(N)]
PARENT = [0] * (N*M)

MOVE = dict()
MOVE['D'] = [1, 0]
MOVE['U'] = [-1, 0]
MOVE['L'] = [0, -1]
MOVE['R'] = [0, 1]
# MOVING = [[1, 0], [-1, 0], [0, -1], [0, 1]]

for i in range(N*M) :
    PARENT[i] = i

ELEMENTS = set()
def findParent(elem) :
    # if PARENT[elem] != elem :
    #     PARENT[elem] =  findParent(elem)
    # return PARENT[elem]

    if PARENT[elem] == elem :
        """
        일반 
        """
        return elem
    PARENT[elem] = findParent( PARENT[elem] )
    return PARENT[elem]

def unionParent(elemA, elemB) :
    elemA = findParent(elemA)
    elemB = findParent(elemB)
    if elemA == elemB :
        return
    if elemA < elemB :
        PARENT[elemB] = elemA
    else :
        PARENT[elemA] = elemB


for position in range(N*M) :
    # M으로 나눈 나머지 : x / 몫 : y
    x = position % M
    y = position // M
    nowMoving = MAP[y][x]
    nextY, nextX = y+MOVE.get(nowMoving)[0] , x+MOVE.get(nowMoving)[1]

    """
    MOVE로 이동된 곳의 Position : 사이클 속에 같이 있는 이어져있는 값
    """
    """
    몫*M + 나머지 = 다음 이동 위치
    - 다음 이동 위치가 범위를 벗어나지 않는지 검사
    """
    nextPosition = (nextY*M) + nextX
    if 0 > nextPosition or nextPosition >= N*M :
        continue
    unionParent(position, nextPosition)


result = 0
VISITED = dict()
for i in range(N*M) :
    if findParent(PARENT[i]) not in VISITED :
        VISITED[PARENT[i]] = True
        result += 1
print(result)

