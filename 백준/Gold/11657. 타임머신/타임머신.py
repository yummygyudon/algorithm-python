# 음의 순환 발생 -> -1 출력

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
dis = [1e9] * (N+1)
# 1번 도시 출발
dis[1] = 0
for _ in range(M) :
    a,b,c = map(int, input().split())
    graph[a].append([b,c])

able = True

# 일반적인 거리 갱신과 동일한 작업
# 시작도시인 1번 도시 제외 각 도시에 대해 for문 돌리기

    # 각 도시에서부터 다른 도시들 방문의 경우
for _ in range(N-1) :
    # 각 도시에서부터 다른 도시들 방문의 경우
    for s in range(1, N+1) :
        for arrv, cost in graph[s] :
            if dis[s] != 1e9 and dis[arrv] > dis[s] + cost :
                dis[arrv] = dis[s] + cost

# N번째 반복 때
# 음수 사이클 체크  -> N번째 반복 때에도 거리 값이 갱신되는것 --> " 음수 순환이 발생 "
for s in range(1, N+1) :
    for arrv, cost in graph[s] :
        if dis[s] != 1e9 and  dis[arrv] > dis[s] + cost : # 값이 또 더 줄어듦
            able = False

if able :
    for i in range(2,N+1) :
        # 1e9이다 --> 해당 도시로 가는 경로가 없다.
        print(dis[i] if dis[i] < 1e9 else -1)
else :
    print(-1)