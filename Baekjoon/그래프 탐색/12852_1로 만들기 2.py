
N = int(input())

dp = [[0,[]] for _ in range(N+1)]
dp[1][0] = 0
dp[1][1] = [1]

for i in range(2,N+1):
    dp[i][0] = dp[i-1][0] + 1
    dp[i][1] = dp[i-1][1] + [i]
    # result.append(i)
    if i % 3 == 0 and dp[i//3][0]+1 < dp[i][0] : # min(dp[i], dp[i//3]+1) 본래 dp 이부분 활용
        dp[i][0] = dp[i//3][0] +1
        dp[i][1] = dp[i//3][1] +[i]
    if i % 2 == 0 and dp[i//2][0]+1 < dp[i][0]:
        dp[i][0] = dp[i // 2][0] + 1
        dp[i][1] = dp[i // 2][1] + [i]
    print(dp)

print(dp[N][0])
print(*dp[N][1][::-1])

'''시간 초과 (BFS) '''
# from collections import deque
# import sys
# input=sys.stdin.readline
# N = int(input())
# result = []
#
# q = deque()
# q.append([N])
# while q:
#     process = q.popleft()
#     print(process)
#     now = process[0]
#     if now == 1 :
#         result = process
#         break
#     if now%3 == 0:
#         q.append([now//3] + process)
#     if now%2 == 0:
#         q.append([now//2] + process)
#     q.append([now-1] + process)
# print(len(result)-1)
# print(*result[::-1]) # 새로운 객체가 들어가게됨.
#
# #[] 객체에 기존 리스트 변수를 더하게 되면 기존 변수에 영향이 없지만
# #q.append(process.append(now-1)) 식으로 하게되면 process 변수가 계속 꼬리게 됨.

