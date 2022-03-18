N = int(input())
dp =[[0]*10 for _ in range(N+1)]
MOD = 10007
for i in range(10) :
    dp[0][i] = 1

for i in range(1, N+1): # 자릿수
    for k in range(10): # 0~9 범위
        for p in range(k+1): # 나 (dp[i][k]) 보다 작은 숫자 갯수들만큼 전단계 자릿수의 경우의 수들을 모두 누적합
            # [i][k] : i자릿수일 때 마지막 자리 숫자가 k인 경우
            # 이전 자릿수까지의 경우의수는 동일하니
            # 매번 해당 자릿수의 경우만 구하면 됨
            dp[i][k] += dp[i-1][p]

print(dp[N][9]%MOD)
