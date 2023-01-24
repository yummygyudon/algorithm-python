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

for _ in range(2) :
    for x,y in route :
        union_parent(Parent, x, y)

print(len(set(Parent[1:])))