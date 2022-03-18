N, K = map(int, input().split())
coin = []
for _ in range(N):
    coin.append(int(input()))

dp = [0]*(K+1)
dp[0]=1
# 아... 순서가 바뀌어서 같은 동전을 여러번 반복해서 합이 너무 커지넹..
# for i in range(1, K+1):
#     for k in coin :
#         if i-k >= 0 :
#             dp[i] += dp[i-k]
#             print(dp)

for c in coin :
    for i in range(1,K+1) :
        if i-c >= 0 : # 가장 작은 동전이 1보다 크더라도
            dp[i] += dp[i-c] # [i-c]위치는 무조건 dp[0]이므로 1로 시작할 수 있음/
            print(dp)
print(dp[K])
