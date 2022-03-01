start, end = map(int,input().split())
cnt = 1
# end==start 의 경우 → 1도 포함
# 아래 편집 작업을
while end != start :
    # if end < start :
    #     cnt = -1
    #     break
    # if int(str(end)[-1])%2 == 0 :
    t = end
    if end % 2 == 0:
        end//=2
    elif end%10 == 1 : # 끝자리가 1인 경우
        # 비효율적인 작업
        # tmp = str(end)
        # tmp = tmp[:len(tmp)-1]
        # end = int(tmp)
        end//=10
    # 위 경우를 모두 해당 안되는 것은 불가능 & 무한 루프 시작된 것
    cnt += 1
    if t == end :
        cnt = -1
        break
print(cnt)

"""
bfs 방식
- bottomUp 방식 -

<무한루프문>
큐에 아무 값도 안남아있으면
break & -1 출력
 
큐에 1을 붙인 경우 & 2를 곱한 모든 경우 append

popleft작업은 처음에 무조건적으로 수행해서
end값과 크거나 같을 때까지 꺼낸 것 검사
크면 continue해서 pop만했던 상태에서 다시 루프 돌게 (잘못된 값만 계속 있으면 큐가 비게 됨 -> 안남아있으면  -1 출력)
같으면 같이 append되있던 count 값 출력 & break

"""
from collections import deque
start, end = map(int,input().split())
q = deque()
q.append([start,1])
result = -1
while q :
    n, cnt = q.popleft()
    if n > end : # 큐가 비게끔 만드는 효과
        continue
    if n == end :
        result = cnt
        break
    q.append([int(str(n)+'1'), cnt+1])
    q.append([n*2, cnt+1])
print(result)






