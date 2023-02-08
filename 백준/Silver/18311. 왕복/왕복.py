N, K = map(int, input().split())
SECTIONS = [0]+list(map(int,input().split()))
# pathCost = sum(SECTIONS)

for i in range(1,N+1) :
    K -= SECTIONS[i]
    if K < 0 :
        print(i)
        break
if K >= 0 :
    for i in range(N, 0, -1) :
        K -= SECTIONS[i]
        if K < 0 :
            print(i)
            break