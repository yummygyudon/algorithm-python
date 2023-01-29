import sys
input = sys.stdin.readline

N = int(input())
CHILD = [[] for _ in range(N)]
PARENT = list(map(int, input().split()))
DEL = int(input())
ROOT = 0
REMOVED = -1e9

for idx, parentNum in enumerate(PARENT,start=0) :
    if (parentNum == -1) :
        """
        부모 -1로 입력 받을 때 : 자신이 루트라는 의미
        - 따로 해당 idx 등록할 노드가 없음
        """
        ROOT = idx
        continue
    CHILD[parentNum].append(idx)

"""
부모로서 등록되어있는 PARENT 에서 해당 노드 삭제 처리
CHILD에 자신의 자식으로 등록되어 있는 노드들도 DFS로 삭제 처리 메서드 실행
"""
def removeChildrenNodes(removeNode) :
    PARENT[removeNode] = REMOVED
    for i in range(len(CHILD[removeNode])) :
        removeChildrenNodes(CHILD[removeNode][i])


removeChildrenNodes(DEL)
# print(PARENT)
# print(CHILD)
# 

COUNT = 0

for i in range(N) :
    """
    자신이 삭제되지 않았으며
    어떤 노드도 자신을 부모로 같지 않을 경우
    == "리프 노드"
    """
    if not PARENT[i] == REMOVED and i not in PARENT:
        COUNT += 1

print(COUNT)