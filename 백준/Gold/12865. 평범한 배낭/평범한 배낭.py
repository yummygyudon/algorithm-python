T, W = map(int, input().split())

w, v = [0]*(T+1), [0]*(T+1)

for i in range(1,T+1) :
    weight, value = map(int,input().split())
    w[i] = weight
    v[i] = value

dp = [0]*(W+1)

for i in range(1, T+1):
    for k in range(W,0,-1) :
        if k >= w[i] :
            dp[k] = max(dp[k], dp[k-w[i]]+v[i])
print(max(dp))