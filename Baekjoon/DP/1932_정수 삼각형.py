N = int(input()) # 단계수 == 맨 밑바닥

triangle = []
for _ in range(N):
    triangle.append(list(map(int,input().split())))
print(triangle)

# [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
dp = [[0]*N for _ in range(N)]
for i in range(N): # 맨 아래 단계 dp만 triangle과 일치시키기
    dp[N-1][i] = triangle[N-1][i]
# [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [4, 5, 2, 6, 5]]
print(dp)

# 정삼각형보다 직각 삼각형으로 생각하면 편함
for i in range(N-2,-1,-1): # 3 2 1 0  0 # 단계 : 역방향 진행
    for k in range(i+1) : # 0 1 2 3 # 각 단계 소속 값들 개수 == 단계
        dp[i][k] = max(triangle[i][k] + dp[i+1][k], triangle[i][k] + dp[i+1][k+1])
# 각 단계 각 값마다 아랫 단계의 (자신 + 자신의 위치였던 값) 과
#                           (자신 + 자신의 위치 오른쪽에 있던 값) 중 큰 값만 dp에 저장

print(dp[0][0])