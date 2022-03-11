# print(len(set([1,1,1,3])))
def find_parent(Parent, x) :
    if Parent[x] != x :
        Parent[x] = find_parent(Parent,Parent[x])
    return Parent[x]

def union_parent(Parent, a, b) :
    a = find_parent(Parent,a)
    b = find_parent(Parent,b)
    if a < b :
        Parent[b] = a
    else :
        Parent[a] = b
N, M = map(int, input().split())
route = [list(map(int,input().split())) for _ in range(M)]

Parent = [0] * (N+1)
for i in range(N+1):
    Parent[i] = i

# 한번만 하면 순서에 따라 업데이트 되지 않음.
for _ in range(2) :
    for x,y in route :
        union_parent(Parent, x, y)

print(len(set(Parent[1:])))