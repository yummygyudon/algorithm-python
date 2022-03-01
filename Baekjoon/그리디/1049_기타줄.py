N, M = map(int, input().split())
# price=[]
g, e = [], []
for _ in range(M) :
    group, each = map(int, input().split())
    g.append(group)
    e.append(each)
g.sort()
e.sort()
if g[0] > e[0]*6 :
    buy_s = (N//6)*6*e[0]
else :
    buy_s = N//6*g[0]
buy_e = N%6*e[0]
if buy_e > g[0] :
    buy_e = g[0]

print(buy_s + buy_e)
