from itertools import combinations


def dfs(idx, cnt) :
    global mn
    if cnt == N//2 : # 팀 반갈만큼 1과 0처리 했을 때
        start = link = 0
        for i in range(N) :
            for k in range(N):
                if check[i] == 1 and check[k] == 1:
                    start += combi_spec[i][k]
                elif check[i] == 0 and check[k] == 0 : # 체크 안된 대상
                    link += combi_spec[i][k] # 다른 팀
        mn = min(mn, abs(start - link))

    for i in range(idx,N) : # 0, 4
        if check[i] : # 이미 위치가 바뀌어서 조합을 해봤던 check된 선수라면 패스
            continue
        # 한명 check[i] 당 한번씩 1로 바꾸고
        # 다음 순서를 위해 다시 0으로 바꿔주고
        # 다음 순서 체크
        check[i] = 1
        dfs(i+1,cnt+1)
        check[i] = 0
N = int(input())
check = [0 for _ in range(N)]
combi_spec =[]
for _ in range(N) :
    combi_spec.append(list(map(int, input().split())))

mn = 10000
dfs(0,0)
print(mn)

""" 시간 초과 """
# # print(list(combinations(members,N//2)))
# # N이 4일 경우, [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)] 식으로 짝지어짐.
# possible_team = combinations(members,N//2)
# mn = 1e9
# for team1 in possible_team :
#     t1, t2 = 0, 0
#     team2 = list(set(members)- set(team1)) # team1의 구성원을 제외한 나머지 팀
#     # print(f"team1 : {team1}")
#     # print(f"team2 : {team2}")
#     # 구성원이 많을 때, 팀 내에서 2명씩의 combi점수의 합 -> 그 팀의 총 combi 점수
#     for combi in combinations(team1,2) :
#         t1 += combi_spec[combi[0]][combi[1]]
#         t1 += combi_spec[combi[1]][combi[0]]
#     for combi in combinations(team2,2) :
#         t2 += combi_spec[combi[0]][combi[1]]
#         t2 += combi_spec[combi[1]][combi[0]]
#     mn = min(mn, abs(t1-t2))
# print(mn)

# def dfs(result, a, b) :
#     global mn
#     if cnt  0 :
#         mn = min(result,mn)
#
#     for i in range(N) :
#         for k in range(1,N) :
#             start = combi_spec[i][k] + combi_spec[k][i]
#             link = combi_spec[N-1-i][N-1-k] + combi_spec[N-1-k][N-1-i]
