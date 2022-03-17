

# 음수들만 있을 때, 0으로 넣었던 것이 문제 발생
# N = int(input())
# nums = list(map(int, input().split()))
# dp = [[0]*N for i in range(N)]
# mx = -1e9
# for i in range(N):
#     dp[i][i] = nums[i]
#
# print(dp)
#
# for i in range(N):
#     for k in range(i+1, N) :
#         # if i == k :
#         #     dp[i][k] =
#         #     continue
#         dp[i][k] = nums[k] + dp[i][k-1]
#         mx = max(mx, dp[i][k])
# print(dp)
# print(mx)



''' 2차원 배열 활용 - 메모리 초과 ( 예제는 통과 ) '''
N = int(input())
nums = list(map(int, input().split()))
dp = [[0]*(N-i) for i in range(N)]
mx = -1e9
for i in range(N):
    mx = max(mx,nums[i])
    dp[i][0] = nums[i]

# print(dp)
for i in range(N):
    idx = i+1
    for k in range(1, N-i) :
        # if i == k :
        #     dp[i][k] =
        #     continue
        dp[i][k] = nums[idx] + dp[i][k-1]
        mx = max(mx, dp[i][k])
        idx += 1
# print(dp)
print(mx)

''' 현타가 오네요... 어이없... '''
N = int(input())
nums = list(map(int, input().split()))
s = [nums[0]]
for i in range(N-1) :
    s.append(max(s[i]+nums[i+1], nums[i+1]))
    print(s)
print(max(s))
