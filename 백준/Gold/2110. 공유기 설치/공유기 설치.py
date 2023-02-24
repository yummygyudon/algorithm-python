import sys
input = sys.stdin.readline

N, C = map(int, input().split())
h = []
for _ in range(N) :
    h.append(int(input()))
h.sort()

start = 1 
end = h[N-1]
ans = 0
while start <= end :
    dis = (start + end) // 2 # 처음에는 중간값을 거리로 
  # 공유기 개수가 부족하면 end를 줄여서 거리 줄여보기
  # 공유기 개수가 같으면 (start+1)로 end를 넘어가게 하기
  # 공유기 개수가 넘으면 충분하기 때문에 거리 늘려보기
    st = h[0]
    cnt = 1 # 첫집에 무조건 공유기 한 개 설치

    for i in range(1, N) :
        if h[i] >= st+dis :
            cnt +=1
            st = h[i]

    if cnt >= C :
        ans = dis
        start = dis+1
    else :
        end = dis-1
print(ans)