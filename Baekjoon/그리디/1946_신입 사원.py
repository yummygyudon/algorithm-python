import sys
TC = int(sys.stdin.readline())
for _ in range(TC) :
    ap = int(sys.stdin.readline())
    # score = [1e9,1e9]
    # cnt = 0
    rank =[]
    for i in range(ap):
        a, b = map(int,sys.stdin.readline().split())
        rank.append([a,b])
    rank.sort(key = lambda x : x[0])
    cnt = 1
    mx = rank[0]
    for k in range(1, len(rank)) :
        if rank[k][1] < mx[1] :
            cnt += 1
            mx = rank[k]
    print(cnt)