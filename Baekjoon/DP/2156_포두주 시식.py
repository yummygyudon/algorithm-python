''' 1912 연속합 문제와 유사 '''
N = int(input())
wine = [0]*(N+1) # 병 번호별 용량담기
dp = [0]*(N+1)

for i in range(1, N+1) :
    wine[i] = int(input())

dp[1] = wine[1]
if N > 1 :
    dp[2] = wine[1]+wine[2]
if N > 2 :
    dp[3] = wine[1]+wine[2]+wine[3]

for i in range(3,N+1):
    dp[i] = max(dp[i-1], dp[i-2]+wine[i], dp[i-3]+wine[i]+wine[i-1])
print(dp[N])
