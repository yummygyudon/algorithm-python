T, W = map(int, input().split())

w, v = [0]*(T+1), [0]*(T+1)

for i in range(1,T+1) :
    weight, value = map(int,input().split())
    w[i] = weight
    v[i] = value

dp = [0]*(W+1)


for i in range(1, T+1): # 1, 2, 3, 4번 물건 각각
    for k in range(W,0,-1) : # 감당 가능 무게 경우의 수 7~1키로까지 감당가능
        # for k in range()
        if k >= w[i] : # 각 물건의 무게가 매 감당 가능 무게보다 작을 경우만
            dp[k] = max(dp[k], dp[k-w[i]]+v[i])
            # [k-w[i]] : 이 물건이 담겼을 때 "잔여 가능 무게 : dp[k-w[i]]"일 때
            # 그 이전까지 가능했던 dp[k-w[i]]가 갖고 있던 가치와 이번 물건의 가치: v[i] 를 더해줌

print(max(dp))
