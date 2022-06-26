N = int(input())
check = [0 for _ in range(N)]
combi_spec =[]
for _ in range(N) :
    combi_spec.append(list(map(int, input().split())))
    
def dfs(idx, cnt) :
    global mn
    if cnt == N//2 : 
        start = link = 0
        for i in range(N) :
            for k in range(N):
                if check[i] == 1 and check[k] == 1:
                    start += combi_spec[i][k]
                elif check[i] == 0 and check[k] == 0 : 
                    link += combi_spec[i][k]
        mn = min(mn, abs(start - link))

    for i in range(idx,N) : 
        if check[i] :
            continue
        check[i] = 1
        dfs(i+1,cnt+1)
        check[i] = 0


mn = 10000
dfs(0,0)
print(mn)