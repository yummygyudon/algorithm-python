''' 문제 설명이 너무 빈약한듯.. '''
# N =int(input())
# nums = list(map(int, input().split()))
# dp = [nums[0]]
# cnt=1
# for i in range(1, N) :
#     if nums[i] > dp[-1] :
#         dp.append(nums[i])
#         cnt+=1
# print(cnt)


# N =int(input())
# nums = list(map(int, input().split()))
# dp = [0]*N
#
# for i in range(1,N) :
#     if nums[i] > nums[i-1] and dp[i] < dp[i-1]:
#         dp[i] = dp[i-1]+1
#     else :
#         dp[i] += 1
#
#
# print(dp)
# print(cnt)

N = int(input())
nums = list(map(int, input().split()))
dp = [0]*N
for i in range(N):
    for k in range(i):
        # 처음 도착한 수인데 값은 더 클 때
        if nums[i] > nums[k] and dp[i] < dp[k]:
            dp[i] = dp[k]
    dp[i] += 1
print(max(dp))